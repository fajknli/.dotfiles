# curl 命令详解

## 一句话理解 curl

curl 是网络请求工具，用来**发送 HTTP 请求**、下载文件、测试 API。

```bash
# 获取网页内容
curl https://example.com

# 下载文件
curl -O https://example.com/file.zip

# 发送 JSON 数据
curl -X POST -H "Content-Type: application/json" -d '{"name":"test"}' https://api.example.com
```

## 最常用场景

### 1. 查看网页内容

```bash
# 获取网页源码
curl https://example.com

# 显示响应头
curl -I https://example.com

# 显示请求和响应详情
curl -v https://example.com

# 跟随重定向
curl -L https://example.com
```

### 2. 下载文件

```bash
# 下载并保存为原始文件名
curl -O https://example.com/file.zip

# 指定保存文件名
curl -o myfile.zip https://example.com/file.zip

# 断点续传
curl -C - -O https://example.com/largefile.zip

# 限速下载（500KB/s）
curl --limit-rate 500k -O https://example.com/file.zip
```

### 3. 测试 API

```bash
# GET 请求
curl https://api.example.com/users

# POST 请求（表单）
curl -X POST -d "name=test&age=18" https://api.example.com/users

# POST 请求（JSON）
curl -X POST -H "Content-Type: application/json" -d '{"name":"test","age":18}' https://api.example.com/users

# PUT 请求
curl -X PUT -d "name=new" https://api.example.com/users/1

# DELETE 请求
curl -X DELETE https://api.example.com/users/1
```

## 核心参数

| 参数 | 说明 | 例子 |
|------|------|------|
| `-X` | 指定请求方法 | `-X POST` |
| `-H` | 添加请求头 | `-H "Content-Type: application/json"` |
| `-d` | 发送数据（POST） | `-d "key=value"` |
| `-O` | 保存为原始文件名 | `-O https://example.com/file` |
| `-o` | 指定保存文件名 | `-o output.txt` |
| `-I` | 只显示响应头 | `-I https://example.com` |
| `-v` | 详细输出（调试用） | `-v https://example.com` |
| `-L` | 跟随重定向 | `-L https://example.com` |
| `-C -` | 断点续传 | `-C - -O file` |
| `-b` | 发送 Cookie | `-b "name=value"` |
| `-c` | 保存 Cookie | `-c cookie.txt` |
| `-A` | 设置 User-Agent | `-A "Mozilla/5.0"` |
| `-e` | 设置 Referer | `-e https://google.com` |
| `--limit-rate` | 限速 | `--limit-rate 500k` |
| `--max-time` | 超时时间（秒） | `--max-time 30` |
| `--connect-timeout` | 连接超时（秒） | `--connect-timeout 10` |
| `-k` | 跳过 SSL 证书验证 | `-k https://self-signed.bad` |

## 实际例子

### 1. 测试接口连通性

```bash
# 检查网站是否正常
curl -I https://example.com
# 返回 200 表示正常

# 检查响应时间
curl -o /dev/null -s -w '连接时间：%{time_connect}s\n总时间：%{time_total}s\n' https://example.com

# 检查状态码
curl -s -o /dev/null -w '%{http_code}' https://example.com
```

### 2. 发送 JSON 数据

```bash
# 标准 JSON POST
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"123456"}'

# 从文件读取 JSON
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d @data.json
```

### 3. 添加认证

```bash
# Basic 认证
curl -u username:password https://api.example.com

# Bearer Token 认证
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com

# API Key 认证
curl -H "X-API-Key: YOUR_KEY" https://api.example.com
```

### 4. 携带 Cookie

```bash
# 发送 Cookie
curl -b "session_id=abc123" https://example.com

# 发送 Cookie 文件
curl -b cookies.txt https://example.com

# 保存响应 Cookie
curl -c cookies.txt https://example.com/login -d "user=test&pass=123"
```

### 5. 设置请求头

```bash
# 设置 User-Agent（伪装浏览器）
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" https://example.com

# 设置 Referer
curl -e "https://google.com" https://example.com

# 多个请求头
curl -H "Accept: application/json" -H "X-Custom: value" https://api.example.com
```

### 6. 下载文件（你之前用的）

