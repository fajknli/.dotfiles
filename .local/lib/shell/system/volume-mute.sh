#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-07 09:25
# Filename:     volume-mute.sh


set -e  # 出现错误立即退出

# 配置变量
NOTIFY_TIMEOUT=1000  # 通知显示时间（毫秒）

# 错误处理函数
error_exit() {
    echo "错误: $1" >&2
    exit 1
}

# 检查依赖
check_dependencies() {
    if ! command -v wpctl >/dev/null 2>&1; then
        error_exit "未找到 wpctl 命令，请安装 wireplumber"
    fi

    if ! command -v notify-send >/dev/null 2>&1; then
        error_exit "未找到 notify-send 命令，请安装 libnotify"
    fi
}

# 获取当前音量
get_current_volume() {
    output=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ 2>/dev/null) || true
    if [ -z "$output" ]; then
        error_exit "无法获取音量信息"
    fi
    echo "$output" | awk '{volume = $2 * 100; printf "%d", volume}'
}

# 获取静音状态
get_mute_status() {
    if wpctl get-volume @DEFAULT_AUDIO_SINK@ | grep -q "MUTED"; then
        echo "muted"
    else
        echo "unmuted"
    fi
}

# 创建音量进度条
create_volume_bar() {
    volume="$1"
    width=10
    filled=$((volume * width / 100))
    empty=$((width - filled))

    # 确保至少显示一个字符
    if [ "$filled" -eq 0 ] && [ "$volume" -gt 0 ]; then
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

    # 获取当前状态
    current_volume=$(get_current_volume)
    current_mute_status=$(get_mute_status)

    if [ -z "$current_volume" ]; then
        error_exit "无法获取当前音量"
    fi

    # 切换静音状态
    wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle

    # 获取切换后的状态
    new_mute_status=$(get_mute_status)

    # 创建进度条
    volume_bar=$(create_volume_bar "$current_volume")

    # 发送通知
    if [ "$new_mute_status" = "muted" ]; then
        notify-send -t "$NOTIFY_TIMEOUT" "🔇 静音" \
            "已静音\n当前音量: ${current_volume}%\n${volume_bar}"
    else
        notify-send -t "$NOTIFY_TIMEOUT" "🔊 取消静音" \
            "已取消静音\n当前音量: ${current_volume}%\n${volume_bar}"
    fi
}

# 运行主函数
main "$@"
