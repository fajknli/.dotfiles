# 用户和组管理

## 一句话理解

Linux 中每个进程都有一个用户和组归属，通过用户和组来控制文件访问权限。

```bash
# 查看当前用户
whoami

# 查看用户ID和组ID
id

# 查看所有用户
cat /etc/passwd

# 查看所有组
cat /etc/group
```

## 用户管理

### 创建用户

```bash
# 基本创建
sudo useradd username

# 创建并设置家目录
sudo useradd -m username

# 指定家目录
sudo useradd -m -d /home/myuser username

# 指定UID
sudo useradd -u 1500 username

# 指定登录shell
sudo useradd -s /bin/bash username

# 添加备注
sudo useradd -c "这是备注信息" username

# 创建时指定主组和附加组
sudo useradd -m -g users -G wheel,docker username

# 创建后设置密码
sudo passwd username
```

### useradd 常用选项

| 选项 | 说明 | 例子 |
|------|------|------|
| `-m` | 创建家目录 | `sudo useradd -m john` |
| `-d` | 指定家目录路径 | `sudo useradd -d /home/john john` |
| `-s` | 指定登录shell | `sudo useradd -s /bin/zsh john` |
| `-u` | 指定UID | `sudo useradd -u 1500 john` |
| `-g` | 指定主组 | `sudo useradd -g users john` |
| `-G` | 指定附加组 | `sudo useradd -G wheel,docker john` |
| `-c` | 添加备注 | `sudo useradd -c "John Doe" john` |
| `-r` | 创建系统用户 | `sudo useradd -r service_user` |

### 修改用户

```bash
# 修改用户名
sudo usermod -l newname oldname

# 修改家目录
sudo usermod -d /home/newhome username

# 移动家目录内容到新位置
sudo usermod -m -d /home/newhome username

# 修改登录shell
sudo usermod -s /bin/zsh username

# 修改UID
sudo usermod -u 1600 username

# 锁定账户（禁止登录）
sudo usermod -L username

# 解锁账户
sudo usermod -U username

# 修改主组
sudo usermod -g newgroup username

# 添加附加组（-a 必须和 -G 一起用，否则会覆盖原有组）
sudo usermod -aG docker username

# 设置账户过期日期
sudo usermod -e "2026-12-31" username

# 清空过期日期（永不过期）
sudo usermod -e "" username
```

### 删除用户

```bash
# 删除用户（保留家目录和邮件）
sudo userdel username

# 删除用户并删除家目录和邮件
sudo userdel -r username

# 强制删除（即使还在登录）
sudo userdel -f username
```

### 密码管理

```bash
# 设置/修改密码
sudo passwd username

# 删除密码（无密码登录）
sudo passwd -d username

# 锁定密码（禁止登录）
sudo passwd -l username

# 解锁密码
sudo passwd -u username

# 设置密码过期信息
sudo passwd -e username  # 强制下次登录修改密码

# 查看密码状态
sudo passwd -S username
```

### 密码过期管理（chage）

```bash
# 查看密码信息
sudo chage -l username

# 设置密码最长使用天数
sudo chage -M 90 username

# 设置密码最短使用天数（0表示无限制）
sudo chage -m 7 username

# 设置密码过期前警告天数
sudo chage -W 7 username

# 设置账户过期日期
sudo chage -E "2026-12-31" username

# 取消过期（永不过期）
sudo chage -E -1 username

# 强制下次登录修改密码
sudo chage -d 0 username
```

## 组管理

### 创建组

```bash
# 创建普通组
sudo groupadd groupname

# 创建系统组（GID < 1000）
sudo groupadd -r groupname

# 指定GID
sudo groupadd -g 1500 groupname
```

### 修改组

```bash
# 修改组名
sudo groupmod -n newname oldname

# 修改GID
sudo groupmod -g 1600 groupname
```

### 删除组

```bash
# 删除组
sudo groupdel groupname

# 注意：如果有用户的主组是这个组，不能删除
# 需要先修改用户的主组或删除用户
```

### 组内成员管理

