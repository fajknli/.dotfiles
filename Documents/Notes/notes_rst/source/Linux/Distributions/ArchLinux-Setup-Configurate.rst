Arch Linux 安装和配置
########################

1. 安装Archlinux
=====================

1.1 字体设置和网络设置
-----------------------

进入archlinux后，默认是root账户，可以先设置个字体

::

    setfont ter-v32n

    setfont -n

再把网络连接上，这里使用无线网络，使用iwd工具

::

    $ iwctl

    [iwd]# station wlan0 scan

    [iwd]# station wlan0 get-networks

    [iwd]# station wlan0 connect Xiaomi_wyks

连接那个网络后输入密码然后差不多就可以连接上网络了，如果没有就自己网上搜

1.2 脚本自动化安装
--------------------

先禁用 reflector 服务,一个当你安装东西时给你连接上国外源的工具，下载速度60kb/s,国内的都1200kb/s 

::

    systemctl stop reflector.service

再配置国内源

::

    vim /etc/pacman.d/mirrorlist

删除文件内容，再在顶部添加

::

    Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch
    Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
    Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch

更新软件包缓存：

::

    pacman -Syyu

两次 y 能避免从损坏的镜像切换到正常的镜像时出现的问题。

如果您从一个较新的镜像切换到较旧的镜像，以下命令可以降级部分包，以避免系统的部分更新。

::

    pacman -Syyuu

然后进行配置安装，然后就重新启动就可以了

::

    archinstall


1.3 手动安装(适合双系统)
-------------------------

先安装windows,到后面要联网，直接shift+F10打开CMD输入'OOBE\BYPASSNRO',进去之后先搞驱动，也就是系统
更新

windows主要用来玩游戏，500G够了，其他的磁盘或者分区就不管了

1.3.1 分区
'''''''''''

::

    fdisk /dev/nvme0n1
    分/,/home,swap三个区，其实有第四个，就是windows的EFI(ESP)区,到时候直接挂载过来就好

    /,和/home随便分，swap就分个和内存一样的就欧克，小一点也可以,/home分区只是为了以后重装系统的
    时候可以不清除这个分区，可以继续挂载使用

1.3.2 格式化分区
''''''''''''''''''

::

    不用格式化 EFI 分区,因为它是windows的，这个可以公用 

    格式化 Swap 分区
    mkswap /dev/nvme0n1pX

    格式化/和/home分区
    mkfs.ext4 /dev/nvme0n1pX
    因为这个分区想使用ext4的

除了这些，还要使用fdisk,给它们都打上标识，比如/和/home 使用linux filesystem,swap 分区标上
linux swap ,efi分区还是不管

然后就准备挂载了,先挂载到根分区

::

    mount /dev/nvme0n1pX /mnt
    这里的/mnt就是新系统的/根目录，我觉得可以自己创一个空目录然后这样搞，反正最后也是要umount
    不过算了，/mnt就是空的，然后再在里面创一个/home目录,也就是/mnt/home,然后还有个/mnt/boot给那个
    windows的efi分区，swap 分区就一个命令就欧克了，不用这样挂载。

    然后把对应分区都挂载进去
    mount /dev/nvme0n1pX /mnt/home
    mount /dev/nvme0n1pX /mnt/boot
    swapon /dev/nvme0n1pX 这个分区得是swap分区

    df -h 查看挂载如何，free -h 查看swap交换空间



1.3.3 为新系统安装一些工具
'''''''''''''''''''''''''''''

::

    pacstrap -K /mnt base base-devel linux linux-firmware (intel-ucode 或者amd-ucode)

    默认情况下，pacstrap 在安装内核相关包（如 linux、linux-lts）时会自动触发 mkinitcpio 生成 initramfs
    在 pacstrap -K 命令中，-K 选项用于 在安装时跳过对已安装文件的内核 hooks 处理（即不运行 mkinitcpio）

    pacstrap -K /mnt iwd vim git grub

1.3.4 生成 fstab 文件
'''''''''''''''''''''''

fstab 用来定义磁盘分区。它是 Linux 系统中重要的文件之一。使用 genfstab 自动根据当前挂载情况生成并写入 fstab 文件

::

    genfstab -U /mnt > /mnt/etc/fstab

复查一下 /mnt/etc/fstab 确保没有错误：

::

    cat /mnt/etc/fstab

1.3.5 进入系统
'''''''''''''''

::

    arch-chroot /mnt

1.3.6 设置时间和时区
'''''''''''''''''''''''''

::

    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

然后运行 hwclock(8) 以生成 /etc/adjtime：

::

    hwclock --systohc

