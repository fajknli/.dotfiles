#!/usr/bin/env python3

# Author:       fajknli,deepseek
# Emial         fajknli@gmail.com
# Created Time: 2025-08-01 20:13
# Filename:     pinyin-1.py


import os
from pypinyin import lazy_pinyin

# 替换abc 为想要操作的文件名
chinese_file = "a"
pinyin_file = "b"
output_file = "c"

def clean_pinyin(text):
    pinyin = lazy_pinyin(text)
    return "'".join(pinyin)  # 直接返回用'连接的拼音

# 第一步：处理中文文件生成拼音文件
with open(chinese_file, "r", encoding="utf-8") as f_in, \
     open(pinyin_file, "w", encoding="utf-8") as f_out:

    for line in f_in:  # 逐行读取
        if line.strip():  # 跳过空行
            pinyin_line = clean_pinyin(line.strip())
            f_out.write(pinyin_line + "\n")  # 每行拼音写入文件

# 第二步：合并两个文件
def combine_columns(file1_path, file2_path, output_path):
    first_fields = []

    # 读取第一个文件的所有行首字段
    with open(file1_path, 'r', encoding='utf-8') as f1:
        first_fields = [line.split()[0] if line.strip() else '' for line in f1]

    # 合并两个文件
    with open(file2_path, 'r', encoding='utf-8') as f2, \
         open(output_path, 'w', encoding='utf-8') as out_f:

        for i, line in enumerate(f2):
            # 获取对应的首字段，如果超出范围则用空字符串
            first_col = first_fields[i] if i < len(first_fields) else ''
            out_f.write(f"{first_col} {line.strip()} 0\n")

# 执行合并
combine_columns(chinese_file, pinyin_file, output_file)
