# crontab - 定时任务

## 一句话理解

crontab 用于配置定时任务，让系统在指定时间自动执行命令或脚本。

```bash
# 编辑当前用户的定时任务
crontab -e

# 查看当前用户的定时任务
crontab -l
```

## 常用场景

### 1. 编辑和管理定时任务

```bash
# 编辑定时任务
crontab -e

# 查看定时任务
crontab -l

# 删除所有定时任务
crontab -r

# 删除前确认
crontab -ri

# 从文件加载任务
crontab tasks.txt
```

### 2. 常用时间示例

```bash
# 每天早上 5 点执行
0 5 * * * /path/to/script.sh

# 每周一早上 8 点
0 8 * * 1 /path/to/script.sh

# 每月1号凌晨 0 点
0 0 1 * * /path/to/script.sh

# 每 15 分钟执行
*/15 * * * * /path/to/script.sh

# 每小时执行一次
0 * * * * /path/to/script.sh
```

### 3. 日志备份示例

```bash
# 每天凌晨 2 点备份日志
0 2 * * * tar -czf /backup/logs-$(date +\%Y\%m\%d).tar.gz /var/log/

# 每周日清理旧日志
0 3 * * 0 find /var/log -name "*.log" -mtime +30 -delete
```

### 4. 系统维护示例

```bash
# 每天更新系统
0 4 * * * pacman -Syu --noconfirm

# 每小时检查磁盘空间
0 * * * * df -h > /tmp/disk_usage

# 每周清理 pacman 缓存
0 5 * * 0 pacman -Sc --noconfirm
```

### 5. 邮件通知

```bash
# 任务输出会发邮件给用户
0 9 * * 1 echo "Weekly report" | mail -s "Report" user@example.com

# 禁用邮件输出（重定向到 /dev/null）
0 9 * * * /path/to/script.sh > /dev/null 2>&1
```

## 时间格式说明

```
* * * * * command
│ │ │ │ │
│ │ │ │ └── 星期几（0-7，0和7都表示周日）
│ │ │ └──── 月份（1-12）
│ │ └────── 日期（1-31）
│ └──────── 小时（0-23）
└────────── 分钟（0-59）
```

### 特殊符号

| 符号 | 说明 | 例子 |
|------|------|------|
| `*` | 任意值 | `* * * * *` 每分钟 |
| `,` | 列举 | `1,15,30 * * * *` 第1、15、30分钟 |
| `-` | 范围 | `1-5 * * * *` 第1到5分钟 |
| `/` | 间隔 | `*/15 * * * *` 每15分钟 |

### 星期几缩写

| 数字 | 英文 | 中文 |
|------|------|------|
| 0或7 | Sun | 周日 |
| 1 | Mon | 周一 |
| 2 | Tue | 周二 |
| 3 | Wed | 周三 |
| 4 | Thu | 周四 |
| 5 | Fri | 周五 |
| 6 | Sat | 周六 |

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-e` | 编辑定时任务 | `crontab -e` |
| `-l` | 查看定时任务 | `crontab -l` |
| `-r` | 删除所有任务 | `crontab -r` |
| `-u user` | 指定用户（需 root） | `sudo crontab -u www-data -e` |
| `-i` | 删除前确认 | `crontab -ri` |

## 常见问题

### 1. 环境变量不同怎么办？

cron 执行时环境变量与终端不同，建议使用绝对路径。

```bash
# 错误（PATH 可能不包含 /usr/local/bin）
0 * * * * mycommand

# 正确（使用绝对路径）
0 * * * * /usr/local/bin/mycommand

# 或在 crontab 开头设置 PATH
PATH=/usr/local/bin:/usr/bin:/bin
0 * * * * mycommand
```

### 2. 任务没有执行怎么办？

```bash
# 查看 cron 日志
sudo journalctl -u cronie
grep CRON /var/log/syslog

# 检查 cron 服务状态
sudo systemctl status cronie

# 测试任务（重定向输出）
* * * * * echo "test" >> /tmp/cron-test.log 2>&1
```

### 3. 如何每 N 秒执行一次？

cron 最小单位是分钟，用 sleep 实现秒级。

```bash
# 每 30 秒（每分钟执行两次）
* * * * * /path/to/script.sh
* * * * * sleep 30 && /path/to/script.sh

# 或使用系统定时器（systemd timer）
```

### 4. 如何防止任务重叠执行？

```bash
# 使用 flock 防止重叠
* * * * * flock -n /tmp/myscript.lock -c /path/to/script.sh

# 使用 pid 文件
0 * * * * [ -f /tmp/script.pid ] && kill -0 $(cat /tmp/script.pid) || /path/to/script.sh
```

## 常用时间模板

| 表达式 | 说明 |
|--------|------|
| `*/5 * * * *` | 每5分钟 |
| `0 * * * *` | 每小时 |
| `0 0 * * *` | 每天凌晨 |
| `0 0 * * 0` | 每周日凌晨 |
| `0 0 1 * *` | 每月1号凌晨 |
| `0 0 1 1 *` | 每年1月1日凌晨 |
| `0 9-17 * * *` | 工作时间每小时 |
| `0 0,12 * * *` | 每天0点和12点 |

## 快捷别名

```bash
alias crontab-e='crontab -e'
alias crontab-l='crontab -l'
alias crontab-r='crontab -r'
alias crontab-log='sudo journalctl -u cronie -f'
```

## 一句话总结

crontab 核心：`crontab -e` 编辑，`crontab -l` 查看。时间格式：分 时 日 月 周。`*` 任意，`*/N` 间隔，`,` 列举，`-` 范围。命令用绝对路径，输出重定向到文件或 `/dev/null`。不执行时检查 cron 服务状态和日志。
