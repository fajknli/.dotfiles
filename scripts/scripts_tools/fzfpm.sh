#! /usr/bin/env bash
# Author:        a6dg2uv
# Created Time:  2025-04-12

username=$(users)
while IFS= read -r -d '' dir_music;do
    path_dirs+=("$dir_music")
done < <(find /home/$username/Music -mindepth 1 -maxdepth 1 -type d -print0)
for paths in "${path_dirs[@]}";do
    base_dir=$(basename "$paths")
    dirs+=("$base_dir")
done
target_dir=/home/$username/Music/$(printf "%s\n" "${dirs[@]}" | fzf)
find $target_dir -type f | shuf | while read -r song; do
    mpv --shuffle --no-video --term-osd-bar=yes "$song"
    sleep $((10 + RANDOM % 60))  # 10~60 秒随机间隔
done
