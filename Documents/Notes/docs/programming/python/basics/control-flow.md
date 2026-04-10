# Python 控制流

## if 语句

### 基本语法

```python
if condition:
    # 条件为真时执行
    pass
```

### if-else

```python
age = 18

if age >= 18:
    print("成年人")
else:
    print("未成年人")
```

### if-elif-else

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade)  # B
```

### 嵌套 if

```python
x = 10
y = 20

if x > 0:
    if y > 0:
        print("x 和 y 都为正数")
```

### 条件表达式（三元运算符）

```python
# 语法：值1 if 条件 else 值2
age = 20
status = "成年" if age >= 18 else "未成年"

# 等价于
if age >= 18:
    status = "成年"
else:
    status = "未成年"
```

### 多个条件

```python
x = 10

# 与 (and)
if x > 0 and x < 20:
    print("x 在 0 和 20 之间")

# 或 (or)
if x < 0 or x > 20:
    print("x 不在 0 到 20 范围内")

# 非 (not)
if not x == 0:
    print("x 不等于 0")
```

### 链式比较

```python
x = 10

# Python 特有的写法
if 0 < x < 20:
    print("x 在 0 和 20 之间")

# 等价于
if x > 0 and x < 20:
    print("x 在 0 和 20 之间")
```

### 真假值判断

Python 中以下值被视为 False：
- `None`
- `False`
- 任何数值类型的零（0, 0.0, 0j）
- 空序列（`''`, `[]`, `()`）
- 空映射（`{}`）
- 空集合（`set()`）

```python
# 可以直接用变量作为条件
name = "张三"

if name:  # 非空字符串为 True
    print(f"你好，{name}")
else:
    print("名字不能为空")

# 常见用法：检查列表是否为空
items = []
if items:  # 空列表为 False
    print(f"有 {len(items)} 个项目")
else:
    print("没有项目")
```

## for 循环

### 遍历序列

```python
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "Python":
    print(char)

# 遍历元组
colors = ("红", "绿", "蓝")
for color in colors:
    print(color)
```

### range 函数

```python
# range(stop): 0 到 stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop): start 到 stop-1
for i in range(2, 5):
    print(i)  # 2, 3, 4

# range(start, stop, step): 指定步长
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# 倒序
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

### 遍历字典

```python
person = {"name": "张三", "age": 25, "city": "北京"}

# 遍历键
for key in person:
    print(key)

# 遍历值
for value in person.values():
    print(value)

# 遍历键值对
for key, value in person.items():
    print(f"{key}: {value}")
```

### enumerate 获取索引

```python
fruits = ["苹果", "香蕉", "橙子"]

# 使用 enumerate 同时获取索引和值
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
```

### zip 并行遍历

```python
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(f"{name}: {age}岁")
```

## while 循环

### 基本语法

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 无限循环

```python
while True:
    command = input("输入命令 (q 退出): ")
    if command == "q":
        break
    print(f"执行: {command}")
```

### while-else

```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("循环正常结束")  # 没有被 break 打断时执行
```

## break 和 continue

### break：退出循环

```python
# 查找第一个偶数
numbers = [1, 3, 5, 8, 10, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"找到偶数: {num}")
        break
```

### continue：跳过当前迭代

```python
# 打印奇数
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9
```

## pass 语句

```python
# 占位符，什么都不做
def todo_function():
    pass  # 以后实现

if x > 0:
    pass  # 暂时不处理
```

## match-case 语句（Python 3.10+）

```python
# 类似其他语言的 switch
def get_status_code_desc(code):
    match code:
        case 200:
            return "成功"
        case 404:
            return "未找到"
        case 500:
            return "服务器错误"
        case _:  # 默认情况
            return "未知状态码"

# 匹配字面量
def check_value(x):
    match x:
        case 0:
            print("零")
        case 1:
            print("一")
        case _:
            print("其他")

# 匹配结构
def process_point(point):
    match point:
        case (0, 0):
            print("原点")
        case (0, y):
            print(f"Y 轴上的点: {y}")
        case (x, 0):
            print(f"X 轴上的点: {x}")
        case (x, y):
            print(f"点 ({x}, {y})")
```

## 常见模式

### 循环与 else 组合

```python
# 检查是否为质数
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num} 不是质数")
        break
else:
    print(f"{num} 是质数")  # 循环没有被 break 打断时执行
```

### 列表推导式中的条件

```python
# 筛选偶数
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]  # [2, 4, 6]

# 条件表达式
results = ["偶数" if n % 2 == 0 else "奇数" for n in numbers]
```
