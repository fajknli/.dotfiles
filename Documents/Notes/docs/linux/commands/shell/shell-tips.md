# Shell 脚本编程完整指南

## 目录

1. [历史命令快捷方式](#历史命令快捷方式)
2. [变量和参数处理](#变量和参数处理)
3. [条件判断](#条件判断)
4. [循环和迭代](#循环和迭代)
5. [函数编写](#函数编写)
6. [后台进程管理](#后台进程管理)
7. [输入输出重定向](#输入输出重定向)
8. [错误处理](#错误处理)
9. [调试技巧](#调试技巧)
10. [脚本安全](#脚本安全)
11. [常用一行技巧](#常用一行技巧)
12. [完整脚本模板](#完整脚本模板)

---

## 历史命令快捷方式

| 快捷方式 | 作用 | 例子 |
|----------|------|------|
| `!!` | 上一个命令 | `sudo !!` |
| `!$` | 上一个命令的最后一个参数 | `mkdir dir && cd !$` |
| `!^` | 上一个命令的第一个参数 | `echo a b c` → `!^` 输出 `a` |
| `!*` | 上一个命令的所有参数 | `cp a.txt b.txt` → `!*` 是 `a.txt b.txt` |
| `!:n` | 上一个命令的第 n 个参数（从1开始） | `!:1` 是第一个参数 |
| `!-n` | 倒数第 n 条命令 | `!-2` 执行倒数第二条 |
| `!string` | 最近以 string 开头的命令 | `!vim` |
| `!?string?` | 最近包含 string 的命令 | `!?error?` |
| `!!:s/old/new/` | 替换上一个命令中的字符串 | `!!:s/foo/bar/` |
| `^old^new^` | 快速替换上一条命令 | `^foo^bar^` |
| `Alt + .` | 插入上一个命令的最后一个参数 | 多次按往前翻 |

### 历史配置

```bash
# 添加到 ~/.bashrc
export HISTSIZE=10000          # 内存中历史命令数量
export HISTFILESIZE=50000      # 文件中保存数量
export HISTTIMEFORMAT="%F %T " # 显示时间戳
export HISTCONTROL=ignorespace # 空格开头的命令不记录

# 忽略特定命令
export HISTIGNORE="ls:ll:cd:exit:pwd:clear"
```

---

## 变量和参数处理

### 变量定义和作用域

```bash
# 本地变量
var="value"

# 环境变量（子进程继承）
export ENV_VAR="value"

# 只读变量
readonly CONST_VAR="value"

# 局部变量（函数内使用）
local local_var="value"

# 位置参数
$0, $1, $2...     # 脚本名和第1、2...个参数
$#                # 参数个数
$@                # 所有参数（每个参数单独引号）
$*                # 所有参数（一个字符串）
$$                # 当前 Shell PID
$?                # 上一条命令的退出码
$!                # 最后一个后台进程的 PID
```

### 参数扩展（Parameter Expansion）

| 语法 | 说明 | 例子 |
|------|------|------|
| `${var:-default}` | 变量为空或未定义时用默认值 | `name=${1:-"default"}` |
| `${var:=default}` | 变量为空或未定义时赋默认值 | `${VAR:=default}` |
| `${var:?error}` | 变量为空或未定义时显示错误 | `${MUST_SET:?请设置变量}` |
| `${var:+value}` | 变量非空时使用 value | `${DEBUG:+调试模式}` |
| `${#var}` | 字符串长度 | `len=${#str}` |
| `${var#pattern}` | 删除最短前缀 | `file=${path#*/}` |
| `${var##pattern}` | 删除最长前缀 | `filename=${path##*/}` |
| `${var%pattern}` | 删除最短后缀 | `dir=${path%/*}` |
| `${var%%pattern}` | 删除最长后缀 | `base=${name%%.*}` |
| `${var/old/new}` | 替换第一个 | `new=${str/foo/bar}` |
| `${var//old/new}` | 替换所有 | `new=${str//foo/bar}` |
| `${var/#old/new}` | 行首替换 | `${str/#a/A}` |
| `${var/%old/new}` | 行尾替换 | `${str/%z/Z}` |
| `${var^}` | 首字母大写 | `${str^}` |
| `${var^^}` | 全大写 | `${str^^}` |
| `${var,}` | 首字母小写 | `${str,}` |
| `${var,,}` | 全小写 | `${str,,}` |

### 参数扩展例子

```bash
# 默认值和错误处理
filename="${1:?请指定文件名}"
output="${2:-output.txt}"
: ${DEBUG:=0}  # 设置默认值

# 路径处理
path="/home/user/file.txt"
dir="${path%/*}"        # /home/user
file="${path##*/}"      # file.txt
name="${file%.*}"       # file
ext="${file##*.}"       # txt
basename="${file%%.*}"  # file（删掉第一个点及之后）

# 字符串操作
str="hello world hello"
echo "${str/hello/hi}"      # hi world hello
echo "${str//hello/hi}"     # hi world hi
echo "${str#* }"            # world hello（删掉第一个空格前）
echo "${str% *}"            # hello world（删掉最后一个空格后）
```

### 数组

```bash
# 定义数组
arr=(a b c d)
arr=([0]=a [2]=c)

# 索引数组操作
arr[0]="new"
echo "${arr[0]}"        # 第一个元素
echo "${arr[@]}"        # 所有元素
echo "${#arr[@]}"       # 数组长度
echo "${!arr[@]}"       # 所有索引

# 切片
echo "${arr[@]:1:2}"    # 从索引1取2个

# 追加
arr+=(e f)

# 关联数组（需要 bash 4+）
declare -A map
map["key1"]="value1"
map["key2"]="value2"
echo "${map[key1]}"
echo "${!map[@]}"       # 所有键
echo "${map[@]}"        # 所有值

# 遍历数组
for item in "${arr[@]}"; do
    echo "$item"
done

# 遍历索引
for i in "${!arr[@]}"; do
    echo "$i: ${arr[$i]}"
done
```

---

## 条件判断

### 文件测试

| 表达式 | 说明 |
|--------|------|
| `-e file` | 文件存在 |
| `-f file` | 是普通文件 |
| `-d file` | 是目录 |
| `-L file` | 是符号链接 |
| `-s file` | 文件非空 |
| `-r file` | 可读 |
| `-w file` | 可写 |
| `-x file` | 可执行 |
| `file1 -nt file2` | file1 比 file2 新 |
| `file1 -ot file2` | file1 比 file2 旧 |

### 字符串测试

| 表达式 | 说明 |
|--------|------|
| `-z string` | 字符串为空 |
| `-n string` | 字符串非空 |
| `string1 = string2` | 相等 |
| `string1 != string2` | 不等 |
| `string1 < string2` | 小于（字典序） |
| `string1 > string2` | 大于（字典序） |

### 数值比较

| 表达式 | 说明 |
|--------|------|
| `n1 -eq n2` | 等于 |
| `n1 -ne n2` | 不等于 |
| `n1 -gt n2` | 大于 |
| `n1 -ge n2` | 大于等于 |
| `n1 -lt n2` | 小于 |
| `n1 -le n2` | 小于等于 |

### 组合条件

```bash
# [ ] 写法（POSIX 兼容）
[ "$a" = "$b" -a "$c" = "$d" ]  # 与
[ "$a" = "$b" -o "$c" = "$d" ]  # 或
[ ! "$a" = "$b" ]               # 非
[ \( "$a" = "$b" \) -a "$c" = "$d" ]  # 分组

# [[ ]] 写法（bash 增强）
[[ $a = $b && $c = $d ]]        # 不需要引号
[[ $a = $b || $c = $d ]]
[[ ! $a = $b ]]
[[ $a =~ ^[0-9]+$ ]]            # 正则匹配
[[ $filename == *.txt ]]        # 通配符匹配
```

### 多分支选择

```bash
# if-elif-else
if [ condition ]; then
    command
elif [ condition2 ]; then
    command2
else
    command3
fi

# case 语句
case "$var" in
    pattern1)
        command1
        ;;
    pattern2|pattern3)
        command2
        ;;
    *)
        default_command
        ;;
esac

# case 例子
case "$1" in
    start|START)
        echo "启动服务"
        ;;
    stop)
        echo "停止服务"
        ;;
    restart)
        echo "重启服务"
        ;;
    *)
        echo "用法: $0 {start|stop|restart}"
        exit 1
        ;;
esac
```

### 条件短路

```bash
# 前一个成功则执行（AND）
command1 && command2

# 前一个失败则执行（OR）
command1 || command2

# 组合
command1 && command2 || command3

# 实际例子
[ -f "$file" ] && source "$file"
[ -d "$dir" ] || mkdir -p "$dir"
grep -q "error" log && echo "发现错误" || echo "无错误"

# 三元运算符效果
result=$([ condition ] && echo "true" || echo "false")
```

---

## 循环和迭代

### for 循环

```bash
# 遍历列表
for i in 1 2 3 4 5; do
    echo $i
done

# 遍历范围
for i in {1..10}; do
    echo $i
done
for i in {1..10..2}; do   # 步长2
    echo $i
done

# C 风格
for ((i=0; i<10; i++)); do
    echo $i
done

# 遍历文件
for file in *.txt; do
    echo "处理: $file"
done

# 遍历命令输出
for dir in $(ls -d */); do
    echo "目录: $dir"
done

# 遍历数组
arr=(a b c)
for item in "${arr[@]}"; do
    echo "$item"
done
```

### while 循环

```bash
# 基本
while [ condition ]; do
    command
done

# 读取文件
while IFS= read -r line; do
    echo "$line"
done < file.txt

# 读取 CSV
while IFS=',' read -r col1 col2 col3; do
    echo "$col1 - $col2"
done < data.csv

# 计数
count=0
while [ $count -lt 10 ]; do
    echo $count
    ((count++))
done

# 无限循环
while true; do
    command
    sleep 1
done
```

### until 循环

```bash
# 直到条件为真才停止
until [ -f /tmp/ready ]; do
    echo "等待文件..."
    sleep 1
done

# 等待服务启动
until curl -s http://localhost:8080/health > /dev/null; do
    echo "等待服务启动..."
    sleep 2
done
```

### 循环控制

```bash
# break：退出循环
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo $i
done

# continue：跳过当前迭代
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        continue
    fi
    echo $i
done

# 退出多层循环
for i in {1..3}; do
    for j in {1..3}; do
        if [ $i -eq 2 -a $j -eq 2 ]; then
            break 2
        fi
        echo "$i $j"
    done
done
```

---

## 函数编写

### 基本函数

```bash
# 定义函数
my_function() {
    echo "Hello"
}

function my_function {   # 另一种写法
    echo "Hello"
}

# 调用函数
my_function
my_function arg1 arg2

# 函数内使用参数
greet() {
    local name="${1:-World}"
    echo "Hello, $name!"
}
```

### 函数返回值

```bash
# 通过退出码返回（0-255）
is_file_exists() {
    [ -f "$1" ] && return 0 || return 1
}

if is_file_exists "/etc/passwd"; then
    echo "文件存在"
fi

# 通过 echo 返回字符串
get_config() {
    echo "value"
}
result=$(get_config)

# 返回多个值（通过全局变量或引用）
get_user_info() {
    local name="$1"
    # 设置全局变量
    USER_UID=$(id -u "$name")
    USER_GID=$(id -g "$name")
}
```

### 函数示例

```bash
# 日志函数
log_info() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') - $*"
}

log_error() {
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') - $*" >&2
}

log_debug() {
    if [ "${DEBUG:-0}" = "1" ]; then
        echo "[DEBUG] $(date '+%Y-%m-%d %H:%M:%S') - $*"
    fi
}

# 错误处理函数
die() {
    log_error "$*"
    exit 1
}

# 确认函数
confirm() {
    local prompt="${1:-是否继续?}"
    read -r -p "$prompt [y/N] " response
    case "$response" in
        [yY][eE][sS]|[yY])
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

# 使用
confirm "删除文件?" || die "用户取消"
```

---

## 后台进程管理

### 后台运行策略对比

| 方式 | 终端关闭后 | 可脱离终端 | 控制台输出 | 适用场景 |
|------|-----------|-----------|-----------|----------|
| `command &` | 停止 | 否 | 显示 | 临时后台任务 |
| `nohup command &` | 继续 | 否 | 输出到 nohup.out | 简单长期任务 |
| `disown` | 继续 | 否 | 已输出 | 已运行任务的脱离 |
| `setsid command` | 继续 | 是 | 显示 | 彻底脱离终端 |
| `command & disown` | 继续 | 否 | 显示 | 常用组合 |
| `(command &)` | 继续 | 是 | 显示 | 子 shell 方式 |

### 各种方式详解

```bash
# 1. 简单后台（终端关闭会停止）
long_running_task &

# 2. nohup（忽略挂断信号）
nohup long_running_task &
nohup long_running_task > /dev/null 2>&1 &  # 丢弃输出

# 3. disown（从 shell 作业表移除）
long_running_task &
disown
disown %1  # 移除指定作业

# 4. setsid（创建新会话，彻底脱离）
setsid long_running_task
setsid sh -c 'cd /app && ./server' &

# 5. 子 shell 方式
(
    cd /app
    ./server
) & disown
```

### 进程组操作

```bash
# 查看进程信息
ps -o pid,ppid,pgid,sid,cmd -p $$  # 当前 shell
ps -o pid,ppid,pgid,sid,cmd -p $PID

# 终止进程组
kill -- -$PGID                    # 负号表示进程组
kill -TERM -$PGID

# 获取进程组 ID
PGID=$(ps -o pgid= $PID | tr -d ' ')
PGID=$(awk '{print $5}' /proc/$PID/stat)

# 终止进程及其所有子进程
terminate_process() {
    local pid=$1
    local pgid=$(ps -o pgid= $pid | tr -d ' ')
    kill -TERM -$pgid
    sleep 2
    kill -KILL -$pgid 2>/dev/null
}
```

### PID 锁机制

```bash
#!/bin/bash
# 防止脚本重复运行

PID_FILE="/var/run/myscript.pid"

check_single_instance() {
    if [ -f "$PID_FILE" ]; then
        local old_pid=$(cat "$PID_FILE")
        if kill -0 "$old_pid" 2>/dev/null; then
            echo "脚本已在运行 (PID: $old_pid)"
            exit 1
        else
            echo "删除过期的 PID 文件"
            rm -f "$PID_FILE"
        fi
    fi
    echo $$ > "$PID_FILE"
    
    # 退出时清理
    trap "rm -f $PID_FILE" EXIT
}

check_single_instance

# 脚本主逻辑
echo "开始执行..."
sleep 100
```

### 进程监控

```bash
# 监控进程并自动重启
monitor_process() {
    local cmd="$1"
    local name="$2"
    
    while true; do
        log_info "启动 $name"
        $cmd
        log_error "$name 异常退出，5秒后重启..."
        sleep 5
    done
}

# 监控 PID
watch_pid() {
    local pid=$1
    while kill -0 "$pid" 2>/dev/null; do
        sleep 1
    done
    echo "进程 $pid 已退出"
}

# 等待多个进程完成
wait_for_all() {
    local pids=("$@")
    for pid in "${pids[@]}"; do
        wait "$pid"
    done
}
```

### 作业控制

```bash
# 查看后台作业
jobs
jobs -l  # 显示 PID

# 将作业放到后台
Ctrl + Z  # 暂停当前前台作业
bg        # 将暂停的作业放到后台运行

# 将作业放到前台
fg
fg %2     # 将作业2放到前台

# 后台作业在退出时发送 SIGHUP
# 让后台作业忽略挂断信号
disown %1
nohup command &  # 直接忽略
```

---

## 输入输出重定向

### 基本重定向

| 写法 | 说明 |
|------|------|
| `> file` | 标准输出到文件（覆盖） |
| `>> file` | 标准输出到文件（追加） |
| `2> file` | 标准错误到文件 |
| `2>> file` | 标准错误到文件（追加） |
| `&> file` | 所有输出到文件（bash） |
| `> file 2>&1` | 所有输出到文件（POSIX） |
| `< file` | 从文件读取输入 |
| `<< EOF` | Here Document |
| `<<< "string"` | Here String |
| `>| file` | 强制覆盖（忽略 noclobber） |

### 文件描述符操作

```bash
# 创建新的文件描述符
exec 3> output.txt    # 打开文件描述符3用于写入
exec 4< input.txt     # 打开文件描述符4用于读取
exec 5>> log.txt      # 追加模式

# 写入文件描述符
echo "hello" >&3

# 读取文件描述符
read -r line <&4

# 复制文件描述符
exec 6>&1             # 保存 stdout
exec 1>log.txt        # 重定向 stdout
echo "这是日志"
exec 1>&6             # 恢复 stdout

# 关闭文件描述符
exec 3>&-
exec 4<&-

# 交换 stdout 和 stderr
command 3>&1 1>&2 2>&3

# 丢弃输出
command > /dev/null 2>&1
```

### Here Document

```bash
# 基本用法
cat << EOF
多行文本
可以包含变量 $HOME
EOF

# 使用引号阻止变量展开
cat << "EOF"
变量 $HOME 不会展开
EOF

# 输出到文件
cat > config.conf << EOF
server=localhost
port=8080
EOF

# 追加到文件
cat >> .bashrc << 'EOF'
alias ll='ls -la'
EOF

# 缩进（<<- 会忽略前导制表符）
cat <<- EOF
	缩进的文本
	每行以制表符开头
EOF
```

### Here String

```bash
# 字符串作为输入
grep "error" <<< "this line has an error"

# 多个字符串
read -r name age <<< "张三 25"

# 配合 while 循环
while read -r line; do
    echo "$line"
done <<< "$(ls -la)"

# 计算字符串长度
wc -c <<< "$string"

# 发送邮件
mail -s "主题" user@example.com <<< "邮件内容"
```

### 进程替换

```bash
# 比较两个命令输出
diff <(ls dir1) <(ls dir2)

# 读取命令输出
while read -r line; do
    echo "$line"
done < <(ps aux)

# 合并文件
paste <(cut -d' ' -f1 file1) <(cut -d' ' -f2 file2)

# 重定向到多个命令
tee >(grep error > errors.log) >(grep warn > warns.log) < input.log
```

---

## 错误处理

### 退出码

```bash
# 查看退出码
command
echo $?  # 0 成功，非0 失败

# 常见退出码
# 0: 成功
# 1: 一般错误
# 2: 命令使用错误
# 126: 命令不可执行
# 127: 命令未找到
# 130: Ctrl+C 终止
# 255: 退出码超出范围

# 设置退出码
exit 0   # 成功
exit 1   # 失败
```

### set 选项

```bash
# 常用选项
set -e   # 命令失败时退出（errexit）
set -u   # 使用未定义变量时报错（nounset）
set -x   # 调试模式，显示执行的命令（xtrace）
set -o pipefail  # 管道中任一命令失败就失败

# 组合使用
set -euxo pipefail

# 取消选项
set +e
set +u
set +x
set +o pipefail

# 临时关闭错误退出
set +e
command_that_may_fail
set -e

# 或者
command_that_may_fail || true  # 忽略失败
```

### trap 信号捕获

```bash
# 捕获信号
trap 'echo "收到 INT 信号"' INT
trap 'echo "收到 TERM 信号"' TERM
trap 'cleanup; exit' EXIT
trap 'echo "脚本被终止"' ERR

# 清理函数
cleanup() {
    echo "清理临时文件..."
    rm -f /tmp/temp_*
}

trap cleanup EXIT

# 忽略信号
trap '' INT   # 忽略 Ctrl+C
trap - INT    # 恢复默认行为

# 常见信号
# EXIT: 脚本退出
# INT: 中断 (Ctrl+C)
# TERM: 终止信号
# HUP: 挂断信号
# ERR: 命令失败
# DEBUG: 每条命令执行前
```

### 完整错误处理示例

```bash
#!/bin/bash
set -euo pipefail

# 错误处理函数
error_handler() {
    local line=$1
    local cmd=$2
    local code=$3
    echo "错误发生在第 $line 行: $cmd (退出码: $code)" >&2
}

trap 'error_handler ${LINENO} "$BASH_COMMAND" $?' ERR

# 需要清理的临时文件
temp_files=()
cleanup() {
    for f in "${temp_files[@]}"; do
        rm -f "$f"
    done
}
trap cleanup EXIT

# 带重试的函数
retry() {
    local max_attempts=${1:-3}
    local delay=${2:-2}
    shift 2
    
    local attempt=1
    while [ $attempt -le $max_attempts ]; do
        if "$@"; then
            return 0
        fi
        echo "尝试 $attempt/$max_attempts 失败，${delay}秒后重试..." >&2
        sleep $delay
        ((attempt++))
    done
    return 1
}

# 使用
retry 5 2 curl -s https://api.example.com || die "API 请求失败"
```

---

## 调试技巧

### 基本调试

```bash
# 调试模式
bash -x script.sh
bash -v script.sh   # 显示原始行
bash -n script.sh   # 语法检查（不执行）

# 脚本内启用
#!/bin/bash -x
# 或
set -x

# 部分调试
set -x
# 要调试的代码
set +x

# 带行号的调试
PS4='+ ${BASH_SOURCE}:${LINENO}: '
set -x
```

### 调试函数

```bash
# 调试日志函数
DEBUG=${DEBUG:-0}

debug() {
    if [ "$DEBUG" -ge 1 ]; then
        echo "[DEBUG] $*" >&2
    fi
}

debug_verbose() {
    if [ "$DEBUG" -ge 2 ]; then
        echo "[DEBUG2] $*" >&2
    fi
}

# 使用
DEBUG=1 ./script.sh
```

### 断言和验证

```bash
# 断言函数
assert() {
    if ! "$@"; then
        echo "断言失败: $*" >&2
        exit 1
    fi
}

assert [ -f "/etc/passwd" ]
assert grep -q "root" /etc/passwd

# 变量验证
validate_var() {
    local var_name=$1
    local var_value=${!var_name}
    if [ -z "$var_value" ]; then
        echo "错误: 变量 $var_name 未设置" >&2
        exit 1
    fi
}
```

---

## 脚本安全

### 输入验证

```bash
# 验证是否为数字
is_number() {
    [[ $1 =~ ^-?[0-9]+$ ]]
}

# 验证是否为浮点数
is_float() {
    [[ $1 =~ ^-?[0-9]*\.?[0-9]+$ ]]
}

# 验证是否为有效路径
is_safe_path() {
    [[ $1 != *".."* && $1 != *"/."* && $1 != *"//"* ]]
}

# 验证 IP 地址
is_ip() {
    [[ $1 =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]
}

# 使用
read -r input
is_number "$input" || die "请输入数字"
```

### 防止注入

```bash
# 始终引用变量
# 错误
rm $file

# 正确
rm "$file"

# 使用 -- 分隔选项和参数
rm -- "$file"
grep -- "--pattern" file.txt

# 使用 read 时
IFS= read -r line  # 保留前导/尾随空格
read -r -p "输入: " input  # 不解释反斜杠

# printf 代替 echo（处理 -n 等特殊情况）
printf '%s\n' "$var"
```

### 临时文件安全

```bash
# 使用 mktemp
temp_file=$(mktemp)
temp_dir=$(mktemp -d)

# 指定模板
temp_file=$(mktemp /tmp/myscript.XXXXXX)

# 确保清理
trap 'rm -f "$temp_file"' EXIT

# 使用临时文件处理数据
curl -s https://api.example.com > "$temp_file"
jq '.data' "$temp_file"

# 进程替换（不需要临时文件）
while read -r line; do
    echo "$line"
done < <(curl -s https://api.example.com)
```

### 权限和路径安全

```bash
# 使用绝对路径
PATH=/usr/local/bin:/usr/bin:/bin
export PATH

# 检查命令是否存在
require_command() {
    command -v "$1" >/dev/null 2>&1 || die "需要安装: $1"
}

require_command jq
require_command curl

# 脚本只能从指定目录运行
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$SCRIPT_DIR" || exit
```

---

## 常用一行技巧

### 文件操作

```bash
# 批量重命名
for f in *.txt; do mv "$f" "${f%.txt}.md"; done
rename 's/\.txt$/\.md/' *.txt

# 批量创建文件
touch file{1..10}.txt
mkdir -p dir/{sub1,sub2,sub3}

# 备份文件
cp file.txt{,.bak}
cp file.txt "file.txt.$(date +%Y%m%d%H%M%S)"

# 删除空文件
find . -type f -empty -delete

# 删除 7 天前的文件
find /tmp -type f -mtime +7 -delete
```

### 文本处理

```bash
# 统计行数
wc -l file.txt

# 去重排序
sort file.txt | uniq -c | sort -rn

# 提取特定列
awk '{print $1, $3}' file.txt
cut -d',' -f1,3 file.csv

# 查找并替换
sed -i 's/old/new/g' file.txt

# 打印匹配行及前后
grep -B2 -A2 "error" log.txt

# 统计日志中错误次数
grep -c "ERROR" app.log

# 提取 IP 地址
grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' access.log
```

### 系统信息

```bash
# 查看最常用命令
history | awk '{print $2}' | sort | uniq -c | sort -rn | head -10

# 查看占用内存最多的进程
ps aux --sort=-%mem | head -10

# 查看占用 CPU 最多的进程
ps aux --sort=-%cpu | head -10

# 查看监听端口
ss -tlnp
netstat -tlnp

# 查看磁盘使用
df -h | awk '$5+0 > 80 {print $1, $5}'

# 查看目录大小
du -sh * | sort -h
```

### 网络相关

```bash
# 获取公网 IP
curl -s ifconfig.me
curl -s ipinfo.io/ip

# 测试端口连通
timeout 5 bash -c "echo > /dev/tcp/google.com/80" && echo "端口开放"

# 批量 ping
for i in {1..254}; do ping -c1 -W1 192.168.1.$i & done

# 下载文件并显示进度
curl -# -O https://example.com/file.zip
wget --show-progress https://example.com/file.zip
```

### 计算

```bash
# 整数运算
echo $((10 + 5))
echo $((10 * 5))

# 浮点运算
echo "scale=2; 10 / 3" | bc
awk 'BEGIN {print 10/3}'

# 随机数
echo $((RANDOM % 100))
shuf -i 1-100 -n 1
```

---

## 完整脚本模板

### 通用脚本模板

```bash
#!/usr/bin/env bash
# 描述: 脚本功能描述
# 作者: fajknli
# 版本: 1.0.0

set -euo pipefail

# ==================== 配置 ====================
readonly SCRIPT_NAME="$(basename "${BASH_SOURCE[0]}")"
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly LOG_DIR="${HOME}/.local/log"
readonly LOG_FILE="${LOG_DIR}/${SCRIPT_NAME%.*}.log"

# 默认值
DEBUG=${DEBUG:-0}
VERBOSE=${VERBOSE:-0}

# ==================== 函数 ====================
log() {
    local level=$1
    shift
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $*"
    echo "$msg" >&2
    [ -d "$LOG_DIR" ] && echo "$msg" >> "$LOG_FILE"
}

log_info() {
    log "INFO" "$@"
}

log_error() {
    log "ERROR" "$@"
}

log_debug() {
    [ "$DEBUG" -eq 1 ] && log "DEBUG" "$@"
}

die() {
    log_error "$@"
    exit 1
}

usage() {
    cat << EOF
用法: $SCRIPT_NAME [选项] [参数]

选项:
    -h, --help      显示帮助
    -v, --verbose   详细输出
    -d, --debug     调试模式
    -f, --file FILE 指定文件

例子:
    $SCRIPT_NAME -f input.txt
EOF
    exit 0
}

cleanup() {
    log_debug "清理临时文件..."
    # 清理代码
}

# ==================== 主逻辑 ====================
trap cleanup EXIT

# 解析参数
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            ;;
        -v|--verbose)
            VERBOSE=1
            shift
            ;;
        -d|--debug)
            DEBUG=1
            set -x
            shift
            ;;
        -f|--file)
            INPUT_FILE="$2"
            shift 2
            ;;
        *)
            die "未知参数: $1"
            ;;
    esac
done

# 验证参数
[ -z "${INPUT_FILE:-}" ] && die "请指定输入文件"

# 创建日志目录
mkdir -p "$LOG_DIR"

# 主逻辑
log_info "开始执行"
log_debug "调试信息"

# 脚本主体...

log_info "执行完成"
exit 0
```

### 服务监控脚本

```bash
#!/bin/bash
# 服务健康检查脚本

SERVICE_NAME="myapp"
URL="http://localhost:8080/health"
MAX_RETRIES=3
RETRY_INTERVAL=5

check_service() {
    local retry=0
    while [ $retry -lt $MAX_RETRIES ]; do
        if curl -s -f "$URL" > /dev/null; then
            echo "服务正常"
            return 0
        fi

# Shell 脚本编程完整指南（续）

## 目录

1. [正则表达式完全指南](#1-正则表达式完全指南)
2. [命令行参数解析](#2-命令行参数解析)
3. [并行执行模式](#3-并行执行模式)
4. [常见陷阱与避坑指南](#4-常见陷阱与避坑指南)
5. [性能优化技巧](#5-性能优化技巧)

---

## 1. 正则表达式完全指南

### 正则表达式类型对比

| 类型 | 命令/环境 | 特点 |
|------|-----------|------|
| 基础正则（BRE） | `grep`（默认）、`sed` | `+` `?` `|` `(` `)` 需要转义 |
| 扩展正则（ERE） | `grep -E`、`egrep`、`awk` | 特殊字符不需要转义 |
| Perl兼容正则（PCRE） | `grep -P`、`perl`、`ripgrep` | 功能最强大 |
| bash 正则 | `[[ str =~ pattern ]]` | ERE 风格 |

### 基础正则（BRE） vs 扩展正则（ERE）

| 功能 | BRE | ERE |
|------|-----|-----|
| 通配符 `.` | 不需要转义 | 不需要转义 |
| 零次或多次 `*` | 不需要转义 | 不需要转义 |
| 一次或多次 `+` | `\+` | `+` |
| 零次或一次 `?` | `\?` | `?` |
| 或 `|` | `\|` | `|` |
| 分组 `()` | `\(\)` | `()` |
| 重复 `{n}` | `\{n\}` | `{n}` |

```bash
# BRE（默认 grep）
grep '\(error\|warning\)' log.txt
sed 's/\([0-9]\+\)/\1/'

# ERE（grep -E）
grep -E '(error|warning)' log.txt
grep -E '[0-9]+' file.txt

# PCRE（grep -P，需要 GNU grep）
grep -P '\d+' file.txt        # \d 是数字
grep -P '(?<=prefix)word'     # 正向预查
```

### 常用正则表达式元字符

| 元字符 | 说明 | 例子 |
|--------|------|------|
| `.` | 任意单个字符（除换行） | `a.c` 匹配 abc、aac |
| `^` | 行首 | `^error` 匹配以 error 开头的行 |
| `$` | 行尾 | `done$` 匹配以 done 结尾的行 |
| `*` | 前一个字符 0 次或多次 | `go*gle` 匹配 ggle、gogle、google |
| `+` | 前一个字符 1 次或多次 | `go+gle` 匹配 gogle、google |
| `?` | 前一个字符 0 次或 1 次 | `colou?r` 匹配 color、colour |
| `{n}` | 恰好 n 次 | `[0-9]{4}` 匹配 4 位数字 |
| `{n,}` | 至少 n 次 | `[0-9]{2,}` 匹配 2 位及以上数字 |
| `{n,m}` | n 到 m 次 | `[0-9]{2,4}` 匹配 2-4 位数字 |
| `[abc]` | 字符集合 | `[aeiou]` 匹配任意元音 |
| `[^abc]` | 排除字符 | `[^0-9]` 匹配非数字 |
| `[a-z]` | 字符范围 | `[a-zA-Z]` 匹配任意字母 |
| `\|` | 或（BRE需转义） | `error\|warning` |
| `()` | 分组（BRE需转义） | `(error)+` 匹配 error、errorerror |
| `\b` | 单词边界 | `\bword\b` 匹配完整单词 |
| `\B` | 非单词边界 | `\Bword\B` 匹配单词内部 |
| `\d` | 数字（PCRE） | `\d+` 匹配一个或多个数字 |
| `\w` | 单词字符（PCRE） | `\w+` 匹配字母数字下划线 |
| `\s` | 空白字符（PCRE） | `\s+` 匹配空白 |
| `\n` | 换行符 | 替换中使用 |

### 实际应用例子

```bash
# IP 地址
grep -E '([0-9]{1,3}\.){3}[0-9]{1,3}' file.txt

# 邮箱地址
grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' file.txt

# URL
grep -E 'https?://[a-zA-Z0-9./?=_-]+' file.txt

# 日期 YYYY-MM-DD
grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}' file.txt

# 时间 HH:MM:SS
grep -E '[0-9]{2}:[0-9]{2}:[0-9]{2}' file.txt

# 手机号（简单）
grep -E '1[3-9][0-9]{9}' file.txt

# 十六进制颜色
grep -E '#[0-9a-fA-F]{6}' file.txt

# 中文
grep -P '[\p{Han}]' file.txt  # 需要 PCRE
```

### bash 正则匹配

```bash
# 基本用法
[[ "hello123" =~ ^[a-z]+[0-9]+$ ]] && echo "匹配"

# 提取匹配部分
str="abc123def"
[[ "$str" =~ ([0-9]+) ]]
echo "${BASH_REMATCH[0]}"  # 整个匹配: 123
echo "${BASH_REMATCH[1]}"  # 第一个分组: 123

# 多个分组
[[ "file_v1.2.3.tar.gz" =~ ([^_]+)_v([0-9.]+)\.(.+) ]]
echo "文件名: ${BASH_REMATCH[1]}"
echo "版本: ${BASH_REMATCH[2]}"
echo "后缀: ${BASH_REMATCH[3]}"

# 正则变量（注意引号）
pattern="^[0-9]+$"
[[ "123" =~ $pattern ]]  # 变量不要加引号
```

---

## 2. 命令行参数解析

### 使用 getopts（POSIX 标准）

```bash
#!/bin/bash

usage() {
    cat << EOF
用法: $0 [选项] [参数]

选项:
    -h          显示帮助
    -v          详细模式
    -f FILE     指定输入文件
    -o FILE     指定输出文件
    -n NUM      指定数字
    -q          安静模式
EOF
    exit 0
}

# 初始化变量
VERBOSE=0
QUIET=0
INPUT_FILE=""
OUTPUT_FILE=""
NUMBER=""

# 解析参数
while getopts "hvf:o:n:q" opt; do
    case $opt in
        h)
            usage
            ;;
        v)
            VERBOSE=1
            ;;
        f)
            INPUT_FILE="$OPTARG"
            ;;
        o)
            OUTPUT_FILE="$OPTARG"
            ;;
        n)
            NUMBER="$OPTARG"
            ;;
        q)
            QUIET=1
            ;;
        \?)
            echo "无效选项: -$OPTARG" >&2
            exit 1
            ;;
        :)
            echo "选项 -$OPTARG 需要参数" >&2
            exit 1
            ;;
    esac
done

# 移除已解析的选项
shift $((OPTIND - 1))

# 剩余的位置参数
echo "剩余参数: $*"

# 验证必需参数
[ -z "$INPUT_FILE" ] && echo "错误: 需要指定 -f" && exit 1
```

### 支持长选项（使用 bash 内置）

```bash
#!/bin/bash

# 手动解析长选项
parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                ;;
            -v|--verbose)
                VERBOSE=1
                shift
                ;;
            -f|--file)
                INPUT_FILE="$2"
                shift 2
                ;;
            --file=*)
                INPUT_FILE="${1#*=}"
                shift
                ;;
            -o|--output)
                OUTPUT_FILE="$2"
                shift 2
                ;;
            --output=*)
                OUTPUT_FILE="${1#*=}"
                shift
                ;;
            --)
                shift
                break
                ;;
            -*)
                echo "未知选项: $1" >&2
                exit 1
                ;;
            *)
                # 位置参数
                POSITIONAL_ARGS+=("$1")
                shift
                ;;
        esac
    done
}
```

### 使用外部工具（推荐用于复杂场景）

```bash
# 安装 argbash 或 docopt.sh

