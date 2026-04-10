# Python 面向对象编程

## 类与对象

### 定义类

```python
class Person:
    """人类"""
    pass

# 创建对象
p = Person()
print(type(p))  # <class '__main__.Person'>
```

### 构造函数 __init__

```python
class Person:
    def __init__(self, name, age):
        self.name = name   # 实例属性
        self.age = age

p = Person("张三", 25)
print(p.name)  # 张三
print(p.age)   # 25
```

### 实例方法

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")
    
    def birthday(self):
        self.age += 1
        print(f"{self.name}生日快乐，现在{self.age}岁")

p = Person("张三", 25)
p.introduce()   # 我叫张三，今年25岁
p.birthday()    # 张三生日快乐，现在26岁
```

## 类属性与实例属性

```python
class Student:
    # 类属性（所有实例共享）
    school = "北京大学"
    count = 0
    
    def __init__(self, name):
        self.name = name    # 实例属性
        Student.count += 1

# 访问类属性
print(Student.school)   # 北京大学

# 通过实例访问类属性
s1 = Student("张三")
s2 = Student("李四")
print(s1.school)        # 北京大学
print(Student.count)    # 2

# 修改类属性
Student.school = "清华大学"
print(s1.school)        # 清华大学
```

## 类方法与静态方法

### 类方法（@classmethod）

```python
class Student:
    count = 0
    
    def __init__(self, name):
        self.name = name
        Student.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def create_from_string(cls, info):
        """工厂方法"""
        name = info.split(",")[0]
        return cls(name)

print(Student.get_count())  # 0
s = Student.create_from_string("张三,25")
print(Student.get_count())  # 1
```

### 静态方法（@staticmethod）

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def is_even(n):
        return n % 2 == 0

# 不需要实例化
print(Math.add(3, 5))     # 8
print(Math.is_even(4))    # True
```

### 三种方法对比

| 类型 | 第一个参数 | 调用方式 | 访问权限 |
|------|-----------|----------|----------|
| 实例方法 | self | 实例.方法() | 可访问实例属性和类属性 |
| 类方法 | cls | 类.方法() 或 实例.方法() | 只能访问类属性 |
| 静态方法 | 无 | 类.方法() 或 实例.方法() | 不能访问类属性和实例属性 |

## 属性封装

### 私有属性

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # 公有属性
        self.__balance = balance    # 私有属性（双下划线）
    
    def get_balance(self):
        """获取余额"""
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

account = BankAccount("张三", 1000)
print(account.owner)        # 张三
# print(account.__balance)  # AttributeError
print(account.get_balance()) # 1000

# 名称修饰（不推荐使用）
print(account._BankAccount__balance)  # 1000，但仍然可以访问
```

### 属性装饰器（@property）

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """获取摄氏度"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """设置摄氏度"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """华氏度（只读）"""
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)        # 25
print(temp.fahrenheit)     # 77.0

temp.celsius = 30          # 使用 setter
print(temp.celsius)        # 30
# temp.fahrenheit = 80     # AttributeError（只读）
```

## 继承

### 单继承

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name}发出声音")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}汪汪叫")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}喵喵叫")

dog = Dog("旺财")
cat = Cat("咪咪")
dog.speak()  # 旺财汪汪叫
cat.speak()  # 咪咪喵喵叫
```

### super() 调用父类

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return f"{self.name}，{self.age}岁"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类构造函数
        self.breed = breed
    
    def info(self):
        return f"{super().info()}，品种：{self.breed}"

dog = Dog("旺财", 3, "金毛")
print(dog.info())  # 旺财，3岁，品种：金毛
```

### 多重继承

```python
class Flyable:
    def fly(self):
        print("飞行中")

class Swimmable:
    def swim(self):
        print("游泳中")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("嘎嘎叫")

duck = Duck()
duck.fly()   # 飞行中
duck.swim()  # 游泳中
duck.quack() # 嘎嘎叫
```

### MRO（方法解析顺序）

```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

d = D()
d.method()              # B
print(D.__mro__)        # (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

## 多态

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

def print_area(shape):
    print(f"面积: {shape.area()}")

rect = Rectangle(5, 3)
circle = Circle(4)
print_area(rect)   # 面积: 15
print_area(circle) # 面积: 50.24
```

## 抽象基类（ABC）

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("汽车启动")
    
    def stop(self):
        print("汽车停止")

# vehicle = Vehicle()  # TypeError，不能实例化抽象类
car = Car()            # 必须实现所有抽象方法
car.start()            # 汽车启动
```

## 运算符重载

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """重载 + 运算符"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """重载 - 运算符"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        """重载 == 运算符"""
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        """重载 print()"""
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)           # Vector(4, 6)
print(v1 == v2)     # False
```

## 特殊方法（魔法方法）

| 方法 | 说明 | 触发时机 |
|------|------|----------|
| `__init__(self, ...)` | 构造函数 | 创建对象时 |
| `__del__(self)` | 析构函数 | 对象销毁时 |
| `__str__(self)` | 字符串表示 | `print(obj)`、`str(obj)` |
| `__repr__(self)` | 开发者字符串 | `repr(obj)` |
| `__len__(self)` | 长度 | `len(obj)` |
| `__getitem__(self, key)` | 索引获取 | `obj[key]` |
| `__setitem__(self, key, value)` | 索引设置 | `obj[key] = value` |
| `__call__(self, *args)` | 可调用对象 | `obj()` |
| `__enter__(self)` | 上下文管理器 | `with obj:` |
| `__exit__(self, ...)` | 上下文管理器 | 退出 with 块 |

```python
class MyList:
    def __init__(self, items):
        self._items = items
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __call__(self):
        print(f"列表内容: {self._items}")

lst = MyList([1, 2, 3])
print(len(lst))    # 3
print(lst[1])      # 2
lst()              # 列表内容: [1, 2, 3]
```
