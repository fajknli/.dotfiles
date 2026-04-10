# sed 命令详解

## 一句话理解 sed

sed 是一个流编辑器，它可以自动编辑文本文件。简单说就是：**找内容，改内容**。

```bash
sed 's/旧内容/新内容/' 文件名
```

## 最常用的场景：替换文本

### 替换每行第一个匹配

```bash
sed 's/old/new/' file.txt
```

### 替换每行所有匹配（加 g）

```bash
sed 's/old/new/g' file.txt
```

### 直接修改文件（加 -i）

```bash
sed -i 's/old/new/g' file.txt
```

### 修改前先备份

```bash
sed -i.bak 's/old/new/g' file.txt
# 会生成 file.txt.bak 备份文件
```

## 匹配指定行

### 只处理第3行

```bash
sed '3s/old/new/' file.txt
```

### 处理第2到第5行

```bash
sed '2,5s/old/new/' file.txt
```

### 处理包含特定内容的行

```bash
sed '/error/s/old/new/' file.txt
```

### 处理从 error 到 warning 之间的行

```bash
sed '/error/,/warning/s/old/new/' file.txt
```

## 删除行

### 删除第3行

```bash
sed '3d' file.txt
```

### 删除第2到第5行

```bash
sed '2,5d' file.txt
```

### 删除空行

```bash
sed '/^$/d' file.txt
```

### 删除包含 error 的行

```bash
sed '/error/d' file.txt
```

### 删除最后一行

```bash
sed '$d' file.txt
```

## 查看/打印行（配合 -n）

-n 表示不自动打印，只打印你指定的行。

### 只打印第3行

```bash
sed -n '3p' file.txt
```

### 只打印第2到第5行

```bash
sed -n '2,5p' file.txt
```

### 只打印包含 error 的行

```bash
sed -n '/error/p' file.txt
```

### 只打印最后一行

```bash
sed -n '$p' file.txt
```

## 插入和追加

### 在第2行前面插入一行

```bash
sed '2i\这是插入的内容' file.txt
```

### 在第2行后面追加一行

```bash
sed '2a\这是追加的内容' file.txt
```

### 在文件末尾追加

```bash
sed '$a\这是追加的内容' file.txt
```

## 实际例子

### 1. 修改配置文件

```bash
# 修改端口号
sed -i 's/port=8080/port=9090/' config.ini

# 取消注释某行（删除开头的#）
sed -i 's/^#enable=true/enable=true/' config.ini

# 注释某行（在行首加#）
sed -i 's/^debug=true/#debug=true/' config.ini
```

### 2. 清理日志文件

```bash
# 删除空行
sed -i '/^$/d' app.log

# 删除所有 INFO 级别的日志
sed -i '/INFO/d' app.log

# 只保留 ERROR 日志
sed -n '/ERROR/p' app.log > error.log
```

### 3. 处理 CSV 文件

```bash
# 交换第一列和第二列
sed -E 's/([^,]*),([^,]*)/\2,\1/' data.csv

# 给所有数字加引号
sed -E 's/([0-9]+)/"\1"/g' data.csv
```

### 4. 批量重命名文件内的内容

```bash
# 批量修改所有 .txt 文件中的 old 为 new
sed -i 's/old/new/g' *.txt
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `-i` | 直接修改文件 | `sed -i 's/old/new/' file` |
| `-i.bak` | 修改并备份 | `sed -i.bak 's/old/new/' file` |
| `-n` | 不自动打印 | `sed -n '3p' file` |
| `-E` | 使用扩展正则（不用转义括号） | `sed -E 's/(old)/new/'` |

## 常用命令速查

| 命令 | 说明 | 例子 |
|------|------|------|
| `s/old/new/` | 替换 | `sed 's/old/new/'` |
| `s/old/new/g` | 全局替换 | `sed 's/old/new/g'` |
| `d` | 删除行 | `sed '/error/d'` |
| `p` | 打印行 | `sed -n '3p'` |
| `i\` | 行前插入 | `sed '2i\hello'` |
| `a\` | 行后追加 | `sed '2a\hello'` |

## 常见坑

### 1. 忘记加 -i 以为修改了文件

```bash
# 这样只是输出到屏幕，文件没变
sed 's/old/new/' file.txt

# 加 -i 才会改文件
sed -i 's/old/new/' file.txt
```

### 2. 路径中有斜杠

```bash
# 错误：斜杠冲突
sed 's/usr/local/opt/' file

# 正确：换一个分隔符（用 | 或 #）
sed 's|/usr/local|/opt|' file
sed 's#/usr/local#/opt#' file
```

### 3. 忘记转义特殊字符

正则中的特殊字符：`.` `*` `[` `]` `^` `$` 等需要转义

```bash
# 匹配 IP 地址（点需要转义）
sed 's/127\.0\.0\.1/localhost/' file
```

## 一句话总结

sed 的核心就是 `s/旧/新/`（替换）和 `d`（删除），掌握这两个就能解决 90% 的需求。
