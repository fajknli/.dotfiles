#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-16 07:27
# Filename:     pull_dae_config.sh


source "$HOME"/.local/lib/shell/network/determine_cn_network_connectivity.sh

if is_cn_network; then
    # mkdir -p "$HOME"/.local/share/proxy-files-dae
    if [ -d "$HOME"/.local/share/proxy-files-dae ]; then
        rm -rf "$HOME"/.local/share/proxy-files-dae
    fi
    git clone https://gitee.com/fajknli/proxy-files-dae.git --depth=1 "$HOME"/.local/share/proxy-files-dae
else
    printf "\033[1;31mYou are not connected to internet\033[0m\n"
fi
