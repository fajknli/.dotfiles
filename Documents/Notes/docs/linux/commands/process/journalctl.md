# journalctl 命令详解

## 一句话理解 journalctl

journalctl 是 systemd 的日志查看工具，用于**查看系统和服务的日志**。所有服务的日志都集中管理，不用去 /var/log 里翻各个文件。

```bash
# 查看所有日志
journalctl

# 查看某个服务的日志
journalctl -u nginx

# 实时跟踪日志
journalctl -f
```

## 最常用场景

### 1. 查看服务日志

```bash
# 查看 nginx 日志
journalctl -u nginx

# 查看最近50行
journalctl -u nginx -n 50

# 查看实时日志（类似 tail -f）
journalctl -u nginx -f

# 查看本次启动以来的日志
journalctl -u nginx -b
```

### 2. 按时间过滤

```bash
# 今天的所有日志
journalctl --since today

# 昨天的日志
journalctl --since yesterday

# 最近1小时
journalctl --since "1 hour ago"

# 指定时间范围
journalctl --since "2026-04-08 10:00:00" --until "2026-04-08 12:00:00"

# 最近30分钟
journalctl --since -30m
```

### 3. 按级别过滤

```bash
# 只看错误级别及以上（err、crit、alert、emerg）
journalctl -p err

# 只看警告及以上
journalctl -p warning

# 级别对照
# 0 emerg（紧急）
# 1 alert（警报）
# 2 crit（严重）
# 3 err（错误）
# 4 warning（警告）
# 5 notice（注意）
# 6 info（信息）
# 7 debug（调试）
```

## 常用参数速查

| 参数 | 说明 | 例子 |
|------|------|------|
| `-u` | 指定服务 | `journalctl -u nginx` |
| `-f` | 实时跟踪 | `journalctl -f` |
| `-n 行数` | 显示最近N行 | `journalctl -n 100` |
| `-b` | 本次启动 | `journalctl -b` |
| `-b -1` | 上次启动 | `journalctl -b -1` |
| `-p` | 按级别过滤 | `journalctl -p err` |
| `-o` | 输出格式 | `journalctl -o json` |
| `-k` | 内核日志 | `journalctl -k` |
| `--since` | 起始时间 | `journalctl --since "1 hour ago"` |
| `--until` | 结束时间 | `journalctl --until "2026-04-08"` |
| `-g` | 正则过滤 | `journalctl -g "error"` |
| `-e` | 跳到最后 | `journalctl -e` |

## 输出格式

```bash
# 默认格式（短格式）
journalctl -o short

# 详细格式（含所有字段）
journalctl -o verbose

# JSON 格式（适合脚本处理）
journalctl -o json

# 带高亮显示
journalctl -o short-full

# 不显示时间戳
journalctl -o cat

# 只显示消息内容
journalctl -o short-monotonic
```

## 实际例子

### 1. 排查服务启动失败

```bash
# 查看服务状态（会显示最后几条日志）
systemctl status nginx

# 查看服务完整日志
journalctl -u nginx -e

# 查看本次启动中该服务的错误
journalctl -u nginx -p err -b

# 查看启动失败时的日志
journalctl -u nginx --since "5 minutes ago"
```

### 2. 系统故障排查

```bash
# 查看内核日志
journalctl -k

# 查看最近的错误日志
journalctl -p err -n 50

# 查看某个时间段的错误
journalctl --since "1 hour ago" -p err

# 查看所有严重级别日志
journalctl -p 2   # crit 及以上
```

### 3. 监控实时日志

```bash
# 实时查看所有日志
journalctl -f

# 实时查看多个服务
journalctl -u nginx -u php-fpm -f

# 实时查看错误日志
journalctl -p err -f
```

### 4. 搜索日志

```bash
# 搜索包含特定关键词
journalctl | grep "Out of memory"

# 使用正则搜索
journalctl -g "failed|error|timeout"

# 搜索某个服务的特定内容
journalctl -u sshd | grep "Failed password"
```

## 日志管理

### 查看磁盘使用

```bash
# 查看日志占用的磁盘空间
journalctl --disk-usage
```

### 清理日志

```bash
# 保留最近2天
sudo journalctl --vacuum-time=2d

# 保留最近500MB
sudo journalctl --vacuum-size=500M

# 保留最近100个文件
sudo journalctl --vacuum-files=100

# 清理归档日志
sudo journalctl --rotate
sudo journalctl --vacuum-time=1d
```

### 日志配置（/etc/systemd/journald.conf）

```ini
# 限制日志最大大小
SystemMaxUse=1G

# 保留多少时间
MaxRetentionSec=30day

# 压缩
Compress=yes

# 存储位置（持久化）
Storage=persistent
```

修改后重启服务：
```bash
sudo systemctl restart systemd-journald
```

## 常用组合速查

| 目的 | 命令 |
|------|------|
| 查看某服务最新日志 | `journalctl -u 服务名 -n 50` |
| 实时监控某服务 | `journalctl -u 服务名 -f` |
| 查看本次启动的错误 | `journalctl -p err -b` |
| 查看上次启动的日志 | `journalctl -b -1` |
| 查看最近1小时日志 | `journalctl --since "1 hour ago"` |
| 查看今天的错误 | `journalctl --since today -p err` |
| 查看内核日志 | `journalctl -k` |
| 查看某服务的全部日志 | `journalctl -u 服务名 -e` |
| 搜索关键词 | `journalctl \| grep 关键词` |
| 导出 JSON | `journalctl -o json` |

## 与 systemctl 配合

```bash
# 服务失败时查看日志
systemctl status nginx
journalctl -u nginx -n 20

# 重启服务并实时查看日志
sudo systemctl restart nginx && journalctl -u nginx -f
```

## 小技巧

### 1. 查看开机耗时

```bash
# 哪个服务启动最慢
systemd-analyze blame

# 查看启动时的日志
journalctl -b | grep "Startup"
```

### 2. 查看特定进程的日志

```bash
# 先找到 PID
ps aux | grep nginx

# 查看该 PID 的日志
journalctl _PID=12345
```

### 3. 查看特定用户的日志

```bash
journalctl _UID=1000
```

### 4. 分页查看（替代 less）

```bash
# 默认已分页，空格翻页，q退出
journalctl -u nginx

# 禁用分页（输出全部）
journalctl -u nginx --no-pager
```

## 快捷命令别名

```bash
# 添加到 .bashrc
alias jc='journalctl'
alias jcu='journalctl -u'
alias jcf='journalctl -f'
alias jcuf='journalctl -u $1 -f'
alias jce='journalctl -p err -b'

# 使用
jcu nginx
jcuf nginx
jce
```

## 一句话总结

journalctl 核心用法：`journalctl -u 服务名` 看指定服务，加 `-f` 实时跟踪，加 `-n 50` 看最近N行，加 `-p err` 只看错误。排查问题时先 `systemctl status` 再看 `journalctl -u 服务名 -e`。
