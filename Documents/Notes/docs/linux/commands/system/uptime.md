# uptime - 查看系统运行时间

## 一句话理解

uptime 显示系统已经运行了多长时间，以及当前登录用户数和系统负载。

```bash
# 查看系统运行时间
uptime

# 输出示例：
# 10:30:45 up 2 days, 5:32, 3 users, load average: 0.08, 0.03, 0.01
```

## 常用场景

### 1. 查看系统运行时长

```bash
# 基本查看
uptime

# 输出解析：
# 10:30:45     - 当前时间
# up 2 days, 5:32 - 已运行 2 天 5 小时 32 分钟
# 3 users      - 当前登录用户数
# load average - 1/5/15 分钟平均负载
```

### 2. 只查看运行时间

```bash
# 提取运行时间
uptime | awk -F 'up ' '{print $2}' | awk -F ',' '{print $1}'

# 输出示例：2 days, 5:32
```

### 3. 监控负载变化

```bash
# 持续查看（每 2 秒刷新）
watch -n 2 uptime

# 只显示负载
watch -n 2 "uptime | awk -F 'load average:' '{print $2}'"
```

### 4. 检查系统是否需要重启

```bash
# 查看是否有内核更新需要重启
if [ -f /var/run/reboot-required ]; then
    echo "系统需要重启"
fi

# 查看内核版本和运行时间判断
uname -r
uptime
```

### 5. 脚本中判断运行时间

```bash
#!/bin/bash
# 获取运行天数
UPTIME_DAYS=$(uptime | awk -F 'up ' '{print $2}' | awk -F ' day' '{print $1}')

if [ -n "$UPTIME_DAYS" ] && [ "$UPTIME_DAYS" -gt 30 ]; then
    echo "系统已运行超过 30 天，建议重启"
fi
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-p` | 更漂亮的输出格式 | `uptime -p` |
| `-s` | 显示系统启动时间 | `uptime -s` |
| `-h` | 帮助 | `uptime -h` |
| `-V` | 显示版本 | `uptime -V` |

## 负载含义

| 负载值 | 含义 |
|--------|------|
| 小于 1.0 | CPU 空闲 |
| 等于 1.0 | CPU 满载 |
| 大于 1.0 | CPU 过载（等待队列） |

**注意**：多核 CPU 负载值需要乘以核心数。4 核 CPU 负载 4.0 才是满载。

```bash
# 查看 CPU 核心数
nproc
# 或
grep -c processor /proc/cpuinfo
```

## 常见问题

### 1. 如何查看系统启动时间？

```bash
# 使用 uptime -s
uptime -s

# 或使用 who -b
who -b

# 或使用 systemd
systemd-analyze
```

### 2. 负载高但 CPU 使用率低怎么办？

可能原因：
- 大量 I/O 等待（磁盘慢）
- 进程处于不可中断睡眠状态（D 状态）
- 内存不足导致频繁换页

```bash
# 查看 I/O 等待
iostat -x 1

# 查看 D 状态进程
ps aux | awk '$8=="D"'

# 查看内存情况
free -h
```

### 3. 如何持续监控负载？

```bash
# 使用 top/htop
htop

# 使用 watch
watch -n 1 uptime

# 记录到文件
while true; do date; uptime; sleep 60; done >> uptime.log
```

## 快捷别名

```bash
alias up='uptime'
alias up-pretty='uptime -p'
alias up-start='uptime -s'
alias load='uptime | awk -F "load average:" "{print \$2}"'
```

## 一句话总结

uptime 核心：查看系统运行时间 `uptime`，更友好格式 `uptime -p`，查看启动时间 `uptime -s`。负载 < 核心数时正常，> 核心数时过载。脚本中可用 `uptime -s` 获取启动时间做判断。
