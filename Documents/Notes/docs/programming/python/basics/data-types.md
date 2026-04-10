# Python 数据类型

## 变量

Python 中的变量不需要声明类型，直接赋值即可。

```python
# 变量赋值
name = "张三"
age = 25
score = 92.5
is_active = True

# 同时赋值多个变量
a, b, c = 1, 2, 3

# 多个变量赋相同值
x = y = z = 0
```

变量命名规则：
- 以字母或下划线开头
- 只能包含字母、数字、下划线
- 区分大小写
- 不能使用关键字（如 `if`、`for`、`while`）

## 基本数据类型

### 整数 (int)

```python
a = 10          # 十进制
b = 0b1010      # 二进制
c = 0o12        # 八进制
d = 0xA         # 十六进制

# 整数没有长度限制
large = 10 ** 100
```

### 浮点数 (float)

```python
pi = 3.14159
e = 2.71828
scientific = 1.23e-4  # 科学计数法
```

### 布尔值 (bool)

```python
is_ok = True
is_error = False

# 布尔值本质是 1 和 0
True + True   # 2
False * 10    # 0
```

### 字符串 (str)

```python
# 定义字符串
single = 'Hello'
double = "World"
multi_line = """这是
多行
字符串"""

# 字符串操作
name = "Python"
name[0]          # 'P'
name[-1]         # 'n'
name[1:4]        # 'yth'
len(name)        # 6

# 字符串拼接
"Hello" + " " + "World"   # "Hello World"

# 字符串格式化
name = "张三"
age = 25
f"我叫{name}，今年{age}岁"   # f-string（推荐）
"我叫%s，今年%d岁" % (name, age)  # % 格式化
"我叫{}，今年{}岁".format(name, age)  # format 方法
```

### 空值 (NoneType)

```python
result = None
if result is None:
    print("没有返回值")
```

## 复合数据类型

### 列表 (list)

有序、可变、可重复。

```python
# 定义
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# 访问
numbers[0]     # 1
numbers[-1]    # 5
numbers[1:3]   # [2, 3]

# 修改
numbers[0] = 10
numbers.append(6)      # [10, 2, 3, 4, 5, 6]
numbers.insert(0, 0)   # [0, 10, 2, 3, 4, 5, 6]
numbers.remove(10)     # 删除值为 10 的元素
last = numbers.pop()   # 删除并返回最后一个元素

# 列表推导式
squares = [x**2 for x in range(5)]   # [0, 1, 4, 9, 16]
```

### 元组 (tuple)

有序、不可变、可重复。

```python
# 定义
point = (10, 20)
single = (1,)     # 单元素元组需要逗号
empty = ()

# 访问
point[0]    # 10
point[-1]   # 20

# 解包
x, y = point   # x=10, y=20

# 元组不可修改
point[0] = 5   # TypeError
```

### 字典 (dict)

无序、键值对、键唯一。

```python
# 定义
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}

# 访问
person["name"]           # "张三"
person.get("age")        # 25
person.get("email", "无") # "无"

# 修改
person["age"] = 26
person["email"] = "zhang@example.com"

# 删除
del person["city"]
age = person.pop("age")

# 遍历
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```

### 集合 (set)

无序、不可重复、可变。

```python
# 定义
fruits = {"apple", "banana", "orange"}

# 操作
fruits.add("grape")
fruits.remove("banana")
is_apple = "apple" in fruits

# 集合运算
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # 并集 {1, 2, 3, 4, 5, 6}
a & b   # 交集 {3, 4}
a - b   # 差集 {1, 2}
a ^ b   # 对称差 {1, 2, 5, 6}
```

## 类型转换

```python
# 转换为整数
int("123")      # 123
int(3.14)       # 3
int(True)       # 1

# 转换为浮点数
float("3.14")   # 3.14
float(5)        # 5.0

# 转换为字符串
str(123)        # "123"
str(3.14)       # "3.14"

# 转换为布尔值
bool(0)         # False
bool(1)         # True
bool("")        # False
bool("abc")     # True
bool([])        # False
```

## 类型检查

```python
type(10)        # <class 'int'>
type(3.14)      # <class 'float'>
type("hello")   # <class 'str'>
type([1, 2])    # <class 'list'>

# 检查类型
isinstance(10, int)     # True
isinstance(10, (int, float))  # True
```

## 可变与不可变

| 类型 | 可变性 |
|------|--------|
| int | 不可变 |
| float | 不可变 |
| bool | 不可变 |
| str | 不可变 |
| tuple | 不可变 |
| list | 可变 |
| dict | 可变 |
| set | 可变 |

```python
# 不可变：修改会创建新对象
a = 10
b = a
a = 20
print(b)    # 10（b 还是原来的值）

# 可变：修改会影响所有引用
a = [1, 2, 3]
b = a
a.append(4)
print(b)    # [1, 2, 3, 4]（b 也被修改）
```
