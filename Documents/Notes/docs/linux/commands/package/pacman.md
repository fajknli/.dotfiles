# pacman - Arch Linux 包管理器

## 一句话理解

pacman 是 Arch Linux 的包管理器，用于安装、更新、删除软件包。

```bash
# 更新系统
sudo pacman -Syu

# 安装软件
sudo pacman -S firefox
```

## 常用场景

### 1. 更新系统

```bash
# 同步数据库并更新所有包
sudo pacman -Syu

# 只同步数据库（不更新）
sudo pacman -Sy

# 强制刷新所有包数据库
sudo pacman -Syy

# 更新时忽略某些包
sudo pacman -Syu --ignore firefox
```

### 2. 安装软件包

```bash
# 安装单个包
sudo pacman -S firefox

# 安装多个包
sudo pacman -S firefox vim git

# 从本地文件安装
sudo pacman -U package.pkg.tar.zst

# 安装时显示详情
sudo pacman -Sv firefox
```

### 3. 删除软件包

```bash
# 删除包（保留依赖）
sudo pacman -R firefox

# 删除包及其依赖（无其他包需要）
sudo pacman -Rs firefox

# 删除包、依赖和配置文件
sudo pacman -Rns firefox

# 强制删除（忽略依赖）
sudo pacman -Rdd firefox
```

### 4. 搜索和查看

```bash
# 搜索包（名称和描述）
pacman -Ss firefox

# 搜索已安装包
pacman -Qs firefox

# 查看包信息
pacman -Si firefox

# 查看已安装包信息
pacman -Qi firefox

# 列出包文件
pacman -Ql firefox

# 查看文件属于哪个包
pacman -Qo /usr/bin/firefox
```

### 5. 管理缓存和数据库

```bash
# 清理缓存（保留最新版）
sudo pacman -Sc

# 清理所有缓存（清空）
sudo pacman -Scc

# 检查数据库一致性
pacman -Dk

# 修复数据库
sudo pacman -Dkr
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-S` | 安装包 | `sudo pacman -S package` |
| `-R` | 删除包 | `sudo pacman -R package` |
| `-U` | 安装本地包 | `sudo pacman -U package.pkg.tar.zst` |
| `-Ss` | 搜索包 | `pacman -Ss keyword` |
| `-Si` | 查看包信息 | `pacman -Si package` |
| `-Qs` | 搜索已安装 | `pacman -Qs keyword` |
| `-Qi` | 查看已安装信息 | `pacman -Qi package` |
| `-Ql` | 列出包文件 | `pacman -Ql package` |
| `-Qo` | 查找文件所属包 | `pacman -Qo /path/to/file` |
| `-Qe` | 列出手动安装包 | `pacman -Qe` |
| `-Qdt` | 列出孤儿包 | `pacman -Qdt` |
| `-Syu` | 更新系统 | `sudo pacman -Syu` |
| `-Sc` | 清理缓存 | `sudo pacman -Sc` |

## 常用组合速查

| 操作 | 命令 |
|------|------|
| 更新系统 | `sudo pacman -Syu` |
| 安装软件 | `sudo pacman -S 包名` |
| 删除软件 | `sudo pacman -R 包名` |
| 删除软件+配置 | `sudo pacman -Rns 包名` |
| 删除孤儿包 | `sudo pacman -Rns $(pacman -Qdtq)` |
| 搜索软件 | `pacman -Ss 关键词` |
| 查看已安装 | `pacman -Q 包名` |
| 列出包文件 | `pacman -Ql 包名` |
| 文件找包 | `pacman -Qo 文件路径` |
| 清理缓存 | `sudo pacman -Sc` |

## 常见问题

### 1. 数据库锁定怎么办？

```bash
# 删除锁文件
sudo rm /var/lib/pacman/db.lck

# 等待其他 pacman 进程结束
ps aux | grep pacman
```

### 2. 签名无效怎么办？

```bash
# 初始化密钥环
sudo pacman-key --init

# 更新密钥
sudo pacman-key --populate archlinux

# 刷新密钥
sudo pacman-key --refresh-keys

# 手动信任密钥
sudo pacman-key --lsign-key "密钥ID"
```

### 3. 如何恢复误删的包？

```bash
# 查看日志
grep "removed" /var/log/pacman.log

# 重新安装
sudo pacman -S 包名
```

### 4. 如何查看包大小？

```bash
# 已安装包大小
pacman -Qi 包名 | grep "Installed Size"

# 未安装包大小
pacman -Si 包名 | grep "Download Size"

# 列出所有包大小排序
pacman -Q | awk '{print $1}' | xargs pacman -Qi | grep -E "Name|Size"
```

## 快捷别名

```bash
alias pac='sudo pacman'
alias pacs='pacman -Ss'
alias pacs-i='pacman -Si'
alias pacq='pacman -Q'
alias pacqi='pacman -Qi'
alias pacql='pacman -Ql'
alias pacqo='pacman -Qo'
alias pacu='sudo pacman -Syu'
alias pacsyu='sudo pacman -Syu'
alias pacr='sudo pacman -Rns'
alias pacc='sudo pacman -Sc'
```

## 配置文件

`/etc/pacman.conf` 主要配置项：

```ini
# 镜像源
[options]
Architecture = auto
Color
ParallelDownloads = 5
CheckSpace

# 启用多线程下载
ParallelDownloads = 10

# 启用仓库
[core]
Include = /etc/pacman.d/mirrorlist

[extra]
Include = /etc/pacman.d/mirrorlist

[community]
Include = /etc/pacman.d/mirrorlist
```

## 一句话总结

pacman 核心：`-Syu` 更新，`-S` 安装，`-Rns` 删除，`-Ss` 搜索，`-Qi` 查信息，`-Qo` 文件找包，`-Sc` 清缓存。Arch 包管理核心工具。
