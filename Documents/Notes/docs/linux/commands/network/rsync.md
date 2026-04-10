# rsync 命令详解

## 一句话理解 rsync

rsync 是远程同步工具，**只传输文件变化的部分**，支持本地和远程同步，支持断点续传。

```bash
# 本地同步
rsync -av source/ dest/

# 远程同步（上传）
rsync -av local/ user@server:/remote/

# 远程同步（下载）
rsync -av user@server:/remote/ local/
```

## 最常用场景

### 1. 本地备份

```bash
# 同步目录（保留权限、时间）
rsync -av /home/user/docs/ /backup/docs/

# 镜像同步（删除目标端多余文件）
rsync -av --delete /home/user/docs/ /backup/docs/

# 显示进度
rsync -av --progress /home/user/docs/ /backup/docs/
```

### 2. 远程同步（SSH）

```bash
# 上传到远程服务器
rsync -av -e ssh local/ user@192.168.1.100:/remote/

# 从远程下载
rsync -av -e ssh user@192.168.1.100:/remote/ local/

# 指定 SSH 端口
rsync -av -e "ssh -p 2222" local/ user@server:/remote/
```

### 3. 增量备份

```bash
# 只同步新文件和修改过的文件
rsync -av --update source/ dest/

# 基于时间戳过滤
rsync -av --newer="2026-04-01" source/ dest/
```

## 核心参数

| 参数 | 说明 | 常用度 |
|------|------|--------|
| `-a` | 归档模式（保留权限、时间、递归） | ⭐⭐⭐ |
| `-v` | 显示详细信息 | ⭐⭐⭐ |
| `-z` | 传输时压缩 | ⭐⭐ |
| `-P` | 显示进度 + 断点续传 | ⭐⭐⭐ |
| `--delete` | 删除目标端源端没有的文件 | ⭐⭐⭐ |
| `--dry-run` | 模拟运行（不实际传输） | ⭐⭐⭐ |
| `--exclude` | 排除文件 | ⭐⭐ |
| `--include` | 包含文件 | ⭐ |
| `-u` | 只更新新文件 | ⭐⭐ |
| `--bwlimit` | 限速（KB/s） | ⭐ |
| `-n` | 同 --dry-run | ⭐⭐⭐ |

## 常用参数详解

### -a 归档模式

```bash
# -a 等于 -rlptgoD 的组合
# -r 递归
# -l 保留符号链接
# -p 保留权限
# -t 保留修改时间
# -g 保留组
# -o 保留所有者
# -D 保留设备文件

rsync -a source/ dest/
```

### -v 显示详情

```bash
# 一级详细
rsync -av source/ dest/

# 二级详细（更详细输出）
rsync -avv source/ dest/
```

### -P 进度和断点续传

```bash
# -P 等于 --progress --partial
rsync -avP source/ dest/
```

### --delete 同步删除

```bash
# 目标端多出来的文件会被删除
rsync -av --delete source/ dest/

# 危险操作：目标端会变得和源端完全一样
rsync -av --delete /empty/ /important/  # 小心！
```

### --dry-run 模拟运行

```bash
# 先看看会做什么，不实际传输
rsync -av --delete --dry-run source/ dest/

# 确认无误后去掉 -n 或 --dry-run
```

## 路径末尾斜杠的区别

| 写法 | 行为 |
|------|------|
| `rsync -av source/ dest/` | 复制 source 下的**内容**到 dest |
| `rsync -av source dest/` | 复制 source **目录本身**到 dest |

```bash
# 示例：source 下有 file.txt
rsync -av source/ dest/   # dest/file.txt
rsync -av source dest/    # dest/source/file.txt
```

## 实际例子

### 1. 网站备份

```bash
# 备份到本地
rsync -av --delete /var/www/html/ /backup/www/

# 备份到远程
rsync -avz --delete -e ssh /var/www/html/ user@backup:/backup/www/

# 带时间戳的备份
rsync -av /var/www/html/ /backup/www_$(date +%Y%m%d)/
```

### 2. 排除文件和目录

