# fstab - 文件系统挂载配置文件

## 一句话理解

/etc/fstab 是 Linux 系统开机自动挂载文件系统的配置文件，定义了磁盘分区、网络存储等设备的挂载方式。

```bash
# 查看 fstab 内容
cat /etc/fstab

# 挂载 fstab 中所有条目
sudo mount -a
```

## 常用场景

### 1. 查看当前 fstab 配置

```bash
# 查看文件内容
cat /etc/fstab

# 过滤掉注释行
grep -v "^#" /etc/fstab | grep -v "^$"

# 输出示例
# UUID=xxx  /  ext4  defaults  0 1
# UUID=yyy  /home  ext4  defaults  0 2
# UUID=zzz  none  swap  sw  0 0
```

### 2. 添加新硬盘开机自动挂载

```bash
# 1. 获取分区 UUID
sudo blkid /dev/sdb1

# 2. 创建挂载点
sudo mkdir -p /mnt/data

# 3. 编辑 fstab
echo "UUID=xxxx-xxxx  /mnt/data  ext4  defaults  0  2" | sudo tee -a /etc/fstab

# 4. 测试挂载
sudo mount -a
```

### 3. 添加 swap 分区

```bash
# 1. 查看 swap 分区 UUID
sudo blkid /dev/sdb2

# 2. 添加到 fstab
echo "UUID=xxxx-xxxx  none  swap  sw  0  0" | sudo tee -a /etc/fstab

# 3. 启用 swap
sudo swapon -a
```

### 4. 挂载 U 盘（带选项）

```bash
# 添加 U 盘挂载配置
# /dev/sdc1  /mnt/usb  vfat  uid=1000,gid=1000,umask=000,noauto  0  0

# 字段说明：
# /dev/sdc1 - 设备
# /mnt/usb - 挂载点
# vfat - 文件系统类型
# uid=1000,gid=1000,umask=000,noauto - 挂载选项
# 0 - dump 备份
# 0 - fsck 检查顺序
```

### 5. 挂载 ISO 镜像

```bash
# 添加 ISO 挂载配置
# /path/to/file.iso  /mnt/iso  iso9660  loop,ro  0  0

# 创建挂载点
sudo mkdir -p /mnt/iso

# 测试挂载
sudo mount -a
```

## fstab 字段说明

```
设备      挂载点     文件系统    选项        dump  pass
UUID=xxx  /mnt/data  ext4      defaults    0     2
```

| 字段 | 说明 |
|------|------|
| 设备 | UUID、LABEL、/dev/sdX 或网络地址 |
| 挂载点 | 挂载到的目录 |
| 文件系统 | ext4、xfs、vfat、ntfs、swap、auto |
| 选项 | 挂载参数，多个用逗号分隔 |
| dump | 备份标志（0=不备份，1=备份） |
| pass | fsck 检查顺序（0=不检查，1=根分区，2=其他） |

## 常用挂载选项

| 选项 | 说明 |
|------|------|
| `defaults` | 默认选项（rw,suid,dev,exec,auto,nouser,async） |
| `rw` / `ro` | 读写 / 只读 |
| `auto` / `noauto` | 是否自动挂载（mount -a 时） |
| `exec` / `noexec` | 是否允许执行二进制文件 |
| `suid` / `nosuid` | 是否允许 setuid 程序 |
| `user` / `nouser` | 是否允许普通用户挂载 |
| `async` / `sync` | 异步 / 同步读写 |
| `atime` / `noatime` | 是否更新访问时间 |
| `relatime` | 相对更新时间（推荐） |
| `uid=1000` | 指定所有者 UID |
| `gid=1000` | 指定所属组 GID |
| `umask=000` | 权限掩码（FAT/NTFS 用） |
| `loop` | 挂载镜像文件 |

## 常见问题

### 1. 如何查找设备 UUID？

```bash
# 查看所有设备 UUID
lsblk -f
blkid

# 查看指定设备
blkid /dev/sda1

# 输出示例
# /dev/sda1: UUID="xxxx-xxxx" TYPE="ext4" PARTUUID="yyy-yyy"
```

### 2. fstab 写错导致无法启动怎么办？

```bash
# 方法1：进入救援模式
# 启动时按 Shift 进入 GRUB，选择 recovery mode
# 编辑 /etc/fstab 修正错误

# 方法2：使用 Live CD
# 用 U 盘启动 Live 系统
sudo mount /dev/sda2 /mnt
sudo vim /mnt/etc/fstab

# 方法3：内核启动参数跳过 fstab
# 在 GRUB 启动参数后添加 "break=pre-mount"
```

### 3. 如何测试 fstab 配置是否正确？

```bash
# 卸载目标挂载点（如果已挂载）
sudo umount /mnt/data

# 测试挂载
sudo mount -a

# 检查挂载结果
mount | grep /mnt/data
df -h /mnt/data

# 如果有错误，会显示具体信息
```

## 配置示例

### 基础配置

```bash
# /etc/fstab

# 根分区
UUID=3e2f8d3a-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /  ext4  defaults,noatime  0  1

# /home 分区
UUID=5c1e8d9b-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /home  ext4  defaults  0  2

# swap 分区
UUID=7b77-0c21-xxxx-xxxx-xxxxxxxxxxxx  none  swap  sw  0  0

# EFI 分区
UUID=7B77-0C21  /boot/efi  vfat  defaults  0  2

# 数据盘
UUID=9a3e2f8d  /mnt/data  ext4  defaults,noatime  0  2

# NTFS 数据盘
UUID=1234567890ABCDEF  /mnt/windows  ntfs-3g  uid=1000,gid=1000,umask=022  0  0

# U 盘（不自动挂载）
/dev/sdc1  /mnt/usb  vfat  uid=1000,gid=1000,umask=000,noauto  0  0

# ISO 镜像
/path/to/ubuntu.iso  /mnt/iso  iso9660  loop,ro  0  0

# NFS 网络共享
192.168.1.100:/share  /mnt/nfs  nfs  defaults  0  0
```

## 快捷别名

```bash
alias fstab='cat /etc/fstab | grep -v "^#" | grep -v "^$"'
alias fstab-edit='sudo vim /etc/fstab'
alias fstab-test='sudo mount -a'
alias fstab-list='findmnt'
```

## 一句话总结

fstab 核心：6 个字段：设备、挂载点、文件系统、选项、dump、pass。用 `blkid` 或 `lsblk -f` 获取 UUID。修改后 `mount -a` 测试。根分区 pass=1，其他 pass=2，swap pass=0。U 盘常用 `noauto` 防止启动时卡住。
