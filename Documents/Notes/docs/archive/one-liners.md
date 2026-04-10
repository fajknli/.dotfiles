# 一行命令

## 远程文件传输

### rsync（指定端口）

```bash
rsync -avz -e "ssh -p 26059" frp_0.64.0_linux_amd64.tar.gz root@119.188.232.23:/root/
```

| 参数 | 说明 |
|------|------|
| `-a` | 归档模式（保留文件信息） |
| `-v` | 详细输出 |
| `-z` | 压缩传输 |
| `-e` | 指定 SSH 命令（可带端口） |

### scp（指定端口）

```bash
scp -P 26059 frp_0.64.0_linux_amd64.tar.gz root@119.188.232.23:/root/
```

### sftp（交互式）

```bash
sftp -P 26059 root@119.188.232.23

# 交互式命令
put frp_0.64.0_linux_amd64.tar.gz /root/
exit
```

### 通过 cat + ssh 传输

```bash
cat frp_0.64.0_linux_amd64.tar.gz | ssh -p 26059 root@119.188.232.23 "cat > /root/frp_0.64.0_linux_amd64.tar.gz"
```

## Arch Linux 换源

### 使用 reflector 生成镜像列表

```bash
sudo reflector --country China --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
```

| 参数 | 说明 |
|------|------|
| `--country China` | 只使用中国镜像 |
| `--age 12` | 只使用最近12小时更新的镜像 |
| `--protocol https` | 只使用 HTTPS 协议 |
| `--sort rate` | 按速度排序 |
| `--save` | 保存到文件 |

## 文件操作

### 快速备份文件

```bash
cp file.txt{,.bak}
```

### 创建目录并进入

```bash
mkdir -p /path/to/dir && cd $_
```

### 查找并删除空文件

```bash
find . -type f -empty -delete
```

### 批量重命名（添加前缀）

```bash
for f in *.txt; do mv "$f" "prefix_$f"; done
```

### 批量重命名（替换扩展名）

```bash
for f in *.txt; do mv "$f" "${f%.txt}.md"; done
```

### 统计目录下文件数量

```bash
ls -1 | wc -l
```

### 统计代码行数

```bash
find . -name "*.py" | xargs wc -l | tail -1
```

### 查看目录下最大的10个文件

```bash
find . -type f -exec du -h {} + | sort -rh | head -10
```

### 快速清空文件内容

```bash
> file.log
```

### 查看压缩文件内容（不解压）

```bash
zcat file.gz | head
zless file.gz
```

## 进程管理

### 查看端口占用

```bash
ss -tlnp | grep :8080
lsof -i :8080
```

### 杀掉所有匹配的进程

```bash
pkill node
killall node
```

### 杀掉占用端口的进程

```bash
lsof -ti :8080 | xargs kill -9
```

### 查看实时日志并过滤

```bash
tail -f app.log | grep ERROR
tail -f app.log | grep --color=always ERROR
```

### 监控命令输出变化

```bash
watch -n 1 'df -h'
watch -d 'ps aux | grep nginx'
```

## 网络相关

### 快速查看公网 IP

```bash
curl ifconfig.me
curl ipinfo.io/ip
```

### 测试网络速度

```bash
curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3 -
```

### 快速启动 HTTP 服务器

```bash
python3 -m http.server 8000
python -m SimpleHTTPServer 8000  # Python 2
```

### 下载文件并解压

```bash
curl -L https://example.com/file.tar.gz | tar xz
```

### 测试 DNS 解析

```bash
dig +short google.com
nslookup google.com
```

## 文本处理

### 批量替换文件内容

```bash
sed -i 's/old/new/g' *.txt
```

### 删除空行

```bash
sed -i '/^$/d' file.txt
```

### 删除注释行

```bash
sed -i '/^#/d' file.txt
```

### 提取列

```bash
awk '{print $1, $3}' file.txt
cut -d',' -f1,3 file.csv
```

### 统计重复行

```bash
sort file.txt | uniq -c | sort -rn
```

### 查看两个文件共有行

```bash
comm -12 file1.txt file2.txt
```

## 系统信息

### 查看内存使用

```bash
free -h
```

### 查看磁盘使用

```bash
df -h
```

### 查看系统负载

```bash
uptime
cat /proc/loadavg
```

### 查看内核版本

```bash
uname -r
```

### 查看 CPU 信息

```bash
lscpu
grep "model name" /proc/cpuinfo | head -1
```

### 查看系统启动时间

```bash
who -b
uptime -s
```

## 开发相关

### 快速生成随机密码

```bash
openssl rand -base64 12
date +%s | sha256sum | base64 | head -c 12
```

### 生成 UUID

```bash
uuidgen
cat /proc/sys/kernel/random/uuid
```

### 格式化 JSON

```bash
echo '{"name":"test"}' | jq .
curl -s https://api.example.com | jq .
```

### 查看命令历史 TOP 10

```bash
history | awk '{print $2}' | sort | uniq -c | sort -rn | head -10
```

## 快捷操作

### 进入上一个目录

```bash
cd -
```

### 重复上一条命令

```bash
!!
```

### 重复上一条命令并加 sudo

```bash
sudo !!
```

### 引用上一条命令的最后一个参数

```bash
echo last_param
!$
```

### 替换上一条命令中的字符串

```bash
grep foo file.txt
^foo^bar^
# 执行 grep bar file.txt
```

## 一句话总结

一行命令的核心是组合：`|` 管道串联，`&&` 条件执行，`$()` 命令替换，`<()` 进程替换。常用场景：文件批量操作、进程管理、网络测试、文本处理。掌握这些可以大幅提高命令行效率。
