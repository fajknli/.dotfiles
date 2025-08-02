Void Linux 安装和配置
################################

1. 安装Void Linux
===================================

1.1 介绍
---------

Void linux 是基于 Linux 内核独立开发的通用操作系统。其特色在于一份二进制/源代码混合式包管理系统，这使得用户能快速安装、更新、移除软件，或者是借助 XBPS 源代码集合从源码直接生成软件。该发行的其他特性包括对 Raspberry Pi 单板计算机（armv6 和 armv7）的支持，每日更新的滚动式开发模式，可以选择 glibc 和 musl 作为 C 库，以及名为 runit 的原生 BSD 风格 init 系统。

1.2 U盘安装VoidLinux
---------------------

1. 去 `Void Linux 官网下载 <https://www.voidlinux.org/download/>`_ ,找到合适自己的版本。

2. 使用 ``dd`` 命令把镜像写入U盘，或者利用手机软件 ``EtchDroid`` 进行此操作。

::

    # dd bs=4M if=/path/to/void-live-ARCH-DATE-VARIANT.iso of=/dev/sdX status=progress && sync

3. U盘启动后，root账号，密码voidlinux进入，再输入 ``sudo void-installer`` 开启安装程序。

4. 接下来有一系列操作，慢慢做完。


2. Void Linux 安装完后的配置
===================================

2.1 更新系统
------------

| 先更新一下xbps：

::

    sudo xbps-install -u xbps

| 登录用户后更新系统

::

    sudo xbps-install -Syu

2.2 更改 sudo 和 grup 配置文件
-------------------------------

下载一个编辑器准备编辑sudo和grup文件，来方便操作

::

    sudo xbps-install vim

1. 编辑sudo 文件来使输入sudo时不需要输入密码

::

    EDITOR=vim sudo -E visudo

按"G"到最下面，改成这样

::

    ## User privilege specification 
    ##             
    #root ALL=(ALL:ALL) ALL 
    root ALL=(ALL) NOPASSWD: SETENV:ALL
    zwron ALL=(ALL) NOPASSWD: SETENV:ALL
    ## Uncomment to allow members of group wheel to execute any command
    # %wheel ALL=(ALL:ALL) ALL
    ## Same thing without a password
    # %wheel ALL=(ALL:ALL) NOPASSWD: ALL
    ## Uncomment to allow members of group sudo to execute any command
    # %sudo ALL=(ALL:ALL) ALL
    ## Uncomment to allow any user to run sudo if they know the password
    ## of the user they are running the command as (root by default).
    # Defaults targetpw  # Ask for the password of the target user
    # ALL ALL=(ALL:ALL) ALL  # WARNING: only use this together with 'Defaults targetpw'
    ## Read drop-in files from /etc/sudoers.d
    #@includedir /etc/sudoers.d

2. 编辑grup文件，让它直接启动时不需要默认等待5s

::

    sudo vim /etc/default/grup

更改如下

::

    #
    # Configuration file for GRUB.
    #
    GRUB_DEFAULT=0
    #GRUB_HIDDEN_TIMEOUT=0
    #GRUB_HIDDEN_TIMEOUT_QUIET=true
    GRUB_TIMEOUT=0
    GRUB_DISTRIBUTOR="Void"
    GRUB_CMDLINE_LINUX_DEFAULT="loglevel=4"
    # Uncomment to use basic console
    #GRUB_TERMINAL_INPUT="console"
    # Uncomment to disable graphical terminal
    #GRUB_TERMINAL_OUTPUT=console
    #GRUB_BACKGROUND=/usr/share/void-artwork/splash.png
    #GRUB_GFXMODE=1920x1080x32
    #GRUB_DISABLE_LINUX_UUID=true
    #GRUB_DISABLE_RECOVERY=true
    # Uncomment and set to the desired menu colors.  Used by normal and wallpaper
    # modes only.  Entries specified as foreground/background.
    #GRUB_COLOR_NORMAL="light-blue/black"
    #GRUB_COLOR_HIGHLIGHT="light-cyan/blue"

配置好就 ``sudo update-grub`` 就OK了


3. 软件的安装
===================================

3.1 系统控制类(不包括基础应用，最多图形)
----------------------------------------

::

    void-repo-nonfree
    elogind
    dbus-elogind
    polkit-elogind
    mesa-dri
    wayland
    wlroots
    wl-clipboard
    wayfire
    waybar
    xdg-utils
    xdg-user-dirs
    xdg-desktop-portal
    rtkit
    freetype
    fontconfig
    harfbuzz
    cairo
    wqy-microhei
    noto-fonts-ttf-extra
    font-hack-ttf
    font-awesome6
    nerd-fonts-otf


3.2 基础类应用
----------------------------------------

