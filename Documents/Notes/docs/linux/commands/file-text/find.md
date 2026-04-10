# find 命令详解

## 基本语法

```bash
find [路径] [选项] [表达式]
```

## 按文件名查找

```bash
find /home -name "*.txt"       # 查找所有 .txt 文件
find . -name "file*"           # 当前目录查找以 file 开头的文件
find / -type d -name "docs"    # 查找名为 docs 的目录
find . -iname "readme"         # 不区分大小写查找 README/readme/ReadMe
```

| 选项 | 说明 |
|------|------|
| `-name "pattern"` | 按文件名匹配（支持通配符 `*`、`?`、`[]`） |
| `-iname "pattern"` | 不区分大小写的 `-name` |
| `-path "pattern"` | 按路径匹配 |
| `-ipath "pattern"` | 不区分大小写的 `-path` |
| `-regex "pattern"` | 使用正则表达式匹配完整路径 |
| `-iregex "pattern"` | 不区分大小写的 `-regex` |

## 按文件类型查找

```bash
find / -type f        # 普通文件
find / -type d        # 目录
find / -type l        # 符号链接
find / -type s        # 套接字文件
find / -type b        # 块设备文件
find / -type c        # 字符设备文件
```

| 选项 | 说明 |
|------|------|
| `-type f` | 普通文件 |
| `-type d` | 目录 |
| `-type l` | 符号链接 |
| `-type b` | 块设备文件 |
| `-type c` | 字符设备文件 |
| `-type p` | 命名管道（FIFO） |
| `-type s` | 套接字文件 |

## 按时间查找

```bash
find / -mtime -7       # 7天内修改过的文件
find / -mtime +30      # 30天前修改过的文件
find / -atime -1       # 24小时内访问过的文件
find / -mmin -60       # 60分钟内修改过的文件
find / -newer file.txt # 比 file.txt 更新的文件
```

| 选项 | 说明 |
|------|------|
| `-mtime n` | n 天前修改（`+n`=超过n天，`-n`=n天内） |
| `-atime n` | n 天前访问 |
| `-ctime n` | n 天前状态变化（权限/所有者） |
| `-mmin n` | n 分钟前修改 |
| `-amin n` | n 分钟前访问 |
| `-cmin n` | n 分钟前状态变化 |
| `-newer file` | 比 file 更新的文件 |
| `-anewer file` | 比 file 更晚访问的文件 |
| `-cnewer file` | 比 file 更晚状态变化的文件 |

## 按大小查找

```bash
find / -size +10M            # 大于 10MB
find / -size -1G             # 小于 1GB
find / -size +100k -size -1M # 100KB 到 1MB 之间
find / -size 0               # 空文件
find / -empty                # 空文件或空目录
```

| 选项 | 说明 |
|------|------|
| `-size n[cwbkMG]` | 大小为 n（c=字节，w=字，b=块，k=KB，M=MB，G=GB） |
| `-size +n` | 大于 n |
| `-size -n` | 小于 n |
| `-empty` | 空文件或空目录 |

## 按权限查找

```bash
find / -perm 644            # 权限完全匹配 644
find / -perm -u=r           # 用户至少可读
find / -perm /a+x           # 任何人至少可执行
find / -user root           # 属于 root 用户
find / -group staff         # 属于 staff 组
find / -nouser              # 没有所属用户（用户被删除）
find / -nogroup             # 没有所属组
```

| 选项 | 说明 |
|------|------|
| `-perm mode` | 权限完全匹配 mode |
| `-perm -mode` | 权限包含所有 mode 位 |
| `-perm /mode` | 权限包含任意 mode 位 |
| `-user name` | 属于用户 name |
| `-group name` | 属于组 name |
| `-nouser` | 没有所属用户 |
| `-nogroup` | 没有所属组 |

## 组合条件

```bash
find / -name "*.log" -and -mtime +30   # 30天前的 .log 文件
find / -name "*.tmp" -or -name "*.temp" # .tmp 或 .temp 文件
find / ! -name "*.txt"                  # 不是 .txt 结尾
find / \( -name "*.c" -or -name "*.h" \) -type f  # 括号分组
```

| 操作符 | 说明 |
|--------|------|
| `-a` / `-and` | 逻辑与（默认，可省略） |
| `-o` / `-or` | 逻辑或 |
| `!` / `-not` | 逻辑非 |
| `\( ... \)` | 分组（注意转义） |

## 对查找结果执行操作

```bash
find . -name "*.bak" -delete                    # 删除所有 .bak 文件
find . -name "*.jpg" -exec chmod 644 {} \;      # 修改权限
find . -name "*.sh" -exec chmod +x {} \;        # 添加执行权限
find . -name "*.old" -ok rm {} \;               # 交互式删除（询问确认）
find . -type f -name "*.log" -exec cat {} \;    # 查看所有 log 文件内容
find . -name "*.txt" -exec cp {} /backup/ \;    # 复制到备份目录
```

