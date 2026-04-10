# Python 标准库速查

## sys - 系统相关

```python
import sys

# 命令行参数
print(sys.argv)           # 脚本名及参数列表

# 退出程序
sys.exit(0)               # 正常退出
sys.exit(1)               # 异常退出

# 标准输入输出
sys.stdin.readline()      # 读取一行
sys.stdout.write("text")  # 写入输出
sys.stderr.write("error") # 写入错误

# Python 版本
print(sys.version)        # 3.12.0
print(sys.version_info)   # (3, 12, 0)

# 平台信息
print(sys.platform)       # linux, win32, darwin

# 模块搜索路径
print(sys.path)           # 列表，可修改

# 递归深度限制
sys.getrecursionlimit()   # 默认 1000
sys.setrecursionlimit(2000)

# 引用计数
a = []
print(sys.getrefcount(a)) # 2
```

## os - 操作系统接口

```python
import os

# 文件和目录操作
os.getcwd()               # 获取当前工作目录
os.chdir("/path")         # 改变目录
os.listdir(".")           # 列出目录内容
os.mkdir("newdir")        # 创建目录
os.makedirs("a/b/c")      # 递归创建目录
os.remove("file.txt")     # 删除文件
os.rmdir("emptydir")      # 删除空目录
os.removedirs("a/b/c")    # 递归删除空目录
os.rename("old", "new")   # 重命名

# 路径操作
os.path.join("dir", "file")     # 拼接路径
os.path.exists("/path")         # 判断是否存在
os.path.isfile("file.txt")      # 是否为文件
os.path.isdir("dir")            # 是否为目录
os.path.abspath("file")         # 绝对路径
os.path.dirname("/a/b/c")       # /a/b
os.path.basename("/a/b/c")      # c
os.path.splitext("file.txt")    # ("file", ".txt")

# 环境变量
os.environ.get("PATH")          # 获取环境变量
os.environ["NEW_VAR"] = "value" # 设置环境变量

# 执行命令
os.system("ls -l")              # 执行系统命令
os.popen("ls -l").read()        # 读取命令输出
```

## math - 数学函数

```python
import math

# 常量
math.pi          # 3.141592653589793
math.e           # 2.718281828459045
math.inf         # 正无穷
math.nan         # 非数字

# 基本运算
math.sqrt(16)    # 4.0
math.pow(2, 3)   # 8.0
math.fabs(-5)    # 5.0

# 取整
math.ceil(3.2)   # 4
math.floor(3.9)  # 3
math.trunc(3.9)  # 3

# 三角函数
math.sin(math.pi/2)   # 1.0
math.cos(0)           # 1.0
math.tan(math.pi/4)   # 1.0
math.degrees(math.pi) # 180.0
math.radians(180)     # 3.141592653589793

# 对数
math.log(100, 10)     # 2.0
math.log10(100)       # 2.0
math.log(2.71828)     # 1.0
math.exp(1)           # 2.71828

# 阶乘
math.factorial(5)     # 120

# 组合数
math.comb(5, 2)       # 10
```

## random - 随机数

```python
import random

# 设置种子（可复现）
random.seed(42)

# 随机浮点数
random.random()           # 0.0 到 1.0
random.uniform(1, 10)     # 1.0 到 10.0

# 随机整数
random.randint(1, 10)     # 1 到 10（包含两端）
random.randrange(10)      # 0 到 9
random.randrange(0, 10, 2) # 0,2,4,6,8

# 从序列中选择
random.choice(["a", "b", "c"])        # 随机一个元素
random.sample(["a", "b", "c"], 2)     # 随机两个（不重复）
random.choices(["a", "b", "c"], k=5)  # 随机5个（可重复）

# 打乱序列
items = [1, 2, 3, 4, 5]
random.shuffle(items)

# 正态分布
random.gauss(0, 1)        # 均值0，标准差1
```

## datetime - 日期时间

```python
from datetime import datetime, date, time, timedelta

# 获取当前时间
now = datetime.now()              # 2024-01-15 14:30:00.123456
today = date.today()              # 2024-01-15

# 创建日期时间对象
dt = datetime(2024, 1, 15, 14, 30, 0)

# 格式化
dt.strftime("%Y-%m-%d %H:%M:%S")  # "2024-01-15 14:30:00"
dt.strftime("%A")                 # "Monday"

# 解析字符串
dt = datetime.strptime("2024-01-15", "%Y-%m-%d")

# 时间差
delta = timedelta(days=7, hours=2)
next_week = now + delta
last_week = now - delta

# 提取部分
year = dt.year
month = dt.month
day = dt.day
hour = dt.hour
minute = dt.minute
second = dt.second

# 比较
if dt1 < dt2:
    print("dt1 早于 dt2")
```

## json - JSON 处理

```python
import json

# Python 对象转 JSON 字符串
data = {"name": "张三", "age": 25, "hobbies": ["读书", "跑步"]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)

# JSON 字符串转 Python 对象
data = json.loads('{"name": "张三", "age": 25}')

# 读取 JSON 文件
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 写入 JSON 文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

## re - 正则表达式

```python
import re

