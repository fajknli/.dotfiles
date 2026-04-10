# w - 查看登录用户

## 一句话理解

w 命令显示当前登录的用户及其正在执行的操作，包括登录时间、终端、CPU 使用率等。

```bash
# 查看所有登录用户
w

# 输出示例：
# 10:30:45 up 2 days, 3 users, load average: 0.08, 0.03, 0.01
# USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
# fajknli  tty2     :0               09:00    2:30m  0.15s  0.05s /usr/bin/gnome-s
# fajknli  pts/0    192.168.1.100    10:00    5.00s  0.02s  0.01s sshd: fajknli
```

## 常用场景

### 1. 查看当前登录用户

```bash
# 基本查看
w

# 不显示标题行
w -h

# 不显示登录时间、JCPU、PCPU 等（短格式）
w -s
```

### 2. 查看特定用户

```bash
# 只显示指定用户
w fajknli

# 排除指定用户
w | grep -v root
```

### 3. 查看用户来源 IP

```bash
# 显示用户登录来源
w | awk 'NR>2 {print $1, $3}'

# 输出示例：
# fajknli :0
# fajknli 192.168.1.100
```

### 4. 统计登录用户数

```bash
# 统计在线用户数
w -h | wc -l

# 或使用
who -q
```

### 5. 监控用户登录

```bash
# 持续监控（每 2 秒刷新）
watch -n 2 w

# 有新用户登录时发送通知（脚本）
#!/bin/bash
last_users=$(w -h | wc -l)
while true; do
    current_users=$(w -h | wc -l)
    if [ $current_users -gt $last_users ]; then
        echo "新用户登录"
    fi
    last_users=$current_users
    sleep 5
done
```

## 输出字段说明

| 字段 | 说明 |
|------|------|
| USER | 用户名 |
| TTY | 终端类型（tty=本地，pts=远程） |
| FROM | 来源 IP（本地显示 :0 或 :1） |
| LOGIN@ | 登录时间 |
| IDLE | 空闲时间 |
| JCPU | 终端所有进程累计 CPU 时间 |
| PCPU | 当前进程 CPU 时间 |
| WHAT | 当前执行的命令 |

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-h` | 不显示标题行 | `w -h` |
| `-s` | 短格式（不显示 LOGIN@、JCPU、PCPU） | `w -s` |
| `-f` | 显示/不显示 FROM 字段 | `w -f` |
| `-u` | 显示当前进程和 CPU 时间 | `w -u` |

## 常见问题

### 1. w 和 who 有什么区别？

| 命令 | 信息 |
|------|------|
| `w` | 详细信息（含负载、用户活动、空闲时间） |
| `who` | 简单信息（用户名、终端、登录时间、来源） |
| `who -q` | 只显示用户名和数量 |

### 2. 如何踢掉其他用户？

```bash
# 查看用户终端
w
# 记住用户的 TTY（如 pts/1）

# 踢掉用户
sudo pkill -t pts/1

# 或使用 skill
sudo skill -KILL -t pts/1

# 或使用 fuser
sudo fuser -k /dev/pts/1
```

### 3. 用户空闲时间很长怎么办？

```bash
# 查看空闲超过 1 小时的用户
w | awk 'NR>2 && $5 ~ /h/ {print $1, $2, $5}'

# 踢掉空闲用户（谨慎操作）
sudo pkill -t $(w | awk 'NR>2 && $5 ~ /h/ {print $2}')
```

## 快捷别名

```bash
alias w-short='w -s'
alias w-noheader='w -h'
alias w-ips='w | awk "NR>2 {print \$1, \$3}"'
alias who-count='who -q'
```

## 一句话总结

w 核心：`w` 查看所有登录用户及其活动，`w -h` 不显示标题，`w -s` 短格式。用 `w` 的 TTY 列配合 `pkill -t` 可踢掉用户。简单查用户用 `who`，详细查用户活动用 `w`。
