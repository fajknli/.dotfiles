# Python 迭代器与生成器

## 迭代器

### 什么是迭代器

迭代器是一个可以记住遍历位置的对象。它从第一个元素开始访问，直到所有元素被访问完结束。

```python
# 可迭代对象（Iterable）：实现了 __iter__ 方法的对象
# 迭代器（Iterator）：实现了 __iter__ 和 __next__ 方法的对象

# 列表是可迭代对象，但不是迭代器
lst = [1, 2, 3]
print(hasattr(lst, "__iter__"))   # True
print(hasattr(lst, "__next__"))   # False

# 使用 iter() 获取迭代器
it = iter(lst)
print(hasattr(it, "__iter__"))    # True
print(hasattr(it, "__next__"))    # True
```

### 迭代器协议

```python
# 使用 next() 遍历迭代器
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # StopIteration
```

### 自定义迭代器

```python
class CountDown:
    """倒计时迭代器"""
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

for num in CountDown(5):
    print(num)  # 5, 4, 3, 2, 1
```

### 斐波那契迭代器

```python
class Fibonacci:
    """斐波那契数列迭代器"""
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return self.a
        if self.count == 1:
            self.count += 1
            return self.b
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.b

for num in Fibonacci(10):
    print(num)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

## 生成器

### 什么是生成器

生成器是一种特殊的迭代器，使用 `yield` 关键字定义，更加简洁。

```python
def count_down(n):
    while n > 0:
        yield n
        n -= 1

for num in count_down(5):
    print(num)  # 5, 4, 3, 2, 1
```

### yield 的工作原理

```python
def simple_generator():
    print("开始")
    yield 1
    print("继续")
    yield 2
    print("结束")

gen = simple_generator()
print(next(gen))  # 开始 / 1
print(next(gen))  # 继续 / 2
print(next(gen))  # 结束 / StopIteration
```

### 生成器表达式

```python
# 列表推导式（立即生成所有值）
squares_list = [x**2 for x in range(10)]
print(squares_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成器表达式（惰性求值）
squares_gen = (x**2 for x in range(10))
print(squares_gen)   # <generator object>
for val in squares_gen:
    print(val)       # 逐个输出
```

## 生成器高级用法

### 带 yield 的生成器函数

```python
def fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(10):
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34
```

### send() 方法

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)           # 启动生成器
print(acc.send(10)) # 10
print(acc.send(20)) # 30
print(acc.send(30)) # 60
```

### throw() 方法

```python
def generator():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        yield "发生值错误"
    except TypeError:
        yield "发生类型错误"

gen = generator()
print(next(gen))          # 1
print(gen.throw(ValueError))  # 发生值错误
print(next(gen))          # 3（继续执行）
```

### close() 方法

```python
def infinite():
    count = 0
    while True:
        try:
            yield count
            count += 1
        except GeneratorExit:
            print("生成器被关闭")
            break

gen = infinite()
print(next(gen))  # 0
print(next(gen))  # 1
gen.close()       # 生成器被关闭
```

## 实际应用

### 1. 读取大文件

```python
def read_large_file(file_path, chunk_size=1024):
    """逐块读取大文件，避免内存溢出"""
    with open(file_path, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# 使用
for chunk in read_large_file('large_file.txt'):
    process(chunk)  # 逐块处理
```

### 2. 无限序列生成

```python
def primes():
    """生成无限素数序列"""
    yield 2
    primes_list = [2]
    n = 3
    while True:
        is_prime = True
        for p in primes_list:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(n)
            yield n
        n += 2

# 取前10个素数
import itertools
for prime in itertools.islice(primes(), 10):
    print(prime)  # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
```

### 3. 流水线处理

```python
def read_numbers(file_path):
    with open(file_path) as f:
        for line in f:
            yield int(line.strip())

def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def square(numbers):
    for n in numbers:
        yield n ** 2

def sum_all(numbers):
    total = 0
    for n in numbers:
        total += n
        yield total

# 流水线：读取 → 过滤偶数 → 平方 → 累加
result = sum_all(square(filter_even(read_numbers('numbers.txt'))))
for val in result:
    print(val)
```

### 4. 惰性求值

```python
def lazy_range(start, end, step=1):
    """惰性版本的 range"""
    current = start
    while current < end:
        yield current
        current += step

# 不会一次性创建所有值
for i in lazy_range(0, 1000000):
    if i > 10:
        break
    print(i)  # 只计算前11个值
```

### 5. 使用 itertools 模块

```python
from itertools import count, cycle, repeat, islice, chain

# count：无限计数
for i in islice(count(5, 2), 5):
    print(i)  # 5, 7, 9, 11, 13

# cycle：无限循环
for i, val in enumerate(islice(cycle(['A', 'B', 'C']), 7)):
    print(val, end=" ")  # A B C A B C A

# repeat：重复值
for val in islice(repeat('Hello', 5), 3):
    print(val)  # Hello Hello Hello

# chain：连接多个迭代器
result = list(chain([1, 2], [3, 4], [5, 6]))
print(result)  # [1, 2, 3, 4, 5, 6]
```

## 迭代器 vs 生成器

| 特性 | 迭代器 | 生成器 |
|------|--------|--------|
| 实现方式 | 定义类，实现 `__iter__` 和 `__next__` | 使用 `yield` 的函数 |
| 代码量 | 较多 | 简洁 |
| 状态保存 | 手动维护 | 自动保存 |
| 适用场景 | 复杂状态逻辑 | 简单序列生成 |
