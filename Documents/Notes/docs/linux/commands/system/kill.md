# kill - 终止进程

## 一句话理解

kill 命令向进程发送信号，最常用于终止进程。默认发送 SIGTERM（15），允许进程清理后退出。

```bash
# 终止进程（优雅退出）
kill 1234

# 强制终止进程
kill -9 1234
```

## 常用场景

### 1. 正常终止进程

```bash
kill 1234
kill -15 1234
```

### 2. 强制终止进程

```bash
kill -9 1234
kill -KILL 1234
```

### 3. 终止多个进程

```bash
kill 1234 5678 9012
pkill nginx
killall nginx
```

### 4. 重新加载配置

```bash
kill -1 1234
kill -HUP 1234
kill -HUP $(cat /var/run/nginx.pid)
```

### 5. 检查进程是否存在

```bash
if kill -0 1234 2>/dev/null; then
    echo "进程存在"
fi
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-l` | 列出所有信号 | `kill -l` |
| `-信号编号` | 用编号指定信号 | `kill -9 1234` |
| `-信号名称` | 用名称指定信号 | `kill -KILL 1234` |
| `-0` | 检查进程是否存在 | `kill -0 1234` |

## 常用信号速查

| 编号 | 名称 | 用途 |
|------|------|------|
| 1 | SIGHUP | 重新加载配置 |
| 2 | SIGINT | Ctrl+C 中断 |
| 9 | SIGKILL | 强制终止（不可捕获） |
| 15 | SIGTERM | 优雅终止（默认） |
| 19 | SIGSTOP | 暂停进程 |

## 常见问题

### 1. kill -9 和 kill -15 有什么区别？

- `kill -15`：进程可执行清理后退出
- `kill -9`：内核直接终止，可能导致数据丢失

优先用 `kill`，无效后再用 `kill -9`。

### 2. 如何杀死所有同名进程？

```bash
pkill nginx
killall nginx
```

### 3. 如何终止进程树（包括子进程）？

```bash
kill -TERM -1234
pkill -P 1234
```

## 快捷别名

```bash
alias kill9='kill -9'
alias killa='killall'
alias psg='ps aux | grep -v grep | grep'
```

## 一句话总结

kill 核心：`kill PID` 优雅终止，`kill -9 PID` 强制终止。优先用默认信号，无效后再用 -9。用 `pkill` 或 `killall` 按名称终止。
