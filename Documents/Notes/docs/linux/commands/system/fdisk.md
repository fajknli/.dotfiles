# fdisk - 磁盘分区工具

## 一句话理解

fdisk 是 Linux 传统的磁盘分区工具，用于创建、删除、修改磁盘分区表。

```bash
# 查看所有磁盘分区
sudo fdisk -l

# 对磁盘进行分区操作
sudo fdisk /dev/sda
```

## 常用场景

### 1. 查看磁盘分区信息

```bash
# 查看所有磁盘
sudo fdisk -l

# 查看指定磁盘
sudo fdisk -l /dev/sda

# 查看磁盘大小和分区数量（简洁）
sudo fdisk -l | grep -E "^Disk /dev/sd|^/dev/sd"
```

### 2. 交互式分区操作

```bash
# 进入交互模式
sudo fdisk /dev/sdb

# 常用交互命令：
# m  - 显示帮助
# p  - 显示当前分区表
# n  - 新建分区
# d  - 删除分区
# t  - 修改分区类型
# w  - 保存并退出
# q  - 不保存退出
```

### 3. 创建新分区

```bash
sudo fdisk /dev/sdb

# 交互步骤：
# 1. 输入 n 创建新分区
# 2. 选择分区类型（p 主分区 / e 扩展分区）
# 3. 输入分区号（默认回车）
# 4. 输入起始扇区（默认回车）
# 5. 输入结束扇区或大小（如 +10G）
# 6. 输入 w 保存退出
```

### 4. 删除分区

```bash
sudo fdisk /dev/sdb

# 交互步骤：
# 1. 输入 p 查看现有分区
# 2. 输入 d 删除分区
# 3. 输入要删除的分区号
# 4. 输入 w 保存退出
```

### 5. 修改分区类型

```bash
sudo fdisk /dev/sdb

# 交互步骤：
# 1. 输入 p 查看分区
# 2. 输入 t 修改类型
# 3. 输入分区号
# 4. 输入类型代码（如 82 为 swap，83 为 Linux，8e 为 LVM）
# 5. 输入 w 保存退出
```

## 常用分区类型代码

| 代码 | 类型 | 说明 |
|------|------|------|
| `83` | Linux | Linux 普通分区（ext4/xfs 等） |
| `82` | Linux swap | 交换分区 |
| `8e` | Linux LVM | LVM 逻辑卷 |
| `ef` | EFI | UEFI 系统分区 |
| `7` | NTFS | Windows NTFS 分区 |
| `c` | FAT32 | Windows FAT32 分区（W95） |

## 交互命令速查

| 命令 | 说明 |
|------|------|
| `m` | 显示帮助菜单 |
| `p` | 显示当前分区表 |
| `n` | 新建分区 |
| `d` | 删除分区 |
| `t` | 修改分区类型 |
| `l` | 列出所有分区类型代码 |
| `u` | 切换显示单位（扇区/柱面） |
| `v` | 检查分区表 |
| `w` | 保存修改并退出 |
| `q` | 不保存退出 |

## 常见问题

### 1. fdisk 和 parted 有什么区别？

| 特性 | fdisk | parted |
|------|-------|--------|
| 分区表类型 | MBR + GPT | MBR + GPT |
| GPT 支持 | 需要 `-t gpt` | 原生支持 |
| 2TB 以上磁盘 | 需 GPT | 原生支持 |
| 交互界面 | 传统 | 更友好 |
| 命令行脚本 | 支持 | 支持 |
| 推荐场景 | MBR、传统系统 | GPT、大磁盘、脚本 |

### 2. 分区后需要做什么？

```bash
# 1. 让内核重新读取分区表
sudo partprobe
# 或
sudo blockdev --rereadpt /dev/sdb

# 2. 格式化分区
sudo mkfs.ext4 /dev/sdb1

# 3. 挂载分区
sudo mount /dev/sdb1 /mnt/data

# 4. 设置开机自动挂载（编辑 /etc/fstab）
UUID=xxxx /mnt/data ext4 defaults 0 2
```

### 3. 如何删除所有分区并重新开始？

```bash
sudo fdisk /dev/sdb

# 交互步骤：
# 1. 输入 d 重复删除直到没有分区
# 2. 输入 w 保存
# 或直接创建新分区表：
# 输入 g 创建新 GPT 分区表
# 输入 o 创建新 MBR 分区表
```

## 快捷别名

```bash
alias fdisk-list='sudo fdisk -l'
alias fdisk-check='sudo fdisk -l | grep -E "^Disk /dev/sd"'
alias part-reload='sudo partprobe'
```

## 一句话总结

fdisk 核心：`sudo fdisk -l` 查看分区，`sudo fdisk /dev/sdb` 进入交互模式。交互中 `p` 查看，`n` 新建，`d` 删除，`t` 改类型，`w` 保存，`q` 退出。分区后需 `partprobe` 刷新并格式化。大磁盘（2TB+）推荐用 `parted` 或 `gdisk`。
