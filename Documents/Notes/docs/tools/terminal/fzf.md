# fzf - 模糊查找器

## 一句话理解

fzf 是一个通用的模糊查找工具，可以快速搜索文件、历史命令、进程等，配合 Ctrl+R 使用体验极佳。

```bash
# 交互式查找文件
find . -type f | fzf

# 交互式查找历史命令（Ctrl+R 增强版）
history | fzf

# 交互式查找并执行
fzf --preview 'cat {}'
```

## 安装

```bash
# Arch Linux
sudo pacman -S fzf

# 启用 bash 集成
source /usr/share/fzf/key-bindings.bash
source /usr/share/fzf/completion.bash
```

## 基本用法

### 文件查找

```bash
# 查找当前目录所有文件
ls | fzf

# 递归查找所有文件
find . -type f | fzf

# 使用 fd 替代 find（更快）
fd . | fzf

# 只查找特定类型
find . -name "*.py" | fzf
fd .py | fzf
```

### 预览功能

```bash
# 预览文件内容
fzf --preview 'cat {}'

# 预览时显示前 100 行
fzf --preview 'head -100 {}'

# 预览图片（需要 chafa）
fzf --preview 'chafa {}'

# 预览时带颜色
fzf --preview 'bat --color=always {}'
```

### 多选

```bash
# 启用多选（Tab 选择，Shift+Tab 取消）
fzf --multi

# 选择多个文件并打开
fd . | fzf --multi | xargs nvim
```

## 常用选项

| 选项 | 说明 |
|------|------|
| `--height 40%` | 设置高度 |
| `--border` | 显示边框 |
| `--multi` | 允许多选 |
| `--preview 'cmd {}'` | 预览命令 |
| `--preview-window right:60%` | 预览窗口位置和大小 |
| `--reverse` | 列表在上，输入框在下 |
| `--cycle` | 循环滚动 |
| `--tac` | 反向显示（最新的在上） |
| `--no-sort` | 不排序 |
| `--exact` | 精确匹配 |
| `--ansi` | 支持 ANSI 颜色 |

## Bash 集成（重要）

### 配置 ~/.bashrc

```bash
# 启用 fzf
if [ -f /usr/share/fzf/key-bindings.bash ]; then
    source /usr/share/fzf/key-bindings.bash
    source /usr/share/fzf/completion.bash
fi

# 设置选项
export FZF_DEFAULT_OPTS="--height 40% --border --reverse --cycle"
export FZF_DEFAULT_COMMAND="fd --hidden --strip-cwd-prefix --exclude .git"
export FZF_CTRL_T_COMMAND="$FZF_DEFAULT_COMMAND"
export FZF_ALT_C_COMMAND="fd --type d --hidden --strip-cwd-prefix --exclude .git"

# 预览配置
export FZF_CTRL_T_OPTS="--preview 'bat --color=always {} 2>/dev/null || cat {}'"
export FZF_ALT_C_OPTS="--preview 'tree -C {} | head -50'"
```

### 快捷键

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + T` | 搜索当前目录文件 |
| `Alt + C` | 搜索并进入目录 |
| `Ctrl + R` | 搜索历史命令（增强版） |

### Ctrl+R 增强效果

```bash
# 默认 Ctrl+R 只能按上下键选择
# 配置 fzf 后，Ctrl+R 会弹出模糊搜索框
# 输入任意关键词，实时过滤历史命令
```

## 高级用法

### 搜索历史命令

```bash
# 自定义历史搜索
history | fzf --tac --no-sort | sed 's/^[0-9]* *//'

# 搜索并直接执行
eval "$(history | fzf --tac --no-sort | sed 's/^[0-9]* *//')"
```

### 搜索进程

```bash
# 搜索并 kill 进程
ps aux | fzf --multi | awk '{print $2}' | xargs kill -9

# 带预览的进程搜索
ps aux | fzf --preview 'echo {}' --preview-window down:5
```

### 搜索 git 分支

```bash
# 切换分支
git branch | fzf | xargs git checkout

# 删除分支
git branch | fzf --multi | xargs git branch -D

# 搜索并查看 commit
git log --oneline | fzf | awk '{print $1}' | xargs git show
```

### 结合其他命令

```bash
# 快速 cd 到常用目录
cd $(find ~ -type d 2>/dev/null | fzf)

# 使用 zoxide + fzf（你笔记中有 zoxide）
z $(zoxide query -l | fzf --height 40% --reverse | awk '{print $2}')

# 交互式 kill 进程
kill -9 $(ps aux | fzf | awk '{print $2}')

# 交互式 ssh
ssh $(grep -v '^#' ~/.ssh/config | grep 'Host ' | awk '{print $2}' | fzf)

# 交互式 docker 容器进入
docker ps | fzf | awk '{print $1}' | xargs docker exec -it bash
```

## 自定义脚本示例

### 脚本：`fd`（快速 cd）

```bash
#!/bin/bash
# ~/.local/bin/fd - 快速跳转到常用目录

TARGET=$(find ~ -maxdepth 3 -type d 2>/dev/null | fzf --height 40% --reverse --preview 'ls -la {}')
if [ -n "$TARGET" ]; then
    cd "$TARGET" || exit
fi
```

### 脚本：`fkill`（交互式杀进程）

```bash
#!/bin/bash
# ~/.local/bin/fkill

ps aux | fzf --multi --reverse | awk '{print $2}' | xargs kill -9
```

### 脚本：`fzf-git`（git 分支管理）

```bash
#!/bin/bash
# ~/.local/bin/fzf-git

BRANCH=$(git branch -a | fzf --height 40% --reverse --preview 'git log --oneline --graph {1} | head -20')
BRANCH=$(echo "$BRANCH" | sed 's/^[* ]*//' | sed 's/remotes\/origin\///')
[ -n "$BRANCH" ] && git checkout "$BRANCH"
```

## 常用组合

| 命令 | 作用 |
|------|------|
| `Ctrl + T` | 搜索文件 |
| `Alt + C` | 搜索目录 |
| `Ctrl + R` | 搜索历史命令 |
| `**` + Tab | 路径补全（需要配置） |
| `kill **` + Tab | 搜索进程 PID |
| `ssh **` + Tab | 搜索 SSH 主机 |
| `cd **` + Tab | 搜索目录 |

## 补全配置

```bash
# ~/.bashrc 中添加
# 启用 ** 补全
source /usr/share/fzf/completion.bash

# 使用示例
# cd **<Tab>        # 选择目录
# vim **<Tab>       # 选择文件
# kill **<Tab>      # 选择进程
# ssh **<Tab>       # 选择 SSH 主机
```

## 配色方案

```bash
# ~/.bashrc
export FZF_DEFAULT_OPTS="
--color=bg+:#313244,bg:#1e1e2e,spinner:#f5e0dc,hl:#f38ba8
--color=fg:#cdd6f4,header:#f38ba8,info:#cba6f7,pointer:#f5e0dc
--color=marker:#b4befe,fg+:#cdd6f4,prompt:#cba6f7,hl+:#f38ba8
"
```

## 一句话总结

fzf 核心：`Ctrl+R` 搜索历史命令（必用），`Ctrl+T` 搜索文件，`Alt+C` 搜索目录，`**`+Tab 补全。配合 `--preview` 预览文件内容，`--multi` 多选。配置好 `~/.bashrc` 后每天都会用到。
