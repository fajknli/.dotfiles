# wpa_cli - WPA 命令行客户端

## 一句话理解

wpa_cli 是 wpa_supplicant 的命令行客户端，用于手动管理 WiFi 连接。iwd 流行之前，这是连接 WiFi 的传统方式。

```bash
# 进入交互模式
wpa_cli

# 直接执行命令
wpa_cli scan
wpa_cli scan_results
wpa_cli add_network
```

## 前提条件

### 启动 wpa_supplicant 服务

```bash
# Void Linux（你笔记中的方式）
sudo ln -s /etc/sv/wpa_supplicant /var/service/

# Arch Linux
sudo systemctl enable --now wpa_supplicant

# 检查状态
sudo systemctl status wpa_supplicant
```

### 查看无线接口

```bash
# 查看网络接口
ip link show

# 常见无线接口名：wlan0、wlp2s0
```

## 交互模式

```bash
# 进入交互模式
sudo wpa_cli

# 交互模式下的命令
> scan
> scan_results
> add_network
> set_network 0 ssid "MyWiFi"
> set_network 0 psk "password"
> enable_network 0
> save_config
> quit
```

## 常用命令

### 扫描网络

```bash
# 触发扫描
sudo wpa_cli scan

# 查看扫描结果
sudo wpa_cli scan_results

# 输出示例
# bssid / frequency / signal level / flags / ssid
# 74:4c:a1:81:39:97 2462 -45 [WPA2-PSK-CCMP][ESS] MyWiFi
# 00:11:22:33:44:55 2412 -70 [WPA2-PSK-CCMP][ESS] AnotherNet
```

### 连接网络

```bash
# 1. 添加网络（返回网络ID，通常是0）
sudo wpa_cli add_network

# 2. 设置 SSID
sudo wpa_cli set_network 0 ssid '"MyWiFi"'

# 3. 设置密码（PSK）
sudo wpa_cli set_network 0 psk '"password"'

# 4. 启用网络
sudo wpa_cli enable_network 0

# 5. 保存配置
sudo wpa_cli save_config

# 6. 断开当前连接
sudo wpa_cli disconnect

# 7. 重新连接
sudo wpa_cli reconnect
```

### 开放网络（无密码）

```bash
# 对于开放网络，设置 key_mgmt 为 NONE
sudo wpa_cli set_network 0 key_mgmt NONE
sudo wpa_cli enable_network 0
```

### 查看状态

```bash
# 当前连接状态
sudo wpa_cli status

# 输出示例
# bssid=74:4c:a1:81:39:97
# freq=2462
# ssid=MyWiFi
# id=0
# mode=station
# pairwise_cipher=CCMP
# group_cipher=CCMP
# key_mgmt=WPA2-PSK
# wpa_state=COMPLETED
# ip_address=192.168.1.100
```

### 管理网络

```bash
# 列出所有网络
sudo wpa_cli list_networks

# 禁用网络
sudo wpa_cli disable_network 0

# 删除网络
sudo wpa_cli remove_network 0

# 选择网络（先禁用其他）
sudo wpa_cli select_network 0
```

## 配置文件方式

### wpa_passphrase 生成配置

```bash
# 生成加密密码
wpa_passphrase "MyWiFi" "password" | sudo tee /etc/wpa_supplicant/wpa_supplicant.conf

# 输出示例
# network={
#     ssid="MyWiFi"
#     #psk="password"
#     psk=4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6
# }
```

### 手动编辑配置

```bash
# /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=/run/wpa_supplicant
update_config=1

network={
    ssid="MyWiFi"
    psk="password"
}

network={
    ssid="PublicWiFi"
    key_mgmt=NONE
}

network={
    ssid="HiddenNet"
    scan_ssid=1
    psk="password"
}
```

### 使用配置文件连接

```bash
# 用配置文件启动
sudo wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf -B

# -B：后台运行
# -i：指定接口
# -c：指定配置文件
```

## 获取 IP 地址

连接 WiFi 后，需要获取 IP 地址：

```bash
# 使用 dhcpcd
sudo dhcpcd wlan0

# 使用 dhclient
sudo dhclient wlan0

# 手动配置（如果有静态 IP）
sudo ip addr add 192.168.1.100/24 dev wlan0
sudo ip route add default via 192.168.1.1
```

## 完整连接流程

```bash
# 1. 确保 wpa_supplicant 运行
sudo systemctl start wpa_supplicant

# 2. 扫描网络
sudo wpa_cli scan
sudo wpa_cli scan_results

# 3. 创建并配置网络
sudo wpa_cli add_network
sudo wpa_cli set_network 0 ssid '"MyWiFi"'
sudo wpa_cli set_network 0 psk '"password"'
sudo wpa_cli enable_network 0

# 4. 获取 IP
sudo dhcpcd wlan0

# 5. 验证
ping 8.8.8.8
```

## 调试命令

```bash
# 查看 wpa_supplicant 日志
sudo journalctl -u wpa_supplicant -f

# 增加日志级别
sudo wpa_cli log_level DEBUG

# 查看 BSS 详细信息
sudo wpa_cli bss 0

# 查看信号强度
sudo wpa_cli signal_poll
```

## 常见问题

### 1. 连接失败

```bash
# 检查密码是否正确
# 检查是否支持加密类型
sudo wpa_cli scan_results
# 查看 flags 列，确认加密类型

# 重新配置
sudo wpa_cli remove_network 0
# 重新添加
```

### 2. 无法获取 IP

```bash
# 手动释放续租
sudo dhcpcd -k wlan0
sudo dhcpcd wlan0

# 检查 DHCP 客户端
sudo systemctl status dhcpcd
```

### 3. 网卡未开启

```bash
# 开启网卡
sudo ip link set wlan0 up

# 检查射频开关
rfkill list
sudo rfkill unblock wifi
```

## 交互模式命令速查

| 命令 | 说明 |
|------|------|
| `scan` | 扫描网络 |
| `scan_results` | 显示扫描结果 |
| `add_network` | 添加网络（返回ID） |
| `set_network <id> ssid "SSID"` | 设置 SSID |
| `set_network <id> psk "PWD"` | 设置密码 |
| `set_network <id> key_mgmt NONE` | 开放网络 |
| `enable_network <id>` | 启用网络 |
| `disable_network <id>` | 禁用网络 |
| `remove_network <id>` | 删除网络 |
| `list_networks` | 列出所有网络 |
| `select_network <id>` | 切换网络 |
| `status` | 查看状态 |
| `save_config` | 保存配置 |
| `disconnect` | 断开连接 |
| `reconnect` | 重新连接 |
| `quit` | 退出 |

## 与 iwctl 对比

| 特性 | wpa_cli | iwctl |
|------|---------|-------|
| 依赖 | wpa_supplicant | iwd |
| 配置方式 | 配置文件 + 命令行 | 命令行为主 |
| 学习曲线 | 较陡 | 较平缓 |
| 交互模式 | 有 | 有 |
| 现代发行版 | 传统 | 新兴 |

## 一句话总结

wpa_cli 核心：`scan` 扫描，`scan_results` 看结果，`add_network` 添加网络，`set_network 0 ssid "SSID"` 设置名称，`set_network 0 psk "密码"` 设密码，`enable_network 0` 连接，`save_config` 保存，`quit` 退出。最后用 `dhcpcd wlan0` 获取 IP。
