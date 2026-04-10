# frp - 内网穿透工具

## 一句话理解

frp（Fast Reverse Proxy）是一个内网穿透工具，将内网服务暴露到公网。

```bash
# 服务端
./frps -c frps.toml

# 客户端
./frpc -c frpc.toml
```

## 配置示例

### 服务端配置 (frps.toml)

```toml
# 绑定端口（客户端连接端口）
bindPort = 7000

# Web 管理界面（可选）
webServer.addr = "0.0.0.0"
webServer.port = 7500
webServer.user = "admin"
webServer.password = "admin123"

# 日志
log.to = "./frps.log"
log.level = "info"
log.maxDays = 3
```

### 客户端配置 (frpc.toml)

```toml
# 服务端地址
serverAddr = "your-server.com"
serverPort = 7000

# 认证（可选）
auth.method = "token"
auth.token = "your-token"

# 代理配置
[[proxies]]
name = "ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000

[[proxies]]
name = "web"
type = "tcp"
localIP = "127.0.0.1"
localPort = 8080
remotePort = 8080
```

## 常用场景

### 1. 暴露 SSH 服务

```toml
[[proxies]]
name = "ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 2222
```

```bash
# 连接
ssh -p 2222 user@your-server.com
```

### 2. 暴露 HTTP 服务

```toml
[[proxies]]
name = "web"
type = "tcp"
localIP = "127.0.0.1"
localPort = 80
remotePort = 8080
```

### 3. 暴露内网多端口

```toml
[[proxies]]
name = "ssh"
type = "tcp"
localIP = "192.168.1.10"
localPort = 22
remotePort = 6000

[[proxies]]
name = "rdp"
type = "tcp"
localIP = "192.168.1.20"
localPort = 3389
remotePort = 63389
```

### 4. 配置 systemd 服务

```ini
# /etc/systemd/system/frpc.service
[Unit]
Description=frp client
After=network.target

[Service]
Type=simple
Restart=always
RestartSec=3
ExecStart=/usr/local/bin/frpc -c /etc/frp/frpc.toml

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable frpc
sudo systemctl start frpc
```

## 常用选项

| 选项 | 说明 | 默认值 |
|------|------|--------|
| `bindPort` | 服务端绑定端口 | 7000 |
| `serverAddr` | 服务端地址 | - |
| `serverPort` | 服务端端口 | 7000 |
| `name` | 代理名称（唯一） | - |
| `type` | 代理类型（tcp/udp/http/https） | tcp |
| `localIP` | 本地服务 IP | 127.0.0.1 |
| `localPort` | 本地服务端口 | - |
| `remotePort` | 远程映射端口 | - |
| `auth.token` | 认证令牌 | - |

## 常用命令

```bash
# 服务端
frps -c frps.toml          # 前台运行
frps -c frps.toml &        # 后台运行

# 客户端
frpc -c frpc.toml
frpc -c frpc.toml &        # 后台运行
frpc reload -c frpc.toml   # 热重载配置
frpc verify -c frpc.toml   # 验证配置

# 查看状态
frpc status -c frpc.toml
```

## 常见问题

### 1. 连接失败

```bash
# 检查服务端端口是否开放
telnet your-server.com 7000

# 检查防火墙
sudo ufw allow 7000/tcp
sudo iptables -A INPUT -p tcp --dport 7000 -j ACCEPT
```

### 2. 配置文件热重载失败

frp 0.40.0+ 支持热重载，需要配置 `allowPorts`：

```toml
allowPorts = [
  { start = 6000, end = 7000 }
]
```

### 3. 使用自定义域名

```toml
[[proxies]]
name = "web"
type = "http"
localPort = 80
customDomains = ["www.your-domain.com"]
```

## 一句话总结

frp 核心：服务端配置 `bindPort`，客户端配置 `serverAddr` 和 `serverPort`，代理配置 `type`、`localPort`、`remotePort`。常用 `tcp` 类型暴露 SSH、RDP 等，`http` 类型暴露 Web 服务。用 systemd 实现开机自启和自动重启。
