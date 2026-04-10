# systemd 服务编写

## 一句话理解

systemd service 是让程序作为系统服务运行的方式，可以设置开机自启、崩溃重启、依赖关系等。

```bash
# 服务文件存放位置
/etc/systemd/system/          # 用户自定义服务（优先级最高）
/usr/lib/systemd/system/      # 系统安装的服务

# 服务操作
sudo systemctl start myapp
sudo systemctl enable myapp
sudo systemctl status myapp
```

## 服务文件基本结构

一个完整的 service 文件包含三个部分：`[Unit]`、`[Service]`、`[Install]`

```ini
[Unit]
Description=服务描述
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/myapp --config /etc/myapp/config
User=myuser
Group=mygroup
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## [Unit] 部分 - 依赖和描述

| 参数 | 说明 | 例子 |
|------|------|------|
| `Description` | 服务描述 | `Description=My App Service` |
| `After` | 在哪些服务之后启动 | `After=network.target` |
| `Before` | 在哪些服务之前启动 | `Before=shutdown.target` |
| `Requires` | 强依赖（依赖挂了本服务也停） | `Requires=docker.service` |
| `Wants` | 弱依赖（依赖挂了本服务继续） | `Wants=network-online.target` |
| `Conflicts` | 冲突服务 | `Conflicts=apache2.service` |

```ini
# 示例：需要网络和Docker
[Unit]
Description=My Web App
After=network.target docker.service
Requires=docker.service
Wants=network-online.target
```

## [Service] 部分 - 核心配置

### Type 类型

| Type | 说明 | 适用场景 |
|------|------|----------|
| `simple` | 默认，ExecStart 进程就是主进程 | 大多数普通程序 |
| `forking` | 程序会 fork 后退出 | 传统守护进程（如 httpd） |
| `oneshot` | 执行一次就退出 | 初始化脚本、配置命令 |
| `notify` | 启动完成后会发通知 | 支持 systemd 通知的程序 |
| `idle` | 空闲时再启动 | 避免输出干扰登录 |

### 核心参数

| 参数 | 说明 | 例子 |
|------|------|------|
| `ExecStart` | 启动命令（必须绝对路径） | `ExecStart=/usr/bin/python3 /app/main.py` |
| `ExecStop` | 停止命令 | `ExecStop=/usr/bin/kill $MAINPID` |
| `ExecReload` | 重载命令 | `ExecReload=/bin/kill -HUP $MAINPID` |
| `Restart` | 重启策略 | `Restart=on-failure` |
| `RestartSec` | 重启等待秒数 | `RestartSec=5` |
| `User` | 运行用户 | `User=nobody` |
| `Group` | 运行组 | `Group=nogroup` |
| `WorkingDirectory` | 工作目录 | `WorkingDirectory=/opt/myapp` |
| `Environment` | 环境变量 | `Environment="PATH=/usr/bin"` |
| `EnvironmentFile` | 环境变量文件 | `EnvironmentFile=/etc/myapp/env` |
| `LimitNOFILE` | 最大文件打开数 | `LimitNOFILE=65535` |
| `TimeoutStartSec` | 启动超时 | `TimeoutStartSec=30` |
| `TimeoutStopSec` | 停止超时 | `TimeoutStopSec=10` |

### Restart 重启策略

| 值 | 说明 |
|------|------|
| `no` | 不自动重启（默认） |
| `always` | 总是重启 |
| `on-failure` | 非正常退出时重启（退出码非0） |
| `on-abnormal` | 异常退出时重启（信号、超时） |
| `on-abort` | 被信号终止时重启 |

### 环境变量设置

```ini
# 单个变量
Environment="JAVA_HOME=/usr/lib/jvm/java-11"

# 多个变量
Environment="JAVA_OPTS=-Xmx2G" "APP_ENV=production"

# 从文件加载
EnvironmentFile=/etc/default/myapp
```

## [Install] 部分 - 安装配置

| 参数 | 说明 |
|------|------|
| `WantedBy` | 被哪个 target 依赖，通常是 `multi-user.target` |
| `RequiredBy` | 强依赖的 target |
| `Also` | 安装时同时安装的其他服务 |

```ini
[Install]
WantedBy=multi-user.target
```

## 完整示例

### 示例1：普通程序

```ini
[Unit]
Description=My Python App
After=network.target

[Service]
Type=simple
User=myuser
Group=mygroup
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/main.py
Restart=on-failure
RestartSec=5
Environment="APP_ENV=production"
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
```

### 示例2：Java 应用

```ini
[Unit]
Description=Spring Boot App
After=network.target

