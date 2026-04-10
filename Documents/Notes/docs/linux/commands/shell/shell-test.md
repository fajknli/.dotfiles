# Shell 测试表达式

## 一句话理解

测试表达式用于判断条件是否成立，常用于 `if` 语句和 `while` 循环。`[` 是 `test` 命令的别名。

```bash
# 两种写法等价
if [ -f /etc/passwd ]; then
    echo "文件存在"
fi

if test -f /etc/passwd; then
    echo "文件存在"
fi
```

## 文件测试

| 表达式 | 说明 | 例子 |
|--------|------|------|
| `-e file` | 文件存在 | `[ -e /etc/passwd ]` |
| `-f file` | 是普通文件 | `[ -f /etc/passwd ]` |
| `-d file` | 是目录 | `[ -d /home ]` |
| `-L file` | 是符号链接 | `[ -L /usr/bin/python ]` |
| `-h file` | 同 -L | `[ -h /usr/bin/python ]` |
| `-s file` | 文件非空（大小>0） | `[ -s log.txt ]` |
| `-r file` | 可读 | `[ -r /etc/passwd ]` |
| `-w file` | 可写 | `[ -w /tmp/file ]` |
| `-x file` | 可执行 | `[ -x /usr/bin/bash ]` |
| `-b file` | 块设备文件 | `[ -b /dev/sda ]` |
| `-c file` | 字符设备文件 | `[ -c /dev/tty ]` |
| `-p file` | 命名管道 | `[ -p /tmp/fifo ]` |
| `-S file` | 套接字 | `[ -S /var/run/docker.sock ]` |
| `-O file` | 所有者是当前用户 | `[ -O ~/.bashrc ]` |
| `-G file` | 组是当前用户组 | `[ -G ~/.bashrc ]` |
| `file1 -nt file2` | file1 比 file2 新 | `[ a.txt -nt b.txt ]` |
| `file1 -ot file2` | file1 比 file2 旧 | `[ a.txt -ot b.txt ]` |
| `file1 -ef file2` | 同一文件（硬链接） | `[ a.txt -ef b.txt ]` |

## 字符串测试

| 表达式 | 说明 | 例子 |
|--------|------|------|
| `-z string` | 字符串为空 | `[ -z "$var" ]` |
| `-n string` | 字符串非空 | `[ -n "$var" ]` |
| `string1 = string2` | 相等 | `[ "$a" = "$b" ]` |
| `string1 == string2` | 相等（bash 扩展） | `[[ "$a" == "$b" ]]` |
| `string1 != string2` | 不等 | `[ "$a" != "$b" ]` |
| `string1 < string2` | 小于（字典序） | `[[ "$a" < "$b" ]]` |
| `string1 > string2` | 大于（字典序） | `[[ "$a" > "$b" ]]` |
| `=~` | 正则匹配 | `[[ "$str" =~ ^[0-9]+$ ]]` |

**注意**：`<` 和 `>` 在 `[ ]` 中需要转义，在 `[[ ]]` 中不需要。

```bash
# 正确写法
[ "$a" \< "$b" ]
[[ "$a" < "$b" ]]
```

## 数值比较

| 表达式 | 说明 | 例子 |
|--------|------|------|
| `n1 -eq n2` | 等于 | `[ 10 -eq 10 ]` |
| `n1 -ne n2` | 不等于 | `[ 10 -ne 5 ]` |
| `n1 -gt n2` | 大于 | `[ 10 -gt 5 ]` |
| `n1 -ge n2` | 大于等于 | `[ 10 -ge 10 ]` |
| `n1 -lt n2` | 小于 | `[ 5 -lt 10 ]` |
| `n1 -le n2` | 小于等于 | `[ 5 -le 10 ]` |

**注意**：数值比较不能用 `=` 或 `>`，那会做字符串比较。

```bash
# 错误：字符串比较，结果是按字典序
[ 10 > 5 ]   # 实际比较字符串 "10" 和 "5"

# 正确：数值比较
[ 10 -gt 5 ]
```

## 组合条件

| 表达式 | 说明 | 例子 |
|--------|------|------|
| `! expr` | 非 | `[ ! -f /tmp/file ]` |
| `expr1 -a expr2` | 与（and） | `[ -f file -a -r file ]` |
| `expr1 -o expr2` | 或（or） | `[ -f file -o -L file ]` |
| `( expr )` | 括号分组 | `[ \( -f file -o -L file \) -a -r file ]` |

### bash 增强版 `[[ ]]`

`[[ ]]` 是 bash 的增强版本，语法更友好：

