# Python 文件操作

## 文件打开与关闭

### open 函数

```python
# 基本语法
file = open("file.txt", "r")  # 打开文件
content = file.read()          # 读取内容
file.close()                   # 关闭文件
```

### 文件模式

| 模式 | 说明 |
|------|------|
| `'r'` | 只读（默认） |
| `'w'` | 写入（覆盖已有内容） |
| `'x'` | 独占创建，文件存在则报错 |
| `'a'` | 追加（在文件末尾添加） |
| `'b'` | 二进制模式 |
| `'t'` | 文本模式（默认） |
| `'+'` | 读写模式 |

```python
# 常用组合
open("file.txt", "r")      # 文本只读
open("file.txt", "w")      # 文本写入（覆盖）
open("file.txt", "a")      # 文本追加
open("file.txt", "rb")     # 二进制只读
open("file.txt", "wb")     # 二进制写入
open("file.txt", "r+")     # 文本读写
```

### with 语句（推荐）

```python
# 使用 with 自动关闭文件
with open("file.txt", "r") as f:
    content = f.read()
# 文件已自动关闭
```

## 读取文件

### read：读取全部内容

```python
with open("file.txt", "r") as f:
    content = f.read()           # 读取全部
    print(content)
    
    f.seek(0)                    # 移动文件指针到开头
    content_5 = f.read(5)        # 读取前5个字符
```

### readline：读取一行

```python
with open("file.txt", "r") as f:
    line = f.readline()           # 读取第一行
    while line:
        print(line.strip())
        line = f.readline()
```

### readlines：读取所有行

```python
with open("file.txt", "r") as f:
    lines = f.readlines()         # 返回列表，每行一个元素
    for line in lines:
        print(line.strip())
```

### 直接遍历文件对象

```python
# 最常用的方式，内存友好
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

## 写入文件

### write：写入字符串

```python
with open("file.txt", "w") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    # 覆盖原有内容
```

### writelines：写入多个字符串

```python
lines = ["第一行\n", "第二行\n", "第三行\n"]
with open("file.txt", "w") as f:
    f.writelines(lines)
```

### 追加内容

```python
with open("file.txt", "a") as f:
    f.write("这是追加的内容\n")
```

## 文件指针操作

```python
with open("file.txt", "r") as f:
    print(f.tell())        # 当前位置（字节）
    f.seek(5)              # 移动到第5个字节
    content = f.read(10)   # 读取10个字节
    f.seek(0, 0)           # 移动到开头
    f.seek(0, 2)           # 移动到末尾
```

## 二进制文件操作

```python
# 读取图片
with open("image.jpg", "rb") as f:
    data = f.read()
    print(f"文件大小: {len(data)} 字节")

# 写入二进制数据
with open("output.jpg", "wb") as f:
    f.write(data)
```

## 文件与目录操作（os 模块）

```python
import os

# 检查文件/目录是否存在
os.path.exists("file.txt")

# 检查是否为文件
os.path.isfile("file.txt")

# 检查是否为目录
os.path.isdir("dir")

# 获取文件大小
os.path.getsize("file.txt")  # 字节

# 获取文件修改时间
os.path.getmtime("file.txt")  # 时间戳

# 重命名
os.rename("old.txt", "new.txt")

# 删除文件
os.remove("file.txt")

# 创建目录
os.mkdir("newdir")           # 单级目录
os.makedirs("a/b/c")         # 多级目录

# 删除目录
os.rmdir("emptydir")         # 只能删除空目录
import shutil
shutil.rmtree("dir")         # 删除目录及其内容

# 列出目录内容
os.listdir(".")
```

## 路径操作（pathlib 模块，推荐）

```python
from pathlib import Path

# 创建路径对象
p = Path("/home/user/file.txt")

# 路径属性
p.name          # file.txt
p.stem          # file
p.suffix        # .txt
p.parent        # /home/user
p.parents[0]    # /home/user
p.parents[1]    # /home

# 路径操作
p = Path(".") / "data" / "file.txt"  # ./data/file.txt
p = Path.home() / "Documents"        # /home/user/Documents

# 检查
p.exists()
p.is_file()
p.is_dir()

# 创建目录
Path("newdir").mkdir()
Path("a/b/c").mkdir(parents=True)

# 遍历目录
for file in Path(".").glob("*.txt"):
    print(file)

for file in Path(".").rglob("*.py"):  # 递归查找
    print(file)

# 读写文件（简洁）
Path("file.txt").write_text("content", encoding="utf-8")
content = Path("file.txt").read_text(encoding="utf-8")

# 删除
Path("file.txt").unlink()       # 删除文件
Path("empty_dir").rmdir()        # 删除空目录
import shutil
shutil.rmtree("dir")              # 删除非空目录
```

## 临时文件

```python
import tempfile

# 创建临时文件
with tempfile.TemporaryFile(mode="w+") as f:
    f.write("临时数据")
    f.seek(0)
    content = f.read()
    # 文件自动删除

# 创建临时目录
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"临时目录: {tmpdir}")
    # 目录自动删除
```

## CSV 文件处理

```python
import csv

# 读取 CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 读取为字典
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# 写入 CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["张三", 25])
    writer.writerow(["李四", 30])

# 写入字典
with open("output.csv", "w", newline="") as f:
    fieldnames = ["name", "age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "张三", "age": 25})
```

## JSON 文件处理

```python
import json

# 写入 JSON
data = {"name": "张三", "age": 25, "hobbies": ["读书", "跑步"]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取 JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# JSON 字符串与 Python 对象转换
json_str = json.dumps(data, ensure_ascii=False)
data = json.loads(json_str)
```

## 常见问题

### 文件编码

```python
# 指定编码
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 常见编码
# utf-8, gbk, gb2312, latin-1
```

### 处理大文件

```python
# 逐行读取，不占用大量内存
with open("large_file.txt", "r") as f:
    for line in f:
        process(line)

# 分块读取
with open("large_file.bin", "rb") as f:
    while True:
        chunk = f.read(8192)  # 8KB 块
        if not chunk:
            break
        process(chunk)
```