# docopt.sh 示例
# 在脚本开头写入文档，自动生成解析代码
: '
Usage:
    myscript [options] <input>

Options:
    -o --output FILE    输出文件
    -v --verbose        详细输出
    -n --number NUM     数字参数
    --debug             调试模式
    -h --help           显示帮助
'

# 然后运行 docopt.sh 生成解析代码
```

### 完整参数解析模板

```bash
#!/bin/bash
# 支持短选项、长选项、默认值、帮助

set -euo pipefail

# 默认值
VERBOSE=0
DEBUG=0
INPUT_FILE=""
OUTPUT_FILE="output.txt"
MAX_RETRIES=3
TIMEOUT=30

usage() {
    cat << EOF
用法: ${0##*/} [选项] <输入文件>

描述:
    脚本功能描述

选项:
    -o, --output FILE   输出文件 (默认: $OUTPUT_FILE)
    -n, --number NUM    重试次数 (默认: $MAX_RETRIES)
    -t, --timeout SEC   超时秒数 (默认: $TIMEOUT)
    -v, --verbose       详细输出
    -d, --debug         调试模式
    -h, --help          显示帮助

例子:
    ${0##*/} -o result.txt -v input.dat
EOF
    exit 0
}

# 参数解析
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            usage
            ;;
        -v|--verbose)
            VERBOSE=1
            shift
            ;;
        -d|--debug)
            DEBUG=1
            set -x
            shift
            ;;
        -o|--output)
            OUTPUT_FILE="$2"
            shift 2
            ;;
        --output=*)
            OUTPUT_FILE="${1#*=}"
            shift
            ;;
        -n|--number)
            MAX_RETRIES="$2"
            shift 2
            ;;
        --number=*)
            MAX_RETRIES="${1#*=}"
            shift
            ;;
        -t|--timeout)
            TIMEOUT="$2"
            shift 2
            ;;
        --timeout=*)
            TIMEOUT="${1#*=}"
            shift
            ;;
        --)
            shift
            break
            ;;
        -*)
            echo "错误: 未知选项 $1" >&2
            exit 1
            ;;
        *)
            INPUT_FILE="$1"
            shift
            ;;
    esac
