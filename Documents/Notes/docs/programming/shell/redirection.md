# Shell 重定向与管道

## 标准输入输出

### 文件描述符

| 描述符 | 名称 | 符号 | 默认 |
|--------|------|------|------|
| 0 | 标准输入 | stdin | 键盘 |
| 1 | 标准输出 | stdout | 终端 |
| 2 | 标准错误 | stderr | 终端 |

```sh
# 查看默认位置
ls -l /proc/$$/fd
```

## 输出重定向

### 覆盖重定向

```sh
# 标准输出重定向到文件（覆盖）
echo "hello" > output.txt

# 标准错误重定向到文件（覆盖）
ls /nonexistent 2> error.txt

# 同时重定向标准输出和标准错误
command > all.txt 2>&1
# 或
command &> all.txt  # bash 扩展

# 重定向到 /dev/null（丢弃输出）
command > /dev/null 2>&1
```

### 追加重定向

```sh
# 标准输出追加
echo "new line" >> output.txt

# 标准错误追加
ls /nonexistent 2>> error.txt

# 同时追加
command >> all.txt 2>&1
```

### 合并重定向

```sh
# 将 stderr 合并到 stdout
command 2>&1

# 将 stdout 和 stderr 合并到文件
command > output.txt 2>&1

# 分别重定向
command > stdout.txt 2> stderr.txt
```

## 输入重定向

### 从文件读取

```sh
# 将文件内容作为命令输入
wc -l < /etc/passwd

# 逐行读取文件
while read line; do
    echo "$line"
done < /etc/passwd
```

### Here Document

```sh
# 多行字符串作为输入
cat << EOF
第一行
第二行
第三行
EOF

# 保存到文件
cat > config.txt << EOF
name=张三
age=25
city=北京
EOF

# 使用变量（不转义）
name="张三"
cat << EOF
Hello $name
EOF

# 禁止变量替换（加引号）
cat << 'EOF'
Hello $name
EOF

# 忽略前导制表符（加 -）
cat <<- EOF
    缩进的行
    也会被忽略
EOF
```

### Here String

```sh
# 将字符串作为输入（bash 扩展）
grep "error" <<< "error message"

# 计算字符串长度
wc -c <<< "hello"
```

## 管道

### 基本用法

```sh
# 将前一个命令的输出作为后一个命令的输入
ls -la | grep ".txt"
cat file.txt | wc -l
ps aux | grep "nginx" | wc -l
```

### 管道链

```sh
# 多个命令串联
cat /var/log/syslog | grep "error" | sort | uniq -c | sort -rn | head -10
```

### 管道与重定向组合

```sh
# 管道输出并保存到文件
command | tee output.txt

# 追加到文件
command | tee -a output.txt

# 同时查看和保存
ls -la | tee listing.txt | grep ".txt"
```

### 进程替换（bash 扩展）

```sh
# 将命令输出作为文件使用
diff <(ls dir1) <(ls dir2)

# 读取两个命令的输出
while read line1 && read line2 <&3; do
    echo "$line1 - $line2"
done < file1.txt 3< <(cat file2.txt)
```

## 高级重定向

### 自定义文件描述符

```sh
# 打开文件用于读取
exec 3< input.txt
read line <&3
exec 3<&-  # 关闭

# 打开文件用于写入
exec 4> output.txt
echo "hello" >&4
exec 4>&-

# 复制描述符
exec 5>&1      # 保存 stdout
exec 1> log.txt
echo "到日志"
exec 1>&5      # 恢复 stdout
```

### 重定向代码块

```sh
# 整个代码块重定向
{
    echo "第一行"
    echo "第二行"
    ls /nonexistent 2>&1
} > output.txt 2>&1
```

```sh
# 循环重定向
for i in 1 2 3; do
    echo "Number: $i"
done > numbers.txt
```

```sh
# 条件重定向
if [ -f "$file" ]; then
    cat "$file"
else
    echo "文件不存在"
fi > result.txt
```

## 常见模式

### 抑制输出

```sh
# 丢弃所有输出
command > /dev/null 2>&1

# 只丢弃标准输出
command > /dev/null

# 只丢弃标准错误
command 2> /dev/null
```

### 同时输出到文件和终端

```sh
# 使用 tee
command | tee output.txt

# 同时追加
command | tee -a output.txt

# 同时记录错误
command 2>&1 | tee output.txt
```

### 读取用户输入

```sh
# 基本读取
echo "请输入姓名:"
read name

# 带提示
read -p "请输入姓名: " name

# 超时读取（bash）
read -t 5 -p "5秒内输入: " input

# 读取密码（不显示）
read -s -p "密码: " password
echo
```

## 实际应用示例

### 日志函数

```sh
#!/bin/sh

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"
}

log_info() {
    log "INFO: $*"
}

log_error() {
    log "ERROR: $*" >&2
}

# 使用
log_info "脚本开始"
log_error "发生错误"
```

### 进度显示

```sh
#!/bin/sh

# 处理文件并显示进度
total=$(wc -l < filelist.txt)
count=0

while read file; do
    count=$((count + 1))
    printf "\r处理进度: %d/%d" "$count" "$total" >&2
    # 处理文件...
done < filelist.txt
echo >&2
```

### 交互式确认

```sh
#!/bin/sh

confirm() {
    printf "%s (y/n): " "$1"
    read answer
    case "$answer" in
        y|Y|yes|YES) return 0 ;;
        *) return 1 ;;
    esac
}

if confirm "确认删除?"; then
    rm -rf /tmp/data
    echo "已删除"
fi
```

### 管道调试

```sh
#!/bin/sh

# 查看管道中间结果
ls -la | tee /tmp/step1.txt | grep ".txt" | tee /tmp/step2.txt | wc -l

# 使用 cat 插入调试
command1 | cat -n | command2  # 显示行号
```

### 错误处理包装

```sh
#!/bin/sh

# 捕获命令输出和错误
run_cmd() {
    output=$( "$@" 2>&1 )
    code=$?
    echo "$output"
    return $code
}

# 使用
if run_cmd ls /nonexistent; then
    echo "成功"
else
    echo "失败"
fi
```

### 多文件处理

```sh
#!/bin/sh

# 同时读取两个文件
while read line1 && read line2 <&3; do
    echo "文件1: $line1"
    echo "文件2: $line2"
done < file1.txt 3< file2.txt
```

## 重定向顺序

```sh
# 顺序很重要

# 正确：先重定向 stdout，再将 stderr 合并到 stdout
command > output.txt 2>&1

# 错误：stderr 先被重定向到当前 stdout（终端），然后 stdout 才重定向到文件
command 2>&1 > output.txt
```

## 快速参考

| 语法 | 说明 |
|------|------|
| `> file` | stdout 覆盖写入 |
| `>> file` | stdout 追加写入 |
| `2> file` | stderr 覆盖写入 |
| `2>> file` | stderr 追加写入 |
| `&> file` | stdout+stderr 覆盖写入 |
| `&>> file` | stdout+stderr 追加写入 |
| `> file 2>&1` | stdout+stderr 覆盖写入（POSIX） |
| `< file` | 从文件读取 |
| `cmd1 \| cmd2` | 管道 |
| `cmd1 && cmd2` | 前成功则执行 |
| `cmd1 \|\| cmd2` | 前失败则执行 |
| `tee file` | 同时输出到文件和 stdout |
