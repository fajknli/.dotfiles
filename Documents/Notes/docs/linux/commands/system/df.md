# df - 查看磁盘空间使用情况

## 一句话理解

df（disk free）显示文件系统的磁盘空间使用情况，包括总容量、已用、可用、使用率。

```bash
# 查看所有挂载点的磁盘使用
df -h

# 输出示例
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/sda2       234G   45G  178G  21% /
# /dev/sda1       511M  4.0K  511M   1% /boot/efi
```

## 常用选项

| 选项 | 说明 |
|------|------|
| `-h` | 人类可读格式（GB、MB） |
| `-H` | 人类可读（1000 进制，不是 1024） |
| `-T` | 显示文件系统类型 |
| `-t type` | 只显示指定类型 |
| `-x type` | 排除指定类型 |
| `--total` | 显示总计 |
| `-i` | 显示 inode 使用情况 |
| `-l` | 只显示本地文件系统 |
| `--output` | 自定义输出字段 |

## 基本用法

### 查看所有挂载点

```bash
# 默认输出（字节）
df

# 人类可读（推荐）
df -h

# 显示文件系统类型
df -Th

# 输出示例
# Filesystem     Type      Size  Used Avail Use% Mounted on
# /dev/sda2      ext4      234G   45G  178G  21% /
# /dev/sda1      vfat      511M  4.0K  511M   1% /boot/efi
```

### 查看指定目录

```bash
# 查看 /home 所在分区的使用情况
df -h /home

# 查看当前目录所在分区
df -h .

# 查看多个目录
df -h / /home
```

### 只显示特定类型

```bash
# 只显示 ext4 文件系统
df -t ext4

# 排除 tmpfs、devtmpfs 等临时文件系统
df -x tmpfs -x devtmpfs
```

## 其他选项

### inode 使用情况

```bash
# 查看 inode 使用（文件数量限制）
df -i

# 人类可读的 inode
df -ih

# 当磁盘还有空间但无法创建文件时，可能是 inode 用完了
```

### 总计显示

```bash
# 显示总计
df --total -h

# 输出示例
# Filesystem      Size  Used Avail Use% Mounted on
# ...
# total           235G   45G  179G  21% -
```

### 自定义输出

```bash
# 只显示需要的字段
df --output=source,size,used,avail,pcent

# 可用字段：source、fstype、size、used、avail、pcent、iused、iavail、ipcent、target
```

## 实际例子

### 1. 检查根分区空间

```bash
df -h /
# 如果 Use% 超过 90%，需要清理
```

### 2. 找出哪个分区满了

```bash
df -h
# 看 Use% 列，找出使用率高的分区
```

### 3. 检查临时文件系统

```bash
# tmpfs 是内存文件系统，重启后消失
df -h /tmp
df -h /dev/shm
```

### 4. 监控脚本

```bash
#!/bin/bash
# 检查根分区使用率
USE=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ $USE -gt 80 ]; then
    echo "警告: 根分区使用率 ${USE}%"
fi
```

### 5. 查看所有挂载点（排除伪文件系统）

```bash
df -h -x tmpfs -x devtmpfs -x squashfs
```

## 常见问题

### 1. df 和 du 结果不一致

```bash
# df 显示已用空间大于 du 统计的总和
# 原因：文件已删除但进程仍持有句柄
lsof | grep deleted

# 重启进程或重启系统
```

### 2. Use% 显示 100% 但 du 显示空间很小

```bash
# 可能是 inode 满了
df -i

# 大量小文件导致
find / -type f -size 0 | wc -l
```

### 3. 挂载点不显示

```bash
# 查看所有块设备
lsblk

# 手动挂载
sudo mount /dev/sdb1 /mnt/usb
```

## 输出字段说明

| 字段 | 说明 |
|------|------|
| Filesystem | 设备文件 |
| Size | 总容量 |
| Used | 已用空间 |
| Avail | 可用空间 |
| Use% | 使用百分比 |
| Mounted on | 挂载点 |
| Type（-T） | 文件系统类型 |
| Inodes（-i） | inode 总数/已用/可用 |

## 快捷别名

```bash
# ~/.bashrc
alias df='df -h'
alias dfi='df -ih'
alias dfm='df -h -x tmpfs -x devtmpfs'
alias df-ext='df -Th'
```

## 一句话总结

df 核心：`df -h` 查看所有分区，`df -h /` 查看根分区，`df -Th` 显示文件系统类型，`df -i` 查看 inode。磁盘空间告警时先用 `df -h` 定位哪个分区满了。
