# traceroute - 网络路由追踪

## 一句话理解

traceroute 显示数据包从本机到目标主机经过的每一跳路由器（路由路径）。

```bash
# 追踪到百度的路由路径
traceroute baidu.com

# 不解析主机名（更快）
traceroute -n baidu.com
```

## 常用场景

### 1. 基本路由追踪

```bash
# 追踪到域名
traceroute google.com

# 追踪到 IP 地址
traceroute 8.8.8.8

# 不解析主机名（显示 IP，更快）
traceroute -n google.com
```

### 2. 设置最大跳数

```bash
# 最多追踪 15 跳
traceroute -m 15 google.com

# 最多追踪 30 跳（默认）
traceroute -m 30 google.com
```

### 3. 设置每跳探测包数量

```bash
# 每跳发送 1 个包
traceroute -q 1 google.com

# 每跳发送 3 个包（默认）
traceroute -q 3 google.com
```

### 4. 设置等待超时

```bash
# 每跳等待 2 秒
traceroute -w 2 google.com

# 使用特定端口
traceroute -p 80 google.com
```

### 5. 使用 TCP 或 UDP

```bash
# 使用 TCP SYN（默认）
traceroute -T google.com

# 使用 ICMP ECHO
traceroute -I google.com

# 使用 UDP（传统方式）
traceroute -U google.com
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-n` | 不解析主机名（显示 IP） | `traceroute -n google.com` |
| `-m N` | 最大跳数 | `traceroute -m 20 google.com` |
| `-q N` | 每跳探测包数量 | `traceroute -q 1 google.com` |
| `-w N` | 每跳等待秒数 | `traceroute -w 2 google.com` |
| `-p N` | 目标端口 | `traceroute -p 80 google.com` |
| `-T` | 使用 TCP SYN | `traceroute -T google.com` |
| `-I` | 使用 ICMP ECHO | `traceroute -I google.com` |
| `-U` | 使用 UDP（默认） | `traceroute -U google.com` |
| `-4` | 强制 IPv4 | `traceroute -4 google.com` |
| `-6` | 强制 IPv6 | `traceroute -6 google.com` |

## 输出说明

```bash
$ traceroute -n google.com
traceroute to google.com (142.250.185.46), 30 hops max, 60 byte packets
 1  192.168.1.1    2.123 ms  2.101 ms  2.089 ms
 2  10.0.0.1      10.234 ms 10.198 ms 10.187 ms
 3  172.16.1.1    15.456 ms 15.432 ms 15.401 ms
 4  100.64.0.1    25.678 ms 25.654 ms 25.632 ms
 5  142.250.185.46 30.123 ms 29.987 ms 30.001 ms
```

| 字段 | 说明 |
|------|------|
| 1,2,3... | 跳数（第几跳） |
| IP 地址 | 该跳路由器的 IP |
| 3 个时间 | 3 个探测包的往返时间（ms） |
| `* * *` | 超时（该跳无响应） |

## 常见问题

### 1. 出现 `* * *` 是什么意思？

- 路由器不响应 ICMP/UDP 探测
- 防火墙丢弃了探测包
- 网络拥塞丢包

```bash
# 尝试使用 TCP 模式
traceroute -T google.com

# 减少等待时间
traceroute -w 1 google.com
```

### 2. traceroute 和 mtr 有什么区别？

| 工具 | 特点 |
|------|------|
| `traceroute` | 单次追踪 |
| `mtr` | 实时追踪 + 统计（持续发送） |

```bash
# mtr 更好用
sudo pacman -S mtr
mtr google.com
```

### 3. 如何排查网络延迟问题？

```bash
# 1. 找出延迟高的跳数
traceroute -n google.com

# 2. 持续监控
mtr -n google.com

# 3. 检查 DNS 解析时间
traceroute -n google.com  # 不加 -n 会解析主机名
```

## 快捷别名

```bash
alias trace='traceroute -n'
alias trace-fast='traceroute -n -q 1 -w 1'
alias trace-tcp='traceroute -T -n'
alias trace-mtr='sudo mtr -n'
```

## 一句话总结

traceroute 核心：`traceroute google.com` 追踪路由，`-n` 不解析主机名（更快），`-m` 改最大跳数，`-q 1` 每跳发 1 个包。出现 `* * *` 表示无响应，用 `-T` 换 TCP 模式。持续监控用 `mtr`。定位延迟问题看每跳时间。
