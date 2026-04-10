# Shell 文本处理

## grep - 文本搜索

### 基本用法

```sh
# 搜索字符串
grep "error" log.txt

# 搜索多个文件
grep "pattern" file1.txt file2.txt

# 递归搜索目录
grep -r "pattern" /var/log/

# 忽略大小写
grep -i "error" log.txt

# 显示行号
grep -n "error" log.txt

# 显示匹配行前后内容
grep -B 2 "error" log.txt   # 前2行
grep -A 3 "error" log.txt   # 后3行
grep -C 2 "error" log.txt   # 前后2行
```

### 反向匹配

```sh
# 显示不匹配的行
grep -v "debug" log.txt

# 排除空行和注释
grep -v '^#' config.conf | grep -v '^$'
```

### 正则表达式

```sh
# 基本正则（默认）
grep "^[0-9]" file.txt        # 以数字开头的行
grep "error$" file.txt        # 以 error 结尾的行
grep "error\|warning" file.txt  # 或（需要转义）

# 扩展正则（-E）
grep -E "error|warning" file.txt
grep -E "[0-9]{3,5}" file.txt

# 固定字符串（-F，快速匹配）
grep -F ".*" file.txt         # 搜索字面量 .*

# 只输出匹配部分（-o）
grep -o "[0-9]\+" file.txt
```

### 常用选项

| 选项 | 说明 |
|------|------|
| `-i` | 忽略大小写 |
| `-v` | 反向匹配 |
| `-n` | 显示行号 |
| `-c` | 只计数 |
| `-l` | 只输出文件名 |
| `-L` | 输出不匹配的文件名 |
| `-r` | 递归搜索 |
| `-w` | 匹配整个单词 |
| `-x` | 匹配整行 |
| `-q` | 安静模式（不输出） |

```sh
# 统计匹配行数
grep -c "error" log.txt

# 只输出文件名
grep -l "error" *.log

# 匹配整个单词
grep -w "to" text.txt  # 匹配 "to"，不匹配 "today"

# 安静模式（只检查退出码）
if grep -q "error" log.txt; then
    echo "发现错误"
fi
```

## sed - 流编辑器

### 替换文本

```sh
# 基本替换（只替换第一个）
sed 's/old/new/' file.txt

# 替换所有
sed 's/old/new/g' file.txt

# 指定行替换
sed '3s/old/new/' file.txt      # 第3行
sed '1,5s/old/new/g' file.txt   # 1-5行
sed '/pattern/s/old/new/' file.txt  # 匹配的行

# 原文件修改
sed -i 's/old/new/g' file.txt
sed -i.bak 's/old/new/g' file.txt  # 备份
```

### 删除行

```sh
# 删除指定行
sed '3d' file.txt           # 删除第3行
sed '1,5d' file.txt         # 删除1-5行
sed '/pattern/d' file.txt   # 删除匹配的行
sed '/^$/d' file.txt        # 删除空行
sed '/^#/d' file.txt        # 删除注释行
```

### 打印行

```sh
# 打印指定行
sed -n '3p' file.txt        # 打印第3行
sed -n '1,5p' file.txt      # 打印1-5行
sed -n '/pattern/p' file.txt # 打印匹配的行

# 打印行号
sed -n '=' file.txt
```

### 插入和追加

```sh
# 在行前插入
sed '2i\新行内容' file.txt

# 在行后追加
sed '2a\新行内容' file.txt

# 替换整行
sed '3c\新内容' file.txt
```

### 多个编辑

```sh
# 使用 -e 或分号
sed -e 's/old/new/' -e 's/foo/bar/' file.txt
sed 's/old/new/; s/foo/bar/' file.txt

# 使用脚本文件
sed -f script.sed file.txt
```

### 实际示例

```sh
# 删除所有注释和空行
sed -e 's/#.*//' -e '/^$/d' config.conf

# 提取 IP 地址
sed -n 's/.*addr:\([0-9.]*\).*/\1/p' ifconfig.txt

# 首行添加内容
sed '1i\# 新头部' file.txt

# 尾行添加内容
sed '$a\# 新尾部' file.txt
```

## awk - 文本处理语言

### 基本用法

```sh
# 打印列
awk '{print $1}' file.txt      # 打印第一列
awk '{print $1, $3}' file.txt  # 打印第一和第三列
awk '{print NF}' file.txt      # 打印列数

# 指定分隔符
awk -F: '{print $1}' /etc/passwd
awk -F'[, ]' '{print $1}' file.txt

# 打印行号
awk '{print NR, $0}' file.txt
```

### 条件匹配

```sh
# 匹配模式
awk '/error/ {print}' log.txt
awk '$3 > 100 {print}' data.txt
awk '$1 == "root" {print}' /etc/passwd

# 范围匹配
awk 'NR>=10 && NR<=20' file.txt

# 开始和结束
awk 'BEGIN {print "开始"} {print} END {print "结束"}' file.txt
```

### 内置变量

| 变量 | 说明 |
|------|------|
| `$0` | 整行 |
| `$1-$n` | 第 n 列 |
| `NF` | 列数 |
| `NR` | 行号 |
| `FS` | 输入分隔符 |
| `OFS` | 输出分隔符 |
| `RS` | 输入行分隔符 |

