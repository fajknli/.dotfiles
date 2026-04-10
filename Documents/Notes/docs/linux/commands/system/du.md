# du - 查看目录/文件磁盘使用量

## 一句话理解

du（disk usage）估算文件或目录占用的磁盘空间大小，常用于找出哪些目录占用空间最大。

```bash
# 查看当前目录总大小
du -sh .

# 查看当前目录下各子目录大小
du -sh *
```

## 常用选项

| 选项 | 说明 |
|------|------|
| `-h` | 人类可读格式（KB、MB、GB） |
| `-s` | 只显示总计（不逐个显示子目录） |
| `-a` | 显示所有文件（不只是目录） |
| `-c` | 显示总计 |
| `-d N` | 递归深度 N 层 |
| `--max-depth=N` | 同上 |
| `-B SIZE` | 指定块大小 |
| `-L` | 跟随符号链接 |
| `--exclude=PATTERN` | 排除匹配的文件 |
| `-t SIZE` | 只显示大于指定大小的项目 |
| `-x` | 不跨文件系统 |

## 基本用法

### 查看目录大小

```bash
# 当前目录总大小
du -sh .

# 指定目录总大小
du -sh /home/user

# 显示每个子目录大小（一级）
du -sh *

# 显示每个子目录大小（深度 1）
du -hd1
```

### 查看文件大小

```bash
# 显示所有文件和目录
du -ah

# 只显示文件（不显示目录）
find . -type f -exec du -h {} \;

# 查看特定文件
du -h file.txt
```

### 排序查看

```bash
# 按大小排序（从大到小）
du -sh * | sort -rh

# 取前 10 个最大的
du -sh * | sort -rh | head -10

# 显示详细信息并排序
du -h --max-depth=1 | sort -rh
```

## 实际例子

### 1. 查找最大的目录

```bash
# 查看根目录下哪些目录占用最大
sudo du -sh /* 2>/dev/null | sort -rh | head -10

# 查看当前目录下最大子目录
du -sh */ | sort -rh | head -5
```

### 2. 查看总大小（排除某些目录）

```bash
# 排除 Downloads 目录
du -sh --exclude=Downloads .

# 排除多个
du -sh --exclude=Downloads --exclude=.cache .

# 排除所有 .git 目录
du -sh --exclude=.git .
```

### 3. 查找超过指定大小的文件

```bash
# 查找大于 100MB 的文件
find . -type f -size +100M -exec du -h {} \;

# 查找大于 1GB 的文件
du -ah . | grep -E '^[0-9.]+G'
```

### 4. 监控脚本

```bash
#!/bin/bash
# 检查 /home 目录大小
SIZE=$(du -s /home 2>/dev/null | cut -f1)
SIZE_GB=$((SIZE / 1024 / 1024))

if [ $SIZE_GB -gt 50 ]; then
    echo "警告: /home 已使用 ${SIZE_GB}GB"
    du -sh /home/* 2>/dev/null | sort -rh | head -5
fi
```

### 5. 查看日志目录大小

```bash
# 查看 /var/log 总大小
sudo du -sh /var/log

# 查看各日志文件/目录大小
sudo du -sh /var/log/* | sort -rh | head -10

# 查看超过 7 天的日志大小
find /var/log -type f -mtime +7 -exec du -ch {} + | tail -1
```

## 深度控制

```bash
# 只看第 1 层子目录
du -hd1

# 只看第 2 层子目录
du -hd2

# 使用 --max-depth（同 -d）
du -h --max-depth=2

# 只显示指定深度的目录
du -h --max-depth=1
```

## 结合其他命令

```bash
# 查找并删除大于 100MB 的日志
find . -name "*.log" -size +100M -exec du -h {} \;
# 确认后删除
find . -name "*.log" -size +100M -delete

# 查找并压缩旧文件
find . -type f -mtime +30 -exec du -h {} \;
# 压缩
find . -type f -mtime +30 -exec gzip {} \;

# 统计代码行数（结合其他工具）
du -sh --exclude=.git .
cloc . 2>/dev/null
```

## 与 df 的区别

| 场景 | 使用 | 说明 |
|------|------|------|
| 查看分区剩余空间 | `df -h` | 整体磁盘使用 |
| 查看目录/文件大小 | `du -sh` | 具体目录占用 |
| 找出哪些目录占空间 | `du -sh * \| sort -rh` | 定位大目录 |
| 查看文件系统 inode | `df -i` | 文件数量限制 |

## 常见问题

### 1. du 很慢怎么办

```bash
# 限制深度
du -hd2

# 排除不重要的目录
du -sh --exclude=.cache --exclude=.npm

# 使用 ncdu（交互式）
sudo pacman -S ncdu
ncdu /
```

### 2. du 和 ls 显示的文件大小不同

```bash
# ls 显示的是文件本身大小
ls -lh file

# du 显示的是磁盘占用（通常更大，有块对齐）
du -h file

# 查看实际块大小
stat file
```

### 3. 无法读取某些目录

```bash
# 使用 sudo
sudo du -sh /root
sudo du -sh /var/log

# 跳过权限不足的目录
du -sh 2>/dev/null
```

## 替代工具

```bash
# ncdu - 交互式磁盘使用分析（推荐）
sudo pacman -S ncdu
ncdu /home

# duc - 带数据库的磁盘使用
sudo pacman -S duc
duc index /home
duc ui

# gdu - Go 写的快速版本
sudo pacman -S gdu
gdu /home
```

## 快捷别名

```bash
# ~/.bashrc
alias du='du -h'
alias dus='du -sh'
alias du1='du -hd1'
alias du-sort='du -sh * | sort -rh'
alias du-top='du -sh * | sort -rh | head -10'
```

## 一句话总结

du 核心：`du -sh .` 看当前目录总大小，`du -sh * | sort -rh` 看各子目录大小并排序，`du -hd1` 看一级子目录大小。配合 `sort -rh` 快速找出大文件大目录。用 `ncdu` 交互式分析更直观。