done

# 验证参数
if [ -z "$INPUT_FILE" ]; then
    echo "错误: 需要指定输入文件" >&2
    usage
fi

if [ ! -f "$INPUT_FILE" ]; then
    echo "错误: 文件不存在: $INPUT_FILE" >&2
    exit 1
fi

# 输出配置
if [ "$VERBOSE" -eq 1 ]; then
    echo "输入文件: $INPUT_FILE"
    echo "输出文件: $OUTPUT_FILE"
    echo "重试次数: $MAX_RETRIES"
    echo "超时: $TIMEOUT"
fi

# 主逻辑...
```

---

## 3. 并行执行模式

### 基础并行：后台任务 + wait

```bash
#!/bin/bash

# 简单并行
task1() { sleep 2; echo "任务1完成"; }
task2() { sleep 3; echo "任务2完成"; }
task3() { sleep 1; echo "任务3完成"; }

# 启动后台任务
task1 &
pid1=$!
task2 &
pid2=$!
task3 &
pid3=$!

# 等待所有完成
wait $pid1 $pid2 $pid3
echo "所有任务完成"
```

### 并行处理文件

```bash
#!/bin/bash

# 并行压缩文件
compress_file() {
    local file=$1
    echo "压缩: $file"
    gzip -c "$file" > "${file}.gz"
}