# 匹配
pattern = r"\d+"  # 匹配一个或多个数字
result = re.match(pattern, "123abc")   # 从开头匹配
result = re.search(pattern, "abc123")  # 搜索任意位置

# 获取匹配内容
if result:
    print(result.group())   # 匹配的字符串
    print(result.start())   # 起始位置
    print(result.end())     # 结束位置

# 查找所有
numbers = re.findall(r"\d+", "a1b2c3")  # ["1", "2", "3"]

# 查找所有（返回迭代器）
for match in re.finditer(r"\d+", "a1b2c3"):
    print(match.group())

# 替换
text = re.sub(r"\d+", "X", "a1b2c3")    # "aXbXcX"
text = re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "a1b2c3")  # "a2b4c6"

# 分割
parts = re.split(r"[,\s]+", "a,b c,d")  # ["a", "b", "c", "d"]

# 编译正则表达式（提高性能）
pattern = re.compile(r"\d+")
result = pattern.search("abc123")
```

## collections - 额外数据结构

```python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter：计数器
counts = Counter("hello world")
print(counts)                    # Counter({'l': 3, 'o': 2, ...})
print(counts.most_common(2))     # [('l', 3), ('o', 2)]

# defaultdict：带默认值的字典
d = defaultdict(list)
d["key"].append(1)               # 不需要检查 key 是否存在
d = defaultdict(int)
d["count"] += 1                  # 默认值为 0

# deque：双端队列
q = deque([1, 2, 3])
q.appendleft(0)                  # [0, 1, 2, 3]
q.popleft()                      # [1, 2, 3]
q.append(4)                      # [1, 2, 3, 4]
q.pop()                          # [1, 2, 3]

# namedtuple：命名元组
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)                  # 10 20
print(p[0], p[1])                # 10 20

# OrderedDict：有序字典（Python 3.7+ 中 dict 已有序）
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od.move_to_end("a")              # 移动到末尾
```

## itertools - 迭代器工具

```python
from itertools import chain, cycle, repeat, islice, count, permutations, combinations, product

# chain：连接多个迭代器
list(chain([1, 2], [3, 4]))     # [1, 2, 3, 4]

# cycle：无限循环
for i, val in enumerate(cycle(["A", "B", "C"])):
    if i >= 6:
        break
    print(val)                   # A, B, C, A, B, C

# repeat：重复值
list(repeat("A", 3))             # ["A", "A", "A"]

# islice：切片
list(islice(count(5), 10))       # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# count：无限计数
for i in islice(count(5, 2), 5):
    print(i)                     # 5, 7, 9, 11, 13

# permutations：排列
list(permutations([1, 2, 3], 2)) # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# combinations：组合
list(combinations([1, 2, 3], 2)) # [(1,2), (1,3), (2,3)]

# product：笛卡尔积
list(product([1, 2], ["a", "b"])) # [(1,'a'), (1,'b'), (2,'a'), (2,'b')]
```

## pathlib - 路径操作

```python
from pathlib import Path

# 创建路径
p = Path("/home/user/file.txt")
p = Path.home() / "Documents"     # /home/user/Documents
p = Path.cwd() / "data" / "file.txt"

# 属性
p.parent          # /home/user
p.parents[0]      # /home/user
p.parents[1]      # /home
p.name            # file.txt
p.stem            # file
p.suffix          # .txt
p.suffixes        # ['.txt']

# 方法
p.exists()                     # 是否存在
p.is_file()                    # 是否为文件
p.is_dir()                     # 是否为目录
p.absolute()                   # 绝对路径
p.resolve()                    # 解析符号链接

# 创建目录
Path("newdir").mkdir()
Path("a/b/c").mkdir(parents=True, exist_ok=True)

# 删除
Path("file.txt").unlink()      # 删除文件
Path("empty_dir").rmdir()      # 删除空目录

# 遍历
for file in Path(".").glob("*.txt"):
    print(file)

for file in Path(".").rglob("*.py"):  # 递归
    print(file)

# 读写文件
Path("file.txt").write_text("content", encoding="utf-8")
content = Path("file.txt").read_text(encoding="utf-8")

# 写入二进制
Path("file.bin").write_bytes(b"content")
data = Path("file.bin").read_bytes()
```

## argparse - 命令行参数解析

```python
import argparse

parser = argparse.ArgumentParser(description="程序描述")

# 位置参数
parser.add_argument("input", help="输入文件")

# 可选参数
parser.add_argument("-o", "--output", help="输出文件")
parser.add_argument("-v", "--verbose", action="store_true", help="详细输出")
parser.add_argument("-n", "--number", type=int, default=1, help="数字参数")

# 限制选项
parser.add_argument("--mode", choices=["fast", "slow"], default="fast")

# 可变参数
parser.add_argument("files", nargs="+", help="多个文件")

args = parser.parse_args()

print(args.input)
if args.verbose:
    print("详细模式")
```
