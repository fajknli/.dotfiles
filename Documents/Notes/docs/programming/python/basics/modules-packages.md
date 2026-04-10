# Python 模块与包

## 模块

### 什么是模块

模块是一个包含 Python 代码的 `.py` 文件。模块可以定义函数、类和变量，也可以包含可执行代码。

### 导入模块

```python
# 导入整个模块
import math
print(math.sqrt(16))  # 4.0

# 导入模块并指定别名
import numpy as np

# 从模块中导入特定函数
from math import sqrt, pi
print(sqrt(25))  # 5.0
print(pi)        # 3.14159...

# 导入模块中的所有内容（不推荐）
from math import *
```

### 模块搜索路径

Python 按以下顺序搜索模块：
1. 当前目录
2. `PYTHONPATH` 环境变量中的目录
3. 标准库目录
4. `site-packages` 目录

```python
import sys
print(sys.path)  # 查看搜索路径

# 添加自定义路径
sys.path.append("/path/to/my/modules")
```

### 创建自己的模块

创建 `mymodule.py`：

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}"

PI = 3.14159

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

使用自定义模块：

```python
import mymodule

print(mymodule.greet("张三"))        # Hello, 张三
print(mymodule.PI)                   # 3.14159
calc = mymodule.Calculator()
print(calc.add(3, 5))                # 8
```

### `if __name__ == "__main__"`

```python
# mymodule.py
def main():
    print("模块被直接运行")

if __name__ == "__main__":
    main()  # 只有直接运行此脚本时才执行
```

- 直接运行脚本时，`__name__` 等于 `"__main__"`
- 被导入时，`__name__` 等于模块名

## 包

### 什么是包

包是包含多个模块的目录，必须包含 `__init__.py` 文件（可以为空）。

```
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

### 导入包中的模块

```python
# 导入整个模块
import mypackage.module1

# 从包中导入模块
from mypackage import module2

# 从模块中导入函数
from mypackage.module1 import my_function

# 导入子包中的模块
import mypackage.subpackage.module3
```

### `__init__.py` 的作用

```python
# mypackage/__init__.py
# 可以是空文件，也可以定义包的初始化代码

# 简化导入
from .module1 import useful_function
from .module2 import another_function

# 定义 `__all__` 列表
__all__ = ["module1", "module2"]
```

### 相对导入

```python
# 在包内部使用相对导入
# mypackage/subpackage/module3.py

# 同级目录
from . import module1

# 上级目录
from .. import module2

# 上级目录的某个模块
from ..module1 import some_function
```

## 常用标准库模块

### sys：系统相关

```python
import sys

# 命令行参数
print(sys.argv)           # 脚本名及参数列表

# 退出程序
sys.exit(0)               # 正常退出

# 标准输入输出
sys.stdin.readline()      # 读取一行
sys.stdout.write("text")  # 写入输出
sys.stderr.write("error") # 写入错误

# Python 版本
print(sys.version)        # 3.12.0

# 平台信息
print(sys.platform)       # linux, win32, darwin
```

### os：操作系统接口

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
```

### datetime：日期时间

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
delta = timedelta(days=7)
next_week = now + delta

# 提取部分
year = dt.year
month = dt.month
day = dt.day
hour = dt.hour
minute = dt.minute
second = dt.second
```

### random：随机数

```python
import random

# 随机浮点数
random.random()           # 0.0 到 1.0
random.uniform(1, 10)     # 1.0 到 10.0

# 随机整数
random.randint(1, 10)     # 1 到 10（包含两端）
random.randrange(0, 10, 2)  # 0,2,4,6,8

# 从序列中随机选择
random.choice(["a", "b", "c"])        # 随机一个元素
random.sample(["a", "b", "c"], 2)     # 随机两个元素（不重复）
random.choices(["a", "b", "c"], k=5)  # 随机5个元素（可重复）

# 打乱序列
items = [1, 2, 3, 4, 5]
random.shuffle(items)

# 设置种子（可复现）
random.seed(42)
```

### json：JSON 处理

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

### re：正则表达式

```python
import re

# 匹配
pattern = r"\d+"  # 匹配一个或多个数字
result = re.match(pattern, "123abc")   # 从开头匹配
result = re.search(pattern, "abc123")  # 搜索任意位置

# 查找所有
numbers = re.findall(r"\d+", "a1b2c3")  # ["1", "2", "3"]

# 替换
text = re.sub(r"\d+", "X", "a1b2c3")    # "aXbXcX"

# 分割
parts = re.split(r"[,\s]+", "a,b c,d")  # ["a", "b", "c", "d"]

# 编译正则表达式（提高性能）
pattern = re.compile(r"\d+")
result = pattern.search("abc123")
```

### collections：额外数据结构

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter：计数器
counts = Counter("hello world")
print(counts.most_common(2))  # [('l', 3), ('o', 2)]

# defaultdict：带默认值的字典
d = defaultdict(list)
d["key"].append(1)  # 不需要检查 key 是否存在

# deque：双端队列
q = deque([1, 2, 3])
q.appendleft(0)     # 左侧添加
q.popleft()         # 左侧弹出

# namedtuple：命名元组
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)     # 10 20
```

### itertools：迭代器工具

```python
from itertools import chain, cycle, permutations, product

# chain：连接多个迭代器
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# cycle：无限循环
for i, val in enumerate(cycle(["A", "B", "C"])):
    if i >= 6:
        break
    print(val)  # A, B, C, A, B, C

# permutations：排列
list(permutations([1, 2, 3], 2))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# product：笛卡尔积
list(product([1, 2], ["a", "b"]))  # [(1,'a'), (1,'b'), (2,'a'), (2,'b')]
```

### pathlib：面向对象的路径操作

```python
from pathlib import Path

# 创建路径
p = Path("/home/user/file.txt")

# 属性
p.parent      # /home/user
p.name        # file.txt
p.stem        # file
p.suffix      # .txt

# 方法
p.exists()               # 是否存在
p.is_file()              # 是否为文件
p.is_dir()               # 是否为目录
p.mkdir(parents=True)    # 创建目录
p.unlink()               # 删除文件
p.rmdir()                # 删除空目录

# 遍历目录
for file in Path(".").glob("*.py"):
    print(file)

# 读写文件
Path("file.txt").write_text("content", encoding="utf-8")
content = Path("file.txt").read_text(encoding="utf-8")
```

## 第三方包管理

### pip 基本命令

```bash
# 安装包
pip install package_name
pip install package==1.2.3      # 指定版本
pip install package>=1.0.0      # 最低版本

# 卸载包
pip uninstall package_name

# 列出已安装包
pip list
pip freeze                       # 导出依赖格式

# 查看包信息
pip show package_name

# 从 requirements.txt 安装
pip install -r requirements.txt

# 生成 requirements.txt
pip freeze > requirements.txt
```

### 虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate          # Windows

# 退出虚拟环境
deactivate

# 删除虚拟环境
rm -rf venv
```
