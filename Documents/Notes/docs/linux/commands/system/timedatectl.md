# timedatectl - 系统时间管理

## 一句话理解

timedatectl 查询和修改系统时间、日期、时区，并配置 NTP 自动同步。

```bash
# 查看当前时间/日期设置
timedatectl status

# 设置时区
sudo timedatectl set-timezone Asia/Shanghai
```

## 常用场景

### 1. 查看时间和日期状态

```bash
# 查看所有时间设置
timedatectl status

# 输出示例：
#                Local time: Thu 2026-04-09 14:30:45 CST
#            Universal time: Thu 2026-04-09 06:30:45 UTC
#                  RTC time: Thu 2026-04-09 06:30:45
#                 Time zone: Asia/Shanghai (CST, +0800)
# System clock synchronized: yes
#               NTP service: active
#         RTC in local TZ: no
```

### 2. 设置时间和日期

```bash
# 设置日期和时间（格式：YYYY-MM-DD HH:MM:SS）
sudo timedatectl set-time "2026-04-09 15:30:00"

# 只设置日期
sudo timedatectl set-time "2026-04-09"

# 只设置时间
sudo timedatectl set-time "15:30:00"
```

### 3. 设置时区

```bash
# 列出所有可用时区
timedatectl list-timezones

# 过滤时区（如亚洲）
timedatectl list-timezones | grep Asia

# 设置时区
sudo timedatectl set-timezone Asia/Shanghai

# 设置 UTC 时区
sudo timedatectl set-timezone UTC
```

### 4. 配置 NTP 自动同步

```bash
# 查看 NTP 状态
timedatectl status | grep NTP

# 启用 NTP 自动同步
sudo timedatectl set-ntp yes

# 禁用 NTP
sudo timedatectl set-ntp no

# 手动同步（需要启用 NTP）
sudo systemctl restart systemd-timesyncd
```

### 5. 硬件时钟（RTC）设置

```bash
# 查看 RTC 是否使用本地时间
timedatectl status | grep "RTC in local TZ"

# 设置 RTC 使用本地时间（双系统时有用）
sudo timedatectl set-local-rtc 1

# 设置 RTC 使用 UTC（推荐）
sudo timedatectl set-local-rtc 0
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `status` | 显示当前状态 | `timedatectl status` |
| `set-time` | 设置时间/日期 | `sudo timedatectl set-time "2026-04-09 15:30:00"` |
| `set-timezone` | 设置时区 | `sudo timedatectl set-timezone Asia/Shanghai` |
| `set-ntp` | 启用/禁用 NTP | `sudo timedatectl set-ntp yes` |
| `set-local-rtc` | RTC 使用本地时间 | `sudo timedatectl set-local-rtc 1` |
| `list-timezones` | 列出所有时区 | `timedatectl list-timezones` |

## 常见问题

### 1. 双系统时间不对怎么办？

Windows 默认使用本地时间，Linux 默认使用 UTC。在 Linux 中设置 RTC 为本地时间：

```bash
sudo timedatectl set-local-rtc 1
```

### 2. NTP 不同步怎么办？

```bash
# 检查 NTP 服务状态
sudo systemctl status systemd-timesyncd

# 启动 NTP 服务
sudo systemctl start systemd-timesyncd

# 手动同步
sudo timedatectl set-ntp yes
sudo systemctl restart systemd-timesyncd

# 查看同步状态
timedatectl status
```

### 3. 如何强制同步时间？

```bash
# 使用 ntpdate（需要安装）
sudo pacman -S ntp
sudo ntpdate pool.ntp.org

# 使用 timedatectl
sudo timedatectl set-ntp yes
sudo systemctl restart systemd-timesyncd
```

### 4. 如何查看时间同步源？

```bash
# 查看 systemd-timesyncd 状态
timedatectl show-timesync

# 查看同步日志
journalctl -u systemd-timesyncd -n 20
```

## 时区参考

| 时区 | 说明 |
|------|------|
| `Asia/Shanghai` | 中国标准时间（CST） |
| `Asia/Hong_Kong` | 香港时间 |
| `Asia/Taipei` | 台北时间 |
| `Asia/Tokyo` | 日本时间 |
| `America/New_York` | 美国东部时间 |
| `Europe/London` | 伦敦时间 |
| `UTC` | 协调世界时 |

## 快捷别名

```bash
alias time-now='timedatectl status'
alias time-set='sudo timedatectl set-time'
alias timezone-list='timedatectl list-timezones | grep'
alias timezone-set='sudo timedatectl set-timezone'
alias time-ntp-on='sudo timedatectl set-ntp yes'
alias time-ntp-off='sudo timedatectl set-ntp no'
```

## 一句话总结

timedatectl 核心：`timedatectl status` 查看时间，`sudo timedatectl set-timezone Asia/Shanghai` 设时区，`sudo timedatectl set-ntp yes` 开启自动同步。双系统时间不对用 `sudo timedatectl set-local-rtc 1`。NTP 不工作时检查 `systemd-timesyncd` 服务。