```bash
# 排除单个文件
rsync -av --exclude="config.php" source/ dest/

# 排除目录
rsync -av --exclude="cache/" source/ dest/

# 排除多个
rsync -av --exclude="*.log" --exclude="tmp/" source/ dest/

# 从文件读取排除列表
rsync -av --exclude-from=exclude-list.txt source/ dest/
# exclude-list.txt 内容：
# *.log
# *.tmp
# cache/
```

### 3. 限速传输

```bash
# 限制为 1MB/s（1024 KB/s）
rsync -av --bwlimit=1024 source/ dest/
```

### 4. SSH 端口转发

```bash
# 你之前用的例子
rsync -avz -e "ssh -p 26059" frp_0.64.0_linux_amd64.tar.gz root@119.188.232.23:/root/
```

### 5. 复制时更改所有者

```bash
# 你之前记的
rsync -av --owner source/ dest/
```

### 6. 只同步新文件

```bash
# 目标端有的文件不覆盖
rsync -avu source/ dest/

# 只同步最近7天的文件
find source/ -type f -mtime -7 -print0 | rsync -av --files-from=- --from0 source/ dest/
```

### 7. 镜像整个目录

```bash
# 完全同步，删除目标端多余文件
rsync -av --delete source/ dest/

# 可以配合 cron 做定时镜像
# crontab -e
# 0 2 * * * rsync -av --delete /data/ /backup/data/
```

## 常用组合速查

| 目的 | 命令 |
|------|------|
| 本地备份 | `rsync -av source/ dest/` |
| 远程上传 | `rsync -av -e ssh local/ user@host:/remote/` |
| 远程下载 | `rsync -av -e ssh user@host:/remote/ local/` |
| 增量备份 | `rsync -avu source/ dest/` |
| 镜像同步 | `rsync -av --delete source/ dest/` |
| 显示进度 | `rsync -avP source/ dest/` |
| 模拟运行 | `rsync -av --dry-run source/ dest/` |
| 限速传输 | `rsync -av --bwlimit=1024 source/ dest/` |
| 排除文件 | `rsync -av --exclude="*.log" source/ dest/` |
| 断点续传 | `rsync -avP source/ dest/` |

## 与 scp 对比

| 场景 | rsync | scp |
|------|-------|-----|
| 首次传输 | 速度相当 | 速度相当 |
| 再次传输（增量） | 快（只传变化） | 慢（全部重传） |
| 断点续传 | 支持（-P） | 不支持 |
| 删除同步 | 支持（--delete） | 不支持 |
| 排除文件 | 支持 | 不支持 |
| 权限保留 | 支持（-a） | 部分支持（-p） |
| 压缩传输 | 支持（-z） | 不支持 |

## 常见问题

### 1. 权限不足

```bash
# 远程需要写权限
rsync -av local/ user@host:/root/  # 需要 root 权限

# 使用 sudo（需配置 sudo 免密）
rsync -av local/ user@host:/root/ --rsync-path="sudo rsync"
```

### 2. 大量小文件慢

```bash
# 使用 -W 禁用增量算法（小文件差异不明显）
rsync -avW source/ dest/

# 或先打包再传输
tar -czf - source/ | ssh user@host "tar -xzf - -C dest/"
```

### 3. 符号链接问题

```bash
# 复制符号链接本身（默认）
rsync -a source/ dest/

# 复制链接指向的内容
rsync -aL source/ dest/
```

## 自动化备份脚本

```bash
#!/bin/bash
# backup.sh

SOURCE="/home/user/data/"
DEST="/backup/data/"
LOG="/var/log/backup.log"

rsync -av --delete --log-file="$LOG" "$SOURCE" "$DEST"

if [ $? -eq 0 ]; then
    echo "$(date): 备份成功" >> "$LOG"
else
    echo "$(date): 备份失败" >> "$LOG"
fi
```

## 一句话总结

rsync 的核心是 `-av`（归档+详细），加 `--delete` 实现镜像同步，加 `-P` 显示进度，加 `--dry-run` 先模拟。日常备份用 `rsync -av source/ dest/` 就够了。
