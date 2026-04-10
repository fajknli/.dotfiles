# dig - DNS 查询工具

## 一句话理解

dig（Domain Information Groper）是功能强大的 DNS 查询工具，比 nslookup 输出更详细、更灵活。

```bash
# 查询域名的 A 记录
dig google.com

# 只显示结果摘要
dig google.com +short
```

## 常用场景

### 1. 基本 DNS 查询

```bash
# 查询 A 记录（IPv4）
dig google.com

# 只显示 IP 地址
dig google.com +short

# 查询 AAAA 记录（IPv6）
dig google.com AAAA
```

### 2. 查询特定 DNS 服务器

```bash
# 使用谷歌 DNS 查询
dig @8.8.8.8 google.com

# 使用 Cloudflare DNS
dig @1.1.1.1 google.com

# 使用阿里 DNS
dig @223.5.5.5 google.com
```

### 3. 查询各种记录类型

```bash
# MX 记录（邮件服务器）
dig google.com MX

# NS 记录（域名服务器）
dig google.com NS

# TXT 记录（SPF、验证等）
dig google.com TXT

# CNAME 记录（别名）
dig www.google.com CNAME

# ANY 记录（所有类型）
dig google.com ANY
```

### 4. 反向 DNS 查询

```bash
# IP 反查域名
dig -x 8.8.8.8

# 简写
dig 8.8.8.8 +short
```

### 5. 追踪 DNS 解析路径

```bash
# 追踪从根服务器开始的解析路径
dig +trace google.com

# 输出示例：
# .           518400  IN  NS  a.root-servers.net.
# com.        172800  IN  NS  a.gtld-servers.net.
# google.com.  172800  IN  NS  ns1.google.com.
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `@server` | 指定 DNS 服务器 | `dig @8.8.8.8 google.com` |
| `+short` | 只显示结果 | `dig google.com +short` |
| `+trace` | 追踪解析路径 | `dig +trace google.com` |
| `+noall` | 不显示所有 | `dig google.com +noall +answer` |
| `+answer` | 只显示回答部分 | `dig google.com +noall +answer` |
| `+stats` | 显示统计信息 | `dig google.com +stats` |
| `+tcp` | 使用 TCP 协议 | `dig google.com +tcp` |
| `+time=N` | 设置超时（秒） | `dig +time=5 google.com` |
| `+retry=N` | 设置重试次数 | `dig +retry=2 google.com` |
| `-4` | 强制 IPv4 | `dig -4 google.com` |
| `-6` | 强制 IPv6 | `dig -6 google.com` |
| `-p` | 指定端口 | `dig -p 53 google.com` |

## 记录类型速查

| 类型 | 说明 | 查询 |
|------|------|------|
| A | IPv4 地址 | `dig google.com A` |
| AAAA | IPv6 地址 | `dig google.com AAAA` |
| MX | 邮件交换记录 | `dig google.com MX` |
| NS | 域名服务器 | `dig google.com NS` |
| CNAME | 别名记录 | `dig www.google.com CNAME` |
| TXT | 文本记录 | `dig google.com TXT` |
| SOA | 权威记录 | `dig google.com SOA` |
| PTR | 反向记录 | `dig -x 8.8.8.8` |
| ANY | 所有记录 | `dig google.com ANY` |

## 输出说明

```bash
$ dig google.com

; <<>> DiG 9.18.28 <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; QUESTION SECTION:
;google.com.            IN  A

;; ANSWER SECTION:
google.com.     300 IN  A   142.250.185.46

;; Query time: 15 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Thu Apr 09 10:30:00 CST 2026
;; MSG SIZE  rcvd: 55
```

| 部分 | 说明 |
|------|------|
| QUESTION | 查询的问题 |
| ANSWER | 查询结果 |
| AUTHORITY | 权威 DNS 服务器 |
| ADDITIONAL | 附加信息 |
| Query time | 查询耗时 |

## 常见问题

### 1. dig 和 nslookup 有什么区别？

| 工具 | 特点 |
|------|------|
| `dig` | 输出详细，功能强大，适合脚本 |
| `nslookup` | 输出简洁，交互模式友好 |

### 2. 如何只获取 IP 地址？

```bash
# 方法1
dig google.com +short

# 方法2
dig google.com | grep -E '^[a-z0-9]' | awk '{print $5}'

# 方法3
host google.com | awk '{print $4}'
```

### 3. 如何批量查询多个域名？

```bash
# 从文件读取
while read domain; do
    dig +short "$domain"
done < domains.txt

# 一行多个
dig +short google.com github.com reddit.com
```

## 快捷别名

```bash
alias d='dig'
alias dg='dig google.com'
alias ds='dig +short'
alias dt='dig +trace'
alias dmx='dig MX +short'
alias dns='dig NS +short'
```

## 一句话总结

dig 核心：`dig google.com` 完整查询，`dig google.com +short` 只看 IP，`dig @8.8.8.8 google.com` 用指定 DNS，`dig +trace google.com` 追踪解析路径，`dig -x 8.8.8.8` 反向查询。DNS 排错首选工具。
