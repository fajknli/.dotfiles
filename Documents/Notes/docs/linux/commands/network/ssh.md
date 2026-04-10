# ssh 命令详解

## 一句话理解 ssh

ssh 是远程登录工具，通过加密连接安全地连接远程服务器。

```bash
# 基本登录
ssh user@hostname

# 指定端口
ssh -p 2222 user@hostname

# 执行远程命令
ssh user@hostname "ls -la"
```

## 最常用场景

### 1. 远程登录

```bash
# 默认端口22
ssh root@192.168.1.100

# 指定端口
ssh -p 26059 root@119.188.232.23

# 使用跳板机
ssh -J jumphost user@target
```

### 2. 执行远程命令

```bash
# 单条命令
ssh user@server "df -h"

# 多条命令
ssh user@server "cd /var/log && grep error app.log"

# 使用 sudo（需要 tty）
ssh -t user@server "sudo systemctl restart nginx"
```

### 3. 文件传输（配合 scp/rsync）

```bash
# scp 上传
scp -P 26059 local.txt root@119.188.232.23:/root/

# scp 下载
scp -P 26059 root@119.188.232.23:/root/remote.txt ./

# rsync 上传（你之前用的）
rsync -avz -e "ssh -p 26059" file.tar.gz root@119.188.232.23:/root/
```

## 核心参数

| 参数 | 说明 | 例子 |
|------|------|------|
| `-p` | 指定端口 | `ssh -p 2222 user@host` |
| `-i` | 指定私钥文件 | `ssh -i ~/.ssh/id_rsa user@host` |
| `-J` | 跳板机 | `ssh -J user@jump user@target` |
| `-t` | 强制分配伪终端 | `ssh -t user@host "sudo cmd"` |
| `-v` | 调试模式（详细输出） | `ssh -v user@host` |
| `-vvv` | 更详细（排错用） | `ssh -vvv user@host` |
| `-C` | 压缩传输 | `ssh -C user@host` |
| `-N` | 不执行远程命令 | `ssh -N -L 8080:localhost:80 user@host` |
| `-f` | 后台运行 | `ssh -f -N -L 8080:localhost:80 user@host` |

## 配置文件（~/.ssh/config）

推荐用配置文件，不用每次都打参数。

```bash
# 编辑配置文件
vim ~/.ssh/config
```

### 基本配置

```
# 单主机配置
Host myserver
    HostName 119.188.232.23
    Port 26059
    User root
    IdentityFile ~/.ssh/id_rsa

# 使用别名登录
# ssh myserver 即可
```

### 常用配置项

| 配置项 | 说明 | 例子 |
|--------|------|------|
| `HostName` | 服务器地址 | `HostName 192.168.1.100` |
| `Port` | 端口 | `Port 2222` |
| `User` | 用户名 | `User root` |
| `IdentityFile` | 私钥路径 | `IdentityFile ~/.ssh/id_rsa` |
| `ProxyJump` | 跳板机 | `ProxyJump user@jump` |
| `ForwardAgent` | 转发密钥代理 | `ForwardAgent yes` |
| `Compression` | 压缩 | `Compression yes` |
| `ServerAliveInterval` | 保活间隔（秒） | `ServerAliveInterval 60` |

### 配置示例

```
# 默认配置（所有主机）
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    Compression yes

# 家庭服务器
Host homeserver
    HostName 192.168.1.100
    User fajknli
    Port 22
    IdentityFile ~/.ssh/home_rsa

# VPS（你之前用的）
Host vps
    HostName 119.188.232.23
    Port 26059
    User root
    IdentityFile ~/.ssh/vps_rsa

# 跳板机方式
Host internal
    HostName 10.0.0.5
    User admin
    ProxyJump user@jumphost.example.com
```

## 密钥认证（免密登录）

### 生成密钥对

```bash
# 生成 RSA 密钥
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# 生成 Ed25519（推荐，更安全）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 指定文件名
ssh-keygen -t rsa -f ~/.ssh/vps_key
```

### 复制公钥到服务器

```bash
# 自动复制（推荐）
ssh-copy-id user@host

# 指定端口
ssh-copy-id -p 26059 root@119.188.232.23

# 手动复制
cat ~/.ssh/id_rsa.pub | ssh user@host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### 密钥文件权限

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/authorized_keys
```

