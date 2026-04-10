# tar 命令详解

## 一句话理解 tar

tar 是打包工具，可以把多个文件/文件夹打包成一个大文件（.tar），通常还会配合压缩（.gz、.xz、.bz2）。

```bash
# 打包压缩
tar -czf archive.tar.gz /path/to/folder

# 解压
tar -xzf archive.tar.gz
```

## 核心概念

| 参数 | 说明 | 常用组合 |
|------|------|----------|
| `-c` | 创建打包文件 | `-czf` 打包压缩 |
| `-x` | 解包 | `-xzf` 解压 |
| `-t` | 查看内容（不解压） | `-tzf` |
| `-z` | 通过 gzip 压缩/解压 | 后缀 .tar.gz 或 .tgz |
| `-j` | 通过 bzip2 压缩/解压 | 后缀 .tar.bz2 |
| `-J` | 通过 xz 压缩/解压 | 后缀 .tar.xz |
| `-v` | 显示过程（verbose） | 可选，看进度 |
| `-f` | 指定文件名 | 必须，后面跟文件名 |
| `-C` | 指定解压目录 | `-C /target/dir` |
| `--exclude` | 排除文件 | `--exclude="*.log"` |

## 最常用场景

### 1. 打包压缩

```bash
# 打包成 .tar.gz（最常用）
tar -czf archive.tar.gz /home/user/docs/

# 打包成 .tar.xz（压缩率更高，更慢）
tar -cJf archive.tar.xz /home/user/docs/

# 打包成 .tar.bz2
tar -cjf archive.tar.bz2 /home/user/docs/

# 显示打包过程
tar -czvf archive.tar.gz docs/
```

### 2. 解压

```bash
# 解压 .tar.gz
tar -xzf archive.tar.gz

# 解压到指定目录
tar -xzf archive.tar.gz -C /target/directory/

# 解压 .tar.xz
tar -xJf archive.tar.xz

# 解压 .tar.bz2
tar -xjf archive.tar.bz2

# 解压 .tar（未压缩）
tar -xf archive.tar
```

### 3. 查看内容（不解压）

```bash
# 查看 .tar.gz 内容
tar -tzf archive.tar.gz

# 查看 .tar.xz 内容
tar -tJf archive.tar.xz

# 查看详细信息（类似 ls -l）
tar -tzvf archive.tar.gz
```

## 常用选项组合

| 目的 | 命令 |
|------|------|
| 打包成 tar.gz | `tar -czf out.tar.gz source/` |
| 打包成 tar.xz | `tar -cJf out.tar.xz source/` |
| 解压 tar.gz | `tar -xzf file.tar.gz` |
| 解压 tar.xz | `tar -xJf file.tar.xz` |
| 解压到指定目录 | `tar -xzf file.tar.gz -C /target/` |
| 查看内容 | `tar -tzf file.tar.gz` |
| 打包时排除某些文件 | `tar -czf out.tar.gz --exclude="*.log" source/` |
| 打包时排除多个目录 | `tar -czf out.tar.gz --exclude="node_modules" --exclude=".git" source/` |

## 实际例子

### 1. 备份目录

```bash
# 备份整个 /home 目录（排除缓存）
tar -czf backup_$(date +%Y%m%d).tar.gz --exclude="*.cache" --exclude=".npm" /home/user/

# 备份系统配置
sudo tar -czf etc_backup.tar.gz /etc/

# 增量备份（只备份新文件和修改过的文件）
tar -czf incremental.tar.gz --newer-mtime="2026-04-01" /home/user/docs/
```

### 2. 解压部分文件

```bash
# 解压单个文件
tar -xzf archive.tar.gz path/to/single/file.txt

# 解压匹配模式的文件
tar -xzf archive.tar.gz --wildcards "*.conf"

# 解压并覆盖（默认会覆盖）
tar -xzf archive.tar.gz --overwrite
```

### 3. 网络传输

