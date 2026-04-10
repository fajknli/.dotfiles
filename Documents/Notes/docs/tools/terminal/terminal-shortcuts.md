# 终端快捷键速查

## 光标移动

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + a` | 跳到行首 |
| `Ctrl + e` | 跳到行尾 |
| `Ctrl + b` | 向左移动一个字符 |
| `Ctrl + f` | 向右移动一个字符 |
| `Alt + b` | 向左移动一个单词 |
| `Alt + f` | 向右移动一个单词 |
| `Ctrl + xx` | 在光标当前位置和行首之间切换 |

## 删除/剪切

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + h` | 删除光标前一个字符 |
| `Ctrl + d` | 删除光标后一个字符 |
| `Ctrl + w` | 删除光标前一个单词 |
| `Alt + d` | 删除光标后一个单词 |
| `Ctrl + u` | 删除光标前所有内容 |
| `Ctrl + k` | 删除光标后所有内容 |
| `Ctrl + y` | 粘贴上次删除的内容 |

## 历史命令

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + p` | 上一条命令 |
| `Ctrl + n` | 下一条命令 |
| `Ctrl + r` | 反向搜索历史命令 |
| `Ctrl + s` | 正向搜索历史命令 |
| `Ctrl + g` | 退出搜索模式 |
| `Ctrl + o` | 执行搜索到的命令 |
| `!!` | 上一条命令 |
| `!$` | 上一条命令的最后一个参数 |
| `!^` | 上一条命令的第一个参数 |
| `!*` | 上一条命令的所有参数 |
| `!n` | 历史中的第 n 条命令 |
| `!-n` | 倒数第 n 条命令 |
| `!string` | 最近以 string 开头的命令 |
| `!?string?` | 最近包含 string 的命令 |
| `^old^new^` | 上一条命令中替换 old 为 new |
| `!!:s/old/new/` | 上一条命令中替换 old 为 new |

## 控制终端

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + l` | 清屏 |
| `Ctrl + c` | 终止当前命令 |
| `Ctrl + z` | 暂停当前命令（后台） |
| `Ctrl + d` | 退出当前 shell |
| `Ctrl + s` | 暂停屏幕输出 |
| `Ctrl + q` | 恢复屏幕输出 |
| `Ctrl + r` | 重绘屏幕（同 Ctrl+l） |

## Tab 补全

| 快捷键 | 作用 |
|--------|------|
| `Tab` | 自动补全命令/文件名 |
| `Alt + /` | 文件名补全（同 Tab） |
| `Alt + ?` | 显示所有可能的补全 |
| `Alt + *` | 将所有可能的补全插入命令行 |

## 作业控制

| 命令/快捷键 | 作用 |
|-------------|------|
| `jobs` | 查看后台作业 |
| `fg %n` | 将作业 n 调到前台 |
| `bg %n` | 将作业 n 放到后台运行 |
| `kill %n` | 终止作业 n |
| `Ctrl + z` | 暂停当前前台作业 |
| `disown %n` | 从 shell 作业表移除（不随 shell 关闭） |

## 命令行编辑模式切换

Bash 默认使用 Emacs 模式，可以切换到 Vi 模式：

```bash
# 切换到 Vi 模式
set -o vi

# 切换回 Emacs 模式
set -o emacs

Vi 模式下，按 `Esc` 进入普通模式，可以使用 vim 风格移动：

| 普通模式 | 作用 |
|----------|------|
| `h/j/k/l` | 左/下/上/右移动 |
| `w/b` | 前/后移动一个单词 |
| `0` | 行首 |
| `$` | 行尾 |
| `i/a` | 进入插入模式 |
| `x` | 删除光标字符 |
| `dw` | 删除单词 |
| `dd` | 删除整行 |
| `u` | 撤销 |
| `p` | 粘贴 |
| `/` | 搜索 |

## 其他有用快捷键

| 快捷键 | 作用 |
|--------|------|
| `Alt + .` | 插入上一个命令的最后一个参数 |
| `Alt + #` | 注释当前行（用于临时保存） |
| `Alt + r` | 撤销对当前命令行的所有修改 |
| `Alt + p` | 显示上一个命令的非交互式补全 |
| `Alt + y` | 从历史中插入之前删除的文本 |
| `Alt + <` | 移动到历史命令的开头 |
| `Alt + >` | 移动到历史命令的末尾 |
| `Alt + .` | 依次插入上一条命令的参数 |

## 常用命令别名

添加到 `~/.bashrc` 或 `~/.bash_aliases`：

```bash
# 文件操作
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias mkdir='mkdir -p'

# 查看
alias df='df -h'
alias du='du -h'
alias free='free -h'
alias grep='grep --color=auto'
alias less='less -R'

# 导航
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias ~='cd ~'
alias -='cd -'

# 快捷编辑
alias vimrc='vim ~/.vimrc'
alias bashrc='vim ~/.bashrc'
alias reload='source ~/.bashrc'

# 网络
alias myip='curl -s ifconfig.me'
alias ports='netstat -tlnp'

# 系统
alias reboot='sudo reboot'
alias poweroff='sudo poweroff'
alias update='sudo pacman -Syu'
```

## 历史命令配置

添加到 `~/.bashrc`：

```bash
# 历史命令大小
export HISTSIZE=10000
export HISTFILESIZE=50000

# 显示时间戳
export HISTTIMEFORMAT="%F %T "

# 忽略重复和空格开头的命令
export HISTCONTROL=ignoreboth

# 忽略特定命令
export HISTIGNORE="ls:ll:cd:exit:pwd:clear"

# 立即追加到历史文件
shopt -s histappend
export PROMPT_COMMAND="history -a;$PROMPT_COMMAND"
```

## 快捷修复技巧

| 场景 | 操作 |
|------|------|
| 命令打错 | `^错误^正确^` 或 `!!:s/错误/正确/` |
| 忘记 sudo | `sudo !!` |
| 创建目录并进入 | `mkdir -p dir && cd !$` |
| 备份文件 | `cp file{,.bak}` |
| 快速清空文件 | `> file` |
| 重复上一个命令但替换参数 | `vim file1` → `!!:s/file1/file2/` |

## 一句话总结

终端快捷键核心：`Ctrl+a/e` 行首/行尾，`Ctrl+u/k` 删前/删后，`Ctrl+r` 搜索历史，`Ctrl+l` 清屏，`!!` 重复上条命令，`!$` 上条命令最后一个参数。忘记加 sudo 用 `sudo !!`。
