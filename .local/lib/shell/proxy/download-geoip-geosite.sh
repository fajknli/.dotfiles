#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-15 11:00
# Filename:     download_geoip_geosite.sh


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

echo "downloading geoip..."

if ! curl -L -# "$geoip" -o geoip.dat; then
    echo "Fail to download geoip" >&2
    exit 1
fi
echo "downloading geoip_sha256sum..."

if ! curl -L -# "$geoip_sha256sum" -o geoip.dat.sha256sum; then
    echo "Fail to download geoip.dat.sha256sum" >&2
    exit 1
fi

echo "downloading geosite..."

if ! curl -L -# "$geosite" -o geosite.dat; then
    echo "Fail to download geosite" >&2
    exit 1
fi

echo "downloading geosite_sha256sum..."

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