# 方法1：逐个启动
for file in *.log; do
    compress_file "$file" &
done
wait

# 方法2：限制并发数
MAX_JOBS=4
job_count=0

for file in *.log; do
    compress_file "$file" &
    ((job_count++))
    
    if [ $job_count -ge $MAX_JOBS ]; then
        wait -n  # 等待任意一个完成（bash 4.3+）
        ((job_count--))
    fi
done
wait
```

### 使用 xargs 并行

```bash
# 基本并行
echo "file1 file2 file3" | xargs -n 1 -P 4 gzip

# 从文件读取
cat filelist.txt | xargs -I {} -P 4 compress {}

# 结合 find
find . -name "*.log" -print0 | xargs -0 -P 4 -I {} gzip {}

# 保留输出顺序
find . -name "*.txt" | xargs -P 4 -I {} sh -c 'wc -l {}' | sort -n
```

### 使用 GNU parallel（推荐）

```bash
# 安装
sudo pacman -S parallel

# 基本用法
parallel gzip ::: file1.log file2.log file3.log

# 从文件读取
parallel -a filelist.txt gzip

# 带参数
parallel --tag "处理文件: {}" gzip {} ::: *.log

# 控制并发数
parallel -j 4 gzip ::: *.log

# 替换字符串
parallel --dry-run "convert {1} -resize {2} {1%.*}_{2}.png" ::: *.png ::: 100 200 400

