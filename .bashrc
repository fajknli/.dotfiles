# ~/.bashrc

# 加载自定义环境变量
if [ -f ~/.bash_exports ]; then
    source ~/.bash_exports
fi

# 加载别名
if [ -f ~/.bash_aliases ]; then
    source ~/.bash_aliases
fi

# 加载函数
if [ -f ~/.bash_functions ]; then
    source ~/.bash_functions
fi

# 加载提示符配置
if [ -f ~/.bash_prompt ]; then
    source ~/.bash_prompt
fi

# 自动启动 Zellij
# eval "$(zellij setup --generate-auto-start bash)"
# 自动启动 zoxide,智能化现代cd
# eval "$(zoxide init --cmd cd bash)"
wl-paste --watch cliphist store &

# Bash 模式
set -o emacs

# 绑定快捷键
# bind '"\ew":"fzfcd\n"'
# bind '"\ee":"mcc\n"'

# Java Home
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
export PATH=$JAVA_HOME/bin:$PATH

# 禁用历史记录临时文件
shopt -s histappend
export HISTFILE=~/.bash_history
export HISTCONTROL=ignoredups:erasedups
export HISTSIZE=100000
export HISTFILESIZE=100000
# 确保历史记录立即写入，而不是生成临时文件
PROMPT_COMMAND="history -a; history -c; history -r; $PROMPT_COMMAND"
