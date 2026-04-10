# dae 代理配置指南

## 一、简介

dae 是一个基于 eBPF 的高性能透明代理工具，支持 TCP/UDP 流量代理，具有低延迟、高吞吐的特点。

## 二、安装

### Arch Linux

```bash
# 从 AUR 安装（通用版）
yay -S dae

# 或安装 AVX2 优化版（x86-64 v3）
yay -S dae-avx2-bin

# 启动服务
sudo systemctl start dae
sudo systemctl enable dae
```

## 三、配置文件结构

```bash
/etc/dae/config.dae          # 主配置文件
/usr/local/share/dae/        # geoip.dat 和 geosite.dat 存放目录
/etc/sysctl.conf             # IP 转发配置
```

## 四、完整配置示例

### 4.1 全局配置

```dae
global {
    # 绑定接口
    wan_interface: auto                    # WAN 接口（本机代理）
    #lan_interface: docker0                # LAN 接口（局域网设备）

    # 日志级别: error, warn, info, debug, trace
    log_level: info

    # 是否允许不安全证书
    allow_insecure: true

    # 自动配置内核参数（ip_forward 等）
    auto_config_kernel_parameter: true

    # 节点延迟差超过此值时切换节点
    check_tolerance: 50ms

    # 禁用等待网络（拉取订阅前）
    disable_waiting_network: false

    # TCP 检查 URL
    tcp_check_url: 'http://cp.cloudflare.com,1.1.1.1,2606:4700:4700::1111'

    # UDP DNS 检查服务器
    udp_check_dns: 'dns.google:53,8.8.8.8,2001:4860:4860::8888'

    # 节点检测间隔
    check_interval: 30s

    # 连接模式: ip, domain, domain+, domain++
    dial_mode: domain

    # 嗅探超时
    sniffing_timeout: 100ms
}
```

### 4.2 订阅配置

```dae
subscription {
    'https://your-subscription-link.com/api/v1/client/subscribe?token=xxx'
    'https://another-link.com/subscribe'
}
```

### 4.3 DNS 配置

```dae
dns {
    upstream {
        alidns: 'udp://dns.alidns.com:53'
        googledns: 'tcp+udp://dns.google:53'
    }
    routing {
        request {
            qtype(https) -> reject
            fallback: alidns
        }
        response {
            upstream(googledns) -> accept
            ip(geoip:private) && !qname(geosite:cn) -> googledns
            fallback: accept
        }
    }
}
```

### 4.4 节点组配置

```dae
group {
    proxy {
        # 节点过滤
        # filter: name(keyword: HK, keyword: SG)

        # 选择策略:
        # random      - 随机选择
        # fixed(0)    - 固定第一个节点
        # min         - 最低延迟
        # min_moving_avg - 移动平均最低延迟（推荐）
        policy: min_moving_avg
    }
}
```

### 4.5 路由规则

```dae
routing {
    # 系统服务直连
    pname(NetworkManager, systemd-resolved, dnsmasq) -> direct

    # 国内 IP 直连
    ip(geoip:cn) -> direct
    dip(geoip:cn) -> direct

    # 组播/广播直连
    dip(224.0.0.0/3, 'ff00::/8') -> direct

    # IPv6 直连（代理不支持时）
    ipversion(6) -> direct

    # UDP 除 DNS/QUIC 外直连
    l4proto(udp) && !dport(53, 443) -> direct

    # 非常用端口直连（避免 BT 走代理）
    !dport(21,23,53,80,123,143,194,443,465,587,853,993,995,998) -> direct

    # 屏蔽广告域名
    domain(ext:'geosite.dat:category-ads') -> block

    # 屏蔽 HTTP/3（消耗资源）
    l4proto(udp) && dport(443) -> block

    # 国内域名直连
    domain(ext:'geosite.dat:cn') -> direct
    domain(ext:'geosite.dat:geolocation-cn') -> direct
    domain(ext:'geosite.dat:china-list') -> direct

    # 国内服务直连
    domain(ext:'geosite.dat:alibaba') -> direct
    domain(ext:'geosite.dat:bilibili') -> direct
    domain(ext:'geosite.dat:tencent') -> direct
    domain(ext:'geosite.dat:zhihu') -> direct
    domain(ext:'geosite.dat:cloudflare-cn') -> direct

    # 特定域名直连
    domain(keyword: 'syncthing.net') -> direct
    domain(keyword: 'tracker') -> direct
    domain(keyword: 'ghproxy') -> direct
    domain(keyword: 'nintendo') -> direct

    # 回退：走代理
    fallback: proxy
}
```

## 五、系统配置

### 5.1 IP 转发（/etc/sysctl.conf）

```bash
net.ipv4.ip_forward = 1
net.ipv6.conf.all.forwarding = 1
```

生效配置：

```bash
sudo sysctl -p
```

### 5.2 geoip.dat / geosite.dat