[Service]
Type=simple
User=myuser
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/java -jar /opt/myapp/app.jar
ExecStop=/bin/kill $MAINPID
Restart=on-failure
RestartSec=10
Environment="JAVA_OPTS=-Xmx1G -Xms256M"
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
```

### 示例3：Forking 守护进程

```ini
[Unit]
Description=My Daemon
After=network.target

[Service]
Type=forking
User=daemon
PIDFile=/run/mydaemon.pid
ExecStart=/usr/sbin/mydaemon --daemon
ExecStop=/usr/sbin/mydaemon --stop
ExecReload=/usr/sbin/mydaemon --reload
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### 示例4：OneShot 脚本

```ini
[Unit]
Description=One-time Setup Script

[Service]
Type=oneshot
ExecStart=/usr/local/bin/setup.sh
ExecStart=/usr/local/bin/init-db.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

### 示例5：虚拟环境中的 Python

```ini
[Unit]
Description=Flask App
After=network.target

[Service]
Type=simple
User=myuser
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/venv/bin/python /opt/myapp/app.py
Restart=on-failure
RestartSec=5
Environment="FLASK_ENV=production"

[Install]
WantedBy=multi-user.target
```

## 常用 target 说明

| Target | 说明 |
|--------|------|
| `multi-user.target` | 多用户模式（正常启动） |
| `graphical.target` | 图形界面模式 |
| `network.target` | 网络已配置 |
| `network-online.target` | 网络已完全可用 |
| `time-sync.target` | 时间已同步 |
| `shutdown.target` | 关机 |
| `reboot.target` | 重启 |

## 服务文件操作

### 创建和启用

```bash
# 创建服务文件
sudo vim /etc/systemd/system/myapp.service

# 重新加载 systemd
sudo systemctl daemon-reload

# 启动服务
sudo systemctl start myapp

# 设置开机自启
sudo systemctl enable myapp

# 查看状态
sudo systemctl status myapp

# 查看日志
sudo journalctl -u myapp -f
```

### 覆盖默认配置

```bash
# 创建覆盖配置目录
sudo systemctl edit myapp

# 这会创建 /etc/systemd/system/myapp.service.d/override.conf

# 覆盖内容示例
[Service]
Environment="APP_ENV=development"
RestartSec=30

# 查看完整配置（包括覆盖）
systemctl cat myapp
```

### 禁用和删除

```bash
# 停止服务
sudo systemctl stop myapp

# 禁用开机自启
sudo systemctl disable myapp

# 删除服务文件
sudo rm /etc/systemd/system/myapp.service

# 重新加载
sudo systemctl daemon-reload
```

## 调试技巧

### 查看启动失败原因

```bash
# 查看详细状态
systemctl status myapp -l

# 查看日志
journalctl -u myapp -e

# 查看最近50行
journalctl -u myapp -n 50

# 实时查看
journalctl -u myapp -f
```

### 测试服务配置

```bash
# 检查是否有语法错误
systemd-analyze verify /etc/systemd/system/myapp.service

# 查看服务依赖树
systemd-analyze dot myapp | dot -Tsvg > deps.svg

# 查看启动时间
systemd-analyze blame
```

## 日志输出配置

```ini
[Service]
# 输出到 journal（默认）
StandardOutput=journal
StandardError=journal

# 输出到文件
StandardOutput=file:/var/log/myapp.log
StandardError=file:/var/log/myapp-error.log

# 输出到 /dev/null（丢弃）
StandardOutput=null
StandardError=null

# 追加到文件
StandardOutput=append:/var/log/myapp.log
```

## 安全加固

```ini
[Service]
# 限制访问
PrivateTmp=yes          # 独立临时目录
NoNewPrivileges=yes     # 禁止提升权限
ProtectSystem=strict    # 只读系统目录
ReadWritePaths=/var/lib/myapp /var/log/myapp

# 限制能力
CapabilityBoundingSet=CAP_NET_BIND_SERVICE

# 限制文件系统
ProtectHome=yes         # 禁止访问 /home
ProtectKernelTunables=yes
ProtectKernelModules=yes
```

## 一句话总结

systemd service 核心：`[Unit]` 定义依赖，`[Service]` 定义启动命令和用户，`[Install]` 定义开机自启。记住 `Type=simple` 最常用，`Restart=on-failure` 自动重启，`User` 不用 root。改完配置要 `systemctl daemon-reload`。
