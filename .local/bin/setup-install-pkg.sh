#!/bin/sh

echo "Download packages"

# ----------------------------------------
# 字体与本地化支持
# ----------------------------------------
FONTS_AND_LOCALE="\
otf-comicshanns-nerd \
adobe-source-han-sans-cn-fonts \
ttf-font-awesome \
ttf-lxgw-wenkai \
ttf-0xproto-nerd \
ttf-opensans \
ttf-liberation \
noto-fonts-emoji \
noto-fonts \
"

# ----------------------------------------
# 网络与系统工具
# pot-translation \
# ----------------------------------------
NETWORK_AND_SYS="\
networkmanager \
iwd \
ntp \
bind \
socat \
lsb-release \
vsftpd \
drill \
nmap \
openbsd-netcat \
inetutils \
"

# ----------------------------------------
# CLI 工具
# ----------------------------------------
CLI_TOOLS="\
fzf \
wf-recorder \
git-crypt \
cronie \
frpc \
ripgrep \
sysstat \
git-filter-repo \
bash-completion \
jq \
man-db \
most \
htop \
fastfetch \
unzip \
zip \
7zip \
exfat-utils \
tree \
make \
shellcheck \
xh \
rustup \
gcc \
tealdeer \
aria2 \
wget \
curl \
rsync \
yt-dlp \
unrar \
wl-mirror \
firejail \
zoxide \
wev \
neomutt \
zoxide \
imagemagick \
chafa \
fd \
lf \
catimg \
w3m \
odt2txt \
ripgrep \
poppler \
bc \
"

# ----------------------------------------
# GUI 应用与桌面增强
# librewolf
# mc
# ----------------------------------------
GUI_APPS="\
alacritty \
mako \
libnotify \
glfw \
gimp \
remmina \
waybar \
mpv \
obs-studio \
newsflash \
element-desktop \
virt-manager \
irssi \
hwinfo \
asciinema \
thunar \
figlet \
fuse2fs \
docker \
gthumb \
foliate \
zathura \
zathura-pdf-poppler \
qutebrowser \
"

#
# ----------------------------------------
# Dirves install
# ----------------------------------------
#
DIRVES="\
intel-media-driver \
libva-utils \
"

#
# ----------------------------------------
# Python Library
# ----------------------------------------
#
PYTHON_LIBRARY="\
pypinyin \
python-polars \
python-orjson \
python-faker \
scrapy \
python-lxml \
python-pyfiglet \
python-rich \
python-tqdm \
python-click \
python-emoji \
python-pillow \
python-sphinx \
python-sphinx-lv2-theme \
python-sphinx-furo \
python-sphinx-autobuild \
python-sphinx-alabaster-theme \
python-guzzle-sphinx-theme \
python-sphinx_rtd_theme \
"



# ----------------------------------------
# Wayland / Hyprland / Sway 系统组件
# ----------------------------------------
#wayland_hyprland=(
#  hyprland hyprlock hypridle hyprpaper hyprpicker xdg-desktop-portal-hyprland
#)

WAYLAND_SWAY="\
sway \
swaylock \
swaybg \
swayidle \
sway-contrib \
"

WAYLAND_NIRI="\
niri \
swaylock \
swaybg \
swayidle \
sway-contrib \
"

WAYLAND_COMMON="\
mako \
wofi \
fuzzel \
grim \
slurp \
wl-clipboard \
brightnessctl \
cliphist \
swayimg \
fcitx5 \
fcitx5-chinese-addons \
fcitx5-configtool \
fcitx5-gtk \
fcitx5-pinyin-zhwiki \
xdg-desktop-portal-wlr \
xdg-desktop-portal-gtk \
xdg-desktop-portal-gnome \
"

GTK_RELATE="\
materia-gtk-theme \
adapta-gtk-theme \
"


AUDIO_AND_BT="\
pipewire \
wireplumber \
pipewire-pulse \
bluez \
bluez-utils \
pavucontrol \
helvum \
ffmpeg \
ffmpegthumbnailer \
"

# ----------------------------------------
# Qt 支持
# ----------------------------------------
QT_SUPPORT="\
qt5-declarative \
layer-shell-qt \
layer-shell-qt5 \
"

# ----------------------------------------
# Server Tools
# ----------------------------------------
SERVER_TOOLS="\
redis \
nginx \
docker \
kubectl \
kubelet \
kubeadm \
cri-o \
crictl \
"
# ----------------------------------------
# Display Manager
# ----------------------------------------
DISPLAY_MANAGER="\
lemurs \
"

# ----------------------------------------
# Game
# ----------------------------------------
GAME="\
prismlauncher \
"

# ----------------------------------------
# Personal applications
# ----------------------------------------
PERSONAL="\
ydotool \
zenity \
wmenu \
sdcv \
dae \
"

# ----------------------------------------
# Archlinux tool applications
# ----------------------------------------
ARCH_TOOL="\
base-devel \
arch-wiki-docs \
arch-wiki-lite \
arch-wiki-docs-zh-cn \
"

### ------------------------
### 安装命令组装
### ------------------------
#ALL_PACKAGES="$SERVER_TOOLS $AUDIO_AND_BT"

#notify-send "[+] 正在安装软件包..."
#sudo pacman -Syu --noconfirm $ALL_PACKAGES

# $WAYLAND_SWAY\
# $SERVER_TOOLS\
sudo pacman -Syu --noconfirm --ask=4 \
$FONTS_AND_LOCALE\
$NETWORK_AND_SYS\
$CLI_TOOLS\
$GUI_APPS\
$DIRVES\
$PYTHON_LIBRARY\
$GTK_RELATE\
$WAYLAND_NIRI\
$WAYLAND_COMMON\
$AUDIO_AND_BT\
$QT_SUPPORT\
$PERSONAL\
$DISPLAY_MANAGER\
$GAME\

echo "Done Downloader-Script"