## 端口转发

### 本地转发（-L）

把远程服务的端口映射到本地。

```bash
# 访问本地 8080 等于访问远程 80
ssh -L 8080:localhost:80 user@server

# 访问本地 3306 等于访问远程 MySQL
ssh -L 3306:localhost:3306 user@server

# 后台运行
ssh -fN -L 8080:localhost:80 user@server
```

### 远程转发（-R）

把本地服务映射到远程。

```bash
# 远程访问 8080 等于访问本地 80
ssh -R 8080:localhost:80 user@server

# 让同事通过你的服务器访问你本地的服务
ssh -R 8080:localhost:3000 user@public-server
```

### 动态转发（-D）

开一个 SOCKS5 代理。

```bash
# 本地 1080 端口作为 SOCKS5 代理
ssh -D 1080 user@server

# 配合浏览器使用（FoxyProxy 等插件）
```

## 跳板机（ProxyJump）

```bash
# 命令行方式
ssh -J user@jumpserver user@target

# 多个跳板机
ssh -J user1@jump1,user2@jump2 user@target

# 配置文件方式
Host target
    HostName 10.0.0.5
    User admin
    ProxyJump user@jumpserver
```

## 远程命令执行

```bash
# 单条命令
ssh user@server "df -h"

# 多条命令
ssh user@server "cd /var/log && tail -20 app.log"

# 执行脚本（本地脚本在远程运行）
ssh user@server 'bash -s' < local_script.sh

# 带参数
ssh user@server "ps aux | grep nginx"

# 使用 sudo（需要 -t）
ssh -t user@server "sudo systemctl restart nginx"
```

## 保活配置（防止断线）

### 客户端配置（~/.ssh/config）

```
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

### 服务端配置（/etc/ssh/sshd_config）

```
ClientAliveInterval 60
ClientAliveCountMax 3
```

## 调试排错

```bash
# 详细输出
ssh -v user@host

# 更详细
ssh -vvv user@host

# 只测试连接（不登录）
ssh -v -T git@github.com

# 查看密钥加载情况
ssh -v user@host 2>&1 | grep "Offering"

# 检查配置语法
sshd -t
```

## 安全建议

### 服务端配置（/etc/ssh/sshd_config）

```
# 禁用 root 登录
PermitRootLogin no

# 禁用密码登录（只允许密钥）
PasswordAuthentication no

# 修改默认端口
Port 2222

# 允许的用户
AllowUsers user1 user2

# 禁止的用户
DenyUsers root

# 空闲超时断开
ClientAliveInterval 300
ClientAliveCountMax 2
```

### 修改配置后重启

```bash
sudo systemctl restart sshd
```

## 常用命令速查

| 目的 | 命令 |
|------|------|
| 基本登录 | `ssh user@host` |
| 指定端口 | `ssh -p 2222 user@host` |
| 指定密钥 | `ssh -i ~/.ssh/key user@host` |
| 执行远程命令 | `ssh user@host "cmd"` |
| 使用跳板机 | `ssh -J user@jump user@target` |
| 本地端口转发 | `ssh -L 8080:localhost:80 user@host` |
| 远程端口转发 | `ssh -R 8080:localhost:80 user@host` |
| 动态SOCKS代理 | `ssh -D 1080 user@host` |
| 后台端口转发 | `ssh -fN -L 8080:localhost:80 user@host` |
| 调试模式 | `ssh -vvv user@host` |

## 配置文件模板

```bash
# ~/.ssh/config

# 全局配置
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    Compression yes

# 家服务器
Host home
    HostName 192.168.1.100
    User fajknli
    Port 22

# VPS
Host vps
    HostName 119.188.232.23
    Port 26059
    User root
    IdentityFile ~/.ssh/vps_key

# GitHub
Host github
    HostName github.com
    User git
    IdentityFile ~/.ssh/github_key
```

## 一句话总结

ssh 核心：`ssh user@host` 登录，`ssh-copy-id` 免密，`~/.ssh/config` 简化连接，`-L` 做端口转发。配置文件配好后直接 `ssh 别名` 就能连。
