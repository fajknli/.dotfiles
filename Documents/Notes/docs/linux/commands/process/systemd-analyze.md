# systemd-analyze - 系统启动分析

## 一句话理解

systemd-analyze 分析系统启动时间，找出哪些服务拖慢了开机速度。

```bash
# 查看启动总耗时
systemd-analyze

# 查看各服务启动耗时
systemd-analyze blame
```

## 常用场景

### 1. 查看启动总时间

```bash
# 查看启动总耗时
systemd-analyze

# 输出示例：
# Startup finished in 2.345s (kernel) + 5.678s (initrd) + 12.345s (userspace) = 20.368s

# 查看固件（BIOS/UEFI）耗时
systemd-analyze firmware

# 查看内核耗时
systemd-analyze kernel
```

### 2. 查看各服务启动耗时

```bash
# 按耗时排序（最慢的在上）
systemd-analyze blame

# 输出示例：
# 5.234s NetworkManager-wait-online.service
# 2.123s docker.service
# 1.456s plymouth-quit-wait.service
# 0.987s systemd-journal-flush.service

# 显示前10个最慢的服务
systemd-analyze blame | head -10
```

### 3. 查看启动依赖关系图

```bash
# 生成启动依赖图（需安装 graphviz）
systemd-analyze dot | dot -Tsvg > boot.svg

# 查看指定单元的依赖
systemd-analyze dot network.target

# 生成文本格式依赖树
systemd-analyze critical-chain
```

### 4. 查看关键启动链

```bash
# 查看导致启动慢的依赖链
systemd-analyze critical-chain

# 输出示例：
# graphical.target @12.345s
# └─multi-user.target @12.345s
#   └─docker.service @10.222s +2.123s
#     └─network-online.target @10.111s
#       └─NetworkManager-wait-online.service @4.877s +5.234s

# 查看特定单元
systemd-analyze critical-chain docker.service
```

### 5. 比较两次启动

```bash
# 保存基准启动数据
systemd-analyze blame > boot1.txt

# 优化后再次保存
systemd-analyze blame > boot2.txt

# 对比差异
diff boot1.txt boot2.txt
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `blame` | 按耗时排序显示服务 | `systemd-analyze blame` |
| `critical-chain` | 显示关键启动链 | `systemd-analyze critical-chain` |
| `dot` | 生成依赖关系图（dot格式） | `systemd-analyze dot` |
| `plot` | 生成启动时间图（SVG） | `systemd-analyze plot > boot.svg` |
| `firmware` | 显示固件启动时间 | `systemd-analyze firmware` |
| `kernel` | 显示内核启动时间 | `systemd-analyze kernel` |
| `initrd` | 显示 initrd 启动时间 | `systemd-analyze initrd` |
| `time` | 显示启动总时间 | `systemd-analyze time` |
| `unit-paths` | 显示单元文件搜索路径 | `systemd-analyze unit-paths` |

## 常用操作速查

| 操作 | 命令 |
|------|------|
| 启动总时间 | `systemd-analyze` |
| 最慢服务 | `systemd-analyze blame` |
| 启动依赖链 | `systemd-analyze critical-chain` |
| 生成 SVG 图 | `systemd-analyze plot > boot.svg` |
| 固件时间 | `systemd-analyze firmware` |
| 内核时间 | `systemd-analyze kernel` |

## 常见问题

### 1. 如何优化启动时间？

```bash
# 1. 找出最慢的服务
systemd-analyze blame | head -10

# 2. 禁用不需要的服务
sudo systemctl disable NetworkManager-wait-online.service

# 3. 延迟启动非关键服务
sudo systemctl edit docker.service
# 添加：
# [Service]
# ExecStartPre=/bin/sleep 10

# 4. 使用 systemd 分析图
systemd-analyze plot > boot.svg
```

### 2. NetworkManager-wait-online.service 很慢怎么办？

```bash
# 检查依赖它的服务
systemctl list-dependencies --after NetworkManager-wait-online.service

# 禁用等待网络（如果不需要）
sudo systemctl mask NetworkManager-wait-online.service

# 或设置超时
sudo mkdir -p /etc/systemd/system/NetworkManager-wait-online.service.d/
echo -e "[Service]\nTimeoutStartSec=10" | sudo tee /etc/systemd/system/NetworkManager-wait-online.service.d/override.conf
```

### 3. 如何查看启动失败的单元？

```bash
# 查看失败的服务
systemctl --failed

# 查看失败服务的日志
journalctl -p 3 -xb
```

### 4. 如何分析容器或 chroot 环境？

```bash
# 指定根目录
systemd-analyze --root=/path/to/root

# 指定镜像
systemd-analyze --image=/path/to/image.raw
```

## 生成启动分析图

```bash
# 安装 graphviz（生成图片用）
sudo pacman -S graphviz

# 生成 SVG 图
systemd-analyze plot > boot.svg

# 生成依赖关系图
systemd-analyze dot | dot -Tsvg > dependencies.svg

# 生成时间线图
systemd-analyze plot --to=15s > boot-15s.svg
```

## 快捷别名

```bash
alias sys-an='systemd-analyze'
alias sys-bl='systemd-analyze blame'
alias sys-cc='systemd-analyze critical-chain'
alias sys-plot='systemd-analyze plot > boot.svg'
```

## 一句话总结

systemd-analyze 核心：`systemd-analyze` 看总时间，`systemd-analyze blame` 找最慢服务，`systemd-analyze critical-chain` 看依赖链。优化启动：禁用不需要的服务，延迟非关键服务。`systemd-analyze plot > boot.svg` 生成可视化分析图。
