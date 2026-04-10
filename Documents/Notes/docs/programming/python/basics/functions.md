# Python 函数

## 函数定义与调用

### 基本定义

```python
def say_hello():
    print("Hello!")

# 调用函数
say_hello()
```

### 带参数的函数

```python
def greet(name):
    print(f"Hello, {name}!")

greet("张三")
```

### 返回值

```python
def add(a, b):
    return a + b

result = add(3, 5)  # 8

# 没有 return 语句的函数返回 None
def do_nothing():
    pass

result = do_nothing()  # None
```

### 多个返回值

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 2, 3, 4, 5])
# minimum = 1, maximum = 5
```

## 参数类型

### 位置参数

```python
def introduce(name, age):
    print(f"{name} 今年 {age} 岁")

introduce("张三", 25)  # 顺序必须一致
```

### 默认参数

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("张三")           # Hello, 张三!
greet("李四", "Hi")     # Hi, 李四!

# 默认参数只计算一次（注意可变对象陷阱）
def add_item(item, lst=[]):
    lst.append(item)
    return lst

add_item(1)  # [1]
add_item(2)  # [1, 2] 而不是 [2]

# 正确做法
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### 关键字参数

```python
def introduce(name, age):
    print(f"{name} 今年 {age} 岁")

introduce(age=25, name="张三")  # 顺序可以任意
```

### 可变参数

```python
# *args：接收任意多个位置参数（元组）
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4, 5)  # 15

# **kwargs：接收任意多个关键字参数（字典）
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="张三", age=25, city="北京")
```

### 参数组合顺序

```python
def func(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass

# / 之前的参数只能位置传递
# * 之后的参数只能关键字传递
```

```python
def example(a, b, /, c, d, *, e, f):
    pass

example(1, 2, 3, d=4, e=5, f=6)  # 正确
# example(1, 2, c=3, d=4, e=5, f=6)  # 也可以
# example(a=1, b=2, c=3, d=4, e=5, f=6)  # 错误，a, b 不能关键字传递
```

## 作用域

### 局部变量与全局变量

```python
x = 10  # 全局变量

def func():
    y = 5  # 局部变量
    print(x)  # 可以访问全局变量

def modify_global():
    global x  # 声明要修改全局变量
    x = 20

modify_global()
print(x)  # 20
```

### 嵌套作用域

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # 声明要修改外层变量
        x = 20
    
    inner()
    print(x)  # 20

outer()
```

### LEGB 规则

变量查找顺序：
1. **L**ocal：局部作用域
2. **E**nclosing：外层函数作用域
3. **G**lobal：全局作用域
4. **B**uilt-in：内置作用域

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # local
    
    inner()

outer()
```

## lambda 表达式

### 基本用法

```python
# 普通函数
def square(x):
    return x ** 2

# lambda 表达式
square = lambda x: x ** 2

# 直接使用
result = (lambda x, y: x + y)(3, 5)  # 8
```

### 常见用途

```python
# 与 sorted 配合
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]
sorted_by_score = sorted(students, key=lambda s: s["score"])

# 与 map 配合
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# 与 filter 配合
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

## 文档字符串（docstring）

```python
def add(a, b):
    """
    计算两个数的和。

    参数:
        a: 第一个数
        b: 第二个数

    返回:
        两个数的和
    """
    return a + b

# 查看文档字符串
help(add)
print(add.__doc__)
```

## 类型注解（Type Hints）

```python
from typing import List, Dict, Optional

# 基本类型
def greet(name: str) -> str:
    return f"Hello, {name}"

# 列表
def process_items(items: List[int]) -> int:
    return sum(items)

# 字典
def get_value(data: Dict[str, int], key: str) -> Optional[int]:
    return data.get(key)

# 多个返回值
def get_min_max(numbers: List[float]) -> tuple[float, float]:
    return min(numbers), max(numbers)
```

## 装饰器

```python
# 简单装饰器
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)

slow_function()  # 自动计时

# 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello")

say_hello()  # 打印3次
```

## 生成器函数

```python
# 使用 yield 的生成器
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)  # 0, 1, 2, 3, 4

# 生成器表达式
squares = (x**2 for x in range(10))
for square in squares:
    print(square)
```

## 递归函数

```python
def factorial(n):
    """计算 n 的阶乘"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

factorial(5)  # 120

# 递归深度限制
import sys
sys.getrecursionlimit()  # 默认 1000
sys.setrecursionlimit(2000)  # 设置新的限制
```
