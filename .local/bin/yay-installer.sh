#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-12 00:15
# Filename:     yay-installer.sh

if ! command -v git; then
    echo "No git, plz install git"
    exit 1
fi

if command -v yay; then
    echo "you already have instlled yay"
    exit 1
fi

if command -v yay-bin; then
    echo "you already have instlled yay-bin"
    exit 1
fi

case $(curl -o /dev/null -s --connect-timeout 5 -w "%{http_code}" https://google.com) in
    200|301|302)
        cd $HOME/.local/share/
        git clone https://aur.archlinux.org/yay-bin.git --depth=1
        cd yay-bin
        makepkg -si
        ;;
    000|401|403|404|500|502)
        echo "You don't cross off THE GREAT FIRE WALL"
        ;;
esac


