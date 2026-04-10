# lspci - 查看PCI设备

## 一句话理解

lspci 列出系统中的所有 PCI 设备，包括显卡、网卡、声卡、USB控制器等。

```bash
# 查看所有 PCI 设备
lspci

# 查看显卡信息
lspci | grep VGA
```

## 常用场景

### 1. 查看所有 PCI 设备

```bash
# 基本列出
lspci

# 输出示例：
# 00:00.0 Host bridge: Intel Corporation 8th Gen Core Processor Host Bridge
# 00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 620
# 00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller
# 00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio
# 01:00.0 Ethernet controller: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411
```

### 2. 查看显卡信息

```bash
# 查看 VGA 控制器
lspci | grep VGA

# 查看 NVIDIA 显卡（详细）
lspci | grep -i nvidia

# 查看 AMD 显卡
lspci | grep -i amd

# 查看显卡详细信息
lspci -v -s $(lspci | grep VGA | cut -d' ' -f1)
```

### 3. 查看网卡信息

```bash
# 查看以太网卡
lspci | grep Ethernet

# 查看无线网卡
lspci | grep -i network

# 查看网卡详细信息
lspci -v -s $(lspci | grep Ethernet | cut -d' ' -f1)
```

### 4. 查看声卡信息

```bash
# 查看音频设备
lspci | grep Audio

# 查看声卡详细信息
lspci -v -s $(lspci | grep Audio | cut -d' ' -f1)
```

### 5. 查看设备详细信息

```bash
# 显示详细信息
lspci -v

# 显示非常详细信息
lspci -vv

# 显示所有信息（包括内核模块）
lspci -vvv

# 显示设备树
lspci -t
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-v` | 显示详细信息 | `lspci -v` |
| `-vv` | 更详细 | `lspci -vv` |
| `-vvv` | 最详细 | `lspci -vvv` |
| `-n` | 显示数字 ID | `lspci -n` |
| `-nn` | 显示数字和文本 ID | `lspci -nn` |
| `-k` | 显示内核驱动 | `lspci -k` |
| `-t` | 树形结构显示 | `lspci -t` |
| `-s` | 指定设备 | `lspci -s 00:02.0` |
| `-d` | 按厂商/设备过滤 | `lspci -d 10de:` |
| `-m` | 机器可解析格式 | `lspci -m` |

## 设备地址说明

```
00:02.0
│  │ │
│  │ └── 功能号（function）
│  └──── 设备号（device）
└─────── 总线号（bus）
```

## 常见问题

### 1. 如何查看显卡驱动是否加载？

```bash
# 查看显卡和驱动
lspci -k | grep -A 2 VGA

# 输出示例：
# 00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 620
#  Subsystem: Dell Device 080b
#  Kernel driver in use: i915
```

### 2. 如何查看设备使用哪个内核模块？

```bash
# 显示内核模块
lspci -k

# 指定设备
lspci -k -s 00:02.0
```

### 3. 如何查找特定厂商的设备？

```bash
# NVIDIA 设备（厂商 ID 10de）
lspci -d 10de:

# Intel 设备（8086）
lspci -d 8086:

# AMD 设备（1002）
lspci -d 1002:

# 同时指定设备 ID
lspci -d 10de:1b80
```

### 4. 如何更新 PCI ID 数据库？

```bash
# 更新 pci.ids 文件
sudo update-pciids

# 手动下载
sudo wget -O /usr/share/misc/pci.ids https://pci-ids.ucw.cz/v2.2/pci.ids
```

## 快捷别名

```bash
alias lspci-v='lspci -v'
alias lspci-k='lspci -k'
alias lspci-tree='lspci -t'
alias lspci-gpu='lspci | grep -E "VGA|3D|Display"'
alias lspci-net='lspci | grep -E "Ethernet|Network"'
alias lspci-audio='lspci | grep Audio'
```

## 相关命令

| 命令 | 说明 |
|------|------|
| `lspci` | PCI 设备 |
| `lsusb` | USB 设备 |
| `lscpu` | CPU 信息 |
| `lshw` | 全部硬件信息 |
| `dmidecode` | BIOS/主板信息 |

## 一句话总结

lspci 核心：`lspci` 列出所有设备，`lspci | grep VGA` 看显卡，`lspci | grep Ethernet` 看网卡，`lspci -k` 显示驱动，`lspci -t` 树形显示。驱动问题用 `lspci -k` 查内核模块，新硬件用 `sudo update-pciids` 更新数据库。
