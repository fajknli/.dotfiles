# systemctl 命令详解

## 一句话理解 systemctl

systemctl 是 systemd 的管理工具，用于**管理系统服务**。启动、停止、重启、开机自启全靠它。

```bash
# 启动服务
sudo systemctl start nginx

# 设置开机自启
sudo systemctl enable nginx

# 查看状态
systemctl status nginx
```

## 最常用场景

### 1. 服务管理

```bash
# 启动服务
sudo systemctl start 服务名

# 停止服务
sudo systemctl stop 服务名

# 重启服务
sudo systemctl restart 服务名

# 重新加载配置（不中断服务）
sudo systemctl reload 服务名

# 查看状态
systemctl status 服务名

# 查看是否运行中
systemctl is-active 服务名

# 查看是否启用
systemctl is-enabled 服务名
```

### 2. 开机自启

```bash
# 启用开机自启
sudo systemctl enable 服务名

# 禁用开机自启
sudo systemctl disable 服务名

# 查看所有开机自启的服务
systemctl list-unit-files --type=service --state=enabled

# 查看失败的服务
systemctl --failed
```

### 3. 服务查询

```bash
# 列出所有服务（含状态）
systemctl list-units --type=service

# 列出所有服务（含未运行的）
systemctl list-units --type=service --all

# 列出所有开机自启的服务
systemctl list-unit-files --type=service --state=enabled

# 按状态过滤
systemctl list-units --type=service --state=running
systemctl list-units --type=service --state=failed
```

## 常用命令速查

| 目的 | 命令 |
|------|------|
| 启动服务 | `sudo systemctl start name` |
| 停止服务 | `sudo systemctl stop name` |
| 重启服务 | `sudo systemctl restart name` |
| 重载配置 | `sudo systemctl reload name` |
| 查看状态 | `systemctl status name` |
| 启用自启 | `sudo systemctl enable name` |
| 禁用自启 | `sudo systemctl disable name` |
| 查看是否运行 | `systemctl is-active name` |
| 查看是否启用 | `systemctl is-enabled name` |
| 查看所有服务 | `systemctl list-units --type=service` |
| 查看失败服务 | `systemctl --failed` |
| 重新加载 systemd | `sudo systemctl daemon-reload` |

## 实际例子

### 1. 日常维护

```bash
# 重启网络服务
sudo systemctl restart NetworkManager

# 重启 SSH
sudo systemctl restart sshd

# 重启 Docker
sudo systemctl restart docker

# 查看 Docker 状态
systemctl status docker
```

### 2. 开机自启管理

```bash
# 启用常用服务
sudo systemctl enable sshd
sudo systemctl enable NetworkManager
sudo systemctl enable docker

# 查看哪些服务会开机自启
systemctl list-unit-files --type=service --state=enabled

# 禁用不必要的服务
sudo systemctl disable bluetooth
sudo systemctl disable cups
```

### 3. 服务故障排查

```bash
# 查看服务状态（含最近日志）
systemctl status nginx

# 查看服务完整日志
sudo journalctl -u nginx

# 查看服务最近日志
sudo journalctl -u nginx -n 50

# 查看实时日志
sudo journalctl -u nginx -f
```

### 4. 管理用户服务（不加 sudo）

```bash
# 用户服务命令（--user）
systemctl --user start 服务名
systemctl --user enable 服务名
systemctl --user status 服务名

# 例子：启动 pipewire
systemctl --user start pipewire
systemctl --user enable pipewire
```

## 服务状态码

| 状态 | 说明 |
|------|------|
| `active (running)` | 正常运行中 |
| `active (exited)` | 执行过一次就退出（正常） |
| `active (waiting)` | 等待中 |
| `inactive` | 未运行 |
| `failed` | 启动失败 |
| `enabled` | 开机自启已启用 |
| `disabled` | 开机自启已禁用 |
| `static` | 无法手动启用，由其他服务触发 |
| `masked` | 被屏蔽，无法启动 |

## 服务文件位置

| 路径 | 说明 |
|------|------|
| `/etc/systemd/system/` | 用户配置的服务（优先级最高） |
| `/usr/lib/systemd/system/` | 系统安装的服务 |
| `/etc/systemd/system/服务名.d/` | 服务配置覆盖目录 |

```bash
# 查看服务文件内容
systemctl cat sshd

# 编辑服务文件（自动创建覆盖配置）
sudo systemctl edit nginx

# 编辑完整服务文件
sudo systemctl edit --full nginx

# 重新加载配置（修改服务文件后执行）
sudo systemctl daemon-reload
```

## 常见问题

### 1. 服务启动失败

```bash
# 查看详细错误
systemctl status 服务名 -l

# 查看日志
journalctl -u 服务名 -e

# 查看最近日志
journalctl -u 服务名 -n 50 --no-pager
```

### 2. 服务被屏蔽

```bash
# 检查是否被屏蔽
systemctl status 服务名
# 显示 masked

# 解除屏蔽
sudo systemctl unmask 服务名
```

### 3. 服务启动太慢

```bash
# 查看启动耗时
systemd-analyze blame

# 查看完整启动链
systemd-analyze critical-chain
```

## 管理系统状态

```bash
# 重启系统
sudo systemctl reboot

# 关机
sudo systemctl poweroff

# 暂停（挂起）
sudo systemctl suspend

# 休眠
sudo systemctl hibernate

# 进入救援模式
sudo systemctl rescue

# 进入紧急模式
sudo systemctl emergency
```

## 管理定时器（替代 cron）

```bash
# 查看所有定时器
systemctl list-timers

# 查看定时器状态
systemctl status 定时器名.timer

# 启动定时器
sudo systemctl start backup.timer

# 启用开机自启
sudo systemctl enable backup.timer
```

## 常用服务名参考

| 服务 | 说明 |
|------|------|
| `sshd` | SSH 服务 |
| `NetworkManager` | 网络管理 |
| `docker` | Docker 容器 |
| `nginx` | Nginx 服务器 |
| `httpd` | Apache 服务器 |
| `mysql` / `mariadb` | MySQL 数据库 |
| `postgresql` | PostgreSQL 数据库 |
| `cron` / `crond` | 定时任务 |
| `firewalld` | 防火墙 |
| `bluetooth` | 蓝牙 |
| `cups` | 打印服务 |

## 快捷命令别名

```bash
# 添加到 .bashrc
alias sc='sudo systemctl'
alias scs='systemctl status'
alias scr='sudo systemctl restart'
alias scst='sudo systemctl start'
alias scsp='sudo systemctl stop'
alias sce='sudo systemctl enable'
alias scd='sudo systemctl disable'

# 使用
scs nginx
scr nginx
sce nginx
```

## 一句话总结

systemctl 记住四个命令：`start`（启动）、`stop`（停止）、`restart`（重启）、`enable`（开机自启）。查看状态用 `status`，看日志用 `journalctl -u 服务名`。
