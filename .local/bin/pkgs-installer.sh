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
arch-wiki-docs \
arch-wiki-lite \
arch-wiki-docs-zh-cn \
firejail \
"

# Ai
ai="\
llama.cpp \
rocm-hip-sdk \
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
make \
shellcheck \
xh \
rustup \
gcc \
yt-dlp \
unrar \
zoxide \
wev \
neomutt \
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

# Python 库 (Python Libraries)
python_libraries="\
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
python-sphinx \
python-sphinx-lv2-theme \
python-sphinx-furo \
python-sphinx-autobuild \
python-sphinx-alabaster-theme \
python-guzzle-sphinx-theme \
python-sphinx_rtd_theme \
"

# 服务器工具 (Server Tools)
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

# 文档与词典 (Documentation & Dictionary)
documentation_dictionary="\
sdcv \
"
# 图标
icon_theme="\
papirus-icon-theme \
"
#gtk 主题
gtk_theme="\
adapta-gtk-theme \
"
# cursor-theme
cursor_theme="\
breeze-cursors \
"

sudo pacman -Syu --noconfirm --needed --color auto \
$documentation_dictionary\
$server_tools\
$python_libraries\
$qt\
$graphics_drivers_libraries\
$audio_bluetooth\
$wayland_wm\
$gui_application\
$cli_tools\
$system_utilities\
$network_tools\
$fonts_localization\
$ai\
$icon_theme\
$gtk_theme\
$cursor_theme\

