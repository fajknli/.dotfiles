#!/bin/sh

while IFS= read -r -d '' dir; do
    path_dirs+=("$dir")
done < <(find /home/a6dg2uv/Music/ -type d -print0)


# read -p "Which one is the playlist you want to listen?" selected_playlist

for path in "${path_dirs[@]}"; do
    base_dir=$(basename "$path")
    dirs+=("$base_dir")
done


j=0
for playlist in "${dirs[@]}"; do
    j=$((j+1))
    playlists+=("$playlist" "      $j.")
done


selected_playlist=$(whiptail --backtitle "Select a Playlist" --title "Select a Playlist" --menu "自己选吧:" 25 60 15 \
"${playlists[@]}" 3>&1 1>&2 2>&3
)

echo "$selected_playlist"

mpv --no-video -playlist=/home/a6dg2uv/Music/$selected_playlist

