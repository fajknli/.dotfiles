# nmcli - NetworkManager 命令行工具

## 一句话理解

nmcli 是 NetworkManager 的命令行客户端，用于管理网络连接（WiFi、有线、移动网络等）。

```bash
# 查看网络状态
nmcli device status

# 连接 WiFi
nmcli device wifi connect "SSID" password "密码"

# 查看连接列表
nmcli connection show
```

## 设备管理

### 查看设备状态

```bash
# 查看所有设备
nmcli device status

# 输出示例
# DEVICE  TYPE      STATE         CONNECTION
# wlan0   wifi      connected     MyWiFi
# eth0    ethernet  unavailable   --
# lo      loopback  unmanaged     --
```

| STATE | 说明 |
|-------|------|
| connected | 已连接 |
| disconnecting | 正在断开 |
| disconnected | 已断开 |
| unavailable | 不可用（无硬件或无网络） |
| unmanaged | 未托管（NetworkManager 不管理） |

### 设备操作

```bash
# 连接设备
nmcli device connect wlan0

# 断开设备
nmcli device disconnect wlan0

# 设置设备自动连接
nmcli device set wlan0 autoconnect yes

# 查看设备详细信息
nmcli device show wlan0
```

## WiFi 管理

### 扫描和连接

```bash
# 扫描 WiFi（需要先打开 WiFi）
nmcli device wifi list

# 连接 WiFi（密码）
nmcli device wifi connect "SSID" password "密码"

# 连接 WiFi（隐藏网络）
nmcli device wifi connect "SSID" password "密码" hidden yes

# 连接 WiFi（交互式输入密码）
nmcli device wifi connect "SSID" --ask
```

### WiFi 操作

```bash
# 开启/关闭 WiFi
nmcli radio wifi on
nmcli radio wifi off

# 查看 WiFi 状态
nmcli radio wifi

# 断开当前 WiFi
nmcli device disconnect wlan0
```

## 连接管理

### 查看连接

```bash
# 查看所有连接
nmcli connection show

# 查看活动连接
nmcli connection show --active

# 查看连接详细信息
nmcli connection show "MyWiFi"

# 查看连接 ID、UUID、类型和设备
nmcli connection show --active | awk '{print $1, $2, $3, $4}'
```

### 创建连接

```bash
# 创建 WiFi 连接
nmcli connection add type wifi con-name "MyNetwork" ifname wlan0 ssid "MyWiFi"
nmcli connection modify "MyNetwork" wifi-sec.key-mgmt wpa-psk
nmcli connection modify "MyNetwork" wifi-sec.psk "password"

# 创建以太网连接（DHCP）
nmcli connection add type ethernet con-name "eth0-dhcp" ifname eth0

# 创建以太网连接（静态 IP）
nmcli connection add type ethernet con-name "eth0-static" ifname eth0
nmcli connection modify "eth0-static" ipv4.method manual
nmcli connection modify "eth0-static" ipv4.addresses 192.168.1.100/24
nmcli connection modify "eth0-static" ipv4.gateway 192.168.1.1
nmcli connection modify "eth0-static" ipv4.dns "8.8.8.8 114.114.114.114"
```

### 修改连接

```bash
# 修改密码
nmcli connection modify "MyWiFi" wifi-sec.psk "newpassword"

# 修改为 DHCP
nmcli connection modify "eth0-static" ipv4.method auto

# 修改为静态 IP
nmcli connection modify "eth0-dhcp" ipv4.method manual
nmcli connection modify "eth0-dhcp" ipv4.addresses 192.168.1.100/24

# 设置自动连接
nmcli connection modify "MyWiFi" connection.autoconnect yes

# 设置连接优先级（数字越大越优先）
nmcli connection modify "MyWiFi" connection.autoconnect-priority 10
```

### 连接操作

```bash
# 连接（激活）
nmcli connection up "MyWiFi"

# 断开
nmcli connection down "MyWiFi"

# 删除连接
nmcli connection delete "MyWiFi"

# 重新加载配置
nmcli connection reload
```

## 网络状态

### 一般状态

```bash
# 网络连接状态
nmcli networking

# 开启/关闭网络
nmcli networking on
nmcli networking off

# 查看 NetworkManager 状态
nmcli general status

# 查看主机名
nmcli general hostname

# 设置主机名
sudo nmcli general hostname mypc
```

### 连接性检查

```bash
# 检查网络连通性
nmcli connectivity check

# 返回值
# none: 无连接
# portal: 需要认证（如公共 WiFi）
# limited: 有限连接（仅本地）
# full: 完全连接
```

## 热点共享

