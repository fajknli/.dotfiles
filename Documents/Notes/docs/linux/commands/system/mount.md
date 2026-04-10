# mount - 挂载文件系统

## 一句话理解

mount 命令将存储设备（硬盘、U盘、ISO）或文件系统挂载到指定目录，使其可访问。

```bash
# 查看所有挂载
mount

# 挂载设备到目录
sudo mount /dev/sdb1 /mnt/usb
```

## 常用场景

### 1. 查看已挂载的文件系统

```bash
# 查看所有挂载
mount

# 只看特定类型
mount -t ext4

# 查看挂载点使用情况（推荐）
df -h
lsblk
```

### 2. 挂载 U 盘 / 硬盘分区

```bash
# 基本挂载
sudo mount /dev/sdb1 /mnt/usb

# 挂载时指定文件系统类型
sudo mount -t vfat /dev/sdb1 /mnt/usb

# 挂载后所有用户可读写
sudo mount -o umask=000 /dev/sdb1 /mnt/usb
```

### 3. 挂载 ISO 镜像文件

```bash
# 创建挂载点
sudo mkdir -p /mnt/iso

# 挂载 ISO 文件
sudo mount -o loop arch.iso /mnt/iso

# 查看 ISO 内容
ls /mnt/iso
```

### 4. 挂载网络文件系统（NFS）

```bash
# 挂载 NFS 共享
sudo mount -t nfs 192.168.1.100:/share /mnt/nfs

# 指定 NFS 版本
sudo mount -t nfs -o nfsvers=4 192.168.1.100:/share /mnt/nfs
```

### 5. 重新挂载（修改挂载选项）

```bash
# 重新挂载为读写模式
sudo mount -o remount,rw /

# 重新挂载为只读模式
sudo mount -o remount,ro /mnt/usb

# 修改挂载选项
sudo mount -o remount,noexec /tmp
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-t type` | 指定文件系统类型 | `mount -t ext4 /dev/sdb1 /mnt` |
| `-o options` | 挂载选项（多个用逗号分隔） | `mount -o rw,noexec /dev/sdb1 /mnt` |
| `-o loop` | 挂载镜像文件 | `mount -o loop arch.iso /mnt` |
| `-o remount` | 重新挂载 | `mount -o remount,rw /` |
| `-o ro` | 只读挂载 | `mount -o ro /dev/sdb1 /mnt` |
| `-o rw` | 读写挂载（默认） | `mount -o rw /dev/sdb1 /mnt` |
| `-o noexec` | 禁止执行二进制文件 | `mount -o noexec /tmp` |
| `-o nosuid` | 禁止 setuid 程序 | `mount -o nosuid /home` |
| `-o umask=000` | 设置权限掩码 | `mount -o umask=000 /dev/sdb1 /mnt` |

## 常见挂载选项

| 选项 | 说明 |
|------|------|
| `rw` | 读写（默认） |
| `ro` | 只读 |
| `exec` | 允许执行二进制（默认） |
| `noexec` | 禁止执行二进制 |
| `suid` | 允许 setuid（默认） |
| `nosuid` | 禁止 setuid |
| `auto` | 允许 mount -a 自动挂载（默认） |
| `noauto` | 禁止自动挂载 |
| `user` | 允许普通用户挂载 |
| `nouser` | 只允许 root 挂载（默认） |
| `defaults` | 默认选项（rw,suid,dev,exec,auto,nouser,async） |

## 常见问题

### 1. 如何卸载挂载点？

```bash
# 卸载设备
sudo umount /mnt/usb

# 卸载设备（用设备名）
sudo umount /dev/sdb1

# 强制卸载（当设备忙时）
sudo umount -l /mnt/usb

# 懒卸载（立即卸载，但等待使用结束）
sudo umount -l /mnt/usb
```

### 2. 设备忙无法卸载怎么办？

```bash
# 查看哪个进程在使用挂载点
lsof /mnt/usb
fuser -v /mnt/usb

# 终止使用该挂载点的进程
fuser -km /mnt/usb

# 然后卸载
sudo umount /mnt/usb
```

### 3. 如何永久挂载（开机自动挂载）？

编辑 `/etc/fstab`：

```bash
# 格式：设备 挂载点 类型 选项 dump pass
/dev/sdb1  /mnt/usb  ext4  defaults  0  0

# UUID 方式（推荐）
UUID=xxxx-xxxx-xxxx  /mnt/usb  ext4  defaults  0  0

# 编辑后测试挂载
sudo mount -a
```

查看设备 UUID：

```bash
lsblk -f
blkid
```

## 快捷别名

```bash
alias mount-list='mount | column -t'
alias umount-all='sudo umount -a'
alias remount-rw='sudo mount -o remount,rw'
alias remount-ro='sudo mount -o remount,ro'
```

## 一句话总结

mount 核心：`mount /dev/sdb1 /mnt` 挂载设备，`umount /mnt` 卸载。`mount -o loop arch.iso /mnt` 挂载 ISO。永久挂载编辑 `/etc/fstab`。设备忙用 `fuser -km /mnt` 再卸载。
