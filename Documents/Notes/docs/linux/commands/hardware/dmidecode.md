# dmidecode - 硬件信息查看

## 一句话理解

dmidecode 读取系统 DMI（SMBIOS）信息，显示 BIOS、主板、内存、CPU 等硬件详细信息。

```bash
# 查看所有硬件信息
sudo dmidecode

# 查看内存信息
sudo dmidecode -t memory
```

## 常用场景

### 1. 查看 BIOS 信息

```bash
# 查看 BIOS 版本
sudo dmidecode -s bios-version

# 查看 BIOS 发布日期
sudo dmidecode -s bios-release-date

# 查看 BIOS 详细信息
sudo dmidecode -t bios
```

### 2. 查看主板信息

```bash
# 查看主板制造商
sudo dmidecode -s baseboard-manufacturer

# 查看主板型号
sudo dmidecode -s baseboard-product-name

# 查看主板序列号
sudo dmidecode -s baseboard-serial-number

# 查看主板详细信息
sudo dmidecode -t baseboard
```

### 3. 查看内存信息

```bash
# 查看内存总数
sudo dmidecode -t memory | grep Size

# 查看内存类型（DDR3/DDR4）
sudo dmidecode -t memory | grep "Type:"

# 查看内存速度
sudo dmidecode -t memory | grep "Speed"

# 查看内存详细信息
sudo dmidecode -t memory
```

### 4. 查看 CPU 信息

```bash
# 查看 CPU 型号
sudo dmidecode -s processor-version

# 查看 CPU 核心数
sudo dmidecode -t processor | grep "Core Count"

# 查看 CPU 详细信息
sudo dmidecode -t processor
```

### 5. 查看系统信息

```bash
# 查看系统制造商
sudo dmidecode -s system-manufacturer

# 查看系统型号
sudo dmidecode -s system-product-name

# 查看序列号
sudo dmidecode -s system-serial-number

# 查看 UUID
sudo dmidecode -s system-uuid
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-t TYPE` | 按类型显示 | `sudo dmidecode -t memory` |
| `-s KEYWORD` | 按关键字显示 | `sudo dmidecode -s bios-version` |
| `-q` | 安静模式（不显示未解码信息） | `sudo dmidecode -q` |
| `-u` | 显示未解码的原始数据 | `sudo dmidecode -u` |
| `--dump-bin FILE` | 导出二进制数据 | `sudo dmidecode --dump-bin data.bin` |
| `--from-dump FILE` | 从二进制文件读取 | `dmidecode --from-dump data.bin` |

## 类型代码速查

| 类型 | 说明 |
|------|------|
| `0` | BIOS |
| `1` | System |
| `2` | Baseboard（主板） |
| `3` | Chassis |
| `4` | Processor（CPU） |
| `5` | Memory Controller |
| `6` | Memory Module |
| `7` | Cache |
| `8` | Port Connector |
| `9` | System Slots |
| `10` | On Board Devices |
| `11` | OEM Strings |
| `12` | System Configuration Options |
| `13` | BIOS Language |
| `16` | Physical Memory Array |
| `17` | Memory Device |
| `19` | Memory Array Mapped Address |
| `20` | Memory Device Mapped Address |
| `32` | System Boot Information |
| `38` | IPMI Device |
| `41` | Onboard Device |

## 常用关键字速查

| 关键字 | 说明 |
|--------|------|
| `bios-vendor` | BIOS 厂商 |
| `bios-version` | BIOS 版本 |
| `bios-release-date` | BIOS 发布日期 |
| `system-manufacturer` | 系统厂商 |
| `system-product-name` | 系统型号 |
| `system-serial-number` | 系统序列号 |
| `system-uuid` | 系统 UUID |
| `baseboard-manufacturer` | 主板厂商 |
| `baseboard-product-name` | 主板型号 |
| `baseboard-serial-number` | 主板序列号 |
| `processor-manufacturer` | CPU 厂商 |
| `processor-version` | CPU 型号 |
| `processor-frequency` | CPU 频率 |

## 常见问题

### 1. 如何查看内存插槽使用情况？

```bash
sudo dmidecode -t memory | grep -E "Locator|Size|Type|Speed" | grep -v "No Module Installed"
```

### 2. 如何获取内存最大支持容量？

```bash
sudo dmidecode -t memory | grep "Maximum Capacity"
```

### 3. 如何查看系统是否支持虚拟化？

```bash
sudo dmidecode -t processor | grep Virtualization
# VT-x（Intel）或 AMD-V（AMD）
```

### 4. dmidecode 需要 root 权限吗？

需要。普通用户执行会提示 "Permission denied"。

```bash
# 需要 sudo
sudo dmidecode

# 或切换到 root
su -
dmidecode
```

## 快捷别名

```bash
alias dmi='sudo dmidecode'
alias dmi-bios='sudo dmidecode -t bios'
alias dmi-board='sudo dmidecode -t baseboard'
alias dmi-mem='sudo dmidecode -t memory'
alias dmi-cpu='sudo dmidecode -t processor'
alias dmi-system='sudo dmidecode -t system'
```

## 实际脚本示例

```bash
#!/bin/bash
# 收集硬件信息脚本

echo "=== 系统信息 ==="
echo "制造商: $(sudo dmidecode -s system-manufacturer)"
echo "型号: $(sudo dmidecode -s system-product-name)"
echo "序列号: $(sudo dmidecode -s system-serial-number)"

echo -e "\n=== BIOS 信息 ==="
echo "版本: $(sudo dmidecode -s bios-version)"
echo "日期: $(sudo dmidecode -s bios-release-date)"

echo -e "\n=== 主板信息 ==="
echo "制造商: $(sudo dmidecode -s baseboard-manufacturer)"
echo "型号: $(sudo dmidecode -s baseboard-product-name)"

echo -e "\n=== CPU 信息 ==="
echo "型号: $(sudo dmidecode -s processor-version)"

echo -e "\n=== 内存信息 ==="
sudo dmidecode -t memory | grep -E "Size:|Type:|Speed:" | head -6
```

## 一句话总结

dmidecode 核心：`sudo dmidecode -t memory` 看内存，`sudo dmidecode -t bios` 看 BIOS，`sudo dmidecode -s system-product-name` 看型号。需要 root 权限。查内存插槽、最大容量、硬件型号首选工具。