```bash
# 不需要引号
[[ -z $var ]]        # 等价于 [ -z "$var" ]

# 支持 && 和 ||
[[ -f file && -r file ]]

# 支持正则匹配
[[ $email =~ ^[a-z]+@[a-z]+\.[a-z]+$ ]]

# 支持通配符
[[ $filename == *.txt ]]

# 支持逻辑运算符
[[ $a -gt 5 && $b -lt 10 ]]
```

## 常用场景

### 1. 检查文件是否存在

```bash
if [ -f "$config_file" ]; then
    source "$config_file"
else
    echo "配置文件不存在: $config_file"
    exit 1
fi
```

### 2. 检查目录是否存在

```bash
if [ ! -d "$backup_dir" ]; then
    mkdir -p "$backup_dir"
    echo "创建备份目录: $backup_dir"
fi
```

### 3. 检查变量是否为空

```bash
if [ -z "$1" ]; then
    echo "请提供参数"
    exit 1
fi

# 或设置默认值
name=${1:-"default"}
```

### 4. 检查命令是否存在

```bash
if [ -x "$(command -v docker)" ]; then
    echo "Docker 已安装"
else
    echo "Docker 未安装"
fi

# 或更简单
if command -v docker &> /dev/null; then
    echo "Docker 已安装"
fi
```

### 5. 检查是否为数字

```bash
if [[ $num =~ ^[0-9]+$ ]]; then
    echo "是数字"
else
    echo "不是数字"
fi
```

### 6. 组合条件

```bash
# 文件存在且可执行
if [ -f "$script" ] && [ -x "$script" ]; then
    ./"$script"
fi

# 使用 -a
if [ -f "$script" -a -x "$script" ]; then
    ./"$script"
fi

# 使用 [[ ]]
if [[ -f $script && -x $script ]]; then
    ./"$script"
fi
```

### 7. 检查终端输出

```bash
# 判断输出是否被重定向
if [ -t 1 ]; then
    echo "输出到终端，可以使用颜色"
else
    echo "输出被管道/重定向，不要使用颜色"
fi
```

## 完整示例

### 脚本参数验证

```bash
#!/bin/bash

# 检查参数数量
if [ $# -ne 2 ]; then
    echo "用法: $0 <输入文件> <输出目录>"
    exit 1
fi

INPUT_FILE=$1
OUTPUT_DIR=$2

# 检查输入文件
if [ ! -f "$INPUT_FILE" ]; then
    echo "错误: 输入文件不存在: $INPUT_FILE"
    exit 1
fi

if [ ! -r "$INPUT_FILE" ]; then
    echo "错误: 输入文件不可读: $INPUT_FILE"
    exit 1
fi

# 检查输出目录
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "输出目录不存在，创建中..."
    mkdir -p "$OUTPUT_DIR"
fi

if [ ! -w "$OUTPUT_DIR" ]; then
    echo "错误: 输出目录不可写: $OUTPUT_DIR"
    exit 1
fi

echo "所有检查通过，开始处理..."
```

## 运算符优先级

从高到低：

1. `!` `-a` `-o` 中的 `!` 最高
2. `-a` 高于 `-o`
3. `( )` 可改变优先级

```bash
# 不加括号：-a 优先级高于 -o
[ $a -eq 1 -o $b -eq 2 -a $c -eq 3 ]
# 等价于 [ $a -eq 1 -o \( $b -eq 2 -a $c -eq 3 \) ]

# 加括号改变优先级
[ \( $a -eq 1 -o $b -eq 2 \) -a $c -eq 3 ]
```

## 快捷写法

```bash
# 短路求值（不写 if）
[ -f /tmp/file ] && echo "文件存在"
[ -f /tmp/file ] || echo "文件不存在"

# 等同于
if [ -f /tmp/file ]; then
    echo "文件存在"
else
    echo "文件不存在"
fi
```

## 常用组合速查

| 目的 | 表达式 |
|------|--------|
| 文件存在 | `[ -e file ]` |
| 是普通文件 | `[ -f file ]` |
| 是目录 | `[ -d dir ]` |
| 可执行 | `[ -x file ]` |
| 变量非空 | `[ -n "$var" ]` 或 `[ "$var" ]` |
| 变量为空 | `[ -z "$var" ]` |
| 字符串相等 | `[ "$a" = "$b" ]` |
| 数值相等 | `[ $a -eq $b ]` |
| 数值大于 | `[ $a -gt $b ]` |
| 文件较新 | `[ a.txt -nt b.txt ]` |
| 命令存在 | `command -v cmd` |

## 一句话总结

测试表达式核心：`-f` 测试文件，`-d` 测试目录，`-z` 测试空字符串，`-eq` 测试数值相等。`[ ]` 最常用，`[[ ]]` 功能更强，数值比较用 `-eq/-ne/-gt/-lt`，字符串比较用 `=`/`!=`。
