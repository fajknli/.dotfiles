#!/bin/bash

# 检查是否提供了目录参数
if [ -z "$1" ]; then
    echo "用法: $0 <目标目录>"
    echo "示例: $0 /path/to/your/folder"
    exit 1
fi

target_dir="$1"

# 检查目录是否存在
if [ ! -d "$target_dir" ]; then
    echo "错误: 目录 '$target_dir' 不存在！"
    exit 1
fi

# 递归处理文件和目录
find "$target_dir" -depth -name "* *" | while read -r file; do
    # 获取文件所在目录和原始文件名
    dir=$(dirname "$file")
    name=$(basename "$file")

    # 替换空格为下划线，并处理其他特殊字符
    new_name=$(echo "$name" | tr ' ' '_' | sed 's/[^[:alnum:]._/-/g')

    # 如果新文件名和旧文件名不同，则重命名
    if [ "$name" != "$new_name" ]; then
        echo "重命名: $file -> $dir/$new_name"
        mv -- "$file" "$dir/$new_name"
    fi
done

echo "处理完成！所有空格已替换为下划线。"