1.3.7 区域和本地化设置
'''''''''''''''''''''''

需要设置这两个文件：locale.gen 与 locale.conf

编辑 /etc/locale.gen，然后取消掉 en_US.UTF-8 UTF-8 和其他需要的 UTF-8 区域设置前的注释（#）

接着执行 locale-gen 以生成 locale 信息：

::

    locale-gen

然后创建 locale.conf(5) 文件，并编辑设定 LANG 变量

::

    vim /etc/locale.conf

    LANG=en_US.UTF-8

1.3.8 网络配置
'''''''''''''''
    
设置主机名

::

    vim /etc/hostname

1.3.9 创建新的 initramfs
'''''''''''''''''''''''''''

::

    mkinitcpio -P  # 为所有已安装的内核生成 initramfs

1.3.10 设置 root/用户 密码
''''''''''''''''''''''''''''

::

    passwd # 设置root密码



1.3.11 安装grub引导程序
''''''''''''''''''''''''

这个可以识别到linux和windows,如果没有就去设置/etc/default/grub，修改：GRUB_DISABLE_OS_PROBER=false
应该需要下载os_prober 包

::
    
    pacman -S os_prober

    vim /etc/default/grub
    # 取消GRUB_DISABLE_OS_PROBER=false 的注释

    # 重新安装 GRUB（UEFI 模式）
    grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
    grub-mkconfig -o /boot/grub/grub.cfg  # 生成 GRUB 配置

* ✅ --efi-directory=/boot 必须指向 ESP（通常是 /boot）
* ✅ --bootloader-id=GRUB 会创建 /EFI/GRUB/grubx64.efi
* ✅ grub-mkconfig 会自动检测 Windows 并添加启动项

查看当前 UEFI 启动项

::

    sudo efibootmgr

输出示例：

::

    BootCurrent: 0000
    BootOrder: 0000,0001,0002,0003
    Boot0000* Windows Boot Manager
    Boot0001* Arch Linux
    Boot0002* Ubuntu
    Boot0003* Fedora

* BootOrder 决定启动顺序。
* Boot0001, Boot0002 等是 UEFI 引导条目。

::

    sudo efibootmgr -o 0001,0000
    # 修改启动顺序

删除无效的 Linux 启动项

假设你要删除 Boot0001（Arch Linux）和 Boot0002（Ubuntu）：

::

    sudo efibootmgr -b 0001 -B  # 删除 Boot0001
    sudo efibootmgr -b 0002 -B  # 删除 Boot0002
    
1.3.12 内核设置(救援模式)
''''''''''''''''''''''''''''

通过archlinux.iso 挂载进入之前系统

::

    mount /dev/nvme0n1pX /mnt       # 挂载根分区（替换 X 为你的分区号）
    mount /dev/nvme0n1p1 /mnt/boot  # 挂载 ESP（如果是 UEFI）
    arch-chroot /mnt                # 切换到已安装的系统

安装 linux-zen 内核
'''''''''''''''''''''

linux-zen 是 Arch Linux 提供的优化内核，适用于桌面和低延迟场景。

::

    pacman -S linux-zen linux-zen-headers  # 安装 Zen 内核

重新生成 initramfs

::

    mkinitcpio -P  # 自动为所有已安装的内核生成 initramfs

安装os_prober,编辑 /etc/default/grub，修改：

::

    GRUB_DISABLE_OS_PROBER=false

更新 GRUB 配置

::

    grub-mkconfig -o /boot/grub/grub.cfg

更换linux内核
'''''''''''''''

下载你想安装的内核
linux  linux-zen   linux-lts

安装后需要更新引导加载程序：

::

    sudo grub-mkconfig -o /boot/grub/grub.cfg

systemd-boot (使用 systemd 的系统)

::

    sudo bootctl update

    sudo reboot

    uname -r  #重启后检查当前运行的内核：


卸载旧内核（可选）

可能需要删除efi/grub的内核相关文件，记得再mkinitcpio -P来检查initramfs

再记得grub-mkconfig -o /boot/grub/grub.cfg来重新设置grub启动

uname -r 查看内核版本

::

    pacman -R linux linux-headers



设置字体大小
'''''''''''''

::

    sudo grub-mkfont -s 32 -o /boot/grub/fonts/unicode.pf2


nvidia驱动问题
'''''''''''''''''

不安装nvidia-dkms,安装这个会无法打开pot,可以安装dkms