# 输出到文件
parallel --results results/ gzip ::: *.log

# 进度显示
parallel --progress gzip ::: *.log

# 超时和重试
parallel --timeout 300 --retries 3 curl -O ::: url1 url2
```

### 生产者-消费者模式

```bash
#!/bin/bash
# 使用命名管道实现任务队列

# 创建命名管道
PIPE="/tmp/task_queue.$$"
mkfifo "$PIPE"
exec 3<> "$PIPE"
rm "$PIPE"

# 生产者：添加任务
add_task() {
    echo "$*" >&3
}

# 消费者：工作进程
worker() {
    local id=$1
    while read -r cmd; do
        echo "[worker $id] 执行: $cmd"
        eval "$cmd"
    done <&3
}

# 启动工作进程
NUM_WORKERS=4
for i in $(seq 1 $NUM_WORKERS); do
    worker $i &
done

# 添加任务
for i in {1..10}; do
    add_task "sleep $((RANDOM % 3)); echo '任务 $i 完成'"
done

# 等待任务完成（发送结束标记）
for i in $(seq 1 $NUM_WORKERS); do
    add_task "exit"
done

wait
```

### 并行任务池

```bash
#!/bin/bash
# 限制最大并发数的任务池

MAX_JOBS=4
running=0
pids=()

