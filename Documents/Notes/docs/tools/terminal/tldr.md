# tldr - 简化的命令手册

## 一句话理解

tldr（Too Long; Didn't Read）是 man 手册的简化版，只显示最常用的命令示例，而不是所有参数。

```bash
# 查看 tar 命令的常用用法
tldr tar

# 而不是
man tar
```

## 安装

```bash
# Arch Linux
sudo pacman -S tldr

# 其他方式
pip install tldr
npm install -g tldr
```

## 基本用法

### 查看命令示例

```bash
# 基本用法
tldr tar
tldr grep
tldr ffmpeg

# 输出示例（tar）
# tar
# Archiving utility.
# Often combined with a compression method, such as gzip or bzip2.
# More information: https://www.gnu.org/software/tar

# - Create an archive from files:
#   tar cf target.tar file1 file2

# - Create a gzipped archive:
#   tar czf target.tar.gz file1 file2

# - Extract an archive into the current directory:
#   tar xf source.tar
```

### 常用选项

```bash
# 更新本地缓存
tldr -u

# 强制更新缓存
tldr -f

# 显示命令所有页面（如果有多平台）
tldr -a tar

# 指定平台（linux、osx、windows、sunos、common）
tldr -p linux tar

# 列出所有命令
tldr -l
```

## 使用场景

### 1. 忘记 tar 压缩命令

```bash
tldr tar
# 看到 czf（压缩）和 xf（解压）示例
```

### 2. 忘记 find 参数

```bash
tldr find
# 显示按名称、按类型、按时间查找的示例
```

### 3. 第一次使用某命令

```bash
tldr ffmpeg
# 快速了解常用操作：格式转换、压缩、剪辑
```

## 客户端选择

| 客户端 | 特点 |
|--------|------|
| `tldr`（Python） | 官方版本，功能完整 |
| `tealdeer`（Rust） | 速度快，推荐 |
| `tldr-cpp`（C++） | 轻量快速 |

```bash
# 安装 tealdeer（推荐）
sudo pacman -S tealdeer

# 使用
tldr tar
# 或
tldr --update
```

## 与 man 对比

| 特性 | man | tldr |
|------|-----|------|
| 信息量 | 完整详尽 | 只列常用示例 |
| 阅读时间 | 长 | 短 |
| 适合场景 | 深入学习、查所有参数 | 快速回想命令用法 |
| 示例 | 无或很少 | 每个场景一个例子 |
| 网络依赖 | 否 | 首次需下载缓存 |

## 常用命令速查

| 命令 | 说明 |
|------|------|
| `tldr command` | 查看命令示例 |
| `tldr -u` | 更新缓存 |
| `tldr -a command` | 显示所有平台页面 |
| `tldr -l` | 列出所有命令 |
| `tldr -p linux command` | 指定平台 |
| `tldr -r` | 随机显示一个命令 |

## 配置

### tealdeer 配置文件 `~/.config/tealdeer/config.toml`

```toml
# 显示颜色
display.compact = false

# 更新源
updates.auto_update = true
updates.interval = "7d"

# 样式
style.command_name = "bold green"
style.example_text = "dim"
style.example_code = "bold"
```

## 实际例子

```bash
# 查看 grep 常用用法
$ tldr grep

# grep
# Find patterns in files using regular expressions.

# - Search for a pattern within a file:
#   grep "search_pattern" path/to/file

# - Search for an exact string (disables regex):
#   grep -F "exact_string" path/to/file

# - Search recursively in a directory:
#   grep -R "search_pattern" path/to/directory

# - Use extended regular expressions (supports ?, +, {}, () and |):
#   grep -E "^[0-9]{3}-[0-9]{3}-[0-9]{4}$" path/to/file
```

## 一句话总结

tldr 核心：`tldr command` 快速查看命令常用示例。忘记 `tar` 参数时 `tldr tar`，忘记 `ffmpeg` 时 `tldr ffmpeg`。比 man 快得多，适合日常快速查阅。安装 `tealdeer` 体验更好。