::

    rxvt-unicode
    light
    grim
    slurp
    tldr
    htop
    zip
    unzip
    mako
    asciinema
    openjdk17
    PrismLauncher
    telegram-desktop
    sioyek
    evince
    lesspass
    cmake
    swaybg
    zellij
    obs
    imv
    mpv
    aria2
    wget
    curl
    rofi
    virt-manager
    libvirt
    qemu
    cmus
    cmus-ffmpeg
    figlet
    Waybar
    swaylock
    wlsunset
    newsflash
    gtypist
    irssi
    tree
    python3-Sphinx
    python3-sphinx_rtd_theme
    fcitx5
    fcitx5-configtool
    fcitx5-chinese-addons
    fcitx5-chinese-addons-icons
    fcitx5-chinese-addons-pinyin-dict-manager
    fcitx5-gtk
    fcitx5-qt
    vsv
    vpm
    make
    vim
    vim-huge
    gimp

安装v2raya （Install with v2ray core）

::

    sudo sh -c "$(wget -qO- https://hubmirror.v2raya.org/v2rayA/v2rayA-installer/raw/main/installer.sh)" @ --with-v2ray

3.3 可替换的应用
---------------------

====== ======
旧应用 新应用
====== ======
ls      lsd
top     htop,btop
====== ======


3.4 编程语言
----------------

* rustup
    | $ rustc --version 查看rust是否安装
    | $ echo $PATH 可以查看rust的系统变量
    | $ rustup update 更新rustup
    | $ rustup self uninstall 卸载rustup
    | $ rustup doc 在浏览器打开rust文档
    | $ cargo --version
    | $ cargo new hello_cargo 创建项目
    | $ cd hello_cargo
    | （cargo new --vcs=其他版本控制）
    | $ cargo build 构建项目
    | $ cargo run 检查并运行
    | $ cargo check 只检查不运行
    | $ cargo build --release 最后发布时用

* gcc
    | gcc 是 Linux 和 UNIX 系统中最常用的 C 语言编译器。使用 gcc 编译 C 程序的基本步骤如下:
    | 1. 编写 C 源代码,如 test.c
    | 2. 使用 gcc 编译源码生成对象文件
    | ``gcc -c test.c -o test.o``
    | 这会生成 test.o 文件
    | 3. 链接对象文件生成可执行文件
    | ``gcc test.o -o test``
    | 这会生成可执行文件 test
    | 4. 运行可执行文件
    | ``./test``
    | gcc 也支持一步直接将 C 源码编译链接成可执行文件:
    | ``gcc test.c -o test``
    | 常用的 gcc 选项包括:
    | - -c 只编译不链接- -o 指定输出文件名 - -g 生成调试信息- -Wall 打开所有警告信息- -O优化级别 -O0无优化 -O3全优化

* python

* python3

* ghc
    | Haskell的开发环境和C语言类似,只需要安装GHC编译器,就可以进行Haskell的代码编译和执行。
    | 主要的步骤包括:
    | 1. 安装GHC编译器
    | 2. 编写Haskell代码,使用任意文本编辑器编写Haskell代码,保存为文件名.hs。
    | 3. 使用GHC编译,在终端运行:ghc hello.hs 来编译Haskell源代码。这会生成可执行文件hello(或hello.exe)。
    | 4. 执行,直接运行生成的可执行文件:./hello。

* nodejs

* openjdk17

3.5 网络工具
--------------

* mtr

* masscan

* gping

*

*

*

*

*

*

*

*


















4. Git 拉取仓库配置 
===================================


5. Void Linux 服务的启动
===================================

启动服务，voidlinux启动服务是创建软链接

.. .. image:: ./image/server.jpg

只是举个例子，有其他服务也可以这样启动。

::

    $ sudo ln -s /etc/sv/rtkit /var/service

6. Void Linux 坏境变量设置
===========================

在/etc/environment里的:

::

    WLR_ NO_HARDWARE_CURSORS=1
    OT_QPA_PLATFORM=wayland-egl
    ELM_DISPLAY=wl
    MOZ_ENABLE_WAYLAND=1
    SDL_VIDEODRIVER=WayLand


7. Void Linux 的一些命令
===================================

voidlinux 搜索包是这个命令：

xbps-query -Rs  包名，什么的

Void Linux上的xbps包管理的主要命令和用法:

- xbps-query - 搜索和显示已安装包信息,加-R参数可以搜索软件仓库中的包

- xbps-install - 安装和更新包,同步软件仓库索引

- xbps-remove - 删除已安装的包,也可以删除无主孤立包和缓存包

- xbps-reconfigure - 重新运行已安装包的配置步骤,可以在配置文件更改后重新配置某些包

- xbps-alternatives - 列出或设置由已安装包提供的可选功能项

- xbps-pkgdb - 报告和修复包数据库问题,也可以修改数据库

- xbps-rindex - 管理本地二进制包仓库

大多数问题可以通过查看这些工具的手册页以及xbps.d(5)手册页得到解答。

8. Void Linux 换源
===================================

`voidlinux 换源 <https://voidlinux.cn/configuration/>`_

::

    mkdir -p /etc/xbps.d
    cp /usr/share/xbps.d/*-repository-*.conf /etc/xbps.d/
    sed -i 's|https://alpha.de.repo.voidlinux.org|https://mirror.sjtu.edu.cn/voidlinux|g' /etc/xbps.d/*-repository-*.conf

之后可用 xbps-query -L 检查是否正确替换。

运行 xbps-install -Su 刷新镜像并更新系统。































