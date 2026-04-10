# ping - 网络连通性测试

## 一句话理解

ping 命令发送 ICMP 数据包测试与目标主机的网络连通性和延迟。

```bash
# 测试与百度的连通性
ping baidu.com

# 发送 4 个包后停止
ping -c 4 baidu.com
```

## 常用场景

### 1. 测试网络连通性

```bash
# 测试域名
ping google.com

# 测试 IP 地址
ping 8.8.8.8

# 测试本地回环（检查网卡是否正常）
ping 127.0.0.1
```

### 2. 限制发送数量

```bash
# 发送 5 个包后停止
ping -c 5 google.com

# 发送 100 个包（每秒 1 个）
ping -c 100 -i 1 google.com
```

### 3. 设置间隔时间

```bash
# 每 0.5 秒发送一个包
ping -i 0.5 google.com

# 每 2 秒发送一个包
ping -i 2 google.com
```

### 4. 设置超时时间

```bash
# 等待每个回复的超时时间（秒）
ping -W 2 google.com

# 设置整个命令的超时时间
ping -w 10 google.com
```

### 5. 检查丢包率和延迟

```bash
# 发送 100 个包并统计结果
ping -c 100 google.com | tail -1

# 输出示例：
# 100 packets transmitted, 98 received, 2% packet loss, time 99123ms
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-c N` | 发送 N 个包后停止 | `ping -c 4 google.com` |
| `-i N` | 间隔 N 秒发送 | `ping -i 0.5 google.com` |
| `-W N` | 等待回复超时 N 秒 | `ping -W 2 google.com` |
| `-w N` | 整个命令超时 N 秒 | `ping -w 10 google.com` |
| `-s N` | 设置数据包大小（字节） | `ping -s 1400 google.com` |
| `-t N` | 设置 TTL 值 | `ping -t 64 google.com` |
| `-4` | 强制使用 IPv4 | `ping -4 google.com` |
| `-6` | 强制使用 IPv6 | `ping -6 google.com` |
| `-q` | 安静模式（只显示统计） | `ping -c 10 -q google.com` |
| `-f` | 洪水模式（需要 root） | `sudo ping -f google.com` |

## 输出说明

```bash
$ ping google.com
PING google.com (142.250.185.46) 56(84) bytes of data.
64 bytes from 142.250.185.46: icmp_seq=1 ttl=115 time=15.2 ms
64 bytes from 142.250.185.46: icmp_seq=2 ttl=115 time=14.8 ms
64 bytes from 142.250.185.46: icmp_seq=3 ttl=115 time=15.0 ms

--- google.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 14.8/15.0/15.2/0.1 ms
```

| 字段 | 说明 |
|------|------|
| `icmp_seq` | 数据包序号 |
| `ttl` | 生存时间（跳数） |
| `time` | 往返延迟（毫秒） |
| `packet loss` | 丢包率 |
| `rtt min/avg/max/mdev` | 最小/平均/最大/标准差延迟 |

## 常见问题

### 1. ping 不通怎么办？

```bash
# 1. 检查本地网卡
ping 127.0.0.1

# 2. 检查网关
ip route | grep default
ping 192.168.1.1

# 3. 检查 DNS 解析
nslookup google.com

# 4. 检查防火墙
sudo iptables -L
sudo firewall-cmd --list-all
```

### 2. 如何测试特定端口的连通性？

ping 只能测 ICMP，不能测端口。测试端口用：

```bash
# 使用 telnet
telnet google.com 80

# 使用 nc
nc -zv google.com 80

# 使用 nmap
nmap -p 80 google.com
```

### 3. TTL 值代表什么？

| TTL | 说明 |
|-----|------|
| 64 | Linux/Unix 系统 |
| 128 | Windows 系统 |
| 255 | 路由器/交换机 |

每次经过一个路由器 TTL 减 1，初始值减去剩余值就是经过的跳数。

## 快捷别名

```bash
alias ping4='ping -c 4'
alias ping10='ping -c 10'
alias ping-fast='ping -i 0.2'
alias ping-loss='ping -c 100 -q'
```

## 一句话总结

ping 核心：`ping google.com` 测试连通性，`ping -c 4 google.com` 发 4 个包，`ping -i 0.5 google.com` 调间隔。关注丢包率和延迟。不通先 ping 127.0.0.1 测本机。测试端口用 `nc -zv`。
