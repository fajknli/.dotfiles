# ip - 网络配置工具

## 一句话理解

ip 命令是 Linux 现代网络配置工具，替代 ifconfig，用于查看和管理网络接口、IP地址、路由表等。

```bash
# 查看所有网络接口
ip addr

# 查看路由表
ip route
```

## 常用场景

### 1. 查看网络接口信息

```bash
# 查看所有接口（简写）
ip addr
ip a

# 查看指定接口
ip addr show wlan0

# 只看 IPv4 地址
ip -4 addr

# 只看 IPv6 地址
ip -6 addr
```

### 2. 启用/禁用网络接口

```bash
# 启用接口
ip link set wlan0 up

# 禁用接口
ip link set wlan0 down
```

### 3. 添加/删除 IP 地址

```bash
# 添加 IP 地址
ip addr add 192.168.1.100/24 dev wlan0

# 删除 IP 地址
ip addr del 192.168.1.100/24 dev wlan0

# 清空接口所有 IP
ip addr flush dev wlan0
```

### 4. 管理路由表

```bash
# 查看路由表
ip route
ip r

# 添加默认网关
ip route add default via 192.168.1.1

# 添加静态路由
ip route add 10.0.0.0/24 via 192.168.1.2

# 删除路由
ip route del default
ip route del 10.0.0.0/24
```

### 5. 查看邻居表（ARP）

```bash
# 查看 ARP 缓存
ip neigh
ip neighbour

# 添加静态 ARP 条目
ip neigh add 192.168.1.50 lladdr aa:bb:cc:dd:ee:ff dev wlan0

# 删除 ARP 条目
ip neigh del 192.168.1.50 dev wlan0
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-4` | 只显示 IPv4 | `ip -4 addr` |
| `-6` | 只显示 IPv6 | `ip -6 addr` |
| `-s` | 显示统计信息 | `ip -s link` |
| `-c` | 彩色输出 | `ip -c addr` |
| `-br` | 简洁输出 | `ip -br addr` |
| `-j` | JSON 格式输出 | `ip -j addr` |

## 常用子命令速查

| 子命令 | 说明 | 常用操作 |
|--------|------|----------|
| `addr` | IP 地址管理 | `add`、`del`、`show`、`flush` |
| `link` | 网络接口管理 | `set up/down`、`show` |
| `route` | 路由表管理 | `add`、`del`、`show` |
| `neigh` | ARP 邻居管理 | `add`、`del`、`show` |

## 常见问题

### 1. ip 和 ifconfig 有什么区别？

| 特性 | ip | ifconfig |
|------|-----|----------|
| 现代内核 | ✅ 原生支持 | ⚠️ 过时 |
| 显示多种信息 | ✅ 分命令查看 | ❌ 全部堆在一起 |
| 输出格式 | 统一风格 | 混乱 |
| 默认安装 | ✅ 是 | ❌ 需额外安装 |

### 2. 如何永久保存 IP 配置？

ip 命令配置临时生效，重启丢失。永久配置需通过发行版工具：

```bash
# Arch Linux: netctl 或 systemd-networkd
# Debian/Ubuntu: /etc/network/interfaces
# RHEL/Fedora: /etc/sysconfig/network-scripts/
```

### 3. 如何查看网络接口统计？

```bash
# 查看收发数据包统计
ip -s link

# 查看更详细统计
ip -s -s link
```

## 快捷别名

```bash
alias ipa='ip addr'
alias ipl='ip link'
alias ipr='ip route'
alias ipn='ip neigh'
alias ipa4='ip -4 addr'
alias ipa6='ip -6 addr'
alias ips='ip -s link'
```

## 一句话总结

ip 核心：`ip addr` 看 IP，`ip link` 看接口状态，`ip route` 看路由，`ip neigh` 看 ARP。`set up/down` 开关接口，`add/del` 增删 IP 和路由。现代 Linux 网络配置首选。
