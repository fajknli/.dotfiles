#!/bin/sh

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-09-04 18:49
# Filename:     test-point-distance.sh


# === 像素距离测量工具 ===
# 点击选择第一个点
coords1=$(slurp -p -f "%x %y" -c "#FF0000")
read x1 y1 <<< $coords1

# 点击选择第二个点
coords2=$(slurp -p -f "%x %y" -c "#00FF00")
read x2 y2 <<< $coords2

# 计算各种距离
horizontal=$(echo "$x2 - $x1" | bc | sed 's/-//')  # 取绝对值
vertical=$(echo "$y2 - $y1" | bc | sed 's/-//')    # 取绝对值
diagonal=$(echo "sqrt(($x2 - $x1)^2 + ($y2 - $y1)^2)" | bc)


notify-send -u low "=== 测量结果 ===
点1: ($x1, $y1)
点2: ($x2, $y2)
水平距离: $horizontal 像素
垂直距离: $vertical 像素
直线距离: $diagonal 像素"
