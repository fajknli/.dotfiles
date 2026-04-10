# Arch Linux 安装和配置

## 1. 安装 Arch Linux

### 1.1 字体设置和网络设置

进入 Arch Linux 后，默认是 root 账户，可以先设置字体：

```bash
setfont ter-v32n
setfont -n
```

连接网络，使用无线网络和 iwd 工具：

```bash
iwctl
[iwd]# station wlan0 scan
[iwd]# station wlan0 get-networks
[iwd]# station wlan0 connect <WiFi名称>
```

### 1.2 脚本自动化安装

先禁用 reflector 服务（会连接国外源，速度很慢）：

```bash
systemctl stop reflector.service
```

配置国内源：

```bash
vim /etc/pacman.d/mirrorlist
```

删除文件内容，在顶部添加：

```text
Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch
```

更新软件包缓存：

```bash
pacman -Syyu
```

两次 `y` 能避免从损坏的镜像切换到正常的镜像时出现的问题。

如果从较新的镜像切换到较旧的镜像，以下命令可以降级部分包：

```bash
pacman -Syyuu
```

然后运行安装脚本：

```bash
archinstall
```

### 1.3 手动安装（适合双系统）

先安装 Windows，后面需要联网时按 `Shift + F10` 打开 CMD，输入 `OOBE\BYPASSNRO`。进入系统后先更新系统和驱动。

Windows 主要用于玩游戏，500GB 足够。

#### 1.3.1 分区

```bash
fdisk /dev/nvme0n1
```

分 `/`、`/home`、swap 三个区。还有 Windows 的 EFI（ESP）分区，到时候直接挂载过来。

- `/` 和 `/home` 大小随意
- swap 分与内存大小相同即可
- `/home` 独立分区是为了重装系统时可以保留数据

#### 1.3.2 格式化分区

```bash
# EFI 分区不用格式化（与 Windows 共用）

# 格式化 swap 分区
mkswap /dev/nvme0n1pX

# 格式化 / 和 /home 分区（使用 ext4）
mkfs.ext4 /dev/nvme0n1pX
```

使用 `fdisk` 给分区打标识：

- `/` 和 `/home`：`linux filesystem`
- swap：`linux swap`
- EFI 分区：保持原样

#### 1.3.3 挂载分区

```bash
mount /dev/nvme0n1pX /mnt                    # 挂载根分区
mkdir -p /mnt/home /mnt/boot
mount /dev/nvme0n1pX /mnt/home               # 挂载 /home
mount /dev/nvme0n1pX /mnt/boot               # 挂载 EFI 分区
swapon /dev/nvme0n1pX                        # 启用 swap

df -h   # 查看挂载情况
free -h # 查看 swap 空间
```

#### 1.3.4 安装基础系统

```bash
# Intel CPU
pacstrap -K /mnt base base-devel linux linux-firmware intel-ucode

# AMD CPU（注释掉上一行，取消注释下一行）
# pacstrap -K /mnt base base-devel linux linux-firmware amd-ucode

pacstrap -K /mnt iwd vim git grub os-prober
```

`-K` 选项用于在安装时跳过 mkinitcpio 处理。

#### 1.3.5 生成 fstab

```bash
genfstab -U /mnt > /mnt/etc/fstab
cat /mnt/etc/fstab   # 复查
```

#### 1.3.6 进入系统

```bash
arch-chroot /mnt
```

#### 1.3.7 设置时间和时区

```bash
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc
```

#### 1.3.8 区域和本地化设置

```bash
vim /etc/locale.gen
# 取消注释 en_US.UTF-8 UTF-8

locale-gen

echo "LANG=en_US.UTF-8" > /etc/locale.conf
```

#### 1.3.9 设置主机名

```bash
echo "你的主机名" > /etc/hostname
```

#### 1.3.10 生成 initramfs

```bash
mkinitcpio -P
```

#### 1.3.11 设置 root 密码

```bash
passwd
```

#### 1.3.12 安装 GRUB 引导程序

```bash
# 编辑 GRUB 配置，启用 os-prober 检测 Windows
vim /etc/default/grub
# 取消注释：GRUB_DISABLE_OS_PROBER=false

# 安装 GRUB（UEFI 模式）
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB

# 生成配置
grub-mkconfig -o /boot/grub/grub.cfg
```

