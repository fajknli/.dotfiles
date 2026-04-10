# iwd - iNet Wireless Daemon

## 一句话理解

iwd 是一个轻量级无线网络管理工具，替代 wpa_supplicant。其命令行工具 `iwctl` 用于管理 WiFi 连接。

```bash
# 进入交互模式
iwctl

# 直接执行命令
iwctl station wlan0 scan
iwctl station wlan0 get-networks
iwctl station wlan0 connect "SSID"
```

## 安装与配置

### 安装

```bash
# Arch Linux
sudo pacman -S iwd

# 启用服务（需先禁用 wpa_supplicant）
sudo systemctl disable wpa_supplicant
sudo systemctl enable --now iwd
```

### 基本配置（/etc/iwd/main.conf）

```ini
[General]
# 启用内置 DHCP 客户端
EnableNetworkConfiguration=true

[Network]
# 启用 IPv6
EnableIPv6=true

[Settings]
# 自动连接已知网络
AutoConnect=true
```

## 设备管理

### 查看设备

```bash
# 列出所有无线设备
iwctl device list

# 查看设备详情
iwctl device show wlan0

# 查看设备状态
iwctl station wlan0 show
```

## WiFi 扫描与连接

### 扫描网络

```bash
# 启动扫描
iwctl station wlan0 scan

# 查看扫描结果
iwctl station wlan0 get-networks

# 输出示例
# ------------------------------------
# Network name                    Security
# ------------------------------------
# MyWiFi                          psk
# PublicWiFi                      open
# HiddenNet                       --   (隐藏)
```

### 连接网络

```bash
# 连接开放网络
iwctl station wlan0 connect "PublicWiFi"

# 连接加密网络（会提示输入密码）
iwctl station wlan0 connect "MyWiFi"

# 连接隐藏网络
iwctl station wlan0 connect-hidden "HiddenNet"

# 连接时指定密码（不推荐，密码会出现在历史中）
iwctl station wlan0 connect "MyWiFi" --passphrase="password"
```

### 断开连接

```bash
# 断开当前连接
iwctl station wlan0 disconnect
```

## 已知网络管理

### 查看已知网络

```bash
# 列出所有已知网络
iwctl known-networks list

# 查看网络详情
iwctl known-networks show "MyWiFi"
```

### 管理已知网络

```bash
# 忘记网络（删除）
iwctl known-networks "MyWiFi" forget

# 设置自动连接
iwctl known-networks "MyWiFi" set-property AutoConnect true

# 修改网络优先级（数值越大越优先）
iwctl known-networks "MyWiFi" set-property Rank 10
```

## 配置持久化

连接过的网络配置保存在 `/var/lib/iwd/` 目录下：

```bash
# 配置文件格式（.psk 或 .open）
/var/lib/iwd/MyWiFi.psk
/var/lib/iwd/PublicWiFi.open
```

### 手动创建配置

```bash
# 创建 PSK 网络配置
sudo cat > /var/lib/iwd/MyWiFi.psk << EOF
[Security]
Passphrase=password

[Settings]
AutoConnect=true
EOF

sudo chmod 600 /var/lib/iwd/MyWiFi.psk
sudo systemctl restart iwd
```

## 网络状态

### 查看连接信息

```bash
# 查看当前连接的详细信息
iwctl station wlan0 show

# 输出示例
# ------------------------------------
# Property              Value
# ------------------------------------
# Scanning              no
# State                 connected
# Connected network     MyWiFi
# IPv4 address          192.168.1.100
# IPv6 address          fe80::...
# Security              WPA2-Personal
# RSSI                  -45 dBm
# Frequency             2412 MHz
```

### 查看 IP 地址

```bash
# 如果 iwd 未启用 DHCP，需要用其他工具获取 IP
# 使用 dhcpcd
sudo dhcpcd wlan0

# 或使用 systemd-networkd
sudo systemctl enable --now systemd-networkd
```