```bash
# 下载 v2raya 安装脚本
wget -qO- https://hubmirror.v2raya.org/v2rayA/v2rayA-installer/raw/main/installer.sh

# 用 curl 代替 wget
curl -fsSL https://hubmirror.v2raya.org/v2rayA/v2rayA-installer/raw/main/installer.sh
```

### 7. 测试上传文件

```bash
# 上传文件（multipart/form-data）
curl -X POST -F "file=@/path/to/file.txt" https://example.com/upload

# 上传多个文件
curl -X POST -F "file1=@a.txt" -F "file2=@b.txt" https://example.com/upload
```

## 输出格式控制

### 只显示特定信息（-w）

```bash
# 只显示状态码
curl -s -o /dev/null -w '%{http_code}\n' https://example.com

# 显示多种信息
curl -s -o /dev/null -w '状态码：%{http_code}\n总时间：%{time_total}s\n' https://example.com

# 常用变量
# %{http_code}      状态码
# %{time_total}     总时间
# %{time_connect}   连接时间
# %{size_download}  下载大小
# %{speed_download} 下载速度
```

### 静默模式（-s）

```bash
# 不显示进度条和错误
curl -s https://example.com

# 静默但显示错误
curl -sS https://example.com

# 只输出响应体，不输出其他
curl -s https://example.com
```

## 与 wget 对比

| 场景 | curl | wget |
|------|------|------|
| 查看网页内容 | ✅ 默认输出到终端 | ❌ 默认保存到文件 |
| 下载文件 | `curl -O` | `wget` |
| 测试 API | ✅ 最常用 | ❌ 不常用 |
| 递归下载 | ❌ 不支持 | ✅ `wget -r` |
| 断点续传 | `curl -C -` | `wget -c` |
| 发送 POST | ✅ 原生支持 | ❌ 需要 `--post-data` |

## 常用组合速查

| 目的 | 命令 |
|------|------|
| GET 请求 | `curl https://api.example.com` |
| POST 表单 | `curl -X POST -d "key=value" https://api.example.com` |
| POST JSON | `curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://api.example.com` |
| 下载文件 | `curl -O https://example.com/file` |
| 指定文件名下载 | `curl -o output.zip https://example.com/file.zip` |
| 只查看响应头 | `curl -I https://example.com` |
| 查看详细请求 | `curl -v https://example.com` |
| 跟随重定向 | `curl -L https://example.com` |
| 添加认证头 | `curl -H "Authorization: Bearer TOKEN" https://api.example.com` |
| Basic 认证 | `curl -u user:pass https://api.example.com` |
| 跳过 SSL 验证 | `curl -k https://self-signed.bad` |
| 设置超时 | `curl --max-time 30 https://example.com` |

## 脚本示例

### 健康检查脚本

```bash
#!/bin/bash
# health_check.sh

URL="https://api.example.com/health"

if curl -s -f -o /dev/null "$URL"; then
    echo "服务正常"
else
    echo "服务异常"
    # 发送告警...
fi
```

### 等待服务启动

```bash
#!/bin/bash
# wait_for_service.sh

URL="http://localhost:8080/health"

echo "等待服务启动..."
until curl -s -f "$URL" > /dev/null; do
    sleep 1
done
echo "服务已启动"
```

### 带重试的请求

```bash
#!/bin/bash
# retry.sh

MAX_RETRIES=3
RETRY=0
URL="https://api.example.com/data"

while [ $RETRY -lt $MAX_RETRIES ]; do
    if curl -s -f "$URL" -o response.json; then
        echo "请求成功"
        break
    else
        RETRY=$((RETRY + 1))
        echo "请求失败，重试 $RETRY/$MAX_RETRIES..."
        sleep 2
    fi
done
```

## 快捷命令别名

```bash
# 添加到 .bashrc
alias curlh='curl -I'                    # 只看头
alias curlv='curl -v'                    # 详细模式
alias curlj='curl -H "Content-Type: application/json"'  # JSON 请求
alias curltime='curl -o /dev/null -s -w "连接：%{time_connect}s\n总时间：%{time_total}s\n"'

# 使用
curlh example.com
curlj -X POST -d '{"name":"test"}' api.example.com
curltime example.com
```

## 一句话总结

curl 核心：`curl URL` 看内容，`curl -O URL` 下载文件，`curl -I URL` 看响应头，`curl -X POST -d "data" URL` 发 POST 请求。测试 API 是 curl 最擅长的。
