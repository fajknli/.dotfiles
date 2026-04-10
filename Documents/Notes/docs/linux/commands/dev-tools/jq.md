# jq 命令详解

## 一句话理解 jq

jq 是命令行 JSON 处理工具，可以**解析、过滤、修改、格式化** JSON 数据。

```bash
# 格式化 JSON
echo '{"name":"test","age":18}' | jq .

# 提取字段
curl https://api.github.com/users/fajknli | jq '.name'

# 过滤数组
curl https://api.github.com/users/fajknli/repos | jq '.[] | .name'
```

## 最常用场景

### 1. 格式化 JSON

```bash
# 美化输出（带颜色）
echo '{"name":"test","age":18}' | jq .

# 紧凑输出（不美化）
echo '{"name":"test","age":18}' | jq -c .

# 从文件读取
jq . data.json
```

### 2. 提取字段

```bash
# 提取单个字段
jq '.name' data.json

# 提取多个字段
jq '{name, age}' data.json

# 嵌套字段
jq '.user.name' data.json

# 提取数组中的元素
jq '.users[0]' data.json
```

### 3. 过滤数组

```bash
# 找出 age 大于 18 的
jq '.[] | select(.age > 18)' data.json

# 找出 name 包含 "test" 的
jq '.[] | select(.name | contains("test"))' data.json

# 取前3个
jq '.[:3]' data.json

# 取后3个
jq '.[-3:]' data.json
```

## 核心语法

| 符号 | 说明 | 例子 |
|------|------|------|
| `.` | 当前对象 | `jq .` |
| `.name` | 获取 name 字段 | `jq '.name'` |
| `[]` | 数组索引 | `jq '.[0]'` |
| `.[]` | 遍历数组 | `jq '.[]'` |
| `|` | 管道 | `jq '.[] | .name'` |
| `select()` | 条件过滤 | `jq 'select(.age>18)'` |
| `{...}` | 构建对象 | `jq '{name, age}'` |
| `[...]` | 构建数组 | `jq '[.name]'` |
| `length` | 长度 | `jq 'length'` |
| `keys` | 所有键 | `jq 'keys'` |
| `has()` | 是否有某键 | `jq 'has("name")'` |

## 实际例子

### 1. API 调试

```bash
# 查看 GitHub 用户信息
curl -s https://api.github.com/users/fajknli | jq '{
  login,
  name,
  bio,
  public_repos,
  followers
}'

# 只提取需要的信息
curl -s https://api.github.com/users/fajknli/repos | jq '.[] | {name, stars: .stargazers_count, language}'

# 按 star 数排序
curl -s https://api.github.com/users/fajknli/repos | jq 'sort_by(-.stargazers_count) | .[] | {name, stars: .stargazers_count}'
```

### 2. 日志处理

```bash
# 从 JSON 日志中提取错误
cat app.log | jq 'select(.level == "ERROR")'

# 只提取消息和时间
cat app.log | jq '{time: .timestamp, msg: .message}'

# 统计错误数量
cat app.log | jq 'select(.level == "ERROR")' | wc -l

# 按级别分组统计
cat app.log | jq -r '.level' | sort | uniq -c
```

### 3. 配置文件处理

```bash
# 提取某个配置项
jq '.server.port' config.json

# 修改配置值（不写回文件）
jq '.server.port = 8080' config.json

# 修改后写回文件
jq '.server.port = 8080' config.json > tmp.json && mv tmp.json config.json

# 合并两个 JSON 文件
jq -s '.[0] * .[1]' file1.json file2.json
```

### 4. 数组操作

```bash
# 获取数组长度
jq 'length' data.json

# 获取所有 name
jq '.[].name' data.json

# 去重
jq 'unique' data.json

# 连接数组
jq 'add' data.json

# 分组
jq 'group_by(.category)' data.json
```

## 常用选项

| 选项 | 说明 |
|------|------|
| `-r` | 输出原始字符串（不带引号） |
| `-c` | 紧凑输出（不美化） |
| `-s` | 将多个输入合并为一个数组 |
| `-n` | 不读取输入，从 null 开始 |
| `-f` | 从文件读取过滤器 |
| `--arg` | 传递变量 |

