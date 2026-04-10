# ss - 查看网络连接和套接字

## 一句话理解

ss（socket statistics）是 netstat 的现代替代品，用于查看网络连接、监听端口、套接字信息，速度更快，输出更详细。

```bash
# 查看所有 TCP 连接
ss -t

# 查看所有监听端口
ss -l
```

## 常用场景

### 1. 查看所有网络连接

```bash
# 查看所有 TCP 连接
ss -t

# 查看所有 UDP 连接
ss -u

# 查看所有 TCP 和 UDP
ss -tu

# 查看所有套接字（TCP、UDP、RAW、UNIX）
ss -a
```

### 2. 查看监听端口

```bash
# 查看所有监听的 TCP 端口
ss -lt

# 查看所有监听的 UDP 端口
ss -lu

# 查看所有监听的端口（TCP+UDP）
ss -l

# 查看监听的端口和进程
ss -ltp
```

### 3. 查看特定端口

```bash
# 查看 80 端口的连接
ss -t sport = :80
ss -t dport = :80

# 查看 22 端口的监听
ss -lt sport = :22

# 查看 443 端口的连接状态
ss -t state listening sport = :443
```

### 4. 查看进程信息

```bash
# 显示进程 PID 和名称
ss -tp

# 显示所有连接及对应进程
ss -tup

# 查看特定端口的进程
ss -tlp | grep :80
```

### 5. 查看连接状态统计

```bash
# 统计 TCP 连接状态
ss -s

# 输出示例：
# TCP:   2 (estab 1, closed 0, orphaned 0, timewait 0)
# Transport Total     IP        IPv6
# RAW       1         0         1
# UDP       5         3         2
# TCP       2         2         0
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-t` | 显示 TCP 连接 | `ss -t` |
| `-u` | 显示 UDP 连接 | `ss -u` |
| `-l` | 显示监听端口 | `ss -l` |
| `-a` | 显示所有连接 | `ss -a` |
| `-p` | 显示进程 PID/名称 | `ss -tp` |
| `-n` | 不解析服务名（显示端口号） | `ss -tn` |
| `-r` | 解析主机名 | `ss -tr` |
| `-i` | 显示 TCP 内部信息 | `ss -ti` |
| `-s` | 显示统计摘要 | `ss -s` |
| `-4` | 只显示 IPv4 | `ss -t4` |
| `-6` | 只显示 IPv6 | `ss -t6` |
| `-m` | 显示套接字内存使用 | `ss -tm` |

## 常用过滤器

| 表达式 | 说明 | 例子 |
|--------|------|------|
| `sport = :端口` | 源端口 | `ss sport = :80` |
| `dport = :端口` | 目标端口 | `ss dport = :80` |
| `state 状态` | TCP 状态 | `ss state established` |
| `state listening` | 监听状态 | `ss -l` |
| `state time-wait` | 等待状态 | `ss state time-wait` |

## TCP 状态说明

| 状态 | 说明 |
|------|------|
| `ESTABLISHED` | 已建立连接 |
| `LISTEN` | 监听中 |
| `TIME-WAIT` | 等待关闭 |
| `CLOSE-WAIT` | 等待本地关闭 |
| `SYN-SENT` | 发送 SYN |
| `SYN-RECV` | 收到 SYN |

## 常见问题

### 1. ss 和 netstat 有什么区别？

| 特性 | ss | netstat |
|------|-----|---------|
| 速度 | 快 | 慢 |
| 信息量 | 更详细 | 基础 |
| 推荐度 | 推荐 | 过时 |

### 2. 如何查看占用端口的进程？

```bash
# 查看 8080 端口被谁占用
ss -tlnp | grep :8080

# 或使用 lsof
lsof -i :8080

# 或使用 fuser
fuser 8080/tcp
```

### 3. 如何查看连接数统计？

```bash
# 统计当前连接数
ss -t | wc -l

# 统计各状态连接数
ss -t state established | wc -l
ss -t state time-wait | wc -l

# 查看所有状态统计
ss -s
```

## 快捷别名

```bash
alias ss-tcp='ss -t'
alias ss-udp='ss -u'
alias ss-list='ss -l'
alias ss-all='ss -tul'
alias ss-proc='ss -tp'
alias ss-port='ss -tlnp | grep'
```

## 一句话总结

ss 核心：`ss -t` 看 TCP，`ss -l` 看监听，`ss -tp` 显示进程，`ss -s` 看统计。替代 netstat，更快更好用。查端口占用用 `ss -tlnp | grep :端口`。