查看本地图像库
'''''''''''''''

::

    pacman -Q | grep -E "mesa|vulkan|nvidia|intel|amd|opengl|wayland|xorg"

----------

2. 添加Archlinux源
====================

2.1 添加Archlinuxcn源
----------------------

因为通过archinstall 脚本安装，自带国内源，我们可以添加 'Archlinuxcn源 <http://repo.archlinuxcn.org>'_ 

在 '/etc/pacman.conf' 文件末尾添加两行：

::

    [archlinuxcn]
    Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch
    Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
    Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch 

2.1.1 新系统中安装 archlinuxcn-keyring 包前需要手动信任 farseerfc 的 key
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

archlinuxcn 社区源的 keyring 包 archlinuxcn-keyring 由 farseerfc 的 key 签署验证，而 Arch Linux 官方 keyring 中包含了 farseerfc 的 key 。自12月初 archlinux-keyring 中删除了一个退任的 master key 导致 farseerfc 的 key 的信任数不足，由 GnuPG 的 web of trust 推算为 marginal trust，从而不再能自动信任 archlinuxcn-keyring 包的签名。

如果你在新系统中尝试安装 archlinuxcn-keyring 包时遇到如下报错：

::

    error: archlinuxcn-keyring: Signature from "Jiachen YANG (Arch Linux Packager Signing Key) " is marginal trust

请使用以下命令在本地信任 farseerfc 的 key 。此 key 已随 archlinux-keyring 安装在系统中，只是缺乏信任：

::

    sudo pacman-key --lsign-key "farseerfc@archlinux.org"

之后继续安装 archlinuxcn-keyring ：

::

    sudo pacman -S archlinuxcn-keyring

安装之后进行更新:

::

    sudo pacman -Syu

2.2 添加Blackarch源
----------------------

获得blackarch-mirror-list:

::

    wget https://blackarch.org/blackarch-mirrorlist

在 '/etc/pacman.conf' 文件末尾添加：

::

    [blackarch]
    Server = https://mirror.sjtu.edu.cn/blackarch/$repo/os/$arch
    Server = https://mirrors.nju.edu.cn/blackarch/$repo/os/$arch
    Server = http://mirrors.nju.edu.cn/blackarch/$repo/os/$arch
    Server = https://mirrors.tuna.tsinghua.edu.cn/blackarch/$repo/os/$arch
    Server = https://mirrors.ustc.edu.cn/blackarch/$repo/os/$arch
    Server = http://mirrors.aliyun.com/blackarch/$repo/os/$arch
    Server = https://mirrors.aliyun.com/blackarch/$repo/os/$arch

刷新关于blackarch的数据库

::

    sudo pacman -Syyu 

信任GPG key

::

    sudo pacman-key --lsign-key noptrix@nullsecurity.net

下载blackarch-keyring

::

    pacman -Sy blackarch-keyring

如果出现了pacman 下载archlinux.db 404的情况

::

    sudo pacman -Scc  # 清理所有缓存
    sudo rm /var/lib/pacman/db.lck  # 删除锁文件（如果存在）
    sudo pacman -Syyu  # 强制刷新数据库并更新系统

2.3 DNS设置
-------------

可能进入新系统没有网络，无法使用包管理器下载软件

::

    echo "nameserver 8.8.8.8" > /etc/resolv.conf

使用 systemd-resolved

::

    sudo vim /etc/systemd/resolved.conf

内容:

::

    [Resolve]
    DNS=8.8.8.8 1.1.1.1
    Domains=example.com

重启:

::

    sudo systemctl restart systemd-resolved

检查:

::

    sudo systemd-resolve --flush-caches  # 清空 DNS 缓存
    sudo systemd-resolve --status        # 检查当前 DNS 配置

2.3 dhcp 设置
-----------------

即使连接了网络和设置了DNS,也可能无法连接网络

配置开机自动 DHCP
使用 systemd-networkd（推荐）

编辑 /etc/systemd/network/20-wired.network：

::

    [Match]
    Name=wlan0

    [Network]
    DHCP=yes

然后启用服务：

::

    sudo systemctl enable --now systemd-networkd


2.4 SDDM卡死
----------------

SDDM 卡死可能与显卡驱动不兼容有关。(尤其是nvidia用户)
办法就是直接使用emptty(一款TUI轻量级DM)

::

    删除sddm
    sudo pacman -Rns sddm

    下载emptty
    sudo pacman -S emptty

但是在此之前已经被sddm卡死了
切换到 TTY 终端排查问题

::

    按 Ctrl + Alt + F2（或 F3-F6）进入 TTY 终端

    因为sddm一般在tty7里，F7就是sddm图形界面


3. 安装v2raya
=================

v2raya软件在archlinuxcn源内，

配置好了archlinuxcn源后,直接 'pacman -Sy v2raya' 安装

4. 安装yay访问AUR
=====================

::

    sudo pacman -S --needed git base-devel
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si

安装后，您可以使用像这样的 yay 命令

1. 查找软件

::

    $ yay firefox

    #OR

    $ yay -Ss firefox

2. 安装软件包：

::

    yay -S package_name

3. 显示包信息

::

    $ yay -Si neofetch

4. 删除包

::

    $ yay -R neofetch

5. 删除包缓存

::

    $ yay -Sc

6. 查看系统的信息，包括包数量，最大的包

::

    $ yay -Ps

删除yay包管理器

::

    $ sudo pacman -Rs yay

5. 添加新用户,并添加到权限组
==============================

::

    useradd <username>
    usermod -aG sudo 用户名  # Ubuntu/Debian 等
    usermod -aG wheel 用户名  # CentOS/RHEL/Fedora 等（部分系统用 wheel 替代 sudo

处理常见问题

sudoers 文件未包含 sudo 组

编辑 /etc/sudoers：

::

    EDITOR=vim visudo  # 必须用 visudo 编辑，避免语法错误！
    以防系统没有vi

    确保存在以下行：
    %sudo ALL=(ALL:ALL) ALL  # Ubuntu/Debian
    %wheel ALL=(ALL:ALL) ALL # CentOS/RHEL/arch

    如果希望免密码使用 sudo，在 /etc/sudoers 中添加：

    用户名 ALL=(ALL) NOPASSWD:ALL

6.递归更改目录下所有文件的所有者
=================================

::

    sudo chown -R 新所有者:新所属组 目录路径

7. pipewire 声音设置
====================

1.安装pipewire pipewire-pulse wireplumber

::

    pacman -S pipewire pipewire-pulse wireplumber

2.检查是否enable和started

::

    systemctl --user status pipewire pipewire-pulse wireplumber

    systemctl --user start pipewire pipewire-pulse wireplumber

    systemctl --user enable pipewire wireplumber

3.重启系统

::

    reboot

Z. 笔记本合屏断电与否
===========================

1. 编辑 /etc/systemd/logind.conf

2. 找到并修改HandleLidSwitch的值为ignore(忽略盖子关闭事件)/lock(锁定屏幕但不会进入睡眠模式)

3. 修改完成后使更改立即生效，重启 'systemd-logind' 服务

Z. 禁用笔记本触摸板
=====================

感觉触摸板在有鼠标的情况下碍事，所以想插入鼠标就禁用触摸板，拔出就开启
但是操作麻烦，就直接禁用了

创建一个udev规则，管理底层硬件的

::

    sudo vim /etc/udev/rules.d/99-disable-touchpad.rules

输入如下内容：

::

    ACTION=="add",SUBSYSTEM=="input",ATTRS{id/vendor}=="093a",ENV{LIBINPUT_IGNORE_DEVICE}="1"

其中的ATTRS{id/vendor}是来自

libinput list-devices 列出硬件信息，我们需要类似/dev/input/eventX的硬件路径

然后再搭配上 udevadm info -a -p $(udevadm info -q path -n /dev/input/eventX)

找到相关硬件的ATTRS{id/vendor},它只是一个标识而已，其他的可以代表这个硬件的标识都可以

然后放入上面那个命令，就欧克了


Z. 自定义快捷键使用
======================

:取色: CTRL_ALT, p, exec, hyprpicker -a
:翻译: CTRL ALT, T, exec, curl "127.0.0.1:60828/selection_translate"
:调亮屏幕: CTRL_ALT_SHIFT, 0, exec, brightnessctl s 2%+
:调暗屏幕: CTRL_ALT_SHIFT, 9, exec, brightnessctl s 2%-
:调高音量: CTRL_ALT, 0,exec, pactl set-sink-volume 0 +2%
:调低音量: CTRL_ALT, 9,exec, pactl set-sink-volume 0 -2%
:静音: CTRL_ALT, 8,exec,pactl set-sink-mute 0 toggle # mute
:截图: ALT CTRL, S, exec, grim -l 0 -g "$(slurp)" - | wl-copy
:右移工作区: ALT, f, workspace, e+1
:左移工作区: ALT, a, workspace, e-1
:super键加回车打开终端: $mainMod, Return, exec, $terminal
:关闭当前窗口: $mainMod SHIFT, Q, killactive,
:退出hyprland: $mainMod, M, exit,
:开启窗口悬浮: $mainMod, V, togglefloating,
:打开菜单: $mainMod, D, exec, $menu
:窗口全屏(打游戏用的): $mainMod, f, fullscreen
:窗口编组(没什么用): $mainMod, g, togglegroup
