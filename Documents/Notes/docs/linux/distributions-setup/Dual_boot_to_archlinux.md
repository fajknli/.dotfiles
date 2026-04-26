# 双系统迁移至 Arch Linux 全记录

> 适用场景：Windows + Linux 双系统，希望彻底移除 Windows，将所有磁盘空间归还给 Linux。  
> 本文以 UEFI + GPT + NVMe 硬盘为例，Linux 使用 systemd-boot 引导，根分区为 ext4。

---

## 一、前置检查

在动刀之前，必须确认以下几点，防止操作后系统无法启动。

### 1. 确认固件模式（UEFI 还是 Legacy BIOS）

```bash
ls /sys/firmware/efi 2>/dev/null && echo "UEFI" || echo "Legacy BIOS"
```

本文适用于 **UEFI** 模式。Legacy BIOS 的操作逻辑有所不同。

### 2. 查看分区布局

```bash
lsblk -f
```

需要明确：
- Linux 的 EFI 分区（`/boot`）和 Windows 的 EFI 分区（`SYSTEM`）是否分开
- Linux 根分区（`/`）的位置和编号
- Windows 各分区的位置和编号（系统盘、MSR、恢复分区）

### 3. 确认 Linux 引导器独立运行

```bash
bootctl status
```

重点确认：
- `Current Entry` 指向 Linux 的启动项（如 `arch-linux.efi`）
- `Boot Loaders Listed in EFI Variables` 中，Linux 启动项对应的分区 PARTUUID 与 `/boot` 分区一致

### 4. 交叉验证分区 PARTUUID

```bash
lsblk -o NAME,PARTUUID /dev/nvme0n1
```

将 `/boot` 分区的 PARTUUID 与 `bootctl status` 输出中的 PARTUUID 逐一比对，确认无误后再继续。

---

## 二、删除 Windows 分区

确认 Linux 引导独立后，可以安全删除 Windows 的所有分区。

### 典型的 Windows 分区组成

| 类型 | 格式 | 大小 | gdisk 代码 |
|------|------|------|------------|
| EFI 系统分区 | FAT32 | 100MB | EF00 |
| MSR 微软保留 | 无 | 16MB | 0C01 |
| Windows 系统盘 | NTFS | 主要空间 | 0700 |
| Windows 恢复分区 | NTFS | 约 1GB | 2700 |

### 使用 gdisk 删除

```bash
sudo gdisk /dev/nvme0n1
```

进入交互界面后：

```
p       # 列出所有分区，确认编号
d → 1   # 删除 EFI 系统分区
d → 2   # 删除 MSR
d → 3   # 删除 Windows 系统盘
d → 4   # 删除恢复分区
w       # 写入更改
y       # 确认
```

> **注意**：`d` 命令只标记删除，`w` 才真正写入磁盘，写入前可随时 `q` 退出放弃操作。

### 刷新内核分区表

```bash
sudo partprobe /dev/nvme0n1
```

---

## 三、扩容 Linux 根分区

删除 Windows 分区后，会出现未分配空间。若空闲空间在根分区后面，可以直接扩容。

### 使用 parted 扩容

```bash
sudo parted /dev/nvme0n1
```

```
resizepart 6 100%   # 将第 6 分区扩展到磁盘末尾，编号按实际情况调整
quit
```

遇到"分区正在使用"的警告时，输入 `Yes` 继续（ext4 支持在线 resize）。

### 通知文件系统新的大小

```bash
sudo resize2fs /dev/nvme0n1p6
```

### 验证

```bash
df -h /
```

---

## 四、处理不连续的空闲空间

若删除的 Windows 分区与 Linux 分区不相邻（例如 Windows 占据磁盘前半段，Linux 在后半段），空闲空间会出现在 Linux 分区的前方，无法直接并入根分区。

此时推荐将这块空间独立挂载为 `/home`。

### 1. 建立新分区

```bash
sudo parted /dev/nvme0n1
```

```
mkpart primary ext4 1MiB 1721GB   # 起始用 1MiB 保证对齐，结束位置按空闲空间实际大小填写
quit
```

> 起始位置必须用 `1MiB` 而非 `0` 或具体字节数，否则会出现对齐警告，影响性能。

查看新分区编号：

```bash
sudo parted /dev/nvme0n1 print
```

### 2. 格式化新分区

```bash
sudo mkfs.ext4 /dev/nvme0n1p1   # 编号按实际情况调整
```

### 3. 迁移 /home 数据

```bash
sudo mount /dev/nvme0n1p1 /mnt
sudo cp -a /home/. /mnt/.
ls /mnt   # 确认用户目录已复制过来
```

### 4. 写入 fstab 实现自动挂载

获取新分区的 UUID：

```bash
sudo blkid /dev/nvme0n1p1
```

将以下内容追加到 `/etc/fstab`（替换 UUID 为实际值）：

```bash
echo 'UUID=<你的UUID> /home ext4 defaults 0 2' | sudo tee -a /etc/fstab
```

验证 fstab 内容：

```bash
cat /etc/fstab
```

### 5. 重启并验证

```bash
sudo reboot
```

重启后：

```bash
df -h /home
```

应显示 `/home` 挂载在新分区上，大小与预期一致。

---

## 五、清理 EFI 启动项

删除 Windows 分区后，EFI 变量里的 Windows 启动项仍然残留，需要手动清除。

```bash
# 查看所有启动项和 ID
efibootmgr

# 删除 Windows Boot Manager（ID 按实际输出填写）
sudo efibootmgr -b 0001 -B

# 若有其他残留项（如旧的 GRUB）也一并清除
sudo efibootmgr -b 0000 -B

# 确认最终状态
efibootmgr
```

完成后启动列表中应只剩 Linux 的启动项。

---

## 六、收尾检查

```bash
# 检查时区和时间同步（双系统时代 RTC 可能被 Windows 设为本地时间）
timedatectl

# 确认时区正确，RTC in local TZ 应为 no（UTC 模式）
# 若需修正：
sudo timedatectl set-timezone Asia/Shanghai
sudo timedatectl set-ntp true

# 检查 swap
swapon --show
```

---

## 附：最终分区布局参考

```
/dev/nvme0n1p1   ext4    1.6TB   /home   （原 Windows 空间）
/dev/nvme0n1p5   vfat    500MB   /boot   （Linux EFI 分区）
/dev/nvme0n1p6   ext4    279GB   /       （Linux 根分区）
```

---

> 操作前请务必备份重要数据。所有分区操作均不可逆。