```bash
# 存放位置
/usr/local/share/dae/geoip.dat
/usr/local/share/dae/geosite.dat

# 下载最新版本
cd /usr/local/share/dae/
sudo curl -L -o geoip.dat https://github.com/daeuniverse/geodata/releases/latest/download/geoip.dat
sudo curl -L -o geosite.dat https://github.com/daeuniverse/geodata/releases/latest/download/geosite.dat
```

## 六、服务管理

```bash
# 启动
sudo systemctl start dae

# 停止
sudo systemctl stop dae

# 重启
sudo systemctl restart dae

# 重载配置
sudo systemctl reload dae

# 开机自启
sudo systemctl enable dae

# 查看状态
sudo systemctl status dae

# 查看日志
sudo journalctl -u dae -f
```

## 七、配置管理脚本

### 7.1 复制配置文件（cp_files_to_dae.sh）

```bash
#!/bin/sh

mkdir -p "$HOME"/.local/share/proxy-files-dae && cd "$HOME"/.local/share/proxy-files-dae || exit 1

# 复制 sysctl.conf
if [ ! -f "/etc/sysctl.conf" ]; then
    sudo cp sysctl.conf /etc/
fi

# 复制 config.dae
if [ ! -d "/etc/dae" ]; then
    sudo mkdir -p /etc/dae/
    sudo cp config.dae /etc/dae/
fi

# 设置权限为 0640
sudo chmod 0640 /etc/dae/config.dae

# 复制 geoip.dat 和 geosite.dat
if [ ! -d "/usr/local/share/dae" ]; then
    sudo mkdir -p /usr/local/share/dae/
    sudo cp geoip.dat geosite.dat /usr/local/share/dae/
fi
```

### 7.2 拉取配置（pull_dae_config_gitee.sh）

```bash
#!/bin/sh

source "$HOME"/.local/lib/shell/network/determine_cn_network_connectivity.sh

if is_cn_network; then
    rm -rf "$HOME"/.local/share/proxy-files-dae
    git clone https://gitee.com/fajknli/proxy-files-dae.git --depth=1 "$HOME"/.local/share/proxy-files-dae
else
    echo "未连接到网络"
fi
```

### 7.3 启动代理（vA）

```bash
#!/bin/sh

source "$HOME"/.local/lib/shell/network/determine_global_network_connectivity.sh

if [ "$(systemctl is-active dae.service)" = "active" ]; then
    echo "dae 已在运行"
    exit 1
fi

# 拉取并复制配置
if [ -d "$HOME"/.local/share/proxy-files-dae ]; then
    source "$HOME"/.local/lib/shell/proxy/cp_files_to_dae.sh
else
    source "$HOME"/.local/lib/shell/proxy/pull_dae_config_gitee.sh
    source "$HOME"/.local/lib/shell/proxy/cp_files_to_dae.sh
fi

# 启动服务
sudo systemctl enable dae.service
sudo systemctl start dae.service
sudo systemctl reload dae.service

if is_global_network; then
    echo "已连接全球网络"
else
    echo "未连接全球网络"
fi
```

### 7.4 停止代理（novA）

```bash
#!/bin/sh

sudo systemctl stop dae
sudo systemctl disable dae

sudo rm /etc/sysctl.conf
sudo rm -r /etc/dae
sudo rm -r /usr/local/share/dae
```

## 八、内核要求

| 特性 | 最低内核版本 |
|------|-------------|
| 绑定 WAN 接口 | >= 5.17 |
| 绑定 LAN 接口 | >= 5.17 |
| trace 命令 | >= 5.15 |

检查内核版本：

```bash
uname -r
```

检查内核配置：

```bash
zcat /proc/config.gz | grep -E 'CONFIG_(BPF|DEBUG_INFO_BTF|KPROBES)='
```

## 九、常见问题

### 1. 连接不上

```bash
# 检查服务状态
sudo systemctl status dae

# 查看日志
sudo journalctl -u dae -n 50

# 检查 IP 转发
cat /proc/sys/net/ipv4/ip_forward
# 应为 1

# 检查防火墙
sudo iptables -L -n -v | grep -i dae
```

### 2. DNS 污染

确保 DNS 流量经过 dae：

```bash
# 检查 DNS 配置
cat /etc/resolv.conf

# 应设置为本地 DNS（如 127.0.0.1）或直接使用 dae 的 DNS
```

### 3. 节点切换慢

调整检测参数：

```dae
check_interval: 15s      # 缩短检测间隔
check_tolerance: 30ms    # 降低切换阈值
```

## 十、配置优先级

```dae
# 规则从上到下匹配，匹配即停止
routing {
    # 1. 精确匹配优先
    domain(suffix: google.com) -> proxy
    
    # 2. 然后 IP 规则
    dip(8.8.8.8) -> proxy
    
    # 3. 最后是域名规则
    domain(geosite:cn) -> direct
    
    # 4. 回退
    fallback: proxy
}
```

## 十一、一句话总结

dae 核心：`wan_interface: auto` 绑定本机，`subscription` 填入订阅链接，`group` 选择节点策略（推荐 `min_moving_avg`），`routing` 配置分流规则，`fallback: proxy` 让剩余流量走代理。配置后 `sudo systemctl start dae` 启动。