```sh
# 修改输出分隔符
awk 'BEGIN {OFS=","} {print $1, $2}' file.txt

# 使用不同的行分隔符
awk 'BEGIN {RS="\n\n"} {print}' file.txt
```

### 计算和统计

```sh
# 求和
awk '{sum += $1} END {print sum}' numbers.txt

# 平均值
awk '{sum += $1; count++} END {print sum/count}' numbers.txt

# 最大值
awk '$1 > max {max = $1} END {print max}' numbers.txt

# 计数
awk '/error/ {count++} END {print count}' log.txt
```

### 格式化输出

```sh
# printf 格式化
awk '{printf "%-10s %5d\n", $1, $2}' data.txt

# 对齐输出
awk '{printf "行号: %4d 内容: %s\n", NR, $0}' file.txt
```

### 条件判断

```sh
# if-else
awk '{if ($1 > 10) print "大"; else print "小"}' file.txt

# 三元运算符
awk '{print ($1 > 10 ? "大" : "小")}' file.txt
```

### 实际示例

```sh
# 统计日志中错误数量
awk '/ERROR/ {count[$2]++} END {for(i in count) print i, count[i]}' log.txt

# 计算 CSV 文件平均值
awk -F, '{sum+=$3; count++} END {printf "平均: %.2f\n", sum/count}' data.csv

# 提取特定字段
ps aux | awk '$3 > 10 {print $2, $3, $11}'  # CPU > 10%

# 分析访问日志
awk '{ip[$1]++} END {for(i in ip) print i, ip[i]}' access.log | sort -k2 -rn | head -10
```

## cut - 列提取

```sh
# 按字符位置
cut -c1-10 file.txt      # 前10个字符
cut -c1,3,5 file.txt     # 第1,3,5个字符

# 按分隔符
cut -d: -f1 /etc/passwd  # 第一列（冒号分隔）
cut -d, -f2,4 file.csv   # 第2和第4列

# 指定输出分隔符
cut -d: -f1,6 --output-delimiter='|' /etc/passwd

# 排除列
cut -d: -f1- --complement -f2 /etc/passwd  # 排除第2列
```

## sort - 排序

```sh
# 基本排序
sort file.txt              # 升序
sort -r file.txt           # 降序

# 数字排序
sort -n numbers.txt
sort -nr numbers.txt

# 按列排序
sort -k2 file.txt          # 按第2列
sort -k2,2 file.txt        # 精确第2列
sort -t: -k3n /etc/passwd  # 按第3列数字排序

# 去重
sort -u file.txt           # 排序并去重

# 忽略大小写
sort -f file.txt

# 人类可读格式
sort -h file.txt           # 1K, 2M, 3G 等
```

## uniq - 去重

```sh
# 基本去重（需要先排序）
sort file.txt | uniq

# 只显示重复行
sort file.txt | uniq -d

# 只显示不重复的行
sort file.txt | uniq -u

# 显示重复次数
sort file.txt | uniq -c
sort file.txt | uniq -c | sort -rn  # 按频率排序

# 忽略前N个字符
uniq -s 2 file.txt
```

## wc - 统计

```sh
# 行数
wc -l file.txt

# 单词数
wc -w file.txt

# 字符数
wc -c file.txt

# 所有统计
wc file.txt

# 多个文件
wc -l *.txt
```

## tr - 字符转换

```sh
# 大小写转换
echo "hello" | tr 'a-z' 'A-Z'   # HELLO
echo "HELLO" | tr 'A-Z' 'a-z'   # hello

# 删除字符
echo "hello123" | tr -d '0-9'   # hello

# 压缩重复字符
echo "hello    world" | tr -s ' '  # hello world

# 替换换行符
cat file.txt | tr '\n' ' '

# 删除非打印字符
tr -cd '\11\12\15\40-\176' < binary.bin
```

## 实际应用示例

### 日志分析脚本

```sh
#!/bin/sh

# 统计日志中的错误类型
grep "ERROR" app.log | \
    sed 's/.*ERROR: //' | \
    sort | \
    uniq -c | \
    sort -rn | \
    head -10
```

### CSV 处理

```sh
#!/bin/sh

# 提取 CSV 中的特定列并计算总和
cut -d, -f3 data.csv | \
    tail -n +2 | \
    awk '{sum+=$1} END {print "总和:", sum}'
```

### 配置解析

```sh
#!/bin/sh

# 解析 INI 配置文件
awk -F= '/^[^#]/ {gsub(/^[ \t]+|[ \t]+$/, "", $1); print $1}' config.ini
```

### 进程监控

```sh
#!/bin/sh

# 查找 CPU 占用最高的进程
ps aux | \
    awk 'NR>1 {print $3, $11}' | \
    sort -k1 -rn | \
    head -5
```

### 文本格式化

```sh
#!/bin/sh

# 格式化输出为表格
printf "%-20s %10s\n" "名称" "价格"
echo "-------------------------"
awk '{printf "%-20s %10.2f\n", $1, $2}' products.txt
```

### 批量重命名（文本处理组合）

```sh
#!/bin/sh

# 将文件名中的空格替换为下划线
for file in *" "*; do
    newname=$(echo "$file" | tr ' ' '_')
    mv "$file" "$newname"
done
```
