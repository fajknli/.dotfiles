# Shell 基础语法

## Shebang

脚本第一行指定解释器。

```sh
#!/bin/sh
#!/bin/bash
#!/usr/bin/env sh
```

## 注释

```sh
# 这是单行注释

: '
这是多行注释
使用冒号和空格
'
```

## 变量

### 定义与使用

```sh
# 定义变量（等号两边不能有空格）
name="张三"
age=25
path=/usr/local/bin

# 使用变量（加 $）
echo "$name"
echo "${name}"  # 花括号可选，用于明确边界

# 只读变量
readonly PI=3.14

# 删除变量
unset name
```

### 变量命名规则

- 只能包含字母、数字、下划线
- 不能以数字开头
- 通常使用大写字母表示环境变量

## 引号

### 双引号 vs 单引号

```sh
name="张三"

# 双引号：解析变量和转义字符
echo "Hello $name"    # Hello 张三
echo "Hello \$name"   # Hello $name

# 单引号：原样输出
echo 'Hello $name'    # Hello $name

# 反引号：命令替换（旧语法）
echo `date`

# $(...)：命令替换（推荐）
echo "$(date)"
```

## 特殊变量

| 变量 | 说明 |
|------|------|
| `$0` | 脚本名称 |
| `$1-$9` | 位置参数 |
| `$#` | 参数个数 |
| `$@` | 所有参数（分开引用） |
| `$*` | 所有参数（合并为字符串） |
| `$$` | 当前进程 ID |
| `$?` | 上一条命令的退出码 |
| `$!` | 后台进程 ID |

```sh
#!/bin/sh
echo "脚本名: $0"
echo "第一个参数: $1"
echo "参数个数: $#"
echo "所有参数: $@"
echo "进程 ID: $$"
```

## 命令替换

```sh
# 推荐写法
current_date=$(date)
files=$(ls -la)

# 旧写法（不推荐）
current_date=`date`

# 嵌套使用
dir_name=$(basename $(pwd))
```

## 算术运算

```sh
# $((...)) 进行算术运算
a=10
b=20
sum=$((a + b))
echo "$sum"  # 30

# 其他运算符
echo $((a - b))   # -10
echo $((a * b))   # 200
echo $((b / a))   # 2
echo $((b % a))   # 0
```

## 退出状态

```sh
# 0 表示成功，非 0 表示失败
ls /tmp
echo $?  # 0（成功）

ls /nonexistent
echo $?  # 非 0（失败）

# 退出脚本
exit 0   # 成功退出
exit 1   # 失败退出
```

## 条件测试

### test 命令

```sh
# 使用 test 命令
test -f /etc/passwd
echo $?  # 0（文件存在）

# 使用 [ ] 简写（注意空格）
[ -f /etc/passwd ]
echo $?  # 0

# 数值比较
[ 10 -eq 10 ]   # 等于
[ 10 -ne 5 ]    # 不等于
[ 10 -gt 5 ]    # 大于
[ 10 -lt 20 ]   # 小于
[ 10 -ge 10 ]   # 大于等于
[ 10 -le 20 ]   # 小于等于

# 字符串比较
[ "$name" = "张三" ]     # 等于
[ "$name" != "李四" ]    # 不等于
[ -z "$name" ]           # 字符串为空
[ -n "$name" ]           # 字符串非空
```

### 文件测试

| 操作符 | 说明 |
|--------|------|
| `-e file` | 文件存在 |
| `-f file` | 是普通文件 |
| `-d file` | 是目录 |
| `-r file` | 可读 |
| `-w file` | 可写 |
| `-x file` | 可执行 |
| `-s file` | 文件非空 |
| `-L file` | 是符号链接 |

```sh
[ -f /etc/passwd ] && echo "文件存在"
[ -d /tmp ] && echo "是目录"
[ -x /bin/ls ] && echo "可执行"
```

### 逻辑组合

```sh
# 与：-a 或 &&
[ -f /etc/passwd -a -r /etc/passwd ]

# 或：-o 或 ||
[ -f /tmp/file -o -d /tmp ]

# 非：!
[ ! -f /tmp/missing ]
```

## 通配符

| 通配符 | 说明 |
|--------|------|
| `*` | 匹配任意字符串 |
| `?` | 匹配单个字符 |
| `[abc]` | 匹配括号内任一字符 |
| `[a-z]` | 匹配范围内的字符 |
| `[!abc]` | 匹配不在括号内的字符 |

```sh
# 列出所有 .txt 文件
ls *.txt

# 列出以 a、b、c 开头的文件
ls [abc]*

# 列出两个字符的文件名
ls ??

# 排除特定文件
ls !(backup).sh  # bash 扩展，POSIX 不支持
```

## 输入输出

```sh
# echo：输出并换行
echo "Hello"
echo -n "不换行"  # 某些 shell 支持

# printf：格式化输出（推荐）
printf "Name: %s, Age: %d\n" "张三" 25

# read：读取输入
echo "请输入姓名:"
read name
echo "你好, $name"
```

## 基本示例

### 判断文件类型

```sh
#!/bin/sh

file="$1"

if [ -f "$file" ]; then
    echo "$file 是普通文件"
elif [ -d "$file" ]; then
    echo "$file 是目录"
else
    echo "$file 不存在"
fi
```

### 循环遍历参数

```sh
#!/bin/sh

for arg in "$@"; do
    echo "参数: $arg"
done
```

### 安全使用变量

```sh
# 总是给变量加双引号，防止空格导致的问题
file="my file.txt"
touch "$file"      # 正确：创建一个文件
# touch $file      # 错误：创建两个文件 "my" 和 "file.txt"

# 使用默认值
name="${1:-默认值}"

# 检查变量是否设置
if [ -z "${var+x}" ]; then
    echo "var 未设置"
fi
```
