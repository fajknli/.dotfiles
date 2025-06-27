#! /usr/bin/env bash

cd $HOME/notes/notes_rst

CURRENT_TIME=$(date "+%Y-%m-%d_%H-%M-%S")  # 格式示例：2024-06-15_15-30-45
TARGET_FILE="note_${CURRENT_TIME}.bk"

rm *.tar.gz

tar -zcvf ${TARGET_FILE}.tar.gz build

# 获取当前时间戳（秒级）
# CURRENT_TIMESTAMP=$(date "+%s")
#
# # 假设有一个旧的时间戳（比如之前记录的时间）
# OLD_TIMESTAMP="1718451005"  # 示例旧时间
#
# # 比较时间戳
# if [ "$CURRENT_TIMESTAMP" -gt "$OLD_TIMESTAMP" ]; then
#     echo "当前时间比旧时间新"
# elif [ "$CURRENT_TIMESTAMP" -lt "$OLD_TIMESTAMP" ]; then
#     echo "当前时间比旧时间旧"
# else
#     echo "时间相同"
# fi

rm -r build && make html


