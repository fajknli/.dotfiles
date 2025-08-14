#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-13 20:05
# Filename:     if_online.sh


if_online() {
    # ping
    if command -v ping >/dev/null 2>&1; then
        if ping -c 1 -W 2 8.8.8.8 >/dev/null 2>&1; then
            return 0
        fi
    fi
    # curl and wget
    if command -v curl >/dev/null 2>&1; then
        if curl -s --max-time 3 "https://example.com" >/dev/null 2>&1; then
            return 0
        fi
    elif command -v wget >/dev/null 2>&1; then
        if wget -q --spider --timeout=3 "https://example" >/dev/null 2>&1; then
            return 0
        fi
    fi
    return 1
}

## verdict network is online of offline
#if  if_online; then
#    echo "Network is online"
#else
#    echo "Network is offline"
#    exit 1
#fi
