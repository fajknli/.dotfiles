String
###########

字符串是 Python 中最常用的数据类型之一，用于表示文本数据。

字符串基础
========================================================

1. 创建字符串
--------------------------------------------------------

::

    # 单引号
    s1 = 'Hello'
    # 双引号
    s2 = "World"
    # 三引号（多行字符串）
    s3 = '''这是一个
    多行
    字符串'''
    s4 = """这也是一个
    多行字符串"""

    print(s1)
    print(s2)
    print(s3)
    print(s4)

2. 字符串索引和切片
--------------------------------------------------------

::

    s = "Python"

    # 索引（从0开始）
    print(s[0])    # 'P' - 第一个字符
    print(s[1])    # 'y'
    print(s[-1])   # 'n' - 最后一个字符
    print(s[-2])   # 'o' - 倒数第二个字符

    # 切片 [start:end:step]
    print(s[0:3])   # 'Pyt' - 索引0到2
    print(s[2:])    # 'thon' - 索引2到最后
    print(s[:4])    # 'Pyth' - 开始到索引3
    print(s[::2])   # 'Pto' - 每隔一个字符
    print(s[::-1])  # 'nohtyP' - 反转字符串

字符串常用方法
========================================================

1. 大小写转换
--------------------------------------------------------

::

    s = "Python Programming"

    print(s.upper())        # 'PYTHON PROGRAMMING'
    print(s.lower())        # 'python programming'
    print(s.capitalize())   # 'Python programming' - 首字母大写
    print(s.title())        # 'Python Programming' - 每个单词首字母大写
    print(s.swapcase())     # 'pYTHON pROGRAMMING' - 大小写互换

2. 查找和替换
--------------------------------------------------------

::

    s = "Hello World, Hello Python"

    # 查找
    print(s.find("Hello"))      # 0 - 第一次出现的位置
    print(s.find("Hello", 1))   # 13 - 从位置1开始查找
    print(s.find("Java"))       # -1 - 未找到
    print(s.index("World"))     # 6 - 类似find，但未找到会报错

    # 替换
    print(s.replace("Hello", "Hi"))     # 'Hi World, Hi Python'
    print(s.replace("Hello", "Hi", 1))  # 'Hi World, Hello Python' - 只替换一次

    # 计数
    print(s.count("Hello"))     # 2 - 出现次数

3. 字符串判断
--------------------------------------------------------

::

    s1 = "Python123"
    s2 = "PYTHON"
    s3 = "python"
    s4 = "123"
    s5 = "   "
    s6 = "Hello World"

    print(s1.isalnum())     # True - 字母或数字
    print(s1.isalpha())     # False - 纯字母
    print(s4.isdigit())     # True - 纯数字
    print(s2.isupper())     # True - 全大写
    print(s3.islower())     # True - 全小写
    print(s5.isspace())     # True - 纯空白字符
    print(s6.istitle())     # True - 每个单词首字母大写

4. 去除空白
--------------------------------------------------------

::

    s = "   Hello World   "

    print(s.strip())        # 'Hello World' - 去除两端空白
    print(s.lstrip())       # 'Hello World   ' - 去除左端空白
    print(s.rstrip())       # '   Hello World' - 去除右端空白

    # 去除特定字符
    s2 = "***Hello***"
    print(s2.strip('*'))    # 'Hello'

5. 对齐和填充
--------------------------------------------------------

::

    s = "Python"

    print(s.ljust(10))      # 'Python    ' - 左对齐，宽度10
    print(s.rjust(10))      # '    Python' - 右对齐，宽度10
    print(s.center(10))     # '  Python  ' - 居中对齐，宽度10

    # 使用指定字符填充
    print(s.ljust(10, '-')) # 'Python----'
    print(s.rjust(10, '*')) # '****Python'
    print(s.center(10, '+')) # '++Python++'

6. 分割和连接
--------------------------------------------------------

::

    s = "apple,banana,orange"

    # 分割
    print(s.split(','))           # ['apple', 'banana', 'orange']
    print(s.split(',', 1))        # ['apple', 'banana,orange'] - 只分割一次

    # 行分割
    s2 = "Line1\nLine2\nLine3"
    print(s2.splitlines())        # ['Line1', 'Line2', 'Line3']

    # 连接
    fruits = ['apple', 'banana', 'orange']
    print(','.join(fruits))       # 'apple,banana,orange'
    print('-'.join(fruits))       # 'apple-banana-orange'

字符串格式化
========================================================

1. f-string (推荐)
--------------------------------------------------------

::

    name = "Alice"
    age = 25
    score = 95.5

    print(f"Name: {name}, Age: {age}")                    # Name: Alice, Age: 25
    print(f"Score: {score:.1f}")                         # Score: 95.5
    print(f"Next year: {age + 1}")                       # Next year: 26
    print(f"Name uppercase: {name.upper()}")             # Name uppercase: ALICE

