# grep 命令详解

## 一句话理解 grep

grep 是搜索文本的工具，在文件或输入中**查找包含指定内容的行**。

```bash
grep "要查找的内容" 文件名
```

## 最常用的场景

### 在文件中搜索

```bash
grep "error" app.log
```

### 在当前目录所有文件中搜索

```bash
grep "error" *
```

### 递归搜索所有子目录

```bash
grep -r "error" /var/log/
```

### 不区分大小写

```bash
grep -i "error" app.log   # 能匹配 Error、ERROR、error
```

## 常用选项

| 选项 | 说明 | 例子 |
|------|------|------|
| `-i` | 忽略大小写 | `grep -i "error" file` |
| `-r` | 递归搜索目录 | `grep -r "pattern" /path/` |
| `-v` | 反向匹配（显示不包含的行） | `grep -v "error" file` |
| `-n` | 显示行号 | `grep -n "error" file` |
| `-c` | 只显示匹配行数 | `grep -c "error" file` |
| `-l` | 只显示包含匹配的文件名 | `grep -l "error" *.log` |
| `-L` | 只显示不包含匹配的文件名 | `grep -L "error" *.log` |
| `-w` | 匹配整个单词 | `grep -w "to" file` |
| `-m 数字` | 最多匹配多少行 | `grep -m 5 "error" file` |
| `-A 数字` | 显示匹配行及后面N行 | `grep -A 2 "error" file` |
| `-B 数字` | 显示匹配行及前面N行 | `grep -B 2 "error" file` |
| `-C 数字` | 显示匹配行及前后各N行 | `grep -C 2 "error" file` |
| `--color` | 高亮显示匹配内容 | `grep --color "error" file` |

## 实际例子

### 1. 搜索日志文件

```bash
# 查找错误
grep "ERROR" app.log

# 查找错误并显示行号
grep -n "ERROR" app.log

# 统计错误数量
grep -c "ERROR" app.log

# 查找错误及其前后3行
grep -C 3 "ERROR" app.log

# 查找错误，最多显示10条
grep -m 10 "ERROR" app.log
```

### 2. 过滤命令输出

```bash
# 查看进程
ps aux | grep "nginx"

# 查看端口占用
netstat -tlnp | grep ":80"

# 查看内存
free -h | grep "Mem"

# 查看CPU信息
lscpu | grep "Model name"

# 排除 grep 自身
ps aux | grep "nginx" | grep -v "grep"
# 或使用
ps aux | grep "[n]ginx"
```

### 3. 搜索代码

```bash
# 查找所有 py 文件中包含 import 的行
grep "import" *.py

# 递归搜索当前目录所有代码
grep -r "def main" .

# 只显示文件名
grep -r -l "TODO" .

# 显示行号
grep -n "class" *.py
```

### 4. 过滤配置文件

```bash
# 查看非注释行
grep -v "^#" /etc/nginx/nginx.conf

# 查看非空行和非注释行
grep -v "^#" /etc/nginx/nginx.conf | grep -v "^$"

# 查看启用的配置
grep "^[a-z]" config.conf
```

### 5. 从文件中提取信息

```bash
# 提取 IP 地址（简单版）
grep -E "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" access.log

# 提取邮箱
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" file.txt

# 提取 HTTP 状态码
grep -E "HTTP/[0-9.]+\" [0-9]{3}" access.log
```

## 常用正则表达式

使用 `-E` 开启扩展正则，不需要转义括号、加号、问号等。

| 正则 | 说明 | 例子 |
|------|------|------|
| `.` | 任意单个字符 | `grep -E "a.c"` 匹配 abc、aac |
| `*` | 前一个字符0次或多次 | `grep -E "go*gle"` 匹配 ggle、gogle、google |
| `+` | 前一个字符1次或多次 | `grep -E "go+gle"` 匹配 gogle、google |
| `?` | 前一个字符0次或1次 | `grep -E "colou?r"` 匹配 color、colour |
| `[abc]` | 匹配 a、b 或 c | `grep -E "[0-9]"` 匹配数字 |
| `[^abc]` | 不匹配 a、b、c | `grep -E "[^0-9]"` 匹配非数字 |
| `^` | 行首 | `grep "^#"` 匹配注释行 |
| `$` | 行尾 | `grep "\.$"` 匹配以句号结尾的行 |
| `\b` | 单词边界 | `grep -w "to"` 或 `grep "\bto\b"` |
| `|` | 或 | `grep -E "error|warning"` |
| `()` | 分组 | `grep -E "(error|warning)"` |
| `{n}` | 重复n次 | `grep -E "[0-9]{4}"` 匹配4位数字 |

