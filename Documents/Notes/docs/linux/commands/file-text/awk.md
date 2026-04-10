# awk 命令详解

## 一句话理解 awk

awk 是一个文本处理工具，擅长**按列处理数据**。它会自动按空格或制表符把每行拆成多个字段。

```bash
awk '{print $1, $3}' file.txt
# $1 表示第一列，$2 第二列，以此类推
```

## 核心概念

| 概念 | 说明 | 例子 |
|------|------|------|
| `$0` | 整行内容 | `{print $0}` |
| `$1, $2, $3...` | 第1、2、3列 | `{print $1, $3}` |
| `$NF` | 最后一列 | `{print $NF}` |
| `NF` | 当前行的列数 | `{print NF}` |
| `NR` | 当前行号 | `{print NR, $0}` |
| `FS` | 输入分隔符（默认空格） | `-F,` 或 `BEGIN{FS=","}` |
| `OFS` | 输出分隔符（默认空格） | `BEGIN{OFS=","}` |

## 基本语法

```bash
awk '动作' 文件名
awk '条件 {动作}' 文件名
awk -F '分隔符' '动作' 文件名
```

## 常用场景

### 1. 打印指定列

```bash
# 打印第1列和第3列
awk '{print $1, $3}' file.txt

# 打印第2列到最后一列
awk '{for(i=2;i<=NF;i++) printf "%s ", $i; print ""}' file.txt

# 打印最后一列
awk '{print $NF}' file.txt
```

### 2. 改变分隔符

```bash
# CSV 文件（逗号分隔）
awk -F ',' '{print $1, $2}' data.csv

# 使用多个分隔符（空格和冒号）
awk -F '[: ]+' '{print $1, $2}' /etc/passwd

# 制表符分隔
awk -F '\t' '{print $1}' file.tsv
```

### 3. 条件过滤

```bash
# 第3列大于100的行
awk '$3 > 100' file.txt

# 第1列等于 "root"
awk '$1 == "root"' /etc/passwd

# 第2列包含 "error"
awk '$2 ~ /error/' app.log

# 行号大于10
awk 'NR > 10' file.txt

# 组合条件
awk '$3 > 100 && $4 == "OK"' file.txt
```

### 4. 计算统计

```bash
# 求和（第3列）
awk '{sum += $3} END {print sum}' file.txt

# 求平均值
awk '{sum += $3} END {print sum/NR}' file.txt

# 求最大值
awk 'max < $3 {max = $3} END {print max}' file.txt

# 计数
awk '/error/ {count++} END {print count}' app.log
```

### 5. 格式化输出

```bash
# 指定输出分隔符
awk 'BEGIN{OFS=","} {print $1, $3}' file.txt

# 添加表头
awk 'BEGIN{print "名称,数量"} {print $1 "," $3}' file.txt

# 对齐输出
awk '{printf "%-10s %5d\n", $1, $3}' file.txt
```

## 实际例子

### 处理日志文件

```bash
# 统计每种状态码的数量
awk '{count[$9]++} END {for(code in count) print code, count[code]}' access.log

# 提取特定时间段的日志（假设第4列是时间）
awk '$4 ~ /10:00:/ || $4 ~ /11:00:/' app.log

# 统计访问量最高的IP
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10
```

### 处理 /etc/passwd

```bash
# 打印用户名和家目录
awk -F ':' '{print $1, $6}' /etc/passwd

# 查找 UID 大于 1000 的用户
awk -F ':' '$3 >= 1000 {print $1, $3}' /etc/passwd

# 统计各 shell 的用户数
awk -F ':' '{count[$NF]++} END {for(shell in count) print shell, count[shell]}' /etc/passwd
```

### 处理 CSV 数据

```bash
# 交换第1列和第2列
awk -F ',' 'BEGIN{OFS=","} {print $2, $1, $3}' data.csv

# 计算平均值并添加新列
awk -F ',' '{avg = ($2 + $3 + $4)/3; print $0 "," avg}' scores.csv

# 过滤掉数值为空的行
awk -F ',' '$2 != "" && $3 != ""' data.csv
```

### 处理命令输出

