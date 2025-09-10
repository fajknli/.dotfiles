#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-05 16:20
# Filename:     apply-preset.sh

# --------------------------------------------
# 脚本： apply-preset.sh
# 功能： 选择预设样式并烧录字幕到视频
# 用法： ./apply-preset.sh <输入视频> <字幕文件> <预设名称>
# 示例： ./apply-preset.sh video.mpix subs.srt bottom-large
# --------------------------------------------

INPUT_VIDEO="$1"
SUBTITLE_FILE="$2"
PRESET_NAME="$3"

# 预设文件路径
PRESET_FILE="templates/style-presets/preset-$PRESET_NAME.txt"

# 检查参数
if [ $# -ne 3 ]; then
    echo "错误：参数错误！"
    echo "用法: $0 <输入视频> <字幕文件> <预设名称>"
    echo "可用预设: bottom-large, top-title, cinematic-white, cn-subtitles"
    exit 1
fi

# 检查预设文件是否存在
if [ ! -f "$PRESET_FILE" ]; then
    echo "错误：预设文件不存在: $PRESET_FILE"
    exit 1
fi

# 读取预设样式
STYLE_PARAMS=$(cat "$PRESET_FILE")
OUTPUT_VIDEO="output_${PRESET_NAME}.mp4"

echo "正在使用预设: $PRESET_NAME"
echo "样式参数: $STYLE_PARAMS"

# 执行FFmpeg命令
ffmpeg -i "$INPUT_VIDEO" -vf "subtitles=$SUBTITLE_FILE:force_style='$STYLE_PARAMS'" -c:a copy "$OUTPUT_VIDEO"

if [ $? -eq 0 ]; then
    echo "✅ 完成！输出文件: $OUTPUT_VIDEO"
else
    echo "❌ 处理失败！"
    exit 1
fi