run_task() {
    local cmd="$1"
    "$cmd" &
    pids+=($!)
    ((running++))
}

wait_for_slot() {
    while [ $running -ge $MAX_JOBS ]; do
        for i in "${!pids[@]}"; do
            if ! kill -0 "${pids[$i]}" 2>/dev/null; then
                unset 'pids[$i]'
                ((running--))
            fi
        done
        sleep 0.1
    done
}

# 使用
for task in "${tasks[@]}"; do
    wait_for_slot
    run_task "$task"
done

# 等待所有完成
wait
```

---

## 4. 常见陷阱与避坑指南

### 陷阱1：变量引号问题

```bash
# ❌ 错误
file="my file.txt"
rm $file          # 实际执行: rm my file.txt（删了两个文件）

# ✅ 正确
rm "$file"        # 删除 "my file.txt"

# ❌ 错误
if [ $var = "value" ]; then   # var 为空时变成 [ = "value" ]

# ✅ 正确
if [ "$var" = "value" ]; then
if [[ $var = "value" ]]; then  # [[ ]] 中不需要引号
```

### 陷阱2：数组遍历

```bash
# ❌ 错误
arr=("a b" "c d")
for item in ${arr[@]}; do   # 拆分成4个元素
    echo "$item"
done

# ✅ 正确
for item in "${arr[@]}"; do  # 保持为2个元素
    echo "$item"
