# last - 查看登录历史记录

## 一句话理解

last 命令显示系统用户登录和注销的历史记录，包括登录时间、持续时间、来源 IP 等。

```bash
# 查看所有登录历史
last

# 查看最近 10 条记录
last -n 10
```

## 常用场景

### 1. 查看登录历史

```bash
# 查看所有登录记录
last

# 查看最近 5 条
last -5

# 查看指定用户的登录历史
last fajknli
```

### 2. 查看重启记录

```bash
# 查看系统重启历史
last reboot

# 输出示例：
# reboot   system boot  6.12.8-arch1-1   Tue Apr  8 10:30   still running
# reboot   system boot  6.12.8-arch1-1   Mon Apr  7 08:15 - 10:30  (2:15)
```

### 3. 查看失败登录尝试

```bash
# 查看失败登录记录
sudo lastb

# 查看最近 10 条失败登录
sudo lastb -10

# 查看特定用户的失败登录
sudo lastb root
```

### 4. 查看指定时间段的登录

```bash
# 查看今天以来的登录
last --since today

# 查看指定日期后的登录
last --since "2026-04-01"

# 查看指定时间段的登录
last --since "2026-04-01" --until "2026-04-08"
```

### 5. 格式化输出

```bash
# 完整时间格式
last -F

# 不显示主机名
last -R

# 不显示域名
last -d

# 显示 IP 地址（不解析域名）
last -i
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-n N` | 显示最近 N 条 | `last -10` |
| `-F` | 显示完整时间 | `last -F` |
| `-R` | 不显示主机名 | `last -R` |
| `-d` | 不显示域名 | `last -d` |
| `-i` | 显示 IP 地址 | `last -i` |
| `-x` | 显示系统关机/运行级别变化 | `last -x` |
| `-t YYYYMMDDHHMMSS` | 显示到指定时间为止 | `last -t 20260408235959` |
| `--since` | 从指定时间开始 | `last --since today` |
| `--until` | 到指定时间为止 | `last --until yesterday` |

## 输出字段说明

| 字段 | 说明 |
|------|------|
| 用户名 | 登录的用户名 |
| 终端 | tty（本地）、pts（远程） |
| 来源 | 登录 IP 或主机名 |
| 登录时间 | 登录日期和时间 |
| 退出时间 | 退出日期和时间（still logged in 表示仍在登录） |
| 持续时间 | 登录持续时长 |

## 常见问题

### 1. 如何清除登录历史？

```bash
# 清空 wtmp 文件（需要 root）
sudo > /var/log/wtmp

# 或使用 logrotate 轮转
sudo logrotate -f /etc/logrotate.d/wtmp
```

### 2. last 和 lastb 有什么区别？

| 命令 | 数据源 | 内容 |
|------|--------|------|
| `last` | `/var/log/wtmp` | 成功登录记录 |
| `lastb` | `/var/log/btmp` | 失败登录记录 |

### 3. 如何监控可疑登录？

```bash
# 查看异常时间登录（如凌晨）
last | grep -E "03:00|04:00|05:00"

# 查看来自国外的登录
last -i | grep -vE "192.168.|10\.|172\.16"

# 持续监控（脚本）
while true; do
    new=$(last -n 1 | head -1)
    echo "$new"
    sleep 10
done
```

## 快捷别名

```bash
alias last10='last -10'
alias last-reboot='last reboot'
alias last-fail='sudo lastb'
alias last-today='last --since today'
alias last-ips='last -i'
```

## 一句话总结

last 核心：`last` 查看登录历史，`last -n 10` 看最近 10 条，`last reboot` 看重启记录，`sudo lastb` 看失败登录。`last -F` 显示完整时间，`last -i` 显示 IP。用于安全审计和故障排查。
