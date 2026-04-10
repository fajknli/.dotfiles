# mkfs - 创建文件系统

## 一句话理解

mkfs（make filesystem）命令用于格式化分区，在设备上创建文件系统。

```bash
# 格式化为 ext4
sudo mkfs.ext4 /dev/sdb1

# 格式化为 FAT32
sudo mkfs.vfat /dev/sdb1
```

## 常用场景

### 1. 格式化为 ext4（Linux 默认）

```bash
# 基本格式化
sudo mkfs.ext4 /dev/sdb1

# 指定卷标
sudo mkfs.ext4 -L mydata /dev/sdb1

# 指定块大小
sudo mkfs.ext4 -b 4096 /dev/sdb1
```

### 2. 格式化为 FAT32（U盘兼容）

```bash
# 格式化为 FAT32
sudo mkfs.vfat -F 32 /dev/sdb1

# 指定卷标
sudo mkfs.vfat -F 32 -n USB /dev/sdb1
```

### 3. 格式化为 NTFS（Windows 兼容）

```bash
# 格式化为 NTFS
sudo mkfs.ntfs /dev/sdb1

# 快速格式化
sudo mkfs.ntfs -f /dev/sdb1

# 指定卷标
sudo mkfs.ntfs -L mydisk /dev/sdb1
```

### 4. 创建交换分区

```bash
# 格式化为 swap
sudo mkswap /dev/sdb1

# 启用 swap
sudo swapon /dev/sdb1

# 查看 swap 状态
swapon --show
```

### 5. 格式化为 xfs（大文件性能好）

```bash
# 格式化为 xfs
sudo mkfs.xfs /dev/sdb1

# 指定卷标
sudo mkfs.xfs -L mydata /dev/sdb1
```

## 常用文件系统命令

| 文件系统 | 命令 | 常用选项 |
|----------|------|----------|
| ext4 | `mkfs.ext4` | `-L` 卷标, `-b` 块大小 |
| ext3 | `mkfs.ext3` | `-L` 卷标 |
| ext2 | `mkfs.ext2` | `-L` 卷标 |
| xfs | `mkfs.xfs` | `-L` 卷标, `-f` 强制 |
| btrfs | `mkfs.btrfs` | `-L` 卷标, `-m` 元数据模式 |
| vfat (FAT32) | `mkfs.vfat` | `-F 32`, `-n` 卷标 |
| ntfs | `mkfs.ntfs` | `-L` 卷标, `-f` 快速 |
| swap | `mkswap` | `-L` 卷标 |

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-L` | 设置卷标 | `mkfs.ext4 -L data /dev/sdb1` |
| `-n` | 设置卷标（vfat） | `mkfs.vfat -n USB /dev/sdb1` |
| `-b` | 设置块大小 | `mkfs.ext4 -b 4096 /dev/sdb1` |
| `-f` | 快速格式化（ntfs） | `mkfs.ntfs -f /dev/sdb1` |
| `-F 32` | FAT32 格式 | `mkfs.vfat -F 32 /dev/sdb1` |
| `-m` | 保留块百分比（ext4） | `mkfs.ext4 -m 1 /dev/sdb1` |

## 常见问题

### 1. 格式化前如何查看分区信息？

```bash
# 查看分区表
lsblk
sudo fdisk -l /dev/sdb

# 确认要格式化的分区正确
# 注意：格式化会清空所有数据！
```

### 2. 格式化后如何挂载？

```bash
# 创建挂载点
sudo mkdir -p /mnt/data

# 挂载分区
sudo mount /dev/sdb1 /mnt/data

# 设置开机自动挂载（编辑 /etc/fstab）
echo "UUID=$(blkid -s UUID -o value /dev/sdb1) /mnt/data ext4 defaults 0 2" | sudo tee -a /etc/fstab
```

### 3. 如何查看文件系统类型？

```bash
# 使用 lsblk
lsblk -f

# 使用 blkid
blkid /dev/sdb1

# 使用 df
df -Th
```

## 文件系统选择指南

| 文件系统 | 适用场景 | 特点 |
|----------|----------|------|
| ext4 | Linux 默认 | 稳定、兼容性好 |
| xfs | 大文件、大容量 | 性能好，适合媒体存储 |
| btrfs | 快照、压缩 | 功能丰富，较复杂 |
| FAT32 | U盘、跨平台 | 兼容性好，单文件<4GB |
| NTFS | Windows 共享 | Windows 原生，Linux 需 ntfs-3g |
| swap | 交换分区 | 虚拟内存 |

## 快捷别名

```bash
alias mkfs-ext4='sudo mkfs.ext4'
alias mkfs-fat32='sudo mkfs.vfat -F 32'
alias mkfs-ntfs='sudo mkfs.ntfs -f'
alias mkswap-enable='sudo mkswap && sudo swapon'
```

## 一句话总结

mkfs 核心：`mkfs.ext4 /dev/sdb1` 格式化为 ext4，`mkfs.vfat -F 32 /dev/sdb1` 格式化为 FAT32。分区后需格式化才能使用。用 `-L` 设置卷标，`blkid` 查看 UUID。格式化会清空所有数据，操作前确认分区正确。
