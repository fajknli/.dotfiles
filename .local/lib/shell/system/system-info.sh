#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-06 15:25
# Filename:     1.sh


# 获取系统信息
TIME=$(date "+%H:%M:%S")
DATE=$(date "+%Y-%m-%d (%A)")
UPTIME=$(uptime -p | sed 's/up //')
MEMORY=$(free -h | awk '/Mem:/ {print $3 "/" $2}')
VOLUME=$(pactl get-sink-volume @DEFAULT_SINK@ | awk '{print $5}' | head -n1) 2>/dev/null || VOLUME="N/A"
BRIGHTNESS=$(ddcutil --bus=8 getvcp 10 | awk '/current value =/ {print $9}' | tr -d ',')%
CPU_TEMP=$(awk '{printf "%d", $1/1000}' /sys/class/thermal/thermal_zone0/temp)°C
CPU=$(awk '{print $1,$2,$3}' /proc/loadavg)
ROOT_DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}')
HOME_DISK_USAGE=$(df -h /home | awk 'NR==2 {print $5}')

# 将信息组合成 wmenu 的输入格式（每行一条信息）
INFO=$(echo -e "🕒 时间: $TIME
📅 日期: $DATE
⏱️ 运行: $UPTIME
💾 内存: $MEMORY
🔋 电量: $BATTERY
🔊 音量: $VOLUME
💡 亮度: $BRIGHTNESS
🌡️ CPU温度: $CPU_TEMP
📊 系统负载: $CPU
💾 /分区: $ROOT_DISK_USAGE 使用
💾 /home分区: $HOME_DISK_USAGE 使用")

notify-send "$INFO"