### 正则例子

```bash
# 匹配 IP 地址
grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" file

# 匹配日期格式 2026-04-08
grep -E "[0-9]{4}-[0-9]{2}-[0-9]{2}" file

# 匹配 error 或 warning（不区分大小写）
grep -iE "error|warning" app.log

# 匹配以 a 开头以 z 结尾的行
grep -E "^a.*z$" file

# 匹配空行
grep "^$" file

# 匹配非空行
grep -v "^$" file
```

## 搜索多个文件

```bash
# 搜索当前目录所有 .log 文件
grep "error" *.log

# 搜索多个指定文件
grep "error" file1.txt file2.txt file3.txt

# 搜索所有文件（包括隐藏文件）
grep -r "pattern" .

# 只搜索特定类型文件
grep --include="*.py" -r "def" .
grep --include="*.{py,js}" -r "function" .

# 排除特定文件
grep --exclude="*.log" -r "error" .
grep --exclude-dir="node_modules" -r "require" .
```

## 与其他命令配合

### 管道用法

```bash
# 查看特定进程
ps aux | grep nginx

# 查看特定端口的连接
ss -tunap | grep :80

# 查看特定用户的进程
ps aux | grep "^username"

# 查看历史命令中某个命令的用法
history | grep "ssh"
```

### 组合多个 grep

```bash
# 同时包含两个关键词
grep "error" app.log | grep "database"

# 包含 error 但不包含 timeout
grep "error" app.log | grep -v "timeout"

# 包含 error 或 warning
grep -E "error|warning" app.log
```

## 输出格式控制

```bash
# 高亮显示（大部分系统默认开启）
grep --color=always "error" file

# 只输出匹配的部分（不输出整行）
grep -o "error" file

# 显示文件名和行号
grep -Hn "error" *.log

# 静默模式（只返回状态码，不输出任何内容）
grep -q "error" file
echo $?  # 0 表示找到，1 表示没找到
```

## 实际脚本用法

### 检查日志中是否有错误

```bash
if grep -q "ERROR" app.log; then
    echo "发现错误"
    grep "ERROR" app.log
else
    echo "没有错误"
fi
```

### 统计错误类型

```bash
grep -o "ERROR_[A-Z_]*" app.log | sort | uniq -c
```

### 监控日志实时输出

```bash
tail -f app.log | grep --line-buffered "ERROR"
```

## 常用组合速查

| 目的 | 命令 |
|------|------|
| 搜索关键字 | `grep "keyword" file` |
| 忽略大小写 | `grep -i "keyword" file` |
| 递归搜索目录 | `grep -r "keyword" /path/` |
| 显示行号 | `grep -n "keyword" file` |
| 反向匹配（排除） | `grep -v "keyword" file` |
| 统计匹配行数 | `grep -c "keyword" file` |
| 显示前后文 | `grep -C 3 "keyword" file` |
| 只显示文件名 | `grep -l "keyword" *.txt` |
| 使用正则 | `grep -E "pattern" file` |
| 匹配整个单词 | `grep -w "word" file` |

## 与 sed 对比

| 场景 | grep | sed |
|------|------|-----|
| 查找内容 | `grep "pattern" file` | `sed -n '/pattern/p' file` |
| 查找并替换 | 不能直接替换 | `sed -i 's/old/new/g' file` |
| 删除匹配行 | `grep -v "pattern" file` | `sed '/pattern/d' file` |
| 提取匹配部分 | `grep -o "pattern" file` | 需要更复杂的写法 |

## 一句话总结

grep 就是**找内容**，配合管道 `|` 使用是最常见的场景。记住 `grep -r`（递归）、`grep -i`（忽略大小写）、`grep -v`（排除）、`grep -E`（正则）就够了。
