#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-07 12:03
# Filename:     minecraft-input.sh

# 创建临时文件
TEMP_FILE=$(mktemp)
trap 'rm -f "$TEMP_FILE"' EXIT

# 启动 ydotoold
pgrep ydotoold >/dev/null || { ydotoold & sleep 0.5; }

# 先启动 zenity
zenity --entry --title="Minecraft中文输入" --text="请输入文本:" 2>/dev/null > "$TEMP_FILE" &

# 给 zenity 一点时间启动，然后切换输入法
sleep 0.5
fcitx5-remote -t

# 等待后台任务完成
wait

# 处理输入
if [ -s "$TEMP_FILE" ]; then
    wl-copy < "$TEMP_FILE"
    sleep 0.2
    ydotool key 29:1 47:1 47:0 29:0 14:1 14:0 28:1 28:0
fi
