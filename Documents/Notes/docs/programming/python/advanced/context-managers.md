# Python 上下文管理器

## 上下文管理器基础

### 什么是上下文管理器

上下文管理器用于管理资源，确保在使用完毕后正确释放（如文件关闭、锁释放、数据库连接关闭等）。

```python
# 不使用上下文管理器
f = open("file.txt", "r")
try:
    content = f.read()
finally:
    f.close()  # 必须手动关闭

# 使用上下文管理器
with open("file.txt", "r") as f:
    content = f.read()
# 自动关闭文件
```

### with 语句语法

```python
with expression [as variable]:
    # 代码块
    pass

# 多个上下文管理器
with open("a.txt") as f1, open("b.txt") as f2:
    content1 = f1.read()
    content2 = f2.read()
```

## 实现上下文管理器

### 使用类（__enter__ 和 __exit__）

```python
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"打开文件: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"关闭文件: {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"发生异常: {exc_type.__name__}: {exc_val}")
        return False  # 返回 True 会抑制异常

with ManagedFile("test.txt", "w") as f:
    f.write("Hello")
# 打开文件: test.txt
# 关闭文件: test.txt
```

### 使用 contextlib 模块

```python
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    print(f"打开文件: {filename}")
    f = open(filename, mode)
    try:
        yield f
    finally:
        print(f"关闭文件: {filename}")
        f.close()

with managed_file("test.txt", "w") as f:
    f.write("Hello")
```

## __exit__ 方法的异常处理

```python
class ResourceManager:
    def __enter__(self):
        print("获取资源")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"捕获到异常: {exc_type.__name__}")
            print(f"异常信息: {exc_val}")
        print("释放资源")
        return True  # 返回 True 会抑制异常传播

with ResourceManager():
    print("使用资源")
    raise ValueError("出错了")
    print("这行不会执行")
# 获取资源
# 使用资源
# 捕获到异常: ValueError
# 异常信息: 出错了
# 释放资源
# 异常被抑制，程序继续执行
```

## 常见应用场景

### 1. 文件操作

```python
# 标准文件操作
with open("data.txt", "r") as f:
    content = f.read()

# 二进制文件
with open("image.jpg", "rb") as f:
    data = f.read()

# 指定编码
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### 2. 线程锁

```python
import threading

lock = threading.Lock()

# 手动管理
lock.acquire()
try:
    # 临界区代码
    pass
finally:
    lock.release()

# 使用上下文管理器
with lock:
    # 临界区代码
    pass
```

### 3. 数据库连接

```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db_connection(db_path):
    conn = sqlite3.connect(db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

with get_db_connection("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
# 自动提交或回滚，自动关闭连接
```

### 4. 计时器

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{name} 耗时: {elapsed:.4f}秒")

with timer("数据处理"):
    sum(range(1000000))
# 数据处理 耗时: 0.0234秒
```

### 5. 临时目录

```python
import tempfile
import shutil
from contextlib import contextmanager

@contextmanager
def temp_dir():
    import tempfile
    import shutil
    dirpath = tempfile.mkdtemp()
    try:
        yield dirpath
    finally:
        shutil.rmtree(dirpath)

with temp_dir() as tmp:
    # 在临时目录中操作
    import os
    with open(os.path.join(tmp, "test.txt"), "w") as f:
        f.write("临时文件")
    # 退出时自动删除临时目录
```

### 6. 重定向标准输出

```python
import sys
from io import StringIO
from contextlib import contextmanager

@contextmanager
def capture_output():
    """捕获标准输出"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_stdout

with capture_output() as output:
    print("这行会被捕获")
    print("这行也会被捕获")
    result = output.getvalue()
print(f"捕获的内容: {result}")
```

### 7. 改变当前目录

```python
import os
from contextlib import contextmanager

@contextmanager
def chdir(path):
    """临时切换工作目录"""
    old_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_dir)

with chdir("/tmp"):
    print(f"当前目录: {os.getcwd()}")  # /tmp
print(f"恢复目录: {os.getcwd()}")      # 原目录
```

### 8. 忽略特定异常

```python
from contextlib import contextmanager

@contextmanager
def ignore_exception(*exceptions):
    try:
        yield
    except exceptions:
        pass  # 忽略指定异常

with ignore_exception(ValueError, TypeError):
    int("not a number")  # 不会抛出异常
    print("继续执行")
```

## contextlib 常用工具

### closing

```python
from contextlib import closing
import urllib.request

# 确保资源被关闭
with closing(urllib.request.urlopen('http://example.com')) as page:
    content = page.read()
```

### suppress

```python
from contextlib import suppress

# 忽略指定异常
with suppress(FileNotFoundError):
    os.remove("nonexistent.txt")  # 文件不存在也不报错
```

### ExitStack

```python
from contextlib import ExitStack

# 管理多个上下文管理器
with ExitStack() as stack:
    files = [stack.enter_context(open(f"file{i}.txt", "w")) for i in range(5)]
    for f in files:
        f.write("Hello")
    # 退出时自动关闭所有文件
```