done
```

### 陷阱3：IFS 影响

```bash
# ❌ 错误
old_ifs=$IFS
IFS=:
read -r a b c <<< "a:b:c"
IFS=$old_ifs

# ✅ 正确（在子 shell 中修改）
(
    IFS=:
    read -r a b c <<< "a:b:c"
)
# 或
IFS=: read -r a b c <<< "a:b:c"
```

### 陷阱4：管道中的变量

```bash
# ❌ 错误：管道中的变量在子 shell 中，外部访问不到
count=0
cat file.txt | while read line; do
    ((count++))
done
echo $count  # 仍然是 0

# ✅ 正确：使用进程替换
count=0
while read line; do
    ((count++))
done < <(cat file.txt)
echo $count

# ✅ 正确：使用 lastpipe（bash 4.2+）
shopt -s lastpipe
cat file.txt | while read line; do
    ((count++))
done
echo $count
```

### 陷阱5：[ ] vs [[ ]]

| 特性 | `[ ]` | `[[ ]]` |
|------|-------|---------|
| POSIX 兼容 | ✅ | ❌（bash/zsh） |
| 变量需要引号 | ✅ | ❌ |
| 支持 `&&` `\|\|` | ❌（用 `-a` `-o`） | ✅ |
| 支持 `=~` 正则 | ❌ | ✅ |
| 支持通配符 | ❌ | ✅ |
| 支持 `<` `>` 字符串比较 | ✅（需转义） | ✅（不需转义） |

```bash
# [ ] 中的问题
[ $a == $b ]        # 错误：== 不是 POSIX，且变量可能为空
[ "$a" = "$b" ]     # 正确

# [[ ]] 更方便
[[ $a == $b ]]      # 正确，不需要引号
[[ $a == *test* ]]  # 通配符
[[ $a =~ ^[0-9]+$ ]] # 正则
```

### 陷阱6：空变量默认值

```bash
# 设置默认值
name=${1:-"default"}   # 如果 $1 为空，使用 default
name=${1:="default"}   # 如果 $1 为空，同时设置 $1

# 常见错误
name=$1
if [ -z "$name" ]; then
    name="default"
fi

# 更简洁
: ${name:="default"}   # 如果 name 为空，设置为 default
```

### 陷阱7：cd 失败

```bash
# ❌ 错误：cd 失败后继续执行
cd /some/path
rm -rf *

# ✅ 正确
cd /some/path || exit 1
rm -rf *

# ✅ 更好：在子 shell 中执行
(
    cd /some/path || exit
    rm -rf *
)
```

### 陷阱8：命令替换中的换行

```bash
# ❌ 错误：换行会被空格替换
files=$(ls)
for file in $files; do ...  # 文件名中的空格会被拆开

# ✅ 正确：使用数组或 while read
files=(*)
for file in "${files[@]}"; do ...

# 或
while IFS= read -r file; do
    ...
done < <(ls)
```

### 陷阱9：信号处理中的陷阱

```bash
# ❌ 错误：trap 中使用了外部命令，但信号中断了
cleanup() {
    rm -f /tmp/temp_*   # 如果被再次中断，可能不执行
}
trap cleanup EXIT