#### 1.3.13 管理 UEFI 启动项

```bash
efibootmgr                    # 查看当前启动项
efibootmgr -o 0001,0000       # 修改启动顺序
efibootmgr -b 0001 -B         # 删除指定启动项
```

## 2. 软件源配置

### 2.1 添加 Arch Linux CN 源

在 `/etc/pacman.conf` 末尾添加：

```text
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
```

信任 GPG key：

```bash
sudo pacman-key --lsign-key "farseerfc@archlinux.org"
sudo pacman -S archlinuxcn-keyring
sudo pacman -Syu
```

### 2.2 添加 BlackArch 源（可选）

获取镜像列表：

```bash
wget https://blackarch.org/blackarch-mirrorlist
```

在 `/etc/pacman.conf` 末尾添加：

```text
[blackarch]
Server = https://mirror.sjtu.edu.cn/blackarch/$repo/os/$arch
Server = https://mirrors.nju.edu.cn/blackarch/$repo/os/$arch
Server = http://mirrors.nju.edu.cn/blackarch/$repo/os/$arch
Server = https://mirrors.tuna.tsinghua.edu.cn/blackarch/$repo/os/$arch
Server = https://mirrors.ustc.edu.cn/blackarch/$repo/os/$arch
Server = http://mirrors.aliyun.com/blackarch/$repo/os/$arch
Server = https://mirrors.aliyun.com/blackarch/$repo/os/$arch
```

更新并信任 GPG key：

```bash
sudo pacman -Syyu
sudo pacman-key --lsign-key noptrix@nullsecurity.net
sudo pacman -Sy blackarch-keyring
```

如果遇到 404 错误：

```bash
sudo pacman -Scc
sudo rm /var/lib/pacman/db.lck
sudo pacman -Syyu
```

## 3. 网络配置

### 3.1 DNS 设置

如果进入新系统没有网络：

```bash
echo "nameserver 8.8.8.8" > /etc/resolv.conf
```

使用 systemd-resolved：

```bash
sudo vim /etc/systemd/resolved.conf
```

内容：

```text
[Resolve]
DNS=8.8.8.8 1.1.1.1
Domains=example.com
```

重启服务：

```bash
sudo systemctl restart systemd-resolved
```

清空 DNS 缓存：

```bash
sudo systemd-resolve --flush-caches
```

检查当前 DNS 配置：

```bash
sudo systemd-resolve --status
```

### 3.2 DHCP 设置

配置开机自动 DHCP（使用 systemd-networkd）：

```bash
sudo vim /etc/systemd/network/20-wired.network
```

内容：

```text
[Match]
Name=wlan0

[Network]
DHCP=yes
```

启用服务：

```bash
sudo systemctl enable --now systemd-networkd
```

## 4. 内核管理

### 4.1 通过 ISO 进入已安装系统（救援模式）

```bash
mount /dev/nvme0n1pX /mnt       # 挂载根分区
mount /dev/nvme0n1p1 /mnt/boot  # 挂载 ESP（UEFI）
arch-chroot /mnt
```

### 4.2 安装 linux-zen 内核

```bash
pacman -S linux-zen linux-zen-headers
mkinitcpio -P
grub-mkconfig -o /boot/grub/grub.cfg
```

### 4.3 更换内核

安装其他内核（如 linux-lts）：

```bash
sudo pacman -S linux-lts
sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo reboot
uname -r   # 重启后检查当前运行的内核
```

卸载旧内核：

```bash
pacman -R linux linux-headers
grub-mkconfig -o /boot/grub/grub.cfg
```

### 4.4 设置 GRUB 字体大小

```bash
sudo grub-mkfont -s 32 -o /boot/grub/fonts/unicode.pf2
```

### 4.5 NVIDIA 驱动问题

如果遇到问题，尝试安装 `nvidia-dkms` 而非 `nvidia`。

查看已安装的图形相关包：

```bash
pacman -Q | grep -E "mesa|vulkan|nvidia|intel|amd|opengl|wayland|xorg"
```

## 5. 用户管理

### 5.1 添加新用户

```bash
useradd -m <用户名>
passwd <用户名>
usermod -aG wheel <用户名>   # Arch 使用 wheel 组
```

### 5.2 配置 sudo

```bash
EDITOR=vim visudo
```

确保存在以下行：

```text
%wheel ALL=(ALL:ALL) ALL
```

