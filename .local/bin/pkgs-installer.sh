#!/bin/sh

# Author:       fajknli
# Email         fajknli@gmail.com
# Created Time: 2025-09-10 00:14
# Filename:     pkgs-installer.sh

# 字体与本地化
fonts_localization="\
otf-comicshanns-nerd \
adobe-source-han-sans-cn-fonts \
ttf-font-awesome \
ttf-lxgw-wenkai \
ttf-0xproto-nerd \
ttf-opensans \
ttf-liberation \
noto-fonts-emoji \
noto-fonts \
noto-fonts-cjk \
fcitx5 \
fcitx5-chinese-addons \
fcitx5-configtool \
fcitx5-gtk \
fcitx5-pinyin-zhwiki \
"

# 网络工具
network_tools="\
networkmanager \
ntp \
bind \
socat \
vsftpd \
drill \
nmap \
openbsd-netcat \
inetutils \
frpc \
curl \
wget \
aria2 \
rsync \
dae \
speedtest-cli \
"

# 系统工具
system_utilities="\
ddcutil \
dmidecode \
sqlite \
lsb-release \
cronie \
sysstat \
htop \
glances \
fastfetch \
man-db \
tealdeer \
bash-completion \
hwinfo \
ncdu \
inxi \
ydotool \
lm_sensors \
zenity \
i2c-tools \
iproute2 \
iputils \
coreutils \
mtr \
base-devel \
arch-wiki-lite \
firejail \
"

# Ai
ai="\
llama.cpp \
"

# 命令行工具
cli_tools="\
iw \
npm \
aerc \
pkgfile \
amdgpu_top \
colordiff \
glow \
cloc \
fzf \
wf-recorder \
git-crypt \
ripgrep \
git-filter-repo \
jq \
most \
unzip \
zip \
7zip \
exfat-utils \
tree \
shellcheck \
xh \
rustup \
yt-dlp \
unrar \
zoxide \
wev \
imagemagick \
chafa \
fd \
lf \
catimg \
w3m \
odt2txt \
poppler \
bc \
figlet \
fuse2fs \
asciinema \
"

# 图形界面应用
gui_application="\
rofi \
alacritty \
tk \
mako \
libnotify \
gimp \
remmina \
waybar \
mpv \
mpv-mpris \
obs-studio \
newsflash \
element-desktop \
virt-manager \
irssi \
thunar \
gthumb \
foliate \
zathura \
zathura-pdf-poppler \
qutebrowser \
prismlauncher \
pavucontrol \
helvum \
"

# wayland/wm相关
wayland_wm="\
sway \
swaylock \
swaybg \
swayidle \
sway-contrib \
niri \
fuzzel \
grim \
slurp \
wl-clipboard \
brightnessctl \
cliphist \
swayimg \
xdg-desktop-portal-wlr \
xdg-desktop-portal-gtk \
xdg-desktop-portal-gnome \
lemurs \
wmenu \
"

# 音频和蓝牙
audio_bluetooth="\
pipewire \
wireplumber \
pipewire-pulse \
bluez \
bluez-utils \
ffmpeg \
ffmpegthumbnailer \
"

# 图像驱动和库
graphics_drivers_libraries="\
intel-media-driver \
libva-utils \
glfw \
vulkan-radeon \
"

# Qt
qt="\
qt5-declarative \
layer-shell-qt \
"

# Python 库
python_libraries="\
mkdocs \
mkdocs-material \
mkdocs-material-extensions \
pypinyin \
mypy \
python-pipx \
python-polars \
python-orjson \
python-faker \
python-transformers \
python-pytorch \
scrapy \
python-lxml \
python-pyfiglet \
python-rich \
python-tqdm \
python-click \
python-emoji \
python-pillow \
"

# 服务器工具
server_tools="\
redis \
nginx \
docker \
kubectl \
kubelet \
kubeadm \
cri-o \
crictl \
"

# 文档与词典
documentation_dictionary="\
sdcv \
"

# 图标
icon_theme="\
papirus-icon-theme \
"

# gtk 主题
gtk_theme="\
adapta-gtk-theme \
"

# cursor-theme
cursor_theme="\
breeze-cursors \
"

# 清理函数
clean_system() {
    echo "=== 清理 pacman 缓存 ==="
    sudo pacman -Sc

    echo ""
    echo "=== 删除孤儿包 ==="
    orphans=$(pacman -Qdtq 2>/dev/null)
    if [ -n "$orphans" ]; then
        echo "发现孤儿包:"
        echo "$orphans"
        echo ""
        printf "是否删除这些孤儿包？(y/N): "
        read answer
        case "$answer" in
            y|Y|yes|YES)
                sudo pacman -Rns $orphans
                ;;
            *)
                echo "跳过删除孤儿包"
                ;;
        esac
    else
        echo "没有孤儿包"
    fi

    echo ""
    echo "=== 清理 journal 日志 ==="
    sudo journalctl --vacuum-size=200M

    echo ""
    echo "=== 清理家目录缓存 ==="
    rm -rf ~/.cache/* 2>/dev/null
    echo "完成"

    echo ""
    echo "=== 磁盘使用情况 ==="
    df -h /
}

# 安装函数
install_packages() {
    sudo pacman -Syu --noconfirm --needed --color auto \
        $documentation_dictionary \
        $server_tools \
        $python_libraries \
        $qt \
        $graphics_drivers_libraries \
        $audio_bluetooth \
        $wayland_wm \
        $gui_application \
        $cli_tools \
        $system_utilities \
        $network_tools \
        $fonts_localization \
        $ai \
        $icon_theme \
        $gtk_theme \
        $cursor_theme
}

# 帮助信息
usage() {
    cat << EOF
用法: $0 [选项]

选项:
    install     安装/更新软件包（默认）
    clean       清理系统（缓存、孤儿包、日志）
    -h, --help  显示帮助

示例:
    $0          安装软件包
    $0 clean    清理系统
EOF
}

# 主逻辑
case "$1" in
    clean)
        clean_system
        ;;
    -h|--help)
        usage
        ;;
    install|"")
        install_packages
        ;;
    *)
        echo "未知选项: $1"
        usage
        exit 1
        ;;
esac
