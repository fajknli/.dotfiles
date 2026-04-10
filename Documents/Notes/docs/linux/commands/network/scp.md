# scp - 安全远程文件复制

## 一句话理解

scp（secure copy）通过 SSH 在本地和远程主机之间安全地复制文件或目录。

```bash
# 本地文件复制到远程
scp file.txt user@host:/path/to/dest/

# 远程文件复制到本地
scp user@host:/path/to/file.txt ./
```

## 常用场景

### 1. 本地复制到远程

```bash
# 复制文件
scp file.txt user@192.168.1.100:/home/user/

# 指定端口
scp -P 2222 file.txt user@host:/home/user/

# 复制目录（递归）
scp -r myfolder/ user@host:/home/user/

# 保留文件属性（时间、权限）
scp -p file.txt user@host:/home/user/
```

### 2. 远程复制到本地

```bash
# 复制文件到当前目录
scp user@host:/home/user/file.txt ./

# 复制目录
scp -r user@host:/home/user/myfolder/ ./

# 复制到指定目录
scp user@host:/home/user/file.txt /tmp/
```

### 3. 远程之间复制

```bash
# 通过本地中转（两台远程主机之间）
scp user1@host1:/path/to/file user2@host2:/path/to/dest/

# 需要免密或手动输入密码
```

### 4. 使用免密认证

```bash
# 生成密钥对
ssh-keygen -t ed25519

# 复制公钥到远程
ssh-copy-id user@host

# 之后 scp 无需输入密码
scp file.txt user@host:/path/
```

### 5. 限制带宽

```bash
# 限制带宽为 1000 Kbit/s
scp -l 1000 largefile.zip user@host:/path/
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-r` | 递归复制目录 | `scp -r dir/ user@host:/path/` |
| `-P port` | 指定 SSH 端口 | `scp -P 2222 file user@host:/path/` |
| `-p` | 保留文件属性（时间、权限） | `scp -p file user@host:/path/` |
| `-q` | 安静模式（不显示进度） | `scp -q file user@host:/path/` |
| `-v` | 详细模式（调试用） | `scp -v file user@host:/path/` |
| `-C` | 压缩传输 | `scp -C file user@host:/path/` |
| `-l limit` | 限制带宽（Kbit/s） | `scp -l 1000 file user@host:/path/` |
| `-i keyfile` | 指定私钥文件 | `scp -i ~/.ssh/id_rsa file user@host:/path/` |
| `-o option` | 传递 SSH 选项 | `scp -o ConnectTimeout=10 file user@host:/path/` |

## 常见问题

### 1. scp 和 rsync 有什么区别？

| 工具 | 特点 | 适用场景 |
|------|------|----------|
| `scp` | 简单、单次复制 | 偶尔传文件 |
| `rsync` | 增量传输、支持断点续传 | 定期同步、大文件 |

```bash
# scp 简单
scp file.txt user@host:/path/

# rsync 强大（增量）
rsync -av file.txt user@host:/path/
```

### 2. 端口不是 22 怎么办？

```bash
# 使用 -P（大写）
scp -P 2222 file.txt user@host:/path/

# 注意：-P 是端口，-p 是保留属性
```

### 3. 如何复制大文件并显示进度？

```bash
# scp 默认显示进度条
scp largefile.zip user@host:/path/

# 使用 pv 更详细
pv largefile.zip | ssh user@host "cat > /path/largefile.zip"

# 使用 rsync 显示进度
rsync -av --progress largefile.zip user@host:/path/
```

### 4. 如何批量复制多个文件？

```bash
# 使用通配符
scp *.txt user@host:/path/

# 使用大括号
scp file{1..10}.txt user@host:/path/

# 复制整个目录
scp -r myfolder/ user@host:/path/
```

## 快捷别名

```bash
alias scpr='scp -r'
alias scpp='scp -p'
alias scpP='scp -P'
alias scpv='scp -v'
```

## 一句话总结

scp 核心：`scp file user@host:/path/` 上传，`scp user@host:/path/file .` 下载，`-r` 复制目录，`-P` 指定端口。简单传文件用 scp，定期同步用 rsync。配合免密 SSH 更方便。
