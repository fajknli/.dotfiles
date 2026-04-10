# ripgrep (rg) - 快速代码搜索工具

## 一句话理解

ripgrep（rg）是一个递归搜索工具，比 grep 更快，自动忽略 .gitignore 中的文件，默认递归搜索。

```bash
# 在当前目录搜索 "hello"
rg hello

# 等价于
grep -r hello . --exclude-dir=.git
```

## 安装

```bash
# Arch Linux
sudo pacman -S ripgrep

# 其他方式
cargo install ripgrep
sudo apt install ripgrep   # Ubuntu
brew install ripgrep       # macOS
```

## 基本用法

### 搜索内容

```bash
# 搜索 "pattern"（默认递归）
rg pattern

# 搜索特定文件类型
rg -t py "def main"
rg -t js "console.log"
rg -t md "fzf"

# 指定文件扩展名
rg -g "*.py" "import"

# 不区分大小写
rg -i "error"

# 整个单词匹配
rg -w "fn"

# 使用正则表达式
rg "fn \w+"

# 固定字符串（更快）
rg -F "https://"
```

### 搜索位置限制

```bash
# 限制搜索目录深度
rg -d 3 pattern

# 只在当前目录（不递归）
rg -d 1 pattern

# 只搜索特定目录
rg pattern src/
rg pattern src/ tests/

# 排除目录
rg pattern --glob '!*.pyc'
rg pattern --glob '!tests/*'

# 排除多个
rg pattern --glob '!*.{pyc,log,tmp}'
```

## 常用选项

| 选项 | 说明 |
|------|------|
| `-i` | 忽略大小写 |
| `-w` | 整个单词匹配 |
| `-F` | 固定字符串（不解析正则） |
| `-l` | 只显示文件名 |
| `-L` | 只显示不匹配的文件名 |
| `-c` | 显示匹配行数 |
| `-n` | 显示行号（默认开启） |
| `-N` | 不显示行号 |
| `-m 10` | 每个文件最多匹配 10 行 |
| `-A 2` | 显示匹配行后 2 行 |
| `-B 2` | 显示匹配行前 2 行 |
| `-C 2` | 显示匹配行前后各 2 行 |
| `-M 100` | 限制匹配行最大长度 |
| `--hidden` | 搜索隐藏文件 |
| `--no-ignore` | 不忽略 .gitignore |
| `--no-ignore-vcs` | 只忽略 .gitignore |
| `-u` | 忽略所有忽略规则（搜索全部） |
| `-uu` | 也搜索二进制文件 |
| `-uuu` | 搜索所有（不排除任何文件） |

## 文件类型过滤

```bash
# 查看支持的文件类型
rg --type-list

# 搜索特定类型
rg -t py "def"
rg -t md "install"
rg -t json "version"

# 搜索类型列表
rg -T py -T js "function"  # 排除 Python 和 JS

# 自定义类型
rg --type-add 'mytype:*.{txt,md}' -t mytype "pattern"
```

## 输出格式

```bash
# 只显示文件名
rg -l pattern

# 只显示匹配内容（不显示行号和文件名）
rg -o pattern

# 显示行号（默认）
rg -n pattern

# JSON 格式输出
rg --json pattern

# 统计匹配数
rg -c pattern

# 统计每个文件匹配数
rg -c pattern

# 显示上下文
rg -C 3 pattern   # 前后各3行
rg -A 5 pattern   # 后5行
rg -B 5 pattern   # 前5行
```

## 与 grep 对比

| 特性 | grep | ripgrep |
|------|------|---------|
| 默认递归 | 需要 -r | 是 |
| .gitignore 忽略 | 否 | 是 |
| 自动忽略二进制 | 否 | 是 |
| 彩色输出 | 需要 --color | 默认开启 |
| 速度 | 慢 | 快 |
| 并行处理 | 否 | 是 |
| 文件类型过滤 | 需要组合 | 内置 |

### 速度对比

```bash
# grep 搜索 Linux 内核
time grep -r "skb" .

# ripgrep 搜索
time rg "skb"

# rg 通常快 3-10 倍
```

## 实际例子

### 1. 代码搜索

```bash
# 搜索 Python 中的 TODO
rg -t py "TODO"

# 搜索函数定义
rg "^def " -t py
rg "^fn " -t rs

# 搜索 import 语句
rg "^import " -t py
rg "^use " -t rs
```

### 2. 配置文件搜索

```bash
# 搜索配置文件中的设置
rg "Proxy" /etc/
rg "Server" ~/.config/

# 排除注释和空行
rg -v "^#|^$" /etc/nginx/nginx.conf
```

### 3. 日志分析

```bash
# 搜索错误日志
rg "ERROR" /var/log/

# 显示上下文
rg -C 3 "ERROR" app.log

# 统计错误数量
rg -c "ERROR" app.log

# 只看今天的日志
rg "2026-04-09" app.log | rg "ERROR"
```

### 4. 项目搜索技巧

```bash
# 在 git 项目中搜索（自动忽略 .gitignore）
rg "pattern"

# 包含隐藏文件
rg --hidden "pattern"

# 搜索所有文件（不忽略任何文件）
rg -u "pattern"

# 包括二进制文件
rg -uu "pattern"
```

## 结合其他命令

```bash
# 搜索并替换（结合 sed）
rg -l "old" | xargs sed -i 's/old/new/g'

# 搜索并查看文件
rg -l "pattern" | xargs nvim

# 搜索并删除匹配的文件
rg -l "TODO" | xargs rm

# 搜索并统计行数
rg "pattern" | wc -l
```

## 配置文件

`~/.config/ripgrep/config`

```bash
# 默认选项
--max-columns=150
--colors=path:fg:magenta
--colors=line:fg:green
--colors=match:fg:red
--colors=match:style:bold

# 忽略大小写（默认）
-i

# 智能大小写（有大小写时区分）
-S

# 不显示行号
-N
```

## 常用别名

```bash
# ~/.bashrc
alias rg='rg --colors=path:fg:cyan --colors=line:fg:yellow --colors=match:fg:red'
alias rgl='rg --files-with-matches'      # 只显示文件名
alias rgc='rg --count'                   # 显示匹配计数
alias rgctx='rg -C 3'                    # 上下文3行
```

## 快速参考

| 目的 | 命令 |
|------|------|
| 搜索文本 | `rg pattern` |
| 搜索特定类型 | `rg -t py pattern` |
| 只显示文件名 | `rg -l pattern` |
| 显示匹配数 | `rg -c pattern` |
| 忽略大小写 | `rg -i pattern` |
| 正则搜索 | `rg 'fn \w+'` |
| 固定字符串 | `rg -F 'https://'` |
| 显示上下文 | `rg -C 3 pattern` |
| 排除目录 | `rg --glob '!test/*' pattern` |
| 搜索隐藏文件 | `rg --hidden pattern` |
| 搜索所有文件 | `rg -u pattern` |

## 一句话总结

ripgrep 核心：`rg pattern` 递归搜索，自动忽略 `.gitignore`，比 grep 快很多。`-t py` 只搜 Python，`-l` 只显示文件名，`-C 3` 显示上下文，`-u` 搜索隐藏文件，`-uu` 搜二进制。日常代码搜索首选。