| 选项 | 说明 |
|------|------|
| `-exec command {} \;` | 对每个文件执行 command（`{}` 替换为文件名） |
| `-exec command {} +` | 更高效，一次传递多个文件给 command |
| `-ok command {} \;` | 交互式 `-exec`，每次执行前询问确认 |
| `-delete` | 删除匹配的文件 |
| `-print` | 打印匹配的文件（默认行为） |
| `-print0` | 以 `\0` 分隔文件名（处理空格和特殊字符） |
| `-ls` | 以 `ls -dils` 格式输出 |

## 安全处理文件名中的空格和特殊字符

默认情况下，find 用换行符分隔文件名。如果文件名包含空格或换行符，直接通过管道传给 xargs 会出错。

```bash
# 错误示例：文件名 "hello world.txt" 会被拆分成两个参数
find . -name "*.txt" | xargs rm

# 正确做法1：使用 -print0 和 xargs -0
find . -name "*.txt" -print0 | xargs -0 rm

# 正确做法2：使用 -exec（最安全，不需要 xargs）
find . -name "*.txt" -exec rm {} +

# 正确做法3：使用 -delete（仅限删除操作）
find . -name "*.txt" -delete
```

实际应用示例：

```bash
# 查找并复制文件到目标目录
find /source -name "*.pdf" -print0 | xargs -0 cp -t /target/

# 查找并统计文件行数
find . -type f -name "*.sh" -print0 | xargs -0 wc -l

# 查找并搜索文件内容
find . -type f -name "*.conf" -print0 | xargs -0 grep -l "error"

# 调试 xargs 执行的命令（-t 显示实际命令）
find . -name "*.log" -print0 | xargs -0 -t rm
```

## 限制搜索深度

```bash
find / -maxdepth 2 -name "*.conf"    # 最多搜索2层
find / -mindepth 3 -name "*.txt"     # 至少搜索3层
find / -maxdepth 1 -type f           # 仅当前目录，不递归
```

## 其他常用选项

```bash
find / -readable                      # 可读的文件
find / -writable                      # 可写的文件
find / -executable                    # 可执行的文件
find / -samefile /path/to/file        # 指向同一 inode 的文件（硬链接）
find / -inum 123456                   # 按 inode 号查找
find / -links +1                      # 硬链接数大于1的文件
```

## 性能优化选项

```bash
find / -O1 -name "*.txt"              # 优化级别1（文件名优先）
find / -O3 -name "*.txt"              # 优化级别3（深度优先）
find / -D tree -name "*.txt"          # 显示搜索树（调试用）
```

| 选项 | 说明 |
|------|------|
| `-O n` | 优化级别（1=文件名优先，3=深度优先） |
| `-D debugopts` | 调试输出（如 `-D tree` 显示搜索树） |
| `-follow` | 跟随符号链接（已弃用，推荐用 `-L`） |
| `-L` | 跟随符号链接 |
| `-P` | 不跟随符号链接（默认） |

## 常见使用场景

### 清理旧日志文件

```bash
# 删除 30 天前的 .log 文件
find /var/log -name "*.log" -mtime +30 -delete

# 压缩 7 天前的日志（不删除）
find /var/log -name "*.log" -mtime +7 -exec gzip {} \;
```

### 查找大文件

```bash
# 查找大于 100MB 的文件
find / -type f -size +100M -exec ls -lh {} \;

# 查找最大的 10 个文件
find / -type f -exec du -b {} + | sort -rn | head -10
```

### 批量修改文件权限

```bash
# 所有目录设为 755
find . -type d -exec chmod 755 {} \;

# 所有文件设为 644
find . -type f -exec chmod 644 {} \;

# 所有 .sh 文件添加执行权限
find . -name "*.sh" -exec chmod +x {} \;
```

### 查找并替换文件内容

```bash
# 查找所有 .txt 文件，将 old 替换为 new
find . -name "*.txt" -exec sed -i 's/old/new/g' {} \;
```

### 统计代码行数

```bash
# 统计所有 .py 文件行数
find . -name "*.py" -exec cat {} \; | wc -l

# 分别显示每个文件的行数
find . -name "*.py" -exec wc -l {} \;
```

### 查找重复文件

```bash
# 按文件大小查找可能的重复文件
find . -type f -size +1M -exec md5sum {} \; | sort | uniq -d --check-chars=32
```

## 与 xargs 配合的常用模式

```bash
# 并行处理（-P 指定并行数）
find . -name "*.jpg" -print0 | xargs -0 -P 4 -I {} convert {} -resize 50% {}

# 分批处理（-n 指定每批数量）
find . -name "*.log" -print0 | xargs -0 -n 100 rm

# 交互式处理（-p 询问确认）
find . -name "*.tmp" -print0 | xargs -0 -p rm
```

## 调试技巧

```bash
# 预览将要执行的命令（-n 模拟运行）
find . -name "*.txt" -exec echo rm {} \;

# 使用 -ok 代替 -exec 交互式确认
find . -name "*.txt" -ok rm {} \;

# 使用 xargs -t 显示执行的命令
find . -name "*.txt" -print0 | xargs -0 -t rm
```
