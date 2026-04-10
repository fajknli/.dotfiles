# lsblk - 列出块设备信息

## 一句话理解

lsblk（list block devices）显示系统中的所有块设备（硬盘、分区、光盘等），以树形结构展示磁盘和分区的层级关系。

```bash
# 查看所有块设备
lsblk

# 输出示例
# NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
# sda      8:0    0 238.5G  0 disk
# ├─sda1   8:1    0   512M  0 part /boot/efi
# ├─sda2   8:2    0 218.6G  0 part /
# └─sda3   8:3    0  19.4G  0 part [SWAP]
# sdb      8:16   0 931.5G  0 disk /home
```

## 常用场景

### 1. 查看所有磁盘和分区

```bash
# 基本查看
lsblk

# 显示文件系统类型和挂载点
lsblk -f

# 显示大小、挂载点、文件系统
lsblk -o NAME,SIZE,MOUNTPOINT,FSTYPE
```

### 2. 查看新插入的 U 盘

```bash
# 插入前后分别运行，对比找出新设备
lsblk

# 只看磁盘（不显示分区）
lsblk -d

# 输出示例（U盘通常显示为 sdc 或 sdd）
# sdc      8:32   1  14.4G  0 disk
# └─sdc1   8:33   1  14.4G  0 part /run/media/user/USB
```

### 3. 查看磁盘是 HDD 还是 SSD

```bash
# ROTA=1 是 HDD，ROTA=0 是 SSD
lsblk -d -o NAME,ROTA,SIZE

# 输出示例
# NAME ROTA  SIZE
# sda    0 238.5G  (SSD)
# sdb    1 931.5G  (HDD)
```

### 4. 查看完整信息（所有者、权限）

```bash
# 显示所有者、组、权限
lsblk -m

# 自定义输出所有有用字段
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,OWNER,GROUP,MODE,LABEL,UUID
```

### 5. 生成 fstab 用的 UUID

```bash
# 查看 UUID
lsblk -f
blkid

# 只获取指定分区的 UUID
lsblk -o UUID -n /dev/sda2

# 输出 UUID 供 fstab 使用
# UUID=3e2f8d3a-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /  ext4  defaults  0 1
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-f` | 显示文件系统类型、UUID、挂载点 | `lsblk -f` |
| `-m` | 显示所有者、组、权限 | `lsblk -m` |
| `-o` | 自定义输出字段 | `lsblk -o NAME,SIZE,MOUNTPOINT` |
| `-l` | 列表格式（非树形） | `lsblk -l` |
| `-p` | 显示完整设备路径 | `lsblk -p` |
| `-J` | JSON 格式输出 | `lsblk -J` |
| `-r` | 原始格式（无表格边框） | `lsblk -r` |
| `-n` | 不显示标题行 | `lsblk -n` |
| `-d` | 只显示磁盘（不显示分区） | `lsblk -d` |
| `-S` | 只显示 SCSI 设备 | `lsblk -S` |

## 常用输出字段

| 字段 | 说明 |
|------|------|
| `NAME` | 设备名称 |
| `SIZE` | 大小 |
| `TYPE` | 类型（disk/part/rom） |
| `MOUNTPOINT` | 挂载点 |
| `FSTYPE` | 文件系统类型 |
| `UUID` | 通用唯一标识符 |
| `LABEL` | 分区标签 |
| `PARTUUID` | 分区 UUID |
| `OWNER` | 所有者 |
| `GROUP` | 所属组 |
| `MODE` | 权限模式 |
| `ROTA` | 是否旋转磁盘（HDD=1, SSD=0） |

## 常见问题

### 1. 新插入的磁盘不显示

```bash
# 重新扫描 SCSI 总线
echo "- - -" | sudo tee /sys/class/scsi_host/host0/scan

# 或使用 partprobe 重新读取分区表
sudo partprobe

# 检查物理连接
dmesg | tail
```

### 2. 分区没有挂载点

```bash
# 手动挂载
sudo mount /dev/sdb1 /mnt

# 查看分区文件系统类型
lsblk -f /dev/sdb1

# 如果是新磁盘，需要先格式化
sudo mkfs.ext4 /dev/sdb1
```

### 3. lsblk 和 fdisk 显示结果不一致

```bash
# 重新读取分区表
sudo partprobe

# 或使用 blockdev 重新扫描
sudo blockdev --rereadpt /dev/sda
```

## 与其他命令对比

| 命令 | 用途 | 特点 |
|------|------|------|
| `lsblk` | 列出块设备 | 树形结构，信息全面 |
| `fdisk -l` | 查看分区 | 传统工具，更详细 |
| `df -h` | 查看挂载点使用 | 显示已挂载分区空间 |
| `blkid` | 查看 UUID | 只显示 UUID 和文件系统 |
| `ls /dev/sd*` | 查看设备文件 | 最简单，信息最少 |

## 快捷别名

```bash
alias lsblk='lsblk -f'
alias lsblk-tree='lsblk'
alias lsblk-size='lsblk -o NAME,SIZE,MOUNTPOINT'
alias lsblk-disk='lsblk -d -o NAME,SIZE,MODEL'
alias lsblk-ssd='lsblk -d -o NAME,ROTA,SIZE | grep " 0 "'
```

## 一句话总结

lsblk 核心：`lsblk` 查看磁盘树，`lsblk -f` 看文件系统和 UUID，`lsblk -o NAME,SIZE,MOUNTPOINT` 自定义输出。装新硬盘、查分区、找 UUID 写 fstab 都用它。比 `fdisk -l` 更直观。
