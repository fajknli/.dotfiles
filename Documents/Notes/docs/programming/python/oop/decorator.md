# Python 装饰器

## 装饰器基础

### 什么是装饰器

装饰器是一个函数，它接收另一个函数作为参数，并返回一个新的函数。装饰器可以在不修改原函数代码的情况下，给函数添加额外功能。

```python
def decorator(func):
    def wrapper():
        print("执行前")
        func()
        print("执行后")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()
# 执行前
# Hello
# 执行后
```

### 手动调用装饰器（等价写法）

```python
def say_hello():
    print("Hello")

say_hello = decorator(say_hello)
say_hello()
```

## 装饰带参数的函数

```python
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
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

result = slow_function(1000000)
# slow_function 耗时: 0.0234秒
```

## 装饰带返回值的函数

```python
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_result
def get_message():
    return "hello world"

print(get_message())  # HELLO WORLD
```

## 带参数的装饰器

```python
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

say_hello()
# Hello
# Hello
# Hello
```

## 多个装饰器

```python
def decorator_a(func):
    def wrapper():
        print("装饰器 A 开始")
        func()
        print("装饰器 A 结束")
    return wrapper

def decorator_b(func):
    def wrapper():
        print("装饰器 B 开始")
        func()
        print("装饰器 B 结束")
    return wrapper

@decorator_a
@decorator_b
def say_hello():
    print("Hello")

say_hello()
# 装饰器 A 开始
# 装饰器 B 开始
# Hello
# 装饰器 B 结束
# 装饰器 A 结束
```

## 保留函数元信息（functools.wraps）

```python
from functools import wraps

def decorator(func):
    @wraps(func)  # 保留原函数的名称、文档等
    def wrapper(*args, **kwargs):
        """包装函数"""
        print("执行前")
        return func(*args, **kwargs)
    return wrapper

@decorator
def say_hello():
    """打招呼函数"""
    print("Hello")

print(say_hello.__name__)  # say_hello（没有 wraps 会变成 wrapper）
print(say_hello.__doc__)   # 打招呼函数
```

## 类装饰器

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"调用次数: {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello")

say_hello()  # 调用次数: 1 / Hello
say_hello()  # 调用次数: 2 / Hello
```

## 装饰器示例

### 1. 执行时间计时器

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 耗时: {end - start:.6f}秒")
        return result
    return wrapper

@timer
def calculate():
    sum(range(1000000))

calculate()
```

### 2. 缓存结果（Memoization）

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # 12586269025，计算很快
```

### 3. 权限检查

```python
def require_login(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            print("请先登录")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@require_login
def view_profile(user):
    print(f"用户: {user['name']}")

user1 = {"name": "张三", "logged_in": False}
user2 = {"name": "李四", "logged_in": True}

view_profile(user1)  # 请先登录
view_profile(user2)  # 用户: 李四
```

### 4. 重试机制

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"尝试 {attempt + 1} 失败: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            raise Exception(f"重试 {max_attempts} 次后仍然失败")
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("随机失败")
    return "成功"
```

### 5. 日志记录

```python
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logging.info(f"调用 {func.__name__}({signature})")
        try:
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} 返回 {result!r}")
            return result
        except Exception as e:
            logging.exception(f"{func.__name__} 异常: {e}")
            raise
    return wrapper

@log
def divide(a, b):
    return a / b

divide(10, 2)   # 正常
divide(10, 0)   # 记录异常
```

### 6. 限制调用频率

```python
import time
from functools import wraps

def rate_limit(per_second=1):
    interval = 1.0 / per_second
    last_called = 0
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called
            elapsed = time.time() - last_called
            if elapsed < interval:
                time.sleep(interval - elapsed)
            last_called = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(per_second=2)  # 每秒最多2次
def process():
    print("处理中...")

for _ in range(5):
    process()
```
