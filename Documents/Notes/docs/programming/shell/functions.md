# Shell 函数

## 函数定义

### 基本语法

```sh
# 方法一：使用 function 关键字（bash 扩展，POSIX 不推荐）
function myfunc {
    commands
}

# 方法二：POSIX 标准写法（推荐）
myfunc() {
    commands
}
```

### 简单示例

```sh
#!/bin/sh

# 定义函数
hello() {
    echo "Hello, World!"
}

# 调用函数
hello
```

```sh
#!/bin/sh

# 带参数的函数
greet() {
    echo "Hello, $1!"
}

greet "张三"   # Hello, 张三!
greet "李四"   # Hello, 李四!
```

## 函数参数

### 位置参数

```sh
#!/bin/sh

show_args() {
    echo "函数名: $0"
    echo "第一个参数: $1"
    echo "第二个参数: $2"
    echo "参数个数: $#"
    echo "所有参数: $@"
}

show_args a b c
```

### 参数示例

```sh
#!/bin/sh

# 计算两数之和
add() {
    sum=$(( $1 + $2 ))
    echo "$sum"
}

result=$(add 10 20)
echo "结果: $result"  # 结果: 30
```

```sh
#!/bin/sh

# 连接字符串
concat() {
    echo "$1$2"
}

result=$(concat "Hello " "World")
echo "$result"  # Hello World
```

### 参数默认值

```sh
#!/bin/sh

greet() {
    name="${1:-朋友}"
    echo "你好, $name"
}

greet        # 你好, 朋友
greet "张三"  # 你好, 张三
```

## 返回值

### 退出状态码

```sh
#!/bin/sh

# 返回退出码（0-255）
check_file() {
    if [ -f "$1" ]; then
        return 0  # 成功
    else
        return 1  # 失败
    fi
}

check_file "/etc/passwd"
if [ $? -eq 0 ]; then
    echo "文件存在"
else
    echo "文件不存在"
fi
```

### 输出返回值

```sh
#!/bin/sh

# 使用 echo 返回计算结果
get_sum() {
    echo $(( $1 + $2 ))
}

result=$(get_sum 10 20)
echo "和: $result"
```

```sh
#!/bin/sh

# 返回字符串
get_user() {
    echo "张三"
}

name=$(get_user)
echo "姓名: $name"
```

### 状态码 vs 输出

| 方式 | 用途 | 获取方法 |
|------|------|----------|
| `return n` | 返回状态码（0-255） | `$?` |
| `echo text` | 返回数据 | `$(func)` |

## 局部变量

```sh
#!/bin/sh

# local 关键字（POSIX 不支持，仅 bash）
# POSIX sh 使用子 shell 隔离变量

myfunc() {
    var="local"
    echo "函数内: $var"
}

var="global"
myfunc
echo "函数外: $var"  # 仍然是 global
```

### POSIX 兼容的局部变量方式

```sh
#!/bin/sh

# 使用子 shell 隔离变量
myfunc() {
    (
        var="local"
        echo "函数内: $var"
    )
}

var="global"
myfunc
echo "函数外: $var"  # global
```

## 函数嵌套

```sh
#!/bin/sh

outer() {
    echo "外层函数"
    
    inner() {
        echo "内层函数"
    }
    
    inner
}

outer
# 输出:
# 外层函数
# 内层函数
```

## 递归函数

```sh
#!/bin/sh

# 计算阶乘
factorial() {
    if [ "$1" -le 1 ]; then
        echo 1
    else
        n=$1
        sub=$((n - 1))
        sub_fact=$(factorial $sub)
        echo $((n * sub_fact))
    fi
}

result=$(factorial 5)
echo "5! = $result"  # 120
```

```sh
#!/bin/sh

# 递归遍历目录
list_files() {
    for file in "$1"/*; do
        if [ -d "$file" ]; then
            echo "目录: $file"
            list_files "$file"
        else
            echo "文件: $file"
        fi
    done
}

list_files "/tmp"
```

## 函数库

### 创建函数库

```sh
# lib.sh - 公共函数库

# 日志函数
log_info() {
    echo "[INFO] $(date): $*"
}

log_error() {
    echo "[ERROR] $(date): $*" >&2
}

# 文件函数
file_exists() {
    [ -f "$1" ]
}

dir_exists() {
    [ -d "$1" ]
}

# 字符串函数
is_empty() {
    [ -z "$1" ]
}

contains() {
    case "$1" in
        *"$2"*) return 0 ;;
        *) return 1 ;;
    esac
}
```

### 使用函数库

```sh
#!/bin/sh

# 加载函数库
. ./lib.sh

# 使用函数
log_info "脚本开始"

if file_exists "/etc/passwd"; then
    log_info "passwd 文件存在"
fi

if contains "Hello World" "World"; then
    log_info "字符串包含 World"
fi
```

## 实际应用示例

### 带帮助的函数

```sh
#!/bin/sh

usage() {
    cat << EOF
用法: $0 [选项]

选项:
    -h, --help     显示帮助
    -f, --file     指定文件
    -v, --verbose  详细输出
EOF
}

error() {
    echo "错误: $*" >&2
    exit 1
}

# 使用
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    usage
    exit 0
fi
```

### 确认提示函数

```sh
#!/bin/sh

confirm() {
    prompt="${1:-确认执行?}"
    answer=""
    
    printf "%s (y/n): " "$prompt"
    read answer
    
    case "$answer" in
        y|Y|yes|YES)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

# 使用
if confirm "删除文件?"; then
    echo "执行删除"
else
    echo "取消操作"
fi
```

### 颜色输出函数

```sh
#!/bin/sh

# ANSI 颜色代码
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

color_echo() {
    color="$1"
    shift
    printf "${color}%s${NC}\n" "$*"
}

red() {
    color_echo "$RED" "$*"
}

green() {
    color_echo "$GREEN" "$*"
}

yellow() {
    color_echo "$YELLOW" "$*"
}

# 使用
green "成功"
red "失败"
yellow "警告"
```

### 超时执行函数

```sh
#!/bin/sh

timeout() {
    seconds="$1"
    shift
    cmd="$*"
    
    # 启动命令并在后台运行
    eval "$cmd" &
    cmd_pid=$!
    
    # 等待指定时间
    sleep "$seconds"
    
    # 如果命令还在运行，则终止
    if kill -0 "$cmd_pid" 2>/dev/null; then
        kill "$cmd_pid"
        echo "命令执行超时 ($seconds 秒)" >&2
        return 1
    fi
    
    wait "$cmd_pid"
    return $?
}

# 使用
timeout 5 sleep 10
```

## 最佳实践

```sh
# 1. 函数名使用小写加下划线
my_function() {
    ...
}

# 2. 函数定义放在脚本开头
# 3. 使用局部变量（bash）或子 shell（POSIX）
# 4. 明确返回值
# 5. 添加注释

# 检查命令是否存在
check_command() {
    command -v "$1" >/dev/null 2>&1
}

# 使用示例
if check_command "curl"; then
    echo "curl 已安装"
else
    echo "curl 未安装"
fi
```