```bash
# 查看组内成员
getent group groupname
# 或
cat /etc/group | grep groupname

# 添加用户到组
sudo usermod -aG groupname username

# 从组中移除用户
sudo gpasswd -d username groupname

# 设置组管理员
sudo gpasswd -A user1,user2 groupname

# 设置组密码（允许非组成员临时加入）
sudo gpasswd groupname

# 用户临时切换主组（需要密码）
newgrp groupname
```

## 常用组说明

| 组名 | 说明 |
|------|------|
| `wheel` | Arch/RHEL 系统中的 sudo 组 |
| `sudo` | Debian/Ubuntu 系统中的 sudo 组 |
| `docker` | 允许运行 Docker 命令 |
| `video` | 访问视频设备 |
| `audio` | 访问音频设备 |
| `input` | 访问输入设备 |
| `disk` | 直接访问磁盘 |
| `lp` | 打印相关权限 |
| `network` | 网络配置权限 |
| `storage` | 存储设备权限 |
| `power` | 电源管理权限 |

## sudo 配置

### 将用户加入 sudo 组

```bash
# Arch/RHEL 系统
sudo usermod -aG wheel username

# Debian/Ubuntu 系统
sudo usermod -aG sudo username
```

### 编辑 sudoers 文件

```bash
# 必须使用 visudo，不能直接编辑
sudo visudo

# 或指定编辑器
sudo EDITOR=vim visudo
```

### 常用 sudoers 配置

```
# 允许 wheel 组执行所有命令
%wheel ALL=(ALL:ALL) ALL

# 允许 wheel 组免密码执行所有命令
%wheel ALL=(ALL:ALL) NOPASSWD:ALL

# 允许特定用户执行所有命令
username ALL=(ALL:ALL) ALL

# 允许特定用户免密码执行所有命令
username ALL=(ALL:ALL) NOPASSWD:ALL

# 允许特定用户执行特定命令
username ALL=(ALL:ALL) /usr/bin/systemctl restart nginx, /usr/bin/systemctl status nginx

# 允许特定用户免密码执行特定命令
username ALL=(ALL:ALL) NOPASSWD: /usr/bin/pacman -Syu
```

## 查看信息

```bash
# 当前用户信息
id
whoami
groups

# 查看指定用户信息
id username
groups username
finger username  # 需要安装 finger

# 查看 /etc/passwd 格式
# username:password:UID:GID:comment:home:shell
cat /etc/passwd

# 查看 /etc/shadow（密码哈希）
sudo cat /etc/shadow

# 查看 /etc/group 格式
# groupname:password:GID:member1,member2
cat /etc/group

# 查看登录历史
last
lastb  # 失败登录

# 当前登录用户
who
w
```

## 常见问题

### 1. 用户家目录没有创建

```bash
# 手动创建家目录
sudo mkdir /home/username

# 复制默认配置
sudo cp -r /etc/skel/. /home/username/

# 修改所有者
sudo chown -R username:username /home/username

# 或使用命令
sudo mkhomedir_helper username
```

### 2. 切换用户

```bash
# 切换到用户（不加载环境）
su username

# 切换到用户并加载环境
su - username

# 以用户身份执行单条命令
su - username -c "ls -la"
```

### 3. 批量创建用户

```bash
# 从文件批量创建
while read user; do
    sudo useradd -m "$user"
    echo "$user:password" | sudo chpasswd
done < users.txt
```

## 快捷命令

```bash
# 添加到 .bashrc
alias useradd='sudo useradd'
alias userdel='sudo userdel'
alias usermod='sudo usermod'
alias groupadd='sudo groupadd'
alias groupdel='sudo groupdel'
alias groupmod='sudo groupmod'
alias passwd='sudo passwd'
```

## 一句话总结

用户管理：`useradd -m` 创建，`passwd` 设密码，`usermod` 修改，`userdel -r` 删除。组管理：`groupadd` 创建，`usermod -aG` 加用户，`groupdel` 删除。sudo 权限通过 `visudo` 配置 `/etc/sudoers`。
