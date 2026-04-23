#!/bin/bash
# 找大文件 - 用于 Arch Linux
# 用法: chmod +x find_large_files.sh && ./find_large_files.sh

echo "=========================================="
echo "  查找家目录下的大文件 ( > 100M )"
echo "=========================================="
echo ""

# 1. 最大的 30 个文件 ( > 100M )
echo "【最大的 30 个文件】"
echo "排名   大小       路径"
find ~ -type f -size +100M -exec du -h {} + 2>/dev/null | sort -rh | head -30 | nl -w2

echo ""
echo "=========================================="
echo ""

# 2. 最大的 20 个目录
echo "【最大的 20 个目录】"
du -h ~ 2>/dev/null | sort -rh | head -20 | nl -w2

echo ""
echo "=========================================="
echo ""

# 3. 按类型统计大小 (可选)
echo "【按类型统计 (前10)】"
find ~ -type f -name "*.*" 2>/dev/null | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -10 | while read count ext; do
    size=$(find ~ -type f -name "*.$ext" -exec du -ch {} + 2>/dev/null | tail -1 | cut -f1)
    printf "  %-10s %8s 个文件  总大小: %s\n" "$ext" "$count" "$size"
done

echo ""
echo "=========================================="
echo ""

# 4. 特殊：Docker / 缓存 / 日志
echo "【常见大容量目录】"
dirs=(
    "$HOME/.cache"
    "$HOME/.local/share/docker"
    "$HOME/.npm"
    "$HOME/.cargo"
    "$HOME/.gradle"
    "$HOME/.m2"
    "$HOME/.conda"
    "$HOME/.pyenv"
    "$HOME/.rustup"
    "$HOME/Downloads"
    "$HOME/.local/share/Trash"
)

for d in "${dirs[@]}"; do
    if [ -d "$d" ]; then
        size=$(du -sh "$d" 2>/dev/null | cut -f1)
        echo "  $d : $size"
    fi
done

echo ""
echo "=========================================="
echo "完成"
