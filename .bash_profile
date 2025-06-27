# 如果是交互式登录 shell，则加载 .bashrc
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

# 其他登录时需要的配置，比如设置 PATH，或执行一些一次性的命令
# 例如，设置 locale
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
# export LANG=zh_CN.UTF-8
# export LC_ALL=zh_CN.UTF-8

export BROWSER="/usr/bin/firefox"

# 启动一些后台程序（如果需要）
# nohup some_program &

# 其他登录时配置（可以根据需求添加）
# 输入法
#export GTK_IM_MODULE=fcitx
#export QT_IM_MODULE=fcitx
#export XMODIFIERS=@im=fcitx
#export SDL_IM_MODULE=fcitx
#export GLFW_IM_MODULE=ibus
#export GLFW_IM_MODULE=fcitx
#export INPUT_METHOD=fcitx

# Wayland 后端
export MOZ_ENABLE_WAYLAND=1
export QT_QPA_PLATFORM=wayland
export GDK_BACKEND=wayland
export SDL_VIDEODRIVER=wayland
# export WLR_RENDERER=vulkan

# 默认程序
export EDITOR=nvim
export VISUAL=nvim

export QT_QPA_PLATFORM=wayland

