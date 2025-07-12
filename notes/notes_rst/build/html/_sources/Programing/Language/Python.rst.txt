Python
#########

1. python交互界面操作
=======================

1. 从命令行进入python交互界面
------------------------------

::

    python

    or

    python3

    python --version 查看版本

2. 从python交互界面退出到终端环境
-----------------------------------

::

    快捷键: Ctrl + d
    >>>quit()
    >>>exit()

3. 清空已经存在的python交互界面的命令
--------------------------------------

::

    快捷键: Ctrl + c

4. 在终端下直接运行python命令，不进入交互界面
-----------------------------------------------

::

    python -c 'print("Hello, World")'

5. 执行python脚本
---------------------

::

    python <Python Script Name>



2. 变量定义
===========

1. 定义变量与赋值
------------------
::

    # Integer
    a = 2
    print(a)
    # Output: 2
    
    # Integer
    b = 9223372036854775807
    print(b)
    # Output: 9223372036854775807
    
    # Floating point
    pi = 3.14
    print(pi)
    # Output: 3.14
    
    # String
    c = 'A'
    print(c)
    # Output: A
    
    # String
    name = 'John Doe'
    print(name)
    # Output: John Doe
    
    # Boolean
    q = True
    print(q)
    # Output: True
    
    # Empty value or null data type
    x = None
    print(x)
    # Output: None

2. python关键字 
-------------------

您不能使用 python 的关键字作为有效的变量名。您可以通过以下方式查看关键字列表：

::

    import keyword
    print(keyword.kwlist)


    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

3. 变量命名规则
-----------------

1. 变量名必须以字母或下划线开头。

2. 变量名的其余部分可以由字母、数字和下划线组成。

3. 名称区分大小写。

在为变量分配必要的内存区域时，Python 解释器会自动为它选择最合适的内置
类型：

::

    a = 2
    print(type(a))
    # Output: <type 'int'>

    b = 9223372036854775807
    print(type(b))
    # Output: <type 'int'>

    pi = 3.14
    print(type(pi))
    # Output: <type 'float'>

    c = 'A'
    print(type(c))
    # Output: <type 'str'>

    name = 'John Doe'
    print(type(name))
    # Output: <type 'str'>

    q = True
    print(type(q))
    # Output: <type 'bool'>

    x = None
    print(type(x))
    # Output: <type 'NoneType'>

4. Python 中赋值的奥妙
----------------------

在一行中为多个变量分配多个值:

::

    a, b, c = 1, 2, 3
    print(a, b, c)
    # Output: 1 2 3

还可以同时为多个变量赋值

::

    a = b = c = 1
    print(a, b, c)
    # Output: 1 1 1

列表以及字典什么的也可以，它是重新赋值，不是将值添加进去

::

    x = y = [7, 8, 9]
    x = [13, 8, 9]
    print(y)
    print(x)
    # y Output: [7, 8, 9]
    # x Output: [13, 8, 9]

In this case , x=y , if u change any one of them ,it will change them all 

::

    x = y = [7, 8, 9]
    x[0] = 13
    print(y)
    print(x)
    # y Output: [13, 8, 9]
    # x Output: [13, 8, 9]

嵌套列表

::

    x = [1, 2, [3, 4, 5], 6, 7] # this is nested list
    print x[2]
    # Output: [3, 4, 5]
    print x[2][1]
    # Output: 4

Python 中的变量不一定要保持最初定义时的类型

::

    a = 2
    print(a)
    # Output: 2

    a = "New value"
    print(a)
    # Output: New value

3. 缩进代码块
===============

**缩进始终使用 4 个空格**

Python 使用缩进来划分控制和循环结构。这有助于提高 Python 的可读性，但是
需要程序员密切注意空白的使用。因此，编辑器的误判可能导致
代码以意想不到的方式运行。
Python 使用冒号 (:) 和缩进来显示代码块的开始和结束位置（如果您来自其他语言，请不要混淆冒号和缩进）。
如果您来自其他语言，请不要将其与三元运算符混淆）。也就是说，在
Python 中的代码块，如函数、循环、if 子句和其它结构体，没有结束标识符。所有代码块都以
冒号开始，然后包含它下面的缩进行。

::

    def my_function():
        a = 2
        return a
    print(my_function())

    or

    if a > b:
        print(a)
    else:
        print(b)

空块会导致缩进错误（IndentationError）。当您有一个没有内容的块时，请使用 pass（一条什么也不做的命令）。
没有内容：

::

    def will_be_implemented_later():
        pass

4. 数据类型
===========

1. 内置类型
-----------

1. 布尔值
''''''''''''

bool：布尔值，表示 "真 "或 "假"。可以对布尔值进行逻辑运算，如 and、or、not。

::

    x or y   # if x is False then y otherwise x
    x and y  # if x is False then x otherwise y
    not x    # if x is True then False, otherwise True

在 Python 2.x 和 Python 3.x，布尔也是一个 int。bool 类型是 int 类型的子类，True 和
False 是它的唯一实例：

::

    issubclass(bool, int) # True
    isinstance(True, bool) # True
    isinstance(False, bool) # True

如果在算术运算中使用布尔值，它们的整数值（1 和 0 表示 True 和 False）将用于
返回整数结果：

::

    True + False == 1 # 1 + 0 == 1
    True * True == 1 # 1 * 1 == 1

2. 数字
''''''''

- int：整数

