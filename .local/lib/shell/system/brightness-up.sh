#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-07 08:59
# Filename:     brightness-up.sh

set -e  # 出现错误立即退出

# 配置变量
MAX_BRIGHTNESS=100    # 最大亮度限制（%）
NOTIFY_TIMEOUT=1000  # 通知显示时间（毫秒）
BUS_NUMBER=8         # 显示器总线号

# 错误处理函数
error_exit() {
    echo "错误: $1" >&2
    exit 1
}

# 检查依赖
check_dependencies() {
    if ! command -v ddcutil >/dev/null 2>&1; then
        error_exit "未找到 ddcutil 命令，请安装 ddcutil"
    fi

    if ! command -v notify-send >/dev/null 2>&1; then
        error_exit "未找到 notify-send 命令，请安装 libnotify"
    fi
}

# 获取当前亮度
get_current_brightness() {
    output=$(ddcutil --bus "$BUS_NUMBER" getvcp 10 2>/dev/null) || true
    if [ -z "$output" ]; then
        error_exit "无法获取亮度信息"
    fi
    echo "$output" | awk -F'current value =' '{print $2}' | awk '{print $1}' | tr -d ','
}

# 创建亮度进度条
create_brightness_bar() {
    brightness="$1"
    width=10
    filled=$((brightness * width / 100))
    empty=$((width - filled))

    # 确保至少显示一个字符
    if [ "$filled" -eq 0 ] && [ "$brightness" -gt 0 ]; then
        filled=1
        empty=$((width - 1))
    fi

    # 使用 while 循环创建进度条
    bar=""
    i=1
    while [ "$i" -le "$filled" ]; do
        bar="${bar}█"
        i=$((i + 1))
    done

    i=1
    while [ "$i" -le "$empty" ]; do
        bar="${bar}░"
        i=$((i + 1))
    done

    echo "$bar"
}

# 主函数
main() {
    # 检查依赖
    check_dependencies

    # 获取当前亮度
    current_brightness=$(get_current_brightness)

    if [ -z "$current_brightness" ]; then
        error_exit "无法获取当前亮度"
    fi

    # 设置新亮度（增加5）
    new_brightness=$((current_brightness + 5))

    # 限制亮度范围
    if [ "$new_brightness" -gt "$MAX_BRIGHTNESS" ]; then
        new_brightness="$MAX_BRIGHTNESS"
    fi

    # 设置新亮度（快速执行）
    ddcutil --bus "$BUS_NUMBER" setvcp 10 "$new_brightness" >/dev/null 2>&1

    # 创建进度条
    brightness_bar=$(create_brightness_bar "$new_brightness")

    # 发送通知
    if [ "$new_brightness" -ge "$MAX_BRIGHTNESS" ]; then
        notify-send -t "$NOTIFY_TIMEOUT" "☀️ 亮度" \
            "亮度已增至最大: ${new_brightness}%\n${brightness_bar}\n⚠️  已达到最大限制"
    else
        notify-send -t "$NOTIFY_TIMEOUT" "☀️ 亮度" \
            "亮度已增加: ${new_brightness}%\n${brightness_bar}"
    fi
}

# 运行主函数
main "$@"
