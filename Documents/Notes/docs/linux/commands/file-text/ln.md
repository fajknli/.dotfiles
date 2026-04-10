# ln - 创建链接文件

## 一句话理解

ln 命令创建硬链接或符号链接（软链接），类似于 Windows 的快捷方式。

```bash
# 创建符号链接（软链接）
ln -s /usr/bin/python3 python

# 创建硬链接
ln original.txt link.txt
```

## 常用场景

### 1. 创建符号链接（软链接）

```bash
# 链接到文件
ln -s /usr/bin/python3 /usr/local/bin/python

# 链接到目录
ln -s /etc/nginx /home/user/nginx-config

# 使用相对路径
ln -s ../doc/readme.md readme.md

# 覆盖已存在的链接
ln -sf /new/path/file link
```

### 2. 创建硬链接

```bash
# 基本硬链接
ln original.txt hardlink.txt

# 硬链接不能跨文件系统
# 硬链接不能链接目录
```

### 3. 批量创建链接

```bash
# 链接多个文件到目录
ln -s /usr/bin/*.sh /tmp/scripts/

# 使用通配符
ln -s /path/to/*.conf ./
```

### 4. 备份和版本管理

```bash
# 创建备份链接
ln -sf config.conf config.conf.bak

# 内核版本链接
ln -sf vmlinuz-6.12.8 vmlinuz
```

### 5. 查看链接信息

```bash
# 查看链接指向
ls -l link
# link -> /path/to/target

# 查看链接目标
readlink link

# 查看链接规范路径
readlink -f link
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-s` | 创建符号链接（软链接） | `ln -s target link` |
| `-f` | 强制覆盖已存在文件 | `ln -sf target link` |
| `-n` | 将已存在的链接视为文件 | `ln -snf target link` |
| `-v` | 显示详细信息 | `ln -sv target link` |
| `-i` | 覆盖前询问 | `ln -si target link` |
| `-b` | 备份已存在文件 | `ln -sb target link` |
| `-T` | 将链接视为普通文件 | `ln -sT target link` |
| `-r` | 使用相对路径 | `ln -sr target link` |

## 硬链接 vs 符号链接

| 特性 | 硬链接 | 符号链接 |
|------|--------|----------|
| 命令 | `ln target link` | `ln -s target link` |
| 跨文件系统 | ❌ 不行 | ✅ 可以 |
| 链接目录 | ❌ 不行 | ✅ 可以 |
| 删除原文件 | 链接仍有效 | 链接失效（悬空） |
| inode | 相同 | 不同 |
| 文件大小 | 0（与原文件共享） | 路径长度 |
| 查看指向 | 无法直接看 | `readlink` |

## 常见问题

### 1. 符号链接和硬链接选哪个？

| 场景 | 推荐 |
|------|------|
| 快捷方式 | 符号链接 |
| 跨文件系统 | 符号链接 |
| 链接目录 | 符号链接 |
| 节省空间（相同文件） | 硬链接 |
| 备份/版本管理 | 符号链接 |

### 2. 如何查找所有符号链接？

```bash
# 查找当前目录
find . -type l

# 查找并显示指向
find . -type l -ls

# 查找失效链接
find . -type l ! -exec test -e {} \; -print
```

### 3. 如何修复失效的符号链接？

```bash
# 查找失效链接
find . -type l ! -exec test -e {} \; -print

# 删除失效链接
find . -type l ! -exec test -e {} \; -delete

# 重新链接
ln -sf /new/path broken_link
```

### 4. 如何创建多个链接？

```bash
# 链接多个文件到目录（目标必须是目录）
ln -s /usr/bin/python3 /usr/bin/python2 /tmp/links/

# 目标目录需先存在
mkdir -p /tmp/links
```

## 快捷别名

```bash
alias ln='ln -v'
alias lnf='ln -sf'
alias lns='ln -s'
alias lnr='ln -sr'
alias readlinkf='readlink -f'
```

## 一句话总结

ln 核心：`ln -s target link` 创建符号链接（推荐），`ln target link` 创建硬链接（同 inode）。`-f` 强制覆盖，`-v` 显示详情。符号链接可跨文件系统、可链接目录；硬链接不能。查看链接用 `readlink`，查找失效链接用 `find . -type l ! -exec test -e {} \; -print`。
