# Shell 控制流

## if 语句

### 基本语法

```sh
if condition; then
    commands
fi
```

### if-else

```sh
if condition; then
    commands
else
    commands
fi
```

### if-elif-else

```sh
if condition1; then
    commands1
elif condition2; then
    commands2
else
    commands3
fi
```

### 实际示例

```sh
#!/bin/sh

# 数值比较
score=85
if [ "$score" -ge 90 ]; then
    echo "优秀"
elif [ "$score" -ge 80 ]; then
    echo "良好"
elif [ "$score" -ge 60 ]; then
    echo "及格"
else
    echo "不及格"
fi
```

```sh
#!/bin/sh

# 文件检查
file="/etc/passwd"
if [ -f "$file" ] && [ -r "$file" ]; then
    echo "文件存在且可读"
elif [ -f "$file" ] && [ ! -r "$file" ]; then
    echo "文件存在但不可读"
else
    echo "文件不存在"
fi
```

```sh
#!/bin/sh

# 字符串比较
name="张三"
if [ "$name" = "张三" ]; then
    echo "欢迎张三"
elif [ "$name" = "李四" ]; then
    echo "欢迎李四"
else
    echo "未知用户"
fi
```

### 简写形式

```sh
# && 表示前面成功则执行后面
[ -f /etc/passwd ] && echo "文件存在"

# || 表示前面失败则执行后面
[ -f /nonexistent ] || echo "文件不存在"

# 组合使用
[ -f "$file" ] && echo "存在" || echo "不存在"
```

## case 语句

### 基本语法

```sh
case word in
    pattern1)
        commands1
        ;;
    pattern2)
        commands2
        ;;
    *)
        default_commands
        ;;
esac
```

### 实际示例

```sh
#!/bin/sh

# 根据参数执行不同操作
case "$1" in
    start)
        echo "启动服务"
        ;;
    stop)
        echo "停止服务"
        ;;
    restart)
        echo "重启服务"
        ;;
    status)
        echo "查看状态"
        ;;
    *)
        echo "用法: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac
```

```sh
#!/bin/sh

# 匹配文件扩展名
filename="script.sh"
case "$filename" in
    *.sh)
        echo "Shell 脚本"
        ;;
    *.py)
        echo "Python 脚本"
        ;;
    *.c|*.h)
        echo "C 语言文件"
        ;;
    *)
        echo "未知类型"
        ;;
esac
```

```sh
#!/bin/sh

# 匹配多个模式
read answer
case "$answer" in
    y|Y|yes|YES|Yes)
        echo "确认"
        ;;
    n|N|no|NO|No)
        echo "取消"
        ;;
    *)
        echo "无效输入"
        ;;
esac
```

### 使用通配符

```sh
#!/bin/sh

# 匹配以数字开头
case "$1" in
    [0-9]*)
        echo "以数字开头"
        ;;
    [a-z]*)
        echo "以小写字母开头"
        ;;
    [A-Z]*)
        echo "以大写字母开头"
        ;;
    *)
        echo "其他"
        ;;
esac
```

## for 循环

### 遍历列表

```sh
# 基本语法
for var in list; do
    commands
done
```

```sh
# 遍历字符串列表
for name in 张三 李四 王五; do
    echo "姓名: $name"
done
```

```sh
# 遍历命令输出
for file in $(ls *.txt); do
    echo "处理文件: $file"
done
```

```sh
# 遍历数字序列（POSIX 方式）
for i in 1 2 3 4 5; do
    echo "数字: $i"
done
```

```sh
# 使用 seq 命令（如果可用）
for i in $(seq 1 10); do
    echo "$i"
done
```

### 遍历参数

```sh
#!/bin/sh

# 遍历所有参数
for arg in "$@"; do
    echo "参数: $arg"
done
```

```sh
#!/bin/sh

# 遍历除第一个外的参数
first="$1"
shift
for arg in "$@"; do
    echo "剩余参数: $arg"
done
```

## while 循环

### 基本语法

```sh
while condition; do
    commands
done
```

### 实际示例

```sh
#!/bin/sh

# 计数循环
count=1
while [ "$count" -le 5 ]; do
    echo "计数: $count"
    count=$((count + 1))
done
```

```sh
#!/bin/sh

# 读取文件逐行处理
while read line; do
    echo "行内容: $line"
done < /etc/passwd
```

```sh
#!/bin/sh

# 无限循环
while true; do
    echo "按 Ctrl+C 退出"
    sleep 1
done
```

```sh
#!/bin/sh

# 等待文件出现
while [ ! -f "/tmp/ready" ]; do
    echo "等待文件..."
    sleep 2
done
echo "文件已就绪"
```

## until 循环

```sh
# 条件为假时执行（与 while 相反）
until condition; do
    commands
done
```

```sh
#!/bin/sh

# 等待直到文件存在
until [ -f "/tmp/ready" ]; do
    echo "等待文件..."
    sleep 2
done
echo "文件已就绪"
```

```sh
#!/bin/sh

# 计数循环（条件为假时继续）
count=1
until [ "$count" -gt 5 ]; do
    echo "计数: $count"
    count=$((count + 1))
done
```

## break 和 continue

### break

```sh
# 退出循环
for i in 1 2 3 4 5; do
    if [ "$i" -eq 3 ]; then
        break
    fi
    echo "$i"  # 输出 1 2
done
```

### continue

```sh
# 跳过当前迭代
for i in 1 2 3 4 5; do
    if [ "$i" -eq 3 ]; then
        continue
    fi
    echo "$i"  # 输出 1 2 4 5
done
```

### 跳出多层循环

```sh
# 使用 break 2 跳出两层循环
for i in 1 2; do
    for j in a b c; do
        if [ "$i" -eq 2 ] && [ "$j" = "b" ]; then
            break 2
        fi
        echo "$i $j"
    done
done
# 输出: 1 a, 1 b, 1 c, 2 a
```

## 实际应用示例

### 批量重命名文件

```sh
#!/bin/sh

for file in *.txt; do
    if [ -f "$file" ]; then
        new_name="backup_$file"
        mv "$file" "$new_name"
        echo "重命名: $file -> $new_name"
    fi
done
```

### 检查服务状态

```sh
#!/bin/sh

services="nginx mysql redis"

for svc in $services; do
    if pgrep -x "$svc" > /dev/null; then
        echo "$svc: 运行中"
    else
        echo "$svc: 未运行"
    fi
done
```

### 交互式菜单

```sh
#!/bin/sh

while true; do
    echo "=========================="
    echo "1. 显示日期时间"
    echo "2. 显示磁盘使用"
    echo "3. 显示内存使用"
    echo "4. 退出"
    echo "=========================="
    printf "请选择: "
    read choice

    case "$choice" in
        1)
            date
            ;;
        2)
            df -h
            ;;
        3)
            free -h
            ;;
        4)
            echo "再见"
            break
            ;;
        *)
            echo "无效选择"
            ;;
    esac
    echo ""
done
```