2. format() 方法
--------------------------------------------------------

::

    name = "Bob"
    age = 30

    print("Name: {}, Age: {}".format(name, age))         # Name: Bob, Age: 30
    print("Name: {0}, Age: {1}".format(name, age))       # 使用位置
    print("Name: {n}, Age: {a}".format(n=name, a=age))   # 使用关键字

3. % 格式化 (传统方法)
--------------------------------------------------------

::

    name = "Charlie"
    age = 35

    print("Name: %s, Age: %d" % (name, age))             # Name: Charlie, Age: 35

转义字符
========================================================

::

    print("Hello\nWorld")        # 换行
    print("Hello\tWorld")        # 制表符
    print("She said: \"Hello\"") # 双引号
    print('It\'s mine')          # 单引号
    print("Backslash: \\")       # 反斜杠

    # 原始字符串（忽略转义）
    print(r"Hello\nWorld")       # Hello\nWorld
    print(r"C:\Users\Name")      # C:\Users\Name

字符串编码
========================================================

::

    s = "你好，世界"

    # 编码为字节
    bytes_data = s.encode('utf-8')
    print(bytes_data)            # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c'

    # 解码为字符串
    new_s = bytes_data.decode('utf-8')
    print(new_s)                 # 你好，世界

实用技巧
========================================================

1. 检查前缀和后缀
--------------------------------------------------------

::

    s = "hello_world.py"

    print(s.startswith("hello"))    # True
    print(s.endswith(".py"))        # True
    print(s.endswith((".py", ".txt", ".java")))  # True - 元组中任意一个

2. 字符串判断和转换
--------------------------------------------------------

::

    # 检查字符串内容
    s1 = "123"
    s2 = "ABC"
    s3 = "abc123"

    print(s1.isnumeric())    # True
    print(s2.isalpha())      # True
    print(s3.isalnum())      # True

    # 大小写检查
    print("PYTHON".isupper())  # True
    print("python".islower())  # True

3. 字符串映射转换
--------------------------------------------------------

::

    # 创建转换表
    trans_table = str.maketrans('aeiou', '12345')
    s = "hello world"
    print(s.translate(trans_table))  # h2ll4 w4rld

实际应用示例
========================================================

1. 处理用户输入
--------------------------------------------------------

::

    def process_name():
        name = input("请输入姓名: ").strip()
        if name:
            return name.title()  # 首字母大写
        else:
            return "匿名用户"

    print(f"欢迎，{process_name()}!")

2. 文件扩展名处理
--------------------------------------------------------

::

    def get_file_info(filename):
        """获取文件信息"""
        name = filename.rsplit('.', 1)[0]  # 去除扩展名
        extension = filename.rsplit('.', 1)[1] if '.' in filename else ''
        return name, extension

    filename = "document.pdf"
    name, ext = get_file_info(filename)
    print(f"文件名: {name}, 扩展名: {ext}")  # 文件名: document, 扩展名: pdf

3. 生成表格格式
--------------------------------------------------------

::

    def print_table(data):
        """打印格式化的表格"""
        # 找出每列的最大宽度
        col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
        
        for row in data:
            # 每列左对齐，用空格填充
            formatted_row = [str(item).ljust(width) for item, width in zip(row, col_widths)]
            print(' | '.join(formatted_row))

    # 示例数据
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', '25', 'New York'],
        ['Bob', '30', 'London'],
        ['Charlie', '35', 'Tokyo']
    ]

    print_table(data)

4. 密码强度检查
--------------------------------------------------------

::

    def check_password_strength(password):
        """检查密码强度"""
        if len(password) < 8:
            return "弱：密码长度至少8位"
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        score = sum([has_upper, has_lower, has_digit, has_special])
        
        if score == 4:
            return "强"
        elif score >= 2:
            return "中"
        else:
            return "弱"

    print(check_password_strength("Abc123!@#"))  # 强

性能考虑
========================================================

1. 字符串连接
--------------------------------------------------------

::

    # 不推荐 - 每次连接都创建新字符串
    result = ""
    for i in range(1000):
        result += str(i)

    # 推荐 - 使用列表推导式
    result = "".join(str(i) for i in range(1000))

2. 成员检查
--------------------------------------------------------

::

    s = "hello world"

    # 推荐 - 使用 in 运算符
    if "world" in s:
        print("找到")

    # 不推荐 - 使用 find()
    if s.find("world") != -1:
        print("找到")

总结
========================================================

字符串是 Python 编程的基础，掌握好：

基本操作：索引、切片、连接

常用方法：查找、替换、分割、大小写转换

格式化：f-string、format()、% 格式化

编码处理：encode()、decode()

实用技巧：各种字符串判断和处理方法

这些知识对于文本处理、数据清洗、用户交互等场景都非常重要！
