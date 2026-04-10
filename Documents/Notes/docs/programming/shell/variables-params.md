# Shell 变量与参数

## 变量类型

### 环境变量

```sh
# 查看环境变量
echo "$HOME"
echo "$PATH"
echo "$SHELL"
echo "$USER"

# 设置环境变量（当前 shell 及其子进程）
export MY_VAR="hello"

# 设置临时环境变量（仅当前命令）
NAME="张三" ./script.sh
```

### 普通变量

```sh
# 定义变量（等号两边不能有空格）
name="张三"
age=25
path=/usr/local/bin

# 使用变量
echo "$name"
echo "${name}"  # 花括号用于明确边界
```

### 只读变量

```sh
readonly PI=3.14159
PI=3.14  # 错误：只读变量

# 或使用 readonly 命令
name="张三"
readonly name
name="李四"  # 错误
```

## 变量替换

### 默认值

| 语法 | 说明 |
|------|------|
| `${var:-word}` | 如果 var 未设置或为空，使用 word |
| `${var:=word}` | 如果 var 未设置或为空，设置 var 为 word |
| `${var:+word}` | 如果 var 已设置且非空，使用 word |
| `${var:?word}` | 如果 var 未设置或为空，显示 word 并退出 |

```sh
# 使用默认值
name="${1:-默认姓名}"
echo "$name"

# 设置默认值
: "${MY_DIR:=/tmp/default}"
echo "$MY_DIR"

# 条件取值
debug="${DEBUG:+启用调试}"
echo "$debug"  # 如果 DEBUG 有值则输出"启用调试"

# 错误提示
file="${1:?请提供文件名}"
```

### 字符串长度

```sh
name="张三"
echo "${#name}"  # 2（中文字符数取决于编码）

path="/usr/local/bin"
echo "${#path}"  # 13
```

### 子串提取

```sh
str="Hello World"

# 从指定位置开始（0 索引）
echo "${str:0:5}"   # Hello
echo "${str:6:5}"   # World
echo "${str:6}"     # World（到末尾）

# 从末尾开始
echo "${str: -5}"   # World（注意空格）
```

### 字符串删除

| 语法 | 说明 |
|------|------|
| `${var#pattern}` | 删除最短匹配的前缀 |
| `${var##pattern}` | 删除最长匹配的前缀 |
| `${var%pattern}` | 删除最短匹配的后缀 |
| `${var%%pattern}` | 删除最长匹配的后缀 |

```sh
file="/home/user/file.txt"

# 删除前缀
echo "${file#/home/}"     # user/file.txt
echo "${file##*/}"        # file.txt

# 删除后缀
echo "${file%.txt}"       # /home/user/file
echo "${file%/*}"         # /home/user
echo "${file%%/*}"        # （空）

# 实际应用
filename="backup.2024.tar.gz"
echo "${filename%.gz}"     # backup.2024.tar
echo "${filename%%.*}"     # backup
```

### 字符串替换

| 语法 | 说明 |
|------|------|
| `${var/old/new}` | 替换第一个匹配 |
| `${var//old/new}` | 替换所有匹配 |
| `${var/#old/new}` | 替换开头的匹配 |
| `${var/%old/new}` | 替换结尾的匹配 |

```sh
str="one two three two"

echo "${str/two/TWO}"        # one TWO three two
echo "${str//two/TWO}"       # one TWO three TWO
echo "${str/#one/ONE}"       # ONE two three two
echo "${str/%two/END}"       # one two three END
```

## 位置参数

### 基本参数

```sh
#!/bin/sh
echo "脚本名: $0"
echo "参数个数: $#"
echo "所有参数: $@"
echo "第一个: $1"
echo "第二个: $2"
echo "第十个: ${10}"  # 10 以上需要花括号
```

### $@ vs $*

