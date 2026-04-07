#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-21 17:04
# Filename:     network-check.sh


# source "$HOME"/.local/lib/shell/network/determine_global_network_connectivity.sh
# source "$HOME"/.local/lib/shell/network/determine_cn_network_connectivity.sh
source "$HOME"/.local/lib/shell/network/network

if is_cn_network; then
    printf '\033[1;32mYou are in CN network\033[0m\n'
else
    printf '\033[1;31mYou are not in CN network\033[0m\n'
fi

if is_global_network; then
    printf '\033[1;32mYou are in global network\033[0m\n'
else
    printf '\033[1;31mYou are not in global network\033[0m\n'
fi


