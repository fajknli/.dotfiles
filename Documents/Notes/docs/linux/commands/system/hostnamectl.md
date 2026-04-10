# hostnamectl - 主机名管理

## 一句话理解

hostnamectl 查看和修改系统的主机名，支持静态、瞬态和漂亮三种主机名类型。

```bash
# 查看主机名
hostnamectl

# 设置主机名
sudo hostnamectl set-hostname mypc
```

## 常用场景

### 1. 查看主机名信息

```bash
# 查看所有主机名信息
hostnamectl

# 输出示例：
#    Static hostname: archlinux
#    Pretty hostname: My Arch Linux PC
#          Icon name: computer-laptop
#            Chassis: laptop
#         Machine ID: 1234567890abcdef1234567890abcdef
#            Boot ID: abcdef1234567890abcdef1234567890
#     Virtualization: oracle
#   Operating System: Arch Linux
#        CPE OS Name: cpe:/o:archlinux:archlinux:rolling
#             Kernel: Linux 6.12.8-arch1-1
#       Architecture: x86-64
```

### 2. 设置主机名

```bash
# 设置静态主机名
sudo hostnamectl set-hostname arch-pc

# 设置漂亮主机名（包含空格和特殊字符）
sudo hostnamectl set-hostname "My Arch Linux PC" --pretty

# 设置瞬态主机名（临时，重启失效）
sudo hostnamectl set-hostname temp-pc --transient
```

### 3. 查看不同类型的主机名

```bash
# 查看静态主机名
hostnamectl --static

# 查看瞬态主机名
hostnamectl --transient

# 查看漂亮主机名
hostnamectl --pretty
```

### 4. 设置主机名图标和 chassis

```bash
# 设置图标名称
sudo hostnamectl set-icon-name computer-laptop

# 设置设备类型
sudo hostnamectl set-chassis laptop
sudo hostnamectl set-chassis desktop
sudo hostnamectl set-chassis server
sudo hostnamectl set-chassis vm
sudo hostnamectl set-chassis container
```

### 5. 获取纯主机名（脚本用）

```bash
# 获取静态主机名
hostnamectl --static

# 或使用传统命令
hostname

# 获取漂亮主机名
hostnamectl --pretty
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `status` | 显示当前主机名（默认） | `hostnamectl` |
| `set-hostname` | 设置主机名 | `sudo hostnamectl set-hostname name` |
| `--static` | 操作静态主机名 | `hostnamectl --static` |
| `--transient` | 操作瞬态主机名 | `sudo hostnamectl set-hostname name --transient` |
| `--pretty` | 操作漂亮主机名 | `sudo hostnamectl set-hostname "Name" --pretty` |
| `set-icon-name` | 设置图标名称 | `sudo hostnamectl set-icon-name computer` |
| `set-chassis` | 设置设备类型 | `sudo hostnamectl set-chassis laptop` |
| `set-deployment` | 设置部署环境 | `sudo hostnamectl set-deployment production` |
| `set-location` | 设置位置 | `sudo hostnamectl set-location "Beijing"` |

## 主机名类型说明

| 类型 | 说明 | 示例 |
|------|------|------|
| 静态 | 永久主机名，保存在 `/etc/hostname` | `arch-pc` |
| 瞬态 | 临时主机名，重启后恢复静态 | `temp-pc` |
| 漂亮 | 显示用，可含空格和特殊字符 | `My Arch Linux` |

## 常见问题

### 1. hostnamectl 和 hostname 有什么区别？

| 命令 | 特点 |
|------|------|
| `hostname` | 传统命令，只显示/设置静态主机名 |
| `hostnamectl` | 现代命令，支持三种主机名类型 |

```bash
# 传统方式
sudo hostname mypc
sudo echo "mypc" > /etc/hostname

# 现代方式（推荐）
sudo hostnamectl set-hostname mypc
```

### 2. 如何让主机名立即生效？

```bash
# 重启 systemd-hostnamed
sudo systemctl restart systemd-hostnamed

# 或重启 shell
exec $SHELL
```

### 3. 如何在 /etc/hosts 中同步主机名？

```bash
# 查看当前 IP
ip addr show

# 编辑 /etc/hosts
sudo vim /etc/hosts

# 添加或修改
127.0.0.1   localhost mypc
::1         localhost mypc
```

### 4. 如何清除漂亮主机名？

```bash
# 设置为空字符串
sudo hostnamectl set-hostname "" --pretty
```

## 快捷别名

```bash
alias hn='hostnamectl'
alias hn-static='hostnamectl --static'
alias hn-pretty='hostnamectl --pretty'
alias hn-set='sudo hostnamectl set-hostname'
```

## 相关文件

| 文件 | 说明 |
|------|------|
| `/etc/hostname` | 静态主机名存储文件 |
| `/etc/machine-info` | 漂亮主机名和图标存储 |
| `/etc/hosts` | 主机名到 IP 的映射 |

## 一句话总结

hostnamectl 核心：`hostnamectl` 查看所有信息，`sudo hostnamectl set-hostname name` 设置主机名，`hostnamectl --pretty` 查看漂亮名称。三种主机名类型：静态（永久）、瞬态（临时）、漂亮（显示用）。比传统 `hostname` 命令更强大。
