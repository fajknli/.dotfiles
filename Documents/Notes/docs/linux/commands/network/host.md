# host - DNS 查询工具

## 一句话理解

host 是简单的 DNS 查询工具，输出简洁，适合脚本和快速查询。

```bash
# 查询域名的 IP 地址
host google.com

# 指定 DNS 服务器
host google.com 8.8.8.8
```

## 常用场景

### 1. 基本 DNS 查询

```bash
# 查询 A 记录
host google.com

# 输出示例：
# google.com has address 142.250.185.46
# google.com has IPv6 address 2404:6800:4004:80c::200e

# 只查询 IPv4
host -t A google.com

# 只查询 IPv6
host -t AAAA google.com
```

### 2. 查询各种记录类型

```bash
# MX 记录（邮件服务器）
host -t MX google.com

# NS 记录（域名服务器）
host -t NS google.com

# TXT 记录
host -t TXT google.com

# CNAME 记录
host -t CNAME www.google.com
```

### 3. 使用指定 DNS 服务器

```bash
# 使用谷歌 DNS
host google.com 8.8.8.8

# 使用 Cloudflare DNS
host google.com 1.1.1.1

# 使用阿里 DNS
host google.com 223.5.5.5
```

### 4. 反向 DNS 查询

```bash
# IP 反查域名
host 8.8.8.8

# 输出示例：
# 8.8.8.8.in-addr.arpa domain name pointer dns.google.
```

### 5. 详细输出模式

```bash
# 显示详细信息
host -v google.com

# 显示所有记录
host -a google.com
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-t TYPE` | 指定记录类型 | `host -t MX google.com` |
| `-a` | 显示所有记录（同 -v） | `host -a google.com` |
| `-v` | 详细输出 | `host -v google.com` |
| `-C` | 显示 SOA 记录 | `host -C google.com` |
| `-r` | 非递归查询 | `host -r google.com` |
| `-T` | 使用 TCP 协议 | `host -T google.com` |
| `-4` | 只使用 IPv4 | `host -4 google.com` |
| `-6` | 只使用 IPv6 | `host -6 google.com` |
| `-W N` | 设置超时（秒） | `host -W 5 google.com` |
| `-R N` | 设置重试次数 | `host -R 3 google.com` |

## 记录类型速查

| 类型 | 说明 | 查询 |
|------|------|------|
| A | IPv4 地址 | `host -t A google.com` |
| AAAA | IPv6 地址 | `host -t AAAA google.com` |
| MX | 邮件交换记录 | `host -t MX google.com` |
| NS | 域名服务器 | `host -t NS google.com` |
| CNAME | 别名记录 | `host -t CNAME www.google.com` |
| TXT | 文本记录 | `host -t TXT google.com` |
| SOA | 权威记录 | `host -t SOA google.com` |
| PTR | 反向记录 | `host 8.8.8.8` |

## 常见问题

### 1. host、nslookup、dig 有什么区别？

| 工具 | 特点 | 适用场景 |
|------|------|----------|
| `host` | 输出最简洁 | 快速查询、脚本 |
| `nslookup` | 交互模式友好 | 手动交互查询 |
| `dig` | 功能最强大 | 详细分析、排错 |

### 2. 如何在脚本中使用 host？

```bash
#!/bin/bash
# 获取域名 IP
IP=$(host google.com | grep 'has address' | head -1 | awk '{print $4}')
echo "IP: $IP"

# 检查域名是否可解析
if host google.com > /dev/null 2>&1; then
    echo "域名可解析"
fi
```

### 3. 如何批量查询多个域名？

```bash
# 从文件读取
for domain in $(cat domains.txt); do
    echo -n "$domain: "
    host -t A "$domain" | grep 'has address' | awk '{print $4}'
done
```

## 快捷别名

```bash
alias h='host'
alias hmx='host -t MX'
alias hns='host -t NS'
alias htxt='host -t TXT'
alias hshort='host -t A'
```

## 一句话总结

host 核心：`host google.com` 查 IP，`host -t MX google.com` 查邮件服务器，`host google.com 8.8.8.8` 用指定 DNS，`host 8.8.8.8` 反向查询。输出最简洁，适合脚本和快速查询。详细分析用 dig。