::

    a = 2
    b = 100
    c = 123456789
    d = 38563846326424324

Python 中的整数是任意大小的。

.. note::

    在 Python 的旧版本中，有一种 long 类型，它与 int 不同。这两种类型已经
    已经统一。

- 浮点数

精度取决于实现方式和系统架构，对于
CPython 的 float 数据类型对应于 C 语言的 double。

::

    a = 2.0
    b = 100.e0
    c = 123456789.e1

- 复数

::

    a = 2 + 1j
    b = 100 + 10j

如果操作数为复数，<、<=、> 和 >= 操作符将引发 TypeError 异常。

3. 字符串
''''''''''

Python 3.x Version ≥ 3.0

- str: a unicode string. The type of 'hello'
- bytes: a byte string. The type of b'hello'

Python 2.x Version ≤ 2.7

- str: a byte string. The type of 'hello'
- bytes: synonym for str
- unicode: a unicode string. The type of u'hello'


4. 序列和集合
'''''''''''''

Python 区分有序序列和无序集合（如 set 和 dict）。

- 字符串（str、bytes、unicode）是序列
- reversed：具有反转函数的 str 的颠倒顺序

::

    a = reversed('hello')

- tuple 元组：任何类型的 n 个值的有序集合（n >= 0）。

::

    a = (1, 2, 3)
    b = ('a', 1, 'python', (1, 2))
    b[2] = 'something else' # returns a TypeError

支持索引；不可变；如果所有成员都是可散列值，则可散列值

- list 列表：n 个值的有序集合（n >= 0）

::

    a = [1, 2, 3]
    b = ['a', 1, 'python', (1, 2), [1, 2]]
    b[2] = 'something else' # allowed

不可散列；可变。

- set 集合：唯一值的无序集合。项目必须散列。

::

    a = {1, 2, 'a'}

- dict：唯一键值对的无序集合；键必须是可散列的。

::

    a = {1: 'one',
         2: 'two'}

    b = {'a': [1, 2, 3],
         'b': 'a string'}

2. 内置常量
-------------

除了内置数据类型，内置命名空间中还有少量内置常量：

:True：内置类型 bool 的真实值
:False：内置类型 bool 的 false 值
:None：用于指示值不存在的单一实例对象。
:省略号或...：在核心 Python3+ 的任何地方使用，在 Python2.7+ 中作为数组表示法的一部分有限使用。numpy 和相关软件包将其用作数组中的“包含所有内容”引用。
:NotImplemented：用于向 Python 指示特殊方法不支持特定参数，如果可用，Python 将尝试替代方案。

::

    a = None # 不分配任何值。以后可以分配任何有效的数据类型

.. note::

    Python 3.x Version ≥ 3.0:

    None 没有任何自然排序。不再支持使用排序比较操作符（<, <=, >=, >）。 并将引发 TypeError。

    Python 2.x Version ≤ 2.7:

    None 总是小于任何数字（None < -32 的值为 True）。

3. 测试变量类型
---------------

::

    a = '123'
    print(type(a))
    # Out: <class 'str'>

测试某物是否属于 NoneType：

::

    x = None
    if x is None:
        print('Not a surprise, I just defined x as None.')

4. 数据类型之间的转换
----------------------

1. 显式数据类型转换。
例如，"123 "是 str 类型，可以使用 int 函数将其转换为整数。

::

    a = '123'
    b = int(a)

2. 从float字符串（如'123.456'）转换可以使用float函数完成。

::

    a = '123.456'
    b = float(a)
    c = int(a)  # ValueError：以 10 为底的 int() 的无效字面量：'123.456
    d = int(b)  # 123

3. 转换序列或集合类型

::

    a = 'hello'
    list(a) # ['h', 'e', 'l', 'l', 'o']
    set(a)
    # {'o', 'e', 'l', 'h'}
    tuple(a) # ('h', 'e', 'l', 'l', 'o')

4. 在字面定义时明确字符串类型

只需在引号前加上一个字母标签，就可以知道要定义的字符串类型。


:b'foo bar'：在 Python 3 中为字节结果，在 Python 2 中为字符串结果
:u'foo bar'： Python 3 中为 str，Python 2 中为 unicode
:foo bar'：结果字符串
:r'foo bar'：所谓的原始字符串，不需要转义特殊字符，一切都按照您输入的内容逐字记录。都是按您输入的内容逐字记录的

::

    normal = 'foo\nbar'    # foo
                           # bar

    escaped = 'foo\\nbar'  # foo\nbar

    raw = r'foo\nbar'      # foo\nbar

5. 可变和不可变数据类型

向列表中添加一个数字。列表是一种可变数据类型。

::

    def f(m):
        m.append(3)

    x = [1, 2]
    f(x)  # 调用函数对x列表进行操作,结果就是给x列表添加了个'3'
    x == [1, 2] # 已经修改了x列表，所以这个会报错

如果一个对象不能以任何方式改变，则称为不可变对象。例如，整数是不可变的，因为
无法更改：

.. note::

    请注意，变量本身是可变的，因此我们可以重新分配变量 x，但这并不会改变
    x 先前指向的对象。它只是让 x 指向一个新的对象。
    实例可变的数据类型称为可变数据类型，不可变对象和
    数据类型。

============================      ============================
不可变数据类型示例                  可变数据类型示例
============================      ============================
int, long, float, complex          bytearray
str                                list
bytes                              set
tuple                              dict
frozenset
============================      ============================





