# Python 魔法方法

## 魔法方法基础

魔法方法是 Python 中以双下划线开头和结尾的特殊方法，它们在特定操作时被自动调用。

```python
class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"MyClass: {self.name}"

obj = MyClass("test")
print(obj)  # 自动调用 __str__
```

## 对象生命周期

### __init__ 和 __new__

```python
class Person:
    def __new__(cls, *args, **kwargs):
        print("1. 创建实例")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print("2. 初始化实例")
        self.name = name
    
    def __del__(self):
        print("3. 销毁实例")

p = Person("张三")
# 1. 创建实例
# 2. 初始化实例
del p
# 3. 销毁实例
```

## 字符串表示

### __str__ 和 __repr__

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        """面向用户的友好字符串"""
        return f"{self.title} - {self.author}"
    
    def __repr__(self):
        """面向开发者的详细字符串"""
        return f"Book('{self.title}', '{self.author}')"

book = Book("Python入门", "张三")
print(str(book))   # Python入门 - 张三
print(repr(book))  # Book('Python入门', '张三')
```

### __format__

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __format__(self, format_spec):
        if format_spec == "ymd":
            return f"{self.year}-{self.month:02d}-{self.day:02d}"
        elif format_spec == "mdy":
            return f"{self.month}/{self.day}/{self.year}"
        return f"{self.year}/{self.month}/{self.day}"

date = Date(2024, 1, 15)
print(format(date, "ymd"))  # 2024-01-15
print(format(date, "mdy"))  # 1/15/2024
```

## 容器类魔法方法

```python
class MyList:
    def __init__(self, items=None):
        self._items = items or []
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __delitem__(self, index):
        del self._items[index]
    
    def __contains__(self, item):
        return item in self._items
    
    def __iter__(self):
        return iter(self._items)

lst = MyList([1, 2, 3, 4, 5])
print(len(lst))      # 5
print(lst[2])        # 3
lst[2] = 10
print(lst[2])        # 10
print(3 in lst)      # False（已被修改）
for item in lst:
    print(item)      # 1, 2, 10, 4, 5
```

## 运算符重载

### 算术运算符

| 方法 | 运算符 | 说明 |
|------|--------|------|
| `__add__(self, other)` | `+` | 加法 |
| `__sub__(self, other)` | `-` | 减法 |
| `__mul__(self, other)` | `*` | 乘法 |
| `__truediv__(self, other)` | `/` | 除法 |
| `__floordiv__(self, other)` | `//` | 整除 |
| `__mod__(self, other)` | `%` | 取模 |
| `__pow__(self, other)` | `**` | 幂运算 |

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
print(v2 - v1)  # Vector(2, 2)
print(v1 * 3)   # Vector(3, 6)
```

### 反向运算符

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        """当左操作数不支持乘法时调用"""
        return self.__mul__(scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v = Vector(1, 2)
print(3 * v)  # Vector(3, 6)（调用 __rmul__）
```

### 比较运算符

| 方法 | 运算符 | 说明 |
|------|--------|------|
| `__eq__(self, other)` | `==` | 等于 |
| `__ne__(self, other)` | `!=` | 不等于 |
| `__lt__(self, other)` | `<` | 小于 |
| `__le__(self, other)` | `<=` | 小于等于 |
| `__gt__(self, other)` | `>` | 大于 |
| `__ge__(self, other)` | `>=` | 大于等于 |

```python
from functools import total_ordering

@total_ordering  # 只需定义 __eq__ 和 __lt__，自动生成其他比较方法
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __eq__(self, other):
        return self.score == other.score
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __repr__(self):
        return f"Student({self.name}, {self.score})"

s1 = Student("张三", 85)
s2 = Student("李四", 92)
print(s1 < s2)   # True
print(s1 > s2)   # False
```

## 可调用对象

### __call__

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## 上下文管理器

### __enter__ 和 __exit__

```python
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"异常: {exc_val}")
        return False  # 返回 True 会抑制异常

with File("test.txt", "w") as f:
    f.write("Hello")
    # 自动关闭文件
```

## 属性访问

| 方法 | 触发时机 |
|------|----------|
| `__getattr__(self, name)` | 访问不存在的属性 |
| `__setattr__(self, name, value)` | 设置属性值 |
| `__delattr__(self, name)` | 删除属性 |
| `__getattribute__(self, name)` | 访问任何属性（包括存在的） |

```python
class Proxy:
    def __init__(self):
        self._data = {}
    
    def __getattr__(self, name):
        """访问不存在的属性时调用"""
        print(f"获取不存在的属性: {name}")
        return None
    
    def __setattr__(self, name, value):
        """设置任何属性时调用"""
        if name == "_data":
            super().__setattr__(name, value)
        else:
            print(f"设置属性: {name} = {value}")
            self._data[name] = value
    
    def __getattribute__(self, name):
        """访问任何属性时调用（包括存在的）"""
        print(f"访问属性: {name}")
        return super().__getattribute__(name)

p = Proxy()
p.name = "张三"  # 设置属性: name = 张三
print(p.name)    # 访问属性: name / 张三
print(p.age)     # 访问属性: age / 获取不存在的属性: age / None
```

## 索引和切片

```python
class MyArray:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            return MyArray(self.data[key])
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __repr__(self):
        return f"MyArray({self.data})"

arr = MyArray([1, 2, 3, 4, 5])
print(arr[2])       # 3
arr[2] = 10
print(arr[2])       # 10
print(arr[1:4])     # MyArray([2, 10, 4])
```

## 其他魔法方法

| 方法 | 说明 |
|------|------|
| `__hash__(self)` | 定义对象的哈希值（用于字典键、集合） |
| `__bool__(self)` | 定义布尔值（用于 `if obj`） |
| `__int__(self)` | 转换为整数 |
| `__float__(self)` | 转换为浮点数 |
| `__index__(self)` | 用于切片索引 |

```python
class Score:
    def __init__(self, value):
        self.value = value
    
    def __bool__(self):
        return self.value >= 60
    
    def __int__(self):
        return self.value
    
    def __hash__(self):
        return hash(self.value)

s1 = Score(85)
s2 = Score(50)
print(bool(s1))  # True
print(bool(s2))  # False
print(int(s1))   # 85
```