免密码 sudo（可选）：

```text
<用户名> ALL=(ALL) NOPASSWD:ALL
```

### 5.3 更改目录所有者

```bash
sudo chown -R 新所有者:新所属组 目录路径
```

## 6. 声音配置（PipeWire）

```bash
# 安装
pacman -S pipewire pipewire-pulse wireplumber

# 检查状态
systemctl --user status pipewire pipewire-pulse wireplumber

# 启动服务
systemctl --user start pipewire pipewire-pulse wireplumber

# 启用服务
systemctl --user enable pipewire wireplumber

# 重启
reboot
```

## 7. 安装 v2raya

```bash
# 配置好 archlinuxcn 源后
sudo pacman -S v2raya
```

## 8. 安装 yay（AUR 助手）

```bash
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

yay 常用命令：

```bash
yay -Ss firefox        # 搜索软件包
yay -S <包名>          # 安装软件包
yay -Si <包名>         # 显示包信息
yay -R <包名>          # 删除包
yay -Sc                # 删除包缓存
yay -Ps                # 查看系统信息

# 删除 yay
sudo pacman -Rs yay
```

## 9. 常见问题解决

### 9.1 SDDM 卡死（NVIDIA 用户）

切换到 TTY 终端：

```text
Ctrl + Alt + F2（或 F3-F6）
```

解决方案（改用 emptty）：

```bash
sudo pacman -Rns sddm
sudo pacman -S emptty
```

### 9.2 笔记本合盖不睡眠

编辑 `/etc/systemd/logind.conf`：

```text
HandleLidSwitch=ignore   # 忽略盖子关闭事件
# 或 HandleLidSwitch=lock # 锁屏但不睡眠
```

重启服务：

```bash
systemctl restart systemd-logind
```

### 9.3 禁用触摸板

```bash
# 查看触摸板信息
libinput list-devices
udevadm info -a -p $(udevadm info -q path -n /dev/input/eventX)
```

创建 udev 规则：

```bash
sudo vim /etc/udev/rules.d/99-disable-touchpad.rules
```

内容（替换 `ATTRS{id/vendor}` 为实际值）：

```text
ACTION=="add",SUBSYSTEM=="input",ATTRS{id/vendor}=="093a",ENV{LIBINPUT_IGNORE_DEVICE}="1"
```

### 9.4 pacman 数据库问题

```bash
sudo pacman -Scc           # 清理所有缓存
sudo rm /var/lib/pacman/db.lck  # 删除锁文件（如果存在）
sudo pacman -Syyu          # 强制刷新数据库并更新
```

## 10. 自定义快捷键（Hyprland 示例）

```text
# 取色
CTRL_ALT, p, exec, hyprpicker -a

# 翻译
CTRL_ALT, T, exec, curl "127.0.0.1:60828/selection_translate"

# 调亮屏幕
CTRL_ALT_SHIFT, 0, exec, brightnessctl s 2%+

# 调暗屏幕
CTRL_ALT_SHIFT, 9, exec, brightnessctl s 2%-

# 调高音量
CTRL_ALT, 0, exec, pactl set-sink-volume 0 +2%

# 调低音量
CTRL_ALT, 9, exec, pactl set-sink-volume 0 -2%

# 静音
CTRL_ALT, 8, exec, pactl set-sink-mute 0 toggle

# 截图
ALT_CTRL, S, exec, grim -l 0 -g "$(slurp)" - | wl-copy

# 右移工作区
ALT, F, workspace, e+1

# 左移工作区
ALT, A, workspace, e-1

# Super 键加回车打开终端
$mainMod, Return, exec, $terminal

# 关闭当前窗口
$mainMod SHIFT, Q, killactive

# 退出 Hyprland
$mainMod, M, exit

# 开启窗口悬浮
$mainMod, V, togglefloating

# 打开菜单
$mainMod, D, exec, $menu

# 窗口全屏
$mainMod, F, fullscreen

# 窗口编组
$mainMod, G, togglegroup
```

## 11. 有用的命令速查

```bash
# 查看内核版本
uname -r

# 查看系统信息
yay -Ps

# 清空 DNS 缓存
sudo systemd-resolve --flush-caches

# 查看 DNS 状态
sudo systemd-resolve --status

# 查看 UEFI 启动项
efibootmgr

# 更新 GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```
