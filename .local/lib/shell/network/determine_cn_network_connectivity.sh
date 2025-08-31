#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-15 18:43
# Filename:     determine_cn_network_connectivity.sh

is_cn_network() {
    # Ping test. if connected, then exit script and return 0
    local timeout=2
    local test_domains=("223.5.5.5" "119.29.29.29" "163.com")
    if command -v ping >/dev/null 2>&1; then
        for target in "${test_domains[@]}"; do
            if ping -c 1 -W "$timeout" "$target" >/dev/null 2>&1; then
                return 0
            fi
        done
    fi
    # curl and wget
    if command -v curl >/dev/null 2>&1; then
        if curl -s --max-time "$timeout" "http://163.com" >/dev/null 2>&1; then
            return 0
        fi
    elif command -v wget >/dev/null 2>&1; then
        if wget -q --spider --timeout="$timeout" "http://163.com" >/dev/null 2>&1; then
            return 0
        fi
    fi
    # All checks are failed
    return 1
}

if [ -n "$1" ]; then
    case "${1:-}" in
        "--check")
            if is_cn_network; then
                printf '\033[1;32mYou are in CN network\033[0m\n'
            else
                printf '\033[1;31mYou are not in CN network\033[0m\n'
            fi
            ;;
        *)
            printf '\033[1;31mUsage:\033[0m %s \033[1;34m--check\033[0m\n' "$0" >&2
            exit 2
            ;;
    esac
fi




