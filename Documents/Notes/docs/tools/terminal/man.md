# man 手册使用指南

## 一句话理解

man 是 Linux 系统的手册页面，查看命令、函数、配置文件等的详细说明。

```bash
man ls
man 5 passwd
man -k copy
```

## 手册章节

手册分为 9 个章节：

| 章节 | 内容 | 例子 |
|------|------|------|
| 1 | 用户命令 | `man ls` |
| 2 | 系统调用 | `man 2 open` |
| 3 | 库函数 | `man 3 printf` |
| 4 | 特殊文件（/dev） | `man 4 null` |
| 5 | 文件格式和配置文件 | `man 5 passwd` |
| 6 | 游戏 | `man 6 fortune` |
| 7 | 杂项（宏包、协议等） | `man 7 signal` |
| 8 | 系统管理命令 | `man 8 reboot` |
| 9 | 内核例程 | `man 9 kmalloc` |

```bash
# 指定章节
man 1 passwd    # passwd 命令
man 5 passwd    # /etc/passwd 文件格式

# 查看所有章节的匹配
man -a passwd   # 依次显示所有章节
```

## 基本操作

### 移动

| 快捷键 | 作用 |
|--------|------|
| `j` / `k` | 下/上移一行 |
| `Ctrl + d` | 下移半页 |
| `Ctrl + u` | 上移半页 |
| `f` / `b` | 下/上移一页 |
| `g` | 跳转到开头 |
| `G` | 跳转到末尾 |
| `q` | 退出 |

### 搜索

| 快捷键 | 作用 |
|--------|------|
| `/pattern` | 向下搜索 |
| `?pattern` | 向上搜索 |
| `n` | 下一个匹配 |
| `N` | 上一个匹配 |
| `Esc + u` | 取消高亮 |

## 常用命令

```bash
# 查看命令手册
man command

# 查看配置文件手册
man 5 config-file

# 搜索描述（关键词）
man -k keyword
apropos keyword

# 搜索描述（更精确）
man -K keyword   # 全文搜索（较慢）

# 查看简短描述
man -f command
whatis command

# 指定手册路径
man -M /path/to/man command
```

## 实用技巧

### 查看内置命令

```bash
# bash 内置命令没有独立手册页
help cd
help read
help [[
```

### 查看命令位置

```bash
# 查看命令所在章节
man -w ls
# /usr/share/man/man1/ls.1.gz

# 查看命令的所有手册位置
man -aw printf
# /usr/share/man/man1/printf.1.gz
# /usr/share/man/man3/printf.3.gz
```

### 输出重定向

```bash
# 保存到文件
man ls > ls.txt

# 打印为文本（无格式）
man ls | col -b > ls.txt

# 查看为 PDF
man -t ls | ps2pdf - ls.pdf
```

## 配置

### 设置默认章节顺序

```bash
# ~/.manpath 或 /etc/man_db.conf
# 默认搜索顺序
MANDATORY_MANPATH /usr/share/man
MANDATORY_MANPATH /usr/local/share/man
```

### 启用彩色显示

```bash
# 添加到 ~/.bashrc
export PAGER="less -R"
export MANPAGER="less -R"
export LESS_TERMCAP_mb=$'\E[1;31m'     # 开始闪烁
export LESS_TERMCAP_md=$'\E[1;36m'     # 开始粗体
export LESS_TERMCAP_me=$'\E[0m'        # 结束
export LESS_TERMCAP_se=$'\E[0m'        # 结束
export LESS_TERMCAP_so=$'\E[01;33m'    # 开始反向
export LESS_TERMCAP_ue=$'\E[0m'        # 结束
export LESS_TERMCAP_us=$'\E[1;32m'     # 开始下划线
```

### 使用 bat 作为分页器

```bash
# 安装 bat
sudo pacman -S bat

# 设置 manpager
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
```

## 查找相关命令

```bash
# 查找与 copy 相关的命令
man -k copy | grep "\(1\)"

# 查找系统调用
man -k _chdir

# 查看同一命令的不同版本
man -a printf
```

## 快速参考

| 目的 | 命令 |
|------|------|
| 查看命令用法 | `man command` |
| 查看配置文件格式 | `man 5 filename` |
| 搜索命令 | `man -k keyword` |
| 简短描述 | `whatis command` |
| 指定章节 | `man 2 syscall` |
| 查看所有章节 | `man -a command` |
| 保存为文本 | `man command \| col -b > file.txt` |

## 一句话总结

man 核心：`man command` 查看命令，`man 5 config` 看配置文件格式，`j/k` 移动，`/` 搜索，`q` 退出，`man -k keyword` 搜索相关命令。不知道用哪个命令时先用 `man -k` 搜关键词。