## 常用命令

| 命令 | 说明 |
|------|------|
| `iwctl device list` | 列出无线设备 |
| `iwctl device show wlan0` | 设备详情 |
| `iwctl station wlan0 scan` | 扫描 WiFi |
| `iwctl station wlan0 get-networks` | 显示扫描结果 |
| `iwctl station wlan0 connect "SSID"` | 连接网络 |
| `iwctl station wlan0 connect-hidden "SSID"` | 连接隐藏网络 |
| `iwctl station wlan0 disconnect` | 断开连接 |
| `iwctl station wlan0 show` | 连接状态 |
| `iwctl known-networks list` | 已知网络列表 |
| `iwctl known-networks "SSID" forget` | 忘记网络 |

## 故障排查

### 1. 扫描不到网络

```bash
# 检查设备是否开启
iwctl device show wlan0 | grep Powered
# Powered: on

# 手动开启
iwctl device wlan0 set-property Powered on

# 检查射频开关
rfkill list
sudo rfkill unblock wifi
```

### 2. 连接成功但无网络

iwd 默认不启用 DHCP，需要额外配置：

```bash
# 方法1：启用 iwd 内置 DHCP
sudo sed -i 's/#EnableNetworkConfiguration=false/EnableNetworkConfiguration=true/' /etc/iwd/main.conf
sudo systemctl restart iwd

# 方法2：使用 dhcpcd
sudo pacman -S dhcpcd
sudo systemctl enable --now dhcpcd

# 方法3：使用 systemd-networkd
sudo systemctl enable --now systemd-networkd
```

### 3. DNS 解析问题

```bash
# 检查 resolv.conf
cat /etc/resolv.conf

# 如果没有 DNS，手动设置
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

### 4. 与 NetworkManager 冲突

```bash
# 使用 NetworkManager 时，iwd 作为 backend
# 编辑 /etc/NetworkManager/conf.d/wifi-backend.conf
[device]
wifi.backend=iwd

# 重启服务
sudo systemctl restart NetworkManager
```

## 与 wpa_supplicant 对比

| 特性 | iwd | wpa_supplicant |
|------|-----|----------------|
| 配置复杂度 | 简单 | 复杂 |
| 内存占用 | 低 | 高 |
| 启动速度 | 快 | 慢 |
| 命令工具 | iwctl | wpa_cli |
| 配置文件 | /var/lib/iwd/*.psk | /etc/wpa_supplicant/*.conf |
| Arch 默认 | 可选 | 传统 |

## 快捷别名

```bash
# 添加到 .bashrc
alias iw='iwctl'
alias iwscan='iwctl station wlan0 scan && iwctl station wlan0 get-networks'
alias iwconn='iwctl station wlan0 connect'
alias iwdis='iwctl station wlan0 disconnect'
alias iwstatus='iwctl station wlan0 show'
```

## 完整示例

```bash
# 1. 查看设备
iwctl device list
# 确认 wlan0 存在

# 2. 开启设备（如果未开启）
iwctl device wlan0 set-property Powered on

# 3. 扫描网络
iwctl station wlan0 scan
iwctl station wlan0 get-networks

# 4. 连接网络
iwctl station wlan0 connect "MyHomeWiFi"
# 输入密码

# 5. 验证连接
iwctl station wlan0 show
ping -c 3 8.8.8.8

# 6. 设置开机自动连接（默认已开启）
iwctl known-networks list
# MyHomeWiFi 应在列表中

# 7. 断开连接
iwctl station wlan0 disconnect
```

## 一句话总结

iwd 核心：`iwctl device list` 查设备，`iwctl station wlan0 scan` 扫描，`iwctl station wlan0 get-networks` 看结果，`iwctl station wlan0 connect "SSID"` 连接，`iwctl station wlan0 show` 看状态。连接过的网络自动保存到 `/var/lib/iwd/`。
