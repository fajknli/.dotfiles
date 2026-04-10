# uname - 查看系统信息

## 一句话理解

uname（Unix name）显示系统内核、主机名、硬件架构等基本信息。

```bash
# 查看内核名称
uname

# 查看所有系统信息
uname -a
```

## 常用场景

### 1. 查看内核版本

```bash
# 查看内核版本号
uname -r

# 输出示例：6.12.8-arch1-1
```

### 2. 查看系统架构

```bash
# 查看硬件架构
uname -m

# 输出示例：x86_64（64位）、aarch64（ARM）、i686（32位）
```

### 3. 查看所有系统信息

```bash
# 显示所有信息
uname -a

# 输出示例：
# Linux archlinux 6.12.8-arch1-1 #1 SMP PREEMPT_DYNAMIC x86_64 GNU/Linux
# 依次为：内核名称、主机名、内核版本、内核发布日期、硬件架构、操作系统
```

### 4. 查看内核名称和操作系统

```bash
# 查看内核名称
uname -s

# 查看操作系统
uname -o
```

### 5. 查看处理器类型

```bash
# 查看处理器类型
uname -p

# 查看硬件平台
uname -i
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-a` | 显示所有信息 | `uname -a` |
| `-s` | 内核名称 | `uname -s` |
| `-n` | 主机名 | `uname -n` |
| `-r` | 内核版本 | `uname -r` |
| `-v` | 内核版本详细信息 | `uname -v` |
| `-m` | 硬件架构 | `uname -m` |
| `-p` | 处理器类型 | `uname -p` |
| `-i` | 硬件平台 | `uname -i` |
| `-o` | 操作系统 | `uname -o` |

## 输出示例对照

```bash
$ uname -a
Linux archlinux 6.12.8-arch1-1 #1 SMP PREEMPT_DYNAMIC x86_64 GNU/Linux

# 各部分含义：
# Linux        - 内核名称（-s）
# archlinux    - 主机名（-n）
# 6.12.8-arch1-1 - 内核版本（-r）
# #1 SMP...    - 内核版本详情（-v）
# x86_64       - 硬件架构（-m）
# GNU/Linux    - 操作系统（-o）
```

## 常见问题

### 1. 如何判断系统是 32 位还是 64 位？

```bash
uname -m
# x86_64   = 64位
# i386/i686 = 32位
# aarch64   = ARM 64位
# armv7l    = ARM 32位
```

### 2. uname 和 arch 有什么区别？

```bash
# arch 只显示硬件架构（同 uname -m）
arch

# uname 显示更多信息
uname -a
```

### 3. 如何查看发行版信息？

```bash
# uname 不显示发行版信息，需用其他命令
cat /etc/os-release
lsb_release -a   # 需要安装 lsb-release
hostnamectl      # systemd 系统
```

## 快捷别名

```bash
alias kernel='uname -r'
alias arch='uname -m'
alias sysinfo='uname -a'
```

## 一句话总结

uname 核心：`uname -r` 看内核版本，`uname -m` 看架构，`uname -a` 看全部。判断 64 位看 `x86_64`，查看发行版用 `cat /etc/os-release`。
