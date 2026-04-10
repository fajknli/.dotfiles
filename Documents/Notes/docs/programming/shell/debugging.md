# Shell 调试与最佳实践

## 调试技巧

### 语法检查

```sh
# 检查脚本语法（不执行）
sh -n script.sh

# 详细模式（显示执行的每条命令）
sh -v script.sh

# 调试模式（显示命令和参数展开）
sh -x script.sh

# 组合使用
sh -nx script.sh
```

### 脚本内启用调试

```sh
#!/bin/sh

# 开启调试
set -x

# 代码块
echo "这条命令会显示"
result=$((10 + 20))

# 关闭调试
set +x

echo "这条命令不显示"
```

### 调试选项

| 选项 | 说明 |
|------|------|
| `set -x` | 显示命令及其参数 |
| `set -v` | 显示原始命令 |
| `set -n` | 只检查语法，不执行 |
| `set -e` | 遇到错误立即退出 |
| `set -u` | 使用未定义变量时退出 |
| `set -f` | 禁用通配符展开 |

```sh
#!/bin/sh

# 严格模式（推荐）
set -eu

# 遇到未定义变量时报错
echo "$undefined_var"  # 脚本会退出

# 遇到命令失败时退出
cd /nonexistent  # 脚本会退出
```

### 输出调试信息

```sh
#!/bin/sh

# 自定义调试函数
debug() {
    if [ -n "${DEBUG:-}" ]; then
        echo "DEBUG: $*" >&2
    fi
}

# 使用
DEBUG=1 ./script.sh
debug "变量值: $var"
```

```sh
#!/bin/sh

# 带行号的调试
debug() {
    echo "[DEBUG] $(basename "$0"):${1}: ${2}" >&2
}

# 使用（传入行号）
debug "${LINENO}" "开始处理"
```

## 错误处理

### 检查命令执行结果

```sh
#!/bin/sh

# 检查退出码
command
if [ $? -ne 0 ]; then
    echo "命令执行失败"
    exit 1
fi

# 简写
command || { echo "失败"; exit 1; }
```

### 错误处理函数

```sh
#!/bin/sh

error_exit() {
    echo "错误: $1" >&2
    exit "${2:-1}"
}

# 使用
[ -f config.txt ] || error_exit "config.txt 不存在"

# 带退出码
command || error_exit "命令失败" 2
```

### 捕获信号

```sh
#!/bin/sh

# 清理函数
cleanup() {
    echo "清理临时文件..."
    rm -f /tmp/temp.$$
    exit 0
}

# 捕获退出、中断、终止信号
trap cleanup EXIT INT TERM

# 脚本内容
echo "脚本运行中..."
sleep 100
```

```sh
#!/bin/sh

# 忽略信号
trap '' INT   # 忽略 Ctrl+C
trap - INT    # 恢复
```

## 最佳实践

### 脚本头

```sh
#!/bin/sh
# 脚本名称: script.sh
# 描述: 脚本功能说明
# 作者: 姓名
# 版本: 1.0
# 用法: ./script.sh [选项]
```

### 严格模式

```sh
#!/bin/sh

# 推荐设置
set -e          # 错误时退出
set -u          # 未定义变量时报错
set -f          # 禁用通配符（需要时再开启）
set -o pipefail # 管道中任一命令失败则失败（bash）
```

### 安全使用变量

```sh
# 总是给变量加双引号
echo "$var"
[ "$name" = "张三" ]

# 使用花括号明确边界
echo "${name}_suffix"

# 使用默认值
name="${1:-默认值}"

# 检查变量是否设置
if [ -n "${var+set}" ]; then
    echo "变量已设置"
fi
```

### 临时文件

```sh
#!/bin/sh

# 创建临时文件
temp_file=$(mktemp) || exit 1
trap 'rm -f "$temp_file"' EXIT

# 创建临时目录
temp_dir=$(mktemp -d) || exit 1
trap 'rm -rf "$temp_dir"' EXIT

# 使用临时文件
echo "data" > "$temp_file"
```