```bash
# 原始输出（不带引号）
jq -r '.name' data.json

# 紧凑输出
jq -c '.users[]' data.json

# 传递变量
name="test"
jq --arg n "$name" '. | select(.name == $n)' data.json
```

## 复杂过滤

### 条件判断

```bash
# if-then-else
jq 'if .age > 18 then "adult" else "child" end' data.json

# 空值处理（// 默认值）
jq '.name // "unknown"' data.json

# 多个条件
jq 'select(.age > 18 and .active == true)' data.json
```

### 字符串操作

```bash
# 转大写
jq '.name | ascii_upcase' data.json

# 转小写
jq '.name | ascii_downcase' data.json

# 拼接
jq '.first + " " + .last' data.json

# 分割
jq '.tags | split(",")' data.json

# 正则匹配
jq '.email | test("@gmail\\.com$")' data.json
```

### 数学运算

```bash
# 加减乘除
jq '.price * .quantity' data.json

# 求和
jq 'map(.price) | add' data.json

# 平均值
jq 'map(.score) | add / length' data.json

# 最大值
jq 'map(.score) | max' data.json

# 最小值
jq 'map(.score) | min' data.json
```

## 实际数据示例

假设有如下 JSON：

```json
{
  "users": [
    {"name": "张三", "age": 25, "city": "北京"},
    {"name": "李四", "age": 30, "city": "上海"},
    {"name": "王五", "age": 20, "city": "北京"}
  ],
  "total": 3
}
```

常用操作：

```bash
# 获取所有用户名
jq '.users[].name' data.json
# "张三" "李四" "王五"

# 获取不带引号的用户名
jq -r '.users[].name' data.json
# 张三 李四 王五

# 获取年龄大于25的用户
jq '.users[] | select(.age > 25)' data.json

# 获取北京的用户名
jq '.users[] | select(.city == "北京") | .name' data.json

# 重新构建输出
jq '{names: [.users[].name], total: .total}' data.json

# 统计各城市人数
jq '.users | group_by(.city) | map({city: .[0].city, count: length})' data.json
```

## 一行命令速查

| 目的 | 命令 |
|------|------|
| 格式化 JSON | `jq .` |
| 提取字段 | `jq '.name'` |
| 提取嵌套字段 | `jq '.a.b.c'` |
| 提取数组第一个 | `jq '.[0]'` |
| 遍历数组 | `jq '.[]'` |
| 过滤条件 | `jq 'select(.age>18)'` |
| 取前N个 | `jq '[:10]'` |
| 数组长度 | `jq 'length'` |
| 去重 | `jq 'unique'` |
| 排序 | `jq 'sort'` |
| 反向排序 | `jq 'sort_by(-.field)'` |
| 只取某几个字段 | `jq '{a, b}'` |
| 删除字段 | `jq 'del(.field)'` |
| 添加字段 | `jq '.new = "value"'` |
| 合并两个 JSON | `jq -s '.[0] * .[1]'` |
| 输出不带引号 | `jq -r` |

## 脚本示例

### 检查 API 健康状态

```bash
#!/bin/bash
STATUS=$(curl -s https://api.example.com/health | jq -r '.status')
if [ "$STATUS" = "ok" ]; then
    echo "服务正常"
else
    echo "服务异常"
fi
```

### 提取所有邮箱

```bash
curl -s https://api.example.com/users | jq -r '.[].email' > emails.txt
```

### 监控指标

```bash
while true; do
    curl -s https://api.example.com/metrics | jq '{cpu, memory, requests: .requests_per_second}'
    sleep 5
done
```

## 一句话总结

jq 核心：`.` 代表当前对象，`|` 传递数据，`select()` 过滤，`-r` 去掉引号。最常用：`jq '.'` 格式化，`jq '.field'` 提取字段，`jq '.[] | .field'` 遍历数组取字段。
