#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-09 09:51
# Filename:     system-status.sh

# 颜色定义
#RED='\033[1;31m'
#GREEN='\033[1;32m'
#YELLOW='\033[1;33m'
#BLUE='\033[1;34m'
#PURPLE='\033[1;35m'
#CYAN='\033[1;36m'
#WHITE='\033[1;37m'
#NC='\033[0m' # No Color

# 获取系统信息
TIME=$(date "+%H:%M:%S")
DATE=$(date "+%Y-%m-%d (%A)")
UPTIME=$(uptime -p | sed 's/up //')
VOLUME=$(pactl get-sink-volume @DEFAULT_SINK@ | awk '{print $5}' | head -n1 2>/dev/null || echo "N/A")
BRIGHTNESS=$(ddcutil --bus=8 getvcp 10 2>/dev/null | awk '/current value =/ {print $9}' | tr -d ',')%
CPU_TEMP=$(awk '{printf "%d", $1/1000}' /sys/class/thermal/thermal_zone0/temp 2>/dev/null || echo "N/A")°C
CPU_LOAD=$(awk '{printf "%s / %s / %s",$1,$2,$3}' /proc/loadavg 2>/dev/null || echo "N/A")
MEMORY=$(free -h | awk '/Mem:/ {printf "%.1fG / %.1fG (%.1f%%)", $3, $2, $3/$2*100}')
ROOT_DISK_USAGE=$(df -h / | awk 'NR==2 {printf "%s / %s (%s)", $3, $2, $5}')
HOME_DISK_USAGE=$(df -h /home 2>/dev/null | awk 'NR==2 {printf "%s / %s (%s)", $3, $2, $5}' || echo "N/A")

# 获取额外的系统信息
OS_INFO=$(grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '"')
KERNEL=$(uname -r)
SHELL_NAME=$(basename "$SHELL")
CPU_INFO=$(grep 'model name' /proc/cpuinfo | head -1 | cut -d: -f2 | sed 's/^[ \t]*//;s/(R)//g;s/@.*//;s/ *$//')
GPU_INFO=$(lspci 2>/dev/null | grep -i vga | head -1 | cut -d: -f3 | sed 's/^[ \t]*//' || echo "N/A")

# 创建格式化的通知消息
MESSAGE="<b>📅 基本信息:</b>
• <span color='#a0d0a0'><b>时间:</b></span> $TIME
• <span color='#a0d0a0'><b>日期:</b></span> $DATE
• <span color='#a0d0a0'><b>运行时间:</b></span> $UPTIME
• <span color='#a0d0a0'><b>系统:</b></span> $OS_INFO
• <span color='#a0d0a0'><b>内核:</b></span> $KERNEL
• <span color='#a0d0a0'><b>Shell:</b></span> $SHELL_NAME

<b>🔧 硬件状态:</b>
• <span color='#a0d0a0'><b>CPU:</b></span> $CPU_INFO
• <span color='#a0d0a0'><b>CPU温度:</b></span> $CPU_TEMP
• <span color='#a0d0a0'><b>CPU负载:</b></span> $CPU_LOAD
• <span color='#a0d0a0'><b>GPU:</b></span> $GPU_INFO

<b>📊 资源使用:</b>
• <span color='#a0d0a0'><b>内存:</b></span> $MEMORY
• <span color='#a0d0a0'><b>根分区:</b></span> $ROOT_DISK_USAGE
• <span color='#a0d0a0'><b>家目录:</b></span> $HOME_DISK_USAGE

<b>🎚️ 设备设置:</b>
• <span color='#a0d0a0'><b>音量:</b></span> $VOLUME
• <span color='#a0d0a0'><b>亮度:</b></span> $BRIGHTNESS"

# 发送通知（支持HTML格式）
notify-send "系统状态监控" "$MESSAGE"

# 同时在终端输出（带颜色）
# echo -e "${BLUE}╔══════════════════════════════════════════════════╗${NC}"
# echo -e "${BLUE}║                 ${WHITE}系统状态监控${BLUE}                     ║${NC}"
# echo -e "${BLUE}╚══════════════════════════════════════════════════╝${NC}"
# echo -e "${GREEN}📅 时间:${NC} ${WHITE}$TIME${NC}"
# echo -e "${GREEN}📅 日期:${NC} ${WHITE}$DATE${NC}"
# echo -e "${GREEN}⏰ 运行时间:${NC} ${WHITE}$UPTIME${NC}"
# echo -e "${GREEN}🖥️ 系统:${NC} ${WHITE}$OS_INFO${NC}"
# echo -e "${GREEN}🐧 内核:${NC} ${WHITE}$KERNEL${NC}"
# echo -e "${GREEN}🔧 CPU:${NC} ${WHITE}$CPU_INFO${NC}"
# echo -e "${GREEN}🌡️ CPU温度:${NC} ${WHITE}$CPU_TEMP${NC}"
# echo -e "${GREEN}📈 CPU负载:${NC} ${WHITE}$CPU_LOAD${NC}"
# echo -e "${GREEN}🎮 GPU:${NC} ${WHITE}$GPU_INFO${NC}"
# echo -e "${GREEN}💾 内存:${NC} ${WHITE}$MEMORY${NC}"
# echo -e "${GREEN}💿 根分区:${NC} ${WHITE}$ROOT_DISK_USAGE${NC}"
# echo -e "${GREEN}🏠 家目录:${NC} ${WHITE}$HOME_DISK_USAGE${NC}"
# echo -e "${GREEN}🔊 音量:${NC} ${WHITE}$VOLUME${NC}"
# echo -e "${GREEN}💡 亮度:${NC} ${WHITE}$BRIGHTNESS${NC}"