# ✅ 正确：使用局部变量和标志
cleanup_needed=1
cleanup() {
    [ $cleanup_needed -eq 1 ] || return
    cleanup_needed=0
    rm -f /tmp/temp_*
}
trap cleanup EXIT INT TERM
```

### 陷阱10：shebang 问题

```bash
# ❌ 错误：不指定 shell，可能用 sh 执行（不支持 bash 特性）
#!/bin/sh
# 使用了 bash 数组，但 /bin/sh 可能是 dash

# ✅ 正确：明确指定 bash
#!/usr/bin/env bash

# ✅ 可移植脚本：只使用 POSIX 特性
#!/bin/sh
```

### 陷阱11：eval 安全风险

```bash
# ❌ 危险：用户输入可能注入代码
eval "echo $user_input"

# ✅ 安全：避免使用 eval，或严格过滤
printf '%s\n' "$user_input"

# 如果必须使用
safe_eval() {
    # 严格验证
    [[ $1 =~ ^[a-zA-Z0-9_=]+$ ]] && eval "$1"
}
```

### 陷阱12：时间戳和日期

```bash
# ❌ 错误：date 在不同系统上格式不同
date +%s  # Linux 支持，macOS 也支持（但有些旧版不支持）

# ✅ 正确：使用 POSIX 或检测环境
if date --version >/dev/null 2>&1; then
    # GNU date
    timestamp=$(date +%s)
else
    # BSD date
    timestamp=$(date -j -f "%Y-%m-%d %H:%M:%S" "$datetime" +%s)
fi
```

---

## 5. 性能优化技巧

### 避免不必要的子 shell

```bash
# ❌ 慢：管道创建子 shell
cat file.txt | while read line; do
    echo "$line"
done

# ✅ 快：重定向，不需要子 shell
while read line; do
    echo "$line"
done < file.txt

# ❌ 慢：命令替换创建子 shell
result=$(echo "$var" | grep "pattern")

# ✅ 快：使用 bash 内置
[[ $var =~ pattern ]]
result="${BASH_REMATCH[0]}"

# ❌ 慢：管道中的循环
echo "1 2 3" | while read a b c; do ... done

# ✅ 快：here string
while read a b c; do ... done <<< "1 2 3"
```

### 使用内置命令代替外部命令

```bash
# ❌ 慢：外部命令
result=$(echo "$str" | tr 'a-z' 'A-Z')
len=$(echo "$str" | wc -c)

# ✅ 快：bash 内置
result="${str^^}"           # 转大写
len=${#str}                 # 长度

# ❌ 慢：外部 grep
if echo "$str" | grep -q "pattern"; then

# ✅ 快：bash 内置
if [[ $str =~ pattern ]]; then

# ❌ 慢：外部 bc
result=$(echo "scale=2; $a / $b" | bc)

# ✅ 快：awk 或内置（整数）
result=$((a / b))
result=$(awk "BEGIN {printf \"%.2f\", $a / $b}")
```

### 批量操作减少调用

```bash
# ❌ 慢：每个文件调用一次
for file in *.txt; do
    sed -i 's/old/new/g' "$file"
done

# ✅ 快：一次性处理（如果可以）
sed -i 's/old/new/g' *.txt

# ❌ 慢：每个文件调用外部命令
for file in *.txt; do
    lines=$(wc -l < "$file")
    total=$((total + lines))
done

# ✅ 快：一次 wc 处理所有
total=$(wc -l *.txt | tail -1 | awk '{print $1}')
```

### 使用数组代替字符串拼接

```bash
# ❌ 慢：字符串拼接
args=""
for file in *.txt; do
    args="$args $file"
done
command $args

# ✅ 快：数组
args=()
for file in *.txt; do
    args+=("$file")
done
command "${args[@]}"
```

### 重定向优化

```bash
# ❌ 慢：循环中多次打开文件
while read line; do
    echo "$line" >> output.txt
done < input.txt

# ✅ 快：一次重定向
while read line; do
    echo "$line"
done < input.txt > output.txt

# ✅ 更快：使用 exec 重定向整个脚本块
exec > output.txt
while read line; do
    echo "$line"
done < input.txt
exec > /dev/tty  # 恢复
```

### 使用 awk/sed 处理大文件

```bash
# ❌ 慢：bash 循环处理大文件
while read line; do
    field1=$(echo "$line" | cut -d',' -f1)
    field2=$(echo "$line" | cut -d',' -f2)
    echo "$field2,$field1"
done < large.csv

# ✅ 快：awk 一次性处理
awk -F',' '{print $2","$1}' large.csv
```

### 缓存重复结果

```bash
# ❌ 慢：重复计算
for i in {1..100}; do
    date=$(date +%Y%m%d)  # 每次都调用 date
    echo "$date: 处理 $i"
done

# ✅ 快：缓存结果
date=$(date +%Y%m%d)
for i in {1..100}; do
    echo "$date: 处理 $i"
done
```

### 并行处理优化

```bash
# 大量小文件：并行处理
process_file() { gzip "$1"; }
export -f process_file
find . -name "*.log" | xargs -P 4 -I {} bash -c 'process_file "$@"' _ {}

# 大文件：分块处理
split -l 10000 large.txt chunk_
for chunk in chunk_*; do
    process_chunk "$chunk" &
done
wait
cat chunk_*.out > result.txt
rm chunk_*
```

### 性能对比总结

| 操作 | 慢 | 快 |
|------|----|----|
| 字符串转大写 | `echo \| tr` | `${var^^}` |
| 字符串长度 | `echo \| wc -c` | `${#var}` |
| 正则匹配 | `grep` 管道 | `[[ =~ ]]` |
| 文件遍历 | `find -exec {} \;` | `find -exec {} +` |
| 循环重定向 | 循环内 `>>` | 循环外重定向 |
| 文本处理 | bash 循环 | awk/sed |
| 并行 | 串行 | `xargs -P` |

---

## 总结

| 章节 | 核心要点 |
|------|----------|
| 正则表达式 | BRE 需要转义 `+` `?` `\|` `()`；ERE 不需要；bash 用 `[[ =~ ]]` |
| 参数解析 | 简单用 `getopts`，复杂用手动解析或 `docopt` |
| 并行执行 | `&` + `wait`；`xargs -P`；`parallel` 最强大 |
| 常见陷阱 | 变量加引号；用 `[[ ]]` 代替 `[ ]`；注意子 shell 作用域 |
| 性能优化 | 用内置代替外部；批量操作；避免循环中的子 shell |

这份是补充内容，和之前的 `shell-tips.md` 合并才是完整的 Shell 脚本指南。需要我把两部分合并成一份完整文件吗？
