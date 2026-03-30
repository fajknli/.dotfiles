# 如果是交互式登录 shell，则加载 .bashrc
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

# 启动剪切板历史记录
wl-paste --watch cliphist store &

# 启动一些后台程序（如果需要）
# nohup some_program &

if [ -e /home/fajknli/.nix-profile/etc/profile.d/nix.sh ]; then . /home/fajknli/.nix-profile/etc/profile.d/nix.sh; fi # added by Nix installer
