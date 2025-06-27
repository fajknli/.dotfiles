#! /usr/bin/env bash
#

read -p "Ur music Name:"  original_music_name

underline_name=${original_music_name// /_}
# 参数替换，将original_music_name里的空格替换为下划线

mv ~/Downloads/*.m4a ~/Music/$underline_name.m4a || mv ~/Downloads/*.mp3 ~/Music/$underline_name.mp3

ls ~/Music | grep $underline_name

