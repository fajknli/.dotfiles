#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-12 15:30
# Filename:     setup-config.sh

set -e


download_pkg_arch() {
    "$HOME"/.local/bin/setup-install-pkg.sh
}

download_yay() {
    "$HOME"/.local/bin/yay-installer.sh
}


download_geoip_geosite() {
    # 如果无法访问域名 raw.githubusercontent.com，可以使用第二个地址 cdn.jsdelivr.net。
    # 如果无法访问域名 cdn.jsdelivr.net，可以将其替换为 fastly.jsdelivr.net
    geoip="https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/geoip.dat"
    #geoip="https://cdn.jsdelivr.net/gh/Loyalsoldier/v2ray-rules-dat@release/geoip.dat"

    geoip_sha256sum="https://raw.githubusercontent.com/Loyalsoldier/geoip/release/geoip.dat.sha256sum"
    #geosite_sha256sum="https://cdn.jsdelivr.net/gh/Loyalsoldier/geoip@release/geoip.dat.sha256sum"

    geosite="https://github.com/Loyalsoldier/domain-list-custom/releases/latest/download/geosite.dat"
    #geosite="https://cdn.jsdelivr.net/gh/Loyalsoldier/v2ray-rules-dat@release/geosite.dat"

    geosite_sha256sum="https://github.com/Loyalsoldier/domain-list-custom/releases/latest/download/geosite.dat.sha256sum"
    #geosite_sha256sum="https://cdn.jsdelivr.net/gh/Loyalsoldier/v2ray-rules-dat@release/geosite.dat.sha256sum"
    mkdir -p "$HOME"/.local/share/proxy-files-dae && cd "$HOME"/.local/share/proxy-files-dae

    echo "geoip"

    if ! curl -L -# "$geoip" -o geoip.dat; then
        echo "Fail to download geoip" >&2
        exit 1
    fi
    echo "geoip_sha256sum"

    if ! curl -L -# "$geoip_sha256sum" -o geoip.dat.sha256sum; then
        echo "Fail to download geoip.dat.sha256sum" >&2
        exit 1
    fi

    echo "geosite"

    if ! curl -L -# "$geosite" -o geosite.dat; then
        echo "Fail to download geosite" >&2
        exit 1
    fi

    echo "geosite_sha256sum"

    if ! curl -L -# "$geosite_sha256sum" -o geosite.dat.sha256sum; then
        echo "Fail to download geosite.dat.sha256sum" >&2
        exit 1
    fi

    # checksum
    if sha256sum -c geoip.dat.sha256sum; then
        echo "Verify geoip.dat passed: The file matches its expected cryptographic hash"
    else
        echo "Verify geoip.dat failed: The file may be corrupted or tampered with" >&2
        exit 1
    fi

    if sha256sum -c geosite.dat.sha256sum; then
        echo "Verify geosite.dat passed: The file matches its expected cryptographic hash"
    else
        echo "Verify geosite.dat failed: The file may be corrupted or tampered with" >&2
        exit 1
    fi
}


set_proxy() {
    if ! command -v curl; then
        sudo pacman -S curl
    fi
    if ! command -v dae; then
        sudo pacman -S dae
    fi
    if ! command -v git; then
        sudo pacman -S git
    fi
    case $(curl -o /dev/null -s --connect-timeout 5 -w "%{http_code}" https://google.com) in
        200|301|302)
            download_geoip_geosite
            ;;
        000|401|403|404|500|502)
            git clone https://gitee.com/fajknli/proxy-files-dae.git "$HOME"/.local/share/proxy-files-dae
            open_proxy
            ;;
    esac
}

open_proxy() {
    mkdir -p "$HOME"/.local/share/proxy-files-dae && cd "$HOME"/.local/share/proxy-files-dae || exit 1

    # copy sysctl.conf file
    if [ ! -f "/etc/sysctl.conf" ]; then
        echo "Try to copy sysctl.conf to /etc/"
        sudo cp sysctl.conf /etc/ || { echo "Failed to copy sysctl.conf,mayby you dont have permisson"; exit 1; }
    fi

    # copy config.dae
    if [ ! -d "/etc/dae" ]; then
        echo "Try to make /etc/dae/ dir"
        sudo mkdir -p /etc/dae/ || { echo "Cant creat /etc/dae"; exit 1; }
        sudo cp config.dae /etc/dae/ || { echo "Failed to copy config.dae,sure in root?"; exit 1; }
    fi

    # check if config.dae permisson is 0640
    set_perm="$(stat -c "%a" /etc/dae/config.dae)"

    # set permisson
    if [ ! "$set_perm" -eq "640" ]; then
        echo "Change config.dae file mod"
        sudo chmod 0640 /etc/dae/config.dae || { echo "Failed to change permissions"; exit 1; }
    fi

    # cp geoip.dat and geosite.dat to /usr/local/share/dae
    if [ ! -d "/usr/local/share/dae" ]; then
        echo "Try to make a /usr/local/share/dae dir";
        sudo mkdir -p /usr/local/share/dae/
        sudo cp geoip.dat geosite.dat /usr/local/share/dae/ || { echo "Failed to copy files"; exit 1; }
    fi

    echo "start dae..."

    # 重载配置（修改配置后使用）
    sudo systemctl enable dae.service || { echo "Failed to enable service"; exit 1; }

    sudo systemctl start dae.service || { echo "Failed to start service"; exit 1; }

    sudo systemctl reload dae.service || { echo "Failed to reload service"; exit 1; }

    state="$(systemctl is-active dae.service)"

    if [ "$state" = "active" ]; then
        echo "dae is active now..."
    fi
}