```bash
# 查看磁盘使用率超过80%的分区
df -h | awk 'NR>1 && $5+0 > 80 {print $1, $5}'

# 查看内存使用情况
free -m | awk 'NR==2 {print "已用:", $3, "MB", "可用:", $4, "MB"}'

# 查看特定进程的PID
ps aux | awk '/nginx/ && !/grep/ {print $2}'
```

## BEGIN 和 END

| 关键字 | 说明 |
|--------|------|
| `BEGIN` | 处理文件前执行一次（放初始化代码） |
| `END` | 处理文件后执行一次（放汇总代码） |

```bash
# 完整结构
awk 'BEGIN {初始化} 逐行处理 {动作} END {收尾}' file.txt

# 例子：计算平均值
awk 'BEGIN{print "开始计算"} {sum+=$1} END{print "平均值:", sum/NR}' file.txt
```

## 常用内置变量

| 变量 | 说明 |
|------|------|
| `NR` | 当前行号 |
| `NF` | 当前行的列数 |
| `$0` | 整行内容 |
| `$1-$n` | 各列内容 |
| `FS` | 输入分隔符 |
| `OFS` | 输出分隔符 |
| `RS` | 输入记录分隔符（默认换行） |
| `ORS` | 输出记录分隔符（默认换行） |

## 常用模式匹配

```bash
# 正则匹配
awk '/^error/' app.log              # 以 error 开头的行
awk '$2 ~ /^[0-9]+$/' file.txt     # 第2列全是数字的行

# 数值比较
awk '$3 > 100' file.txt
awk '$3 >= 10 && $3 <= 20' file.txt

# 字符串比较
awk '$1 == "root"' /etc/passwd
awk '$1 != "root"' /etc/passwd

# 空值判断
awk '$2 == ""' file.txt            # 第2列为空
awk '$2 != ""' file.txt            # 第2列非空
```

## 内置函数

### 字符串函数

```bash
# 长度
awk '{print length($0)}' file.txt

# 转大写/小写
awk '{print toupper($1), tolower($2)}' file.txt

# 替换
awk '{gsub(/old/, "new", $0); print}' file.txt

# 截取
awk '{print substr($1, 2, 5)}' file.txt  # 从第2个字符取5个
```

### 数学函数

```bash
# 取整
awk '{print int($1)}' file.txt

# 开方
awk '{print sqrt($1)}' file.txt

# 取对数
awk '{print log($1)}' file.txt
```

## 一行命令速查

| 目的 | 命令 |
|------|------|
| 打印第1列和第3列 | `awk '{print $1, $3}'` |
| 打印最后一列 | `awk '{print $NF}'` |
| 打印行号 | `awk '{print NR, $0}'` |
| 打印行数 | `awk 'END{print NR}'` |
| 打印第3列大于100的行 | `awk '$3 > 100'` |
| 打印第1列等于"root"的行 | `awk '$1 == "root"'` |
| 打印第2列包含"error"的行 | `awk '$2 ~ /error/'` |
| 打印第10到第20行 | `awk 'NR>=10 && NR<=20'` |
| 打印不包含"error"的行 | `awk '!/error/'` |
| 对第3列求和 | `awk '{sum+=$3} END{print sum}'` |
| 求第3列平均值 | `awk '{sum+=$3} END{print sum/NR}'` |
| 找出第3列最大值 | `awk 'max<$3{max=$3} END{print max}'` |
| 统计各值的出现次数 | `awk '{count[$1]++} END{for(k in count) print k, count[k]}'` |

## 与 cut、sed、grep 的对比

| 场景 | awk | 替代方案 |
|------|-----|----------|
| 提取第1列 | `awk '{print $1}'` | `cut -d' ' -f1` |
| 按逗号分隔提取 | `awk -F',' '{print $1}'` | `cut -d',' -f1` |
| 条件过滤 | `awk '$3>100'` | `grep` 不够用 |
| 求和统计 | `awk '{sum+=$1} END{print sum}'` | 需要组合命令 |
| 复杂列操作 | `awk '{print $2,$1}'` | `cut` 做不到 |

## 一句话总结

awk 是**按列处理数据**的工具，当你需要提取特定列、按条件过滤列、或对列进行统计计算时用 awk。`cut` 能做的不需要 awk，需要条件判断或计算时必须用 awk。