```bash
# 打包并通过 SSH 传输（不保存中间文件）
tar -czf - /home/user/docs/ | ssh user@remote "tar -xzf - -C /backup/"

# 从远程拉取并解压
ssh user@remote "tar -czf - /data/" | tar -xzf - -C /local/backup/
```

### 4. 打包时保留权限和属性

```bash
# 保留权限、所有者、时间戳
tar -czpf archive.tar.gz source/

# 保留 ACL 和扩展属性
tar --acls --xattrs -czf archive.tar.gz source/
```

## 常见后缀对应参数

| 后缀 | 压缩算法 | 打包参数 | 解压参数 |
|------|----------|----------|----------|
| `.tar` | 无压缩 | `-cf` | `-xf` |
| `.tar.gz` 或 `.tgz` | gzip | `-czf` | `-xzf` |
| `.tar.bz2` 或 `.tbz2` | bzip2 | `-cjf` | `-xjf` |
| `.tar.xz` 或 `.txz` | xz | `-cJf` | `-xJf` |
| `.tar.Z` | compress | `-cZf` | `-xZf` |

## 排除文件技巧

```bash
# 排除单个文件
tar -czf backup.tar.gz --exclude="secret.txt" docs/

# 排除目录
tar -czf backup.tar.gz --exclude="node_modules" --exclude=".git" project/

# 从文件读取排除列表
tar -czf backup.tar.gz --exclude-from=exclude-list.txt docs/

# exclude-list.txt 内容示例
# *.log
# *.tmp
# cache/
```

## 查看打包内容

```bash
# 简单列表
tar -tzf archive.tar.gz

# 详细列表（权限、大小、时间）
tar -tzvf archive.tar.gz

# 过滤查看特定文件
tar -tzf archive.tar.gz | grep ".conf"

# 统计文件数量
tar -tzf archive.tar.gz | wc -l
```

## 拆分大文件

```bash
# 创建 tar 后拆分（每个 1GB）
tar -czf - large_dir/ | split -b 1G - backup.tar.gz.

# 合并并解压
cat backup.tar.gz.* | tar -xzf -

# 或使用 tar 自带的多卷功能
tar -czf - large_dir/ | split -b 1G -d - backup.tar.gz.part
```

## 常见错误

### 1. 忘记指定 -f 参数

```bash
# 错误
tar -czv archive.tar.gz file.txt
# 报错：tar: You must specify one of the -Acdtrux options

# 正确（-f 必须在最后，后面跟文件名）
tar -czvf archive.tar.gz file.txt
```

### 2. 路径问题

```bash
# 打包时带绝对路径（解压时会覆盖原路径）
tar -czf backup.tar.gz /home/user/docs/

# 解压时去掉第一级目录
tar -xzf archive.tar.gz --strip-components=1
```

### 3. 解压到不存在的目录

```bash
# tar 不会自动创建目标目录
tar -xzf file.tar.gz -C /non/existent/dir/
# 报错：Cannot open: No such file or directory

# 先创建目录
mkdir -p /target/dir/
tar -xzf file.tar.gz -C /target/dir/
```

## 性能对比

| 压缩方式 | 压缩速度 | 解压速度 | 压缩率 | 推荐场景 |
|----------|----------|----------|--------|----------|
| 无压缩 `.tar` | 极快 | 极快 | 无 | 临时打包 |
| gzip `.tar.gz` | 快 | 快 | 中 | 日常使用（最常用） |
| bzip2 `.tar.bz2` | 慢 | 中等 | 高 | 需要更小体积 |
| xz `.tar.xz` | 很慢 | 慢 | 最高 | 归档存储，软件发布 |

## 一句话总结

tar 最常用的是两个组合：`tar -czf 目标.tar.gz 源文件`（打包压缩）和 `tar -xzf 文件.tar.gz`（解压）。记住 `-c` 是创建，`-x` 是解压，`-z` 是 gzip，`-f` 后面跟文件名。