### 函数使用

```sh
#!/bin/sh

# 函数命名使用小写加下划线
log_message() {
    echo "[$(date)] $*"
}

# 函数应有明确用途
is_file_exists() {
    [ -f "$1" ]
}

# 函数返回值使用 return
check_user() {
    if grep -q "^$1:" /etc/passwd; then
        return 0
    else
        return 1
    fi
}
```

## 性能优化

### 避免子 shell

```sh
# 不推荐（启动子 shell）
cat file.txt | while read line; do
    echo "$line"
done

# 推荐（重定向）
while read line; do
    echo "$line"
done < file.txt
```

### 减少外部命令

```sh
# 不推荐
result=$(echo "$var" | tr 'a-z' 'A-Z')

# 推荐（使用 shell 内置）
result=$(printf '%s' "$var" | tr 'a-z' 'A-Z')
# 或使用 ${var^^}（bash 扩展）
```

### 批量处理

```sh
# 不推荐（每行调用一次命令）
while read file; do
    grep "pattern" "$file"
done < filelist.txt

# 推荐（一次性处理）
grep "pattern" $(cat filelist.txt)
# 或使用 xargs
xargs grep "pattern" < filelist.txt
```

## 可移植性

### POSIX 兼容写法

```sh
#!/bin/sh

# 不推荐（bash 扩展）
if [[ "$var" == "value" ]]; then
    echo "bash 特有"
fi

# 推荐（POSIX）
if [ "$var" = "value" ]; then
    echo "可移植"
fi
```

### 命令替换

```sh
# 不推荐（反引号已过时）
result=`command`

# 推荐
result=$(command)
```

### 算术运算

```sh
# 推荐
result=$((10 + 20))

# 不推荐（expr 是外部命令）
result=$(expr 10 + 20)
```

### 数组替代

```sh
# POSIX sh 不支持数组，使用字符串分割
items="a b c"
for item in $items; do
    echo "$item"
done
```

## 常见陷阱

### 空格问题

```sh
# 错误：等号两边不能有空格
name = "张三"   # 错误

# 正确
name="张三"

# 错误：变量不加引号
file="my file.txt"
rm $file        # 删除 "my" 和 "file.txt"

# 正确
rm "$file"      # 删除 "my file.txt"
```

### 条件测试

```sh
# 错误：缺少空格
if ["$name" = "张三"]; then   # 语法错误

# 正确
if [ "$name" = "张三" ]; then
```

### 管道中的变量

```sh
# 问题：管道中的变量在子 shell 中
count=0
cat file.txt | while read line; do
    count=$((count + 1))
done
echo "$count"  # 仍是 0

# 解决方案
while read line; do
    count=$((count + 1))
done < file.txt
echo "$count"  # 正确
```

### 退出码

```sh
# 错误：管道返回最后一个命令的退出码
false | true
echo $?  # 0

# 使用 PIPESTATUS（bash）
false | true
echo ${PIPESTATUS[0]}  # 1

# 或使用 set -o pipefail
set -o pipefail
false | true
echo $?  # 1
```

## 代码检查工具

```sh
# shellcheck 静态分析
shellcheck script.sh

# 安装
# apt install shellcheck
# brew install shellcheck

# 检查特定问题
shellcheck -e SC2086 script.sh  # 忽略 SC2086
```

## 检查清单

| 检查项 | 说明 |
|--------|------|
| shebang | 使用 `#!/bin/sh` 或 `#!/bin/bash` |
| 变量引用 | 总是加双引号 `"$var"` |
| 条件测试 | 使用 `[ ]` 并注意空格 |
| 错误处理 | 检查命令执行结果 |
| 临时文件 | 使用 `mktemp` 并 `trap` 清理 |
| 调试 | 使用 `set -x` 或 `sh -x` |
| 可移植性 | 避免 bash 特有语法 |
| 注释 | 复杂逻辑添加注释 |