```bash
# 创建热点
nmcli device wifi hotspot ifname wlan0 ssid "MyHotspot" password "12345678"

# 创建持久热点连接
nmcli connection add type wifi ifname wlan0 con-name "Hotspot" autoconnect yes
nmcli connection modify "Hotspot" 802-11-wireless.mode ap
nmcli connection modify "Hotspot" 802-11-wireless.band bg
nmcli connection modify "Hotspot" wifi-sec.key-mgmt wpa-psk
nmcli connection modify "Hotspot" wifi-sec.psk "12345678"
nmcli connection modify "Hotspot" ipv4.method shared
nmcli connection up "Hotspot"

# 关闭热点
nmcli connection down "Hotspot"
```

## VPN 管理

```bash
# 导入 VPN 配置
nmcli connection import type openvpn file config.ovpn

# 创建 VPN 连接（手动）
nmcli connection add type vpn con-name "MyVPN" vpn-type openvpn

# 连接 VPN
nmcli connection up "MyVPN"

# 断开 VPN
nmcli connection down "MyVPN"
```

## 常用配置参数

| 参数 | 说明 |
|------|------|
| `ipv4.method` | auto（DHCP）或 manual（静态） |
| `ipv4.addresses` | IP 地址/子网掩码 |
| `ipv4.gateway` | 网关 |
| `ipv4.dns` | DNS 服务器（空格分隔） |
| `ipv6.method` | 同上 |
| `connection.autoconnect` | 是否开机自动连接 |
| `connection.autoconnect-priority` | 优先级 |
| `802-11-wireless.ssid` | WiFi SSID |
| `802-11-wireless.mode` | 模式（client/ap） |
| `wifi-sec.key-mgmt` | 加密方式（wpa-psk/none） |
| `wifi-sec.psk` | WiFi 密码 |

## 实际例子

### 连接手机热点

```bash
# 你笔记中提到的手机热点不稳定问题
# 先关闭电源管理
nmcli connection modify "YourHotspot" wifi.powersave 2

# 重连
nmcli connection down "YourHotspot"
nmcli connection up "YourHotspot"

# 全局关闭 WiFi 电源管理
sudo tee /etc/NetworkManager/conf.d/wifi-powersave.conf <<EOF
[connection]
wifi.powersave = 2
EOF
sudo systemctl restart NetworkManager
```

### 双网卡配置

```bash
# 假设 eth0 是内网，wlan0 是外网
# 设置 eth0 静态 IP（不设网关）
nmcli connection modify "eth0-static" ipv4.addresses 10.0.0.100/24
nmcli connection modify "eth0-static" ipv4.gateway ""

# 设置 wlan0 自动获取
nmcli connection modify "MyWiFi" ipv4.method auto
```

### 连接校园网（需要认证）

```bash
# 连接 WiFi
nmcli device wifi connect "CampusWiFi"

# 可能需要设置特殊参数
nmcli connection modify "CampusWiFi" 802-11-wireless-security.key-mgmt wpa-eap
nmcli connection modify "CampusWiFi" 802-1x.eap peap
nmcli connection modify "CampusWiFi" 802-1x.identity "username"
nmcli connection modify "CampusWiFi" 802-1x.password "password"

# 重新连接
nmcli connection down "CampusWiFi"
nmcli connection up "CampusWiFi"
```

## 命令速查

| 目的 | 命令 |
|------|------|
| 查看设备状态 | `nmcli device status` |
| 扫描 WiFi | `nmcli device wifi list` |
| 连接 WiFi | `nmcli device wifi connect "SSID" password "PWD"` |
| 断开设备 | `nmcli device disconnect wlan0` |
| 查看连接 | `nmcli connection show` |
| 连接 | `nmcli connection up "name"` |
| 断开 | `nmcli connection down "name"` |
| 删除 | `nmcli connection delete "name"` |
| 开启 WiFi | `nmcli radio wifi on` |
| 关闭 WiFi | `nmcli radio wifi off` |
| 网络状态 | `nmcli networking status` |
| 重启网络 | `nmcli networking off && nmcli networking on` |

## 快捷别名

```bash
# 添加到 .bashrc
alias nm='nmcli'
alias nmd='nmcli device'
alias nmc='nmcli connection'
alias nmw='nmcli device wifi'

# 使用
nmw list
nmc up MyWiFi
nmd status
```

## 一句话总结

nmcli 核心：`nmcli device status` 看设备，`nmcli device wifi list` 扫 WiFi，`nmcli device wifi connect "SSID" password "密码"` 连接，`nmcli connection show` 看连接列表，`nmcli connection up/down` 激活/关闭。`nmcli radio wifi on/off` 开关 WiFi。