```sh
#!/bin/sh

show_args() {
    echo "使用 \$@:"
    for arg in "$@"; do
        echo "  $arg"
    done
    
    echo "使用 \$*:"
    for arg in $*; do
        echo "  $arg"
    done
}

show_args "a b" c
# 使用 $@:
#   a b
#   c
# 使用 $*:
#   a
#   b
#   c
```

### shift 移动参数

```sh
#!/bin/sh

echo "初始参数: $@"

while [ $# -gt 0 ]; do
    echo "当前第一个: $1"
    shift
done
# 输出:
# 初始参数: a b c d
# 当前第一个: a
# 当前第一个: b
# 当前第一个: c
# 当前第一个: d
```

## 特殊变量

| 变量 | 说明 |
|------|------|
| `$0` | 脚本名称 |
| `$1-$9` | 位置参数 |
| `$#` | 参数个数 |
| `$@` | 所有参数（分开引用） |
| `$*` | 所有参数（合并为字符串） |
| `$$` | 当前 shell 进程 ID |
| `$?` | 上一条命令的退出码 |
| `$!` | 最后一个后台进程的 PID |
| `$-` | 当前 shell 选项 |

```sh
#!/bin/sh

echo "脚本 PID: $$"
echo "上一个命令退出码: $?"
sleep 10 &
echo "后台进程 PID: $!"
echo "Shell 选项: $-"
```

## 命令替换

```sh
# 旧语法（不推荐）
today=`date`
echo "$today"

# 新语法（推荐）
today=$(date)
echo "$today"

# 嵌套使用
file_count=$(ls -1 | wc -l)
dir_name=$(basename "$(pwd)")

# 数学运算
result=$((10 + 20))
```

## 环境变量文件

### /etc/profile 和 ~/.profile

```sh
# 设置 PATH
export PATH="$HOME/bin:$PATH"

# 设置别名
alias ll='ls -la'

# 设置提示符
PS1='\u@\h:\w\$ '
```

### 常用环境变量

```sh
echo "$HOME"      # 用户主目录
echo "$PATH"      # 命令搜索路径
echo "$PWD"       # 当前工作目录
echo "$OLDPWD"    # 上一个工作目录
echo "$UID"       # 用户 ID
echo "$IFS"       # 内部字段分隔符（默认空格、制表、换行）
```

## 实际应用示例

### 解析命令行参数

```sh
#!/bin/sh

verbose=0
output=""
input=""

while [ $# -gt 0 ]; do
    case "$1" in
        -v|--verbose)
            verbose=1
            shift
            ;;
        -o|--output)
            output="$2"
            shift 2
            ;;
        -i|--input)
            input="$2"
            shift 2
            ;;
        -h|--help)
            echo "用法: $0 [-v] [-o output] [-i input]"
            exit 0
            ;;
        *)
            echo "未知选项: $1"
            exit 1
            ;;
    esac
done

echo "verbose: $verbose"
echo "output: $output"
echo "input: $input"
```

### 安全读取配置

```sh
#!/bin/sh

# 加载配置文件
config_file="${1:-./config.sh}"
if [ -f "$config_file" ]; then
    . "$config_file"
else
    echo "配置文件不存在: $config_file"
    exit 1
fi

# 使用带默认值的变量
db_host="${DB_HOST:-localhost}"
db_port="${DB_PORT:-3306}"
db_user="${DB_USER:-root}"

echo "连接 $db_host:$db_port 作为 $db_user"
```

### 临时文件处理

```sh
#!/bin/sh

# 创建临时文件
temp_file="/tmp/script.$$.tmp"
trap "rm -f $temp_file" EXIT

# 使用临时文件
echo "data" > "$temp_file"
cat "$temp_file"

# 自动删除
```

### 检查变量是否设置

```sh
#!/bin/sh

# 检查变量是否设置（包括空值）
if [ -n "${var+set}" ]; then
    echo "var 已设置"
else
    echo "var 未设置"
fi

# 检查变量是否设置且非空
if [ -n "$var" ]; then
    echo "var 已设置且非空"
fi
```
