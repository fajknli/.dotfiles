# ps - 查看进程状态

## 一句话理解

ps（process status）显示当前系统中的进程快照，常用于查看进程 PID、CPU/内存占用、运行状态。

```bash
# 查看所有进程（最常用）
ps aux

# 查看特定进程
ps aux | grep nginx
```

## 常用场景

### 1. 查看所有进程（BSD 风格）

```bash
ps aux

# 输出列说明：
# USER: 运行用户
# PID: 进程ID
# %CPU: CPU使用率
# %MEM: 内存使用率
# VSZ: 虚拟内存(KB)
# RSS: 物理内存(KB)
# TTY: 终端
# STAT: 状态
# START: 启动时间
# TIME: 累计CPU时间
# COMMAND: 命令
```

### 2. 查看所有进程（标准风格）

```bash
ps -ef

# 输出列说明：
# UID: 用户ID
# PID: 进程ID
# PPID: 父进程ID
# C: CPU使用率
# STIME: 启动时间
# TTY: 终端
# TIME: 累计CPU时间
# CMD: 命令
```

### 3. 查看特定用户的进程

```bash
# 查看 root 用户的进程
ps -u root

# 查看当前用户的进程
ps -u $(whoami)
```

### 4. 按 CPU 或内存排序

```bash
# CPU 占用前 10
ps aux --sort=-%cpu | head -10

# 内存占用前 10
ps aux --sort=-%mem | head -10
```

### 5. 查看进程树

```bash
ps auxf
ps -ef --forest
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `aux` | BSD 风格，显示所有进程 | `ps aux` |
| `-ef` | 标准风格，显示所有进程 | `ps -ef` |
| `-u user` | 显示指定用户的进程 | `ps -u root` |
| `-p PID` | 显示指定 PID 的进程 | `ps -p 1234` |
| `--sort=-%cpu` | 按 CPU 降序排序 | `ps aux --sort=-%cpu` |
| `-f` | 完整格式 | `ps -f` |
| `-o` | 自定义输出列 | `ps -o pid,cmd,%cpu` |
| `--forest` | 树形显示 | `ps auxf` |

## 进程状态说明

| 状态 | 说明 |
|------|------|
| `R` | 运行中或可运行 |
| `S` | 可中断睡眠 |
| `D` | 不可中断睡眠（通常为 IO） |
| `Z` | 僵尸进程 |
| `T` | 停止 |
| `t` | 跟踪停止 |
| `X` | 死进程 |

## 常见问题

### 1. ps aux 和 ps -ef 有什么区别？

| 风格 | 命令 | 特点 |
|------|------|------|
| BSD | `ps aux` | 有 %CPU、%MEM、VSZ、RSS、STAT、START |
| 标准 | `ps -ef` | 有 UID、PPID、C、STIME |

推荐 `ps aux`。

### 2. 如何只显示特定列？

```bash
ps -eo pid,user,%cpu,%mem,cmd --sort=-%cpu | head -10
```

### 3. 如何实时监控而不是快照？

```bash
# ps 是快照，实时用 top/htop
top
htop
```

## 快捷别名

```bash
alias psme='ps -u $(whoami)'
alias pscpu='ps aux --sort=-%cpu | head -10'
alias psmem='ps aux --sort=-%mem | head -10'
alias psg='ps aux | grep -v grep | grep'
```

## 一句话总结

ps 核心：`ps aux` 看所有进程，`ps aux | grep nginx` 找特定进程，`ps aux --sort=-%cpu` 按 CPU 排序，`ps auxf` 看进程树。
