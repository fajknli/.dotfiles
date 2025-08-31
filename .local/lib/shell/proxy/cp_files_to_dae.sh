#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-15 13:32


mkdir -p "$HOME"/.local/share/proxy-files-dae && cd "$HOME"/.local/share/proxy-files-dae || exit 1

# copy sysctl.conf file
if [ ! -f "/etc/sysctl.conf" ]; then
    echo "1.Try to copy sysctl.conf to /etc/"
    sudo cp sysctl.conf /etc/ || { echo "Failed to copy sysctl.conf,mayby you dont have permisson"; exit 1; }
fi

# copy config.dae
if [ ! -d "/etc/dae" ]; then
    echo "2.Try to make /etc/dae/ dir"
    sudo mkdir -p /etc/dae/ || { echo "Cant creat /etc/dae"; exit 1; }
    echo "3.Try to copy config.dae to /etc/dae/ direction"
    sudo cp config.dae /etc/dae/ || { echo "Failed to copy config.dae,sure in root?"; exit 1; }
fi

# check if config.dae permisson is 0640
set_perm="$(stat -c "%a" /etc/dae/config.dae)"

# set permisson
if [ ! "$set_perm" -eq "640" ]; then
    echo "4.Change config.dae file permission"
    sudo chmod 0640 /etc/dae/config.dae || { echo "Failed to change permissions"; exit 1; }
fi

# cp geoip.dat and geosite.dat to /usr/local/share/dae
if [ ! -d "/usr/local/share/dae" ]; then
    echo "5.Try to make a /usr/local/share/dae dir";
    sudo mkdir -p /usr/local/share/dae/
    echo "6.Copy geoip.dat and geosite.dat to /usr/local/share/dae direction";
    sudo cp geoip.dat geosite.dat /usr/local/share/dae/ || { echo "Failed to copy files"; exit 1; }
fi
