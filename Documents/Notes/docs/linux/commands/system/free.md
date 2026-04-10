# free - 查看内存使用情况

## 一句话理解

free 命令显示系统内存的使用情况，包括物理内存、交换分区、缓存等。

```bash
# 查看内存（人类可读）
free -h

# 输出示例
#               total        used        free      shared  buff/cache   available
# Mem:           15Gi       2.1Gi        11Gi       123Mi       2.5Gi        13Gi
# Swap:         8.0Gi          0B       8.0Gi
```

## 常用场景

### 1. 查看内存概况

```bash
# 默认显示（字节）
free

# 人类可读格式（推荐）
free -h

# 以 MB 为单位
free -m

# 以 GB 为单位
free -g
```

### 2. 查看内存详细统计

```bash
# 连续显示（每2秒刷新）
free -h -s 2

# 刷新3次后退出
free -h -s 2 -c 3
```

### 3. 查看内存总量和可用量

```bash
# 查看总内存
free -h | grep Mem | awk '{print $2}'

# 查看可用内存（含可回收缓存）
free -h | grep Mem | awk '{print $7}'
```

### 4. 监控内存变化

```bash
# 实时监控
watch -n 1 free -h

# 记录到文件
while true; do date; free -h; echo "---"; sleep 5; done >> mem.log
```

### 5. 查看内存使用率

```bash
# 计算使用率百分比
free | grep Mem | awk '{printf "使用率: %.1f%%\n", $3/$2 * 100}'

# 计算可用率百分比
free | grep Mem | awk '{printf "可用率: %.1f%%\n", $7/$2 * 100}'
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-h` | 人类可读格式 | `free -h` |
| `-m` | 以 MB 为单位 | `free -m` |
| `-g` | 以 GB 为单位 | `free -g` |
| `-s N` | 每 N 秒刷新 | `free -s 2` |
| `-c N` | 刷新 N 次后退出 | `free -c 5` |
| `-t` | 显示总计行 | `free -t` |
| `-b` | 以字节为单位 | `free -b` |
| `-k` | 以 KB 为单位 | `free -k` |

## 输出字段说明

| 字段 | 说明 |
|------|------|
| `total` | 总内存 |
| `used` | 已用内存（total - free - buffers - cache） |
| `free` | 完全未使用的内存 |
| `shared` | 共享内存（tmpfs 等） |
| `buff/cache` | 缓存和缓冲区占用的内存 |
| `available` | 可用内存（含可回收的缓存，推荐看这个） |

## 常见问题

### 1. used 很大但 available 也很大，内存够用吗？

够用。Linux 会把空闲内存用作缓存（buff/cache），当程序需要时会自动释放。**看 available 列**，这才是程序真正可用的内存。

```bash
# 看 available 列
free -h
# Mem: 15Gi total, 2.1Gi used, 11Gi free, 2.5Gi buff/cache, 13Gi available
# 可用内存是 13Gi，不是 11Gi
```

### 2. 如何清空缓存？

```bash
# 清空页面缓存
echo 1 | sudo tee /proc/sys/vm/drop_caches

# 清空目录项和 inode 缓存
echo 2 | sudo tee /proc/sys/vm/drop_caches

# 清空所有缓存
echo 3 | sudo tee /proc/sys/vm/drop_caches
```

### 3. Swap 使用率高说明什么？

- Swap 使用率高通常表示物理内存不足
- 也可能是长期不用的内存被换出
- 用 `vmstat 1` 或 `top` 查看是否频繁换页

## 快捷别名

```bash
alias free='free -h'
alias freem='free -m'
alias freeg='free -g'
alias freeloop='free -h -s 2'
alias freemem='free -h | grep Mem | awk "{print \"可用: \" \$7}"'
```

## 一句话总结

free 核心：`free -h` 查看内存，关注 `available` 列（真正可用内存）。Linux 会用空闲内存做缓存，不用担心 `buff/cache` 占用大。用 `-s` 参数实时监控，`-c` 控制次数。
