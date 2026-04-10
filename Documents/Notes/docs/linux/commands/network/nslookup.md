# nslookup - DNS 查询工具

## 一句话理解

nslookup 用于查询 DNS 域名服务器，获取域名的 IP 地址、MX 记录、NS 记录等信息。

```bash
# 查询域名的 A 记录（IP 地址）
nslookup google.com

# 查询指定 DNS 服务器
nslookup google.com 8.8.8.8
```

## 常用场景

### 1. 查询域名的 A 记录（IP 地址）

```bash
# 基本查询
nslookup google.com

# 输出示例：
# Server:         127.0.0.53
# Address:        127.0.0.53#53
# 
# Non-authoritative answer:
# Name:   google.com
# Address: 142.250.185.46
```

### 2. 使用指定 DNS 服务器查询

```bash
# 使用阿里 DNS
nslookup google.com 223.5.5.5

# 使用谷歌 DNS
nslookup google.com 8.8.8.8

# 使用 Cloudflare DNS
nslookup google.com 1.1.1.1
```

### 3. 查询 MX 记录（邮件服务器）

```bash
# 进入交互模式
nslookup
> set type=MX
> google.com

# 或一行命令
nslookup -type=MX google.com
```

### 4. 查询 NS 记录（域名服务器）

```bash
# 查询 NS 记录
nslookup -type=NS google.com

# 查询 TXT 记录（SPF 等）
nslookup -type=TXT google.com
```

### 5. 反向查询（IP 查域名）

```bash
# 根据 IP 查找域名
nslookup 8.8.8.8

# 输出示例：
# 8.8.8.8.in-addr.arpa   name = dns.google.
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-type=A` | 查询 A 记录（IPv4） | `nslookup -type=A google.com` |
| `-type=AAAA` | 查询 AAAA 记录（IPv6） | `nslookup -type=AAAA google.com` |
| `-type=MX` | 查询 MX 记录 | `nslookup -type=MX google.com` |
| `-type=NS` | 查询 NS 记录 | `nslookup -type=NS google.com` |
| `-type=CNAME` | 查询 CNAME 记录 | `nslookup -type=CNAME google.com` |
| `-type=TXT` | 查询 TXT 记录 | `nslookup -type=TXT google.com` |
| `-type=ANY` | 查询所有记录 | `nslookup -type=ANY google.com` |
| `-port` | 指定 DNS 端口 | `nslookup -port=53 google.com` |
| `-timeout` | 超时时间 | `nslookup -timeout=5 google.com` |
| `-retry` | 重试次数 | `nslookup -retry=3 google.com` |

## 交互模式常用命令

```bash
# 进入交互模式
nslookup

# 设置查询类型
> set type=MX

# 设置 DNS 服务器
> server 8.8.8.8

# 查询域名
> google.com

# 退出
> exit
```

## 记录类型说明

| 类型 | 说明 |
|------|------|
| A | IPv4 地址 |
| AAAA | IPv6 地址 |
| MX | 邮件交换记录 |
| NS | 域名服务器 |
| CNAME | 别名记录 |
| TXT | 文本记录（SPF、验证等） |
| PTR | 反向记录（IP → 域名） |
| SOA | 权威记录 |

## 常见问题

### 1. nslookup 和 dig 有什么区别？

| 工具 | 特点 |
|------|------|
| `nslookup` | 简单易用，交互模式方便 |
| `dig` | 功能更强，输出更详细 |

```bash
# dig 输出更详细
dig google.com
```

### 2. 查询结果中的 "Non-authoritative answer" 是什么意思？

表示答案来自缓存 DNS 服务器，不是权威 DNS 服务器。

- 权威回答：直接来自域名所有者 DNS
- 非权威回答：来自缓存（通常更快但可能不是最新）

### 3. DNS 解析慢怎么办？

```bash
# 测试不同 DNS 服务器
time nslookup google.com 8.8.8.8
time nslookup google.com 223.5.5.5

# 检查本地 DNS 缓存
sudo systemd-resolve --statistics

# 清空 DNS 缓存
sudo systemd-resolve --flush-caches
```

## 快捷别名

```bash
alias nslookup-google='nslookup google.com'
alias nslookup-mx='nslookup -type=MX'
alias nslookup-ns='nslookup -type=NS'
alias nslookup-all='nslookup -type=ANY'
```

## 一句话总结

nslookup 核心：`nslookup google.com` 查 IP，`nslookup -type=MX google.com` 查邮件服务器，`nslookup google.com 8.8.8.8` 用指定 DNS。交互模式 `set type=MX` 切换记录类型。更详细输出用 `dig`。
