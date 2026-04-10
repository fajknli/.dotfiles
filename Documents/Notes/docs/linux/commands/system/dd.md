# dd - 数据复制与转换工具

## 一句话理解

dd 是一个低级别的数据复制工具，用于复制文件、备份磁盘、制作启动盘、磁盘克隆等。

```bash
# 制作 U 盘启动盘
sudo dd if=archlinux.iso of=/dev/sdb bs=4M status=progress

# 备份磁盘到文件
sudo dd if=/dev/sda of=backup.img bs=4M
```

## 常用场景

### 1. 制作 U 盘启动盘

```bash
# 写入 ISO 到 U 盘
sudo dd if=/path/to/arch.iso of=/dev/sdb bs=4M status=progress

# 显示写入进度
sudo dd if=arch.iso of=/dev/sdb bs=4M status=progress

# 写入完成后同步缓存
sync
```

### 2. 备份磁盘或分区

```bash
# 备份整个磁盘
sudo dd if=/dev/sda of=/backup/sda.img bs=4M

# 备份指定分区
sudo dd if=/dev/sda1 of=/backup/sda1.img bs=4M

# 备份时压缩
sudo dd if=/dev/sda bs=4M | gzip > /backup/sda.img.gz
```

### 3. 恢复磁盘或分区

```bash
# 恢复镜像到磁盘
sudo dd if=/backup/sda.img of=/dev/sda bs=4M status=progress

# 恢复压缩镜像
gunzip -c /backup/sda.img.gz | sudo dd of=/dev/sda bs=4M
```

### 4. 克隆磁盘到新磁盘

```bash
# 克隆整个磁盘（目标磁盘必须 >= 源磁盘）
sudo dd if=/dev/sda of=/dev/sdb bs=4M status=progress

# 只克隆有效数据（使用 conv=sparse）
sudo dd if=/dev/sda of=/dev/sdb bs=4M conv=sparse status=progress
```

### 5. 生成测试文件

```bash
# 生成 100MB 的随机数据文件
dd if=/dev/urandom of=test.dat bs=1M count=100

# 生成 100MB 的全零文件
dd if=/dev/zero of=zeros.dat bs=1M count=100

# 生成 1GB 文件用于测试
dd if=/dev/zero of=1gb.dat bs=1M count=1024
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `if=` | 输入文件 | `if=/dev/sda` |
| `of=` | 输出文件 | `of=/backup.img` |
| `bs=` | 块大小 | `bs=4M` |
| `count=` | 复制块数 | `count=100` |
| `skip=` | 跳过输入开头的块 | `skip=100` |
| `seek=` | 跳过输出开头的块 | `seek=100` |
| `status=progress` | 显示进度 | `status=progress` |
| `conv=sparse` | 稀疏文件写入 | `conv=sparse` |
| `conv=noerror` | 忽略读错误 | `conv=noerror` |
| `conv=sync` | 错误时填充零 | `conv=sync` |
| `iflag=direct` | 直接 IO（绕过缓存） | `iflag=direct` |

## 常用输入/输出源

| 设备/文件 | 说明 |
|-----------|------|
| `/dev/sda` | 第一块磁盘 |
| `/dev/sda1` | 第一块磁盘第一分区 |
| `/dev/zero` | 无限零字节 |
| `/dev/urandom` | 无限随机字节 |
| `/dev/null` | 丢弃所有输入 |
| `file.iso` | ISO 镜像文件 |
| `backup.img` | 磁盘镜像文件 |

## 常见问题

### 1. dd 执行太慢怎么办？

```bash
# 增大块大小（bs）
dd if=/dev/sda of=backup.img bs=1M      # 1MB
dd if=/dev/sda of=backup.img bs=4M      # 4MB
dd if=/dev/sda of=backup.img bs=64M     # 64MB

# 使用 direct 绕过缓存（有时更快）
dd if=/dev/sda of=backup.img bs=4M iflag=direct

# 使用其他工具（更快）
# 推荐：ddrescue（有进度条、可断点续传）
sudo pacman -S ddrescue
ddrescue /dev/sda backup.img backup.map
```

### 2. 如何显示进度条？

```bash
# 方法1：status=progress（推荐）
dd if=/dev/sda of=backup.img bs=4M status=progress

# 方法2：使用 pv（pipe viewer）
sudo pacman -S pv
dd if=/dev/sda bs=4M | pv | dd of=backup.img bs=4M

# 方法3：发送 USR1 信号
# 在另一个终端执行
sudo kill -USR1 $(pgrep dd)
```

### 3. 磁盘有坏道无法复制怎么办？

```bash
# 使用 conv=noerror,sync 忽略错误并填充零
sudo dd if=/dev/sda of=backup.img bs=4M conv=noerror,sync status=progress

# 使用 ddrescue（专门处理坏道）
sudo ddrescue -f /dev/sda backup.img backup.map
sudo ddrescue -d -f /dev/sda backup.img backup.map
```

### 4. 如何清空磁盘？

```bash
# 写入零（快速清空，数据仍可能恢复）
sudo dd if=/dev/zero of=/dev/sdb bs=4M status=progress

# 写入随机数据（安全擦除）
sudo dd if=/dev/urandom of=/dev/sdb bs=4M status=progress

# 安全擦除工具
sudo shred -v /dev/sdb
sudo wipe -a /dev/sdb
```

## 进度监控技巧

```bash
# 方法1：status=progress
dd if=/dev/sda of=backup.img bs=4M status=progress

# 方法2：另开终端查看进程信号
watch -n 1 'kill -USR1 $(pgrep dd) 2>/dev/null'

# 方法3：使用 pv
dd if=/dev/sda | pv -s $(blockdev --getsize64 /dev/sda) | dd of=backup.img
```

## 快捷别名

```bash
alias dd-progress='dd status=progress'
alias dd-usb='sudo dd bs=4M status=progress && sync'
alias dd-zero='sudo dd if=/dev/zero of='
alias dd-backup='sudo dd bs=4M status=progress'
```

## 一句话总结

dd 核心：`if=` 输入，`of=` 输出，`bs=` 块大小。制作启动盘：`dd if=镜像 of=/dev/sdX bs=4M status=progress`。备份磁盘：`dd if=/dev/sdX of=备份.img bs=4M`。恢复：反过来。操作前确认设备名，数据无法恢复。大块大小（4M/64M）提升速度。
