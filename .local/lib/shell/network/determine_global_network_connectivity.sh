#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-15 17:46
# Filename:     determine_global_network_connectivity.sh

is_global_network() {
    if ! command -v curl &>/dev/null; then
        echo "You do not instelled curl"
    fi

    case $(curl -o /dev/null -s --connect-timeout 5 -w "%{http_code}" https://google.com) in
        200|301|302)
            return 0
            ;;
        000|401|403|404|500|502)
            return 1
            ;;
    esac
}
if [ -n "$1" ]; then
    case "${1:-}" in
        "--check")
            if is_global_network; then
                printf '\033[1;32mYou are in global network\033[0m\n'
            else
                printf '\033[1;31mYou are not in global network\033[0m\n'
            fi
            ;;
        *)
            printf '\033[1;31mUsage:\033[0m %s \033[1;34m--check\033[0m\n' "$0" >&2
            exit 2
            ;;
    esac
fi
