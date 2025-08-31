#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-14 06:32
# Filename:     get_music.sh


while true; do
    printf "Enter your wyyyy music URL here: "
    read -r  origin_url
    case "$origin_url" in
        "q" | "quit" | "exit")
            exit 1
            ;;
    esac
    printf "Enter your wyyyy music Name: "
    read -r  music_name
    case "$music_name" in
        "q" | "quit" | "exit")
            exit 1
            ;;
    esac
    # tr -s 压缩多个连在一起的空格为一个下划线
    music_name_no_space=$(echo "$music_name" | tr -s ' ' '_')
    if echo "$origin_url" | grep -Eq '^https://.*vuutv=.*&cdntag=.*$'; then
        curl -L -# -o "$music_name_no_space.m4a" "$origin_url"
    fi
done



