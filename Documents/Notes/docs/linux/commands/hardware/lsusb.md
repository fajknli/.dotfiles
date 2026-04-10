# lsusb - 查看USB设备

## 一句话理解

lsusb 列出系统中的所有 USB 设备，包括键盘、鼠标、U盘、摄像头等。

```bash
# 查看所有 USB 设备
lsusb

# 查看详细信息
lsusb -v
```

## 常用场景

### 1. 查看所有 USB 设备

```bash
# 基本列出
lsusb

# 输出示例：
# Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
# Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
# Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
# Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
# Bus 001 Device 003: ID 046d:c077 Logitech, Inc. M105 Optical Mouse
# Bus 001 Device 004: ID 04d9:1702 Holtek Semiconductor, Inc. Keyboard
```

### 2. 查看 USB 设备详细信息

```bash
# 查看所有设备详细信息
lsusb -v

# 查看指定设备详细信息
lsusb -s 001:003 -v

# 查看指定厂商/设备详细信息
lsusb -d 046d:c077 -v
```

### 3. 查看 USB 设备树

```bash
# 树形显示 USB 设备
lsusb -t

# 输出示例：
# /:  Bus 03.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/2p, 5000M
# /:  Bus 02.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/2p, 480M
# /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
#     |__ Port 1: Dev 2, If 0, Class=Hub, Driver=hub/2p, 480M
#         |__ Port 1: Dev 3, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
#         |__ Port 2: Dev 4, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
```

### 4. 查看 USB 设备列表（简洁）

```bash
# 只显示设备 ID 和名称
lsusb | awk -F': ' '{print $2}'

# 只显示设备名称
lsusb | cut -d' ' -f6-

# 显示 USB 设备总数
lsusb | wc -l
```

### 5. 监控 USB 设备插拔

```bash
# 实时监控 USB 事件
sudo udevadm monitor --environment --udev -s usb

# 查看最近 USB 插拔日志
dmesg | grep -i usb | tail -20

# 使用 lsusb 循环监控
while true; do clear; lsusb; sleep 1; done
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-v` | 显示详细信息 | `lsusb -v` |
| `-t` | 树形结构显示 | `lsusb -t` |
| `-s [bus]:[dev]` | 指定总线/设备 | `lsusb -s 001:003` |
| `-d [vendor]:[product]` | 指定厂商/设备 | `lsusb -d 046d:c077` |
| `-V` | 显示版本信息 | `lsusb -V` |

## 设备地址说明

```
Bus 001 Device 003: ID 046d:c077 Logitech, Inc. M105 Optical Mouse
│    │   │        │
│    │   │        └── 厂商/产品 ID
│    │   └────────── 设备号
│    └────────────── 总线号
└─────────────────── 总线
```

## 常见问题

### 1. 如何查看 U 盘挂载点？

```bash
# 1. 插入前后运行 lsusb，找出新设备
lsusb

# 2. 查看块设备
lsblk

# 3. 查看 U 盘挂载位置
df -h | grep media
```

### 2. 如何识别设备厂商？

```bash
# 在线查询 USB ID
# https://linux-usb.org/usb.ids

# 本地查询
grep 046d /usr/share/hwdata/usb.ids

# 更新 USB ID 数据库
sudo update-usbids
```

### 3. 设备不识别怎么办？

```bash
# 查看 USB 错误信息
dmesg | grep -i error | tail -20

# 查看 USB 设备状态
lsusb -t

# 重启 USB 控制器（不推荐）
sudo modprobe -r xhci_hcd && sudo modprobe xhci_hcd
```

### 4. 如何获取设备权限？

```bash
# 查看设备文件权限
ls -la /dev/bus/usb/*/*

# 添加用户到 dialout 组
sudo usermod -aG dialout $USER

# 创建 udev 规则
sudo vim /etc/udev/rules.d/99-usb.rules
# SUBSYSTEM=="usb", ATTR{idVendor}=="046d", MODE="0666"
```

## 快捷别名

```bash
alias lsusb-t='lsusb -t'
alias lsusb-v='lsusb -v'
alias lsusb-tree='lsusb -t'
alias lsusb-count='lsusb | wc -l'
alias lsusb-monitor='watch -n 1 lsusb'
```

## 相关命令

| 命令 | 说明 |
|------|------|
| `lsusb` | USB 设备 |
| `lspci` | PCI 设备 |
| `lsblk` | 块设备（含 U 盘） |
| `dmesg` | 内核消息（插拔日志） |
| `udevadm` | udev 设备管理 |

## 一句话总结

lsusb 核心：`lsusb` 列出所有 USB 设备，`lsusb -t` 树形显示，`lsusb -v` 详细信息。U 盘不识别时 `dmesg | grep -i usb` 查内核日志。`sudo update-usbids` 更新设备数据库。
