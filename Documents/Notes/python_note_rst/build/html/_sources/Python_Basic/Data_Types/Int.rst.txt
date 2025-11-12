Int
#######

基本概念
==========

1. 基本整数操作
-----------------

::

    # 定义整数
    a = 10
    b = -5
    c = 0

    # 基本算术运算
    print(5 + 3)    # 加法: 8
    print(10 - 4)   # 减法: 6
    print(3 * 4)    # 乘法: 12
    print(15 / 3)   # 除法: 5.0 (返回浮点数)
    print(15 // 3)  # 整数除法: 5 (返回整数)
    print(17 % 5)   # 取模: 2
    print(2 ** 3)   # 幂运算: 8

    # 赋值运算符
    x = 5
    x += 3  # 等同于 x = x + 3
    print(x)  # 8

2. 整数类型的特点
-----------------

::

    # Python 整数是任意精度的
    big_number = 123456789012345678901234567890
    print(big_number)  # 可以处理非常大的整数

    # 类型检查
    num = 42
    print(type(num))  # <class 'int'>
    print(isinstance(num, int))  # True

3. 进制表示
-----------

::

    # 不同进制的整数表示
    decimal = 100        # 十进制
    binary = 0b1100100   # 二进制 (前缀 0b 或 0B)
    octal = 0o144        # 八进制 (前缀 0o 或 0O)
    hexadecimal = 0x64   # 十六进制 (前缀 0x 或 0X)

    print(binary)    # 100
    print(octal)     # 100
    print(hexadecimal)  # 100

    # 进制转换函数
    print(bin(100))  # '0b1100100'
    print(oct(100))  # '0o144'
    print(hex(100))  # '0x64'

4. 常用整数函数和方法
------------------------

::

    # 绝对值
    print(abs(-10))  # 10

    # 幂运算
    print(pow(2, 3))  # 8

    # 最大值和最小值
    print(max(1, 5, 2, 8))  # 8
    print(min(1, 5, 2, 8))  # 1

    # 四舍五入
    print(round(3.14159))    # 3
    print(round(3.14159, 2)) # 3.14

    # 转换为整数
    print(int(3.14))     # 3
    print(int("123"))    # 123
    print(int("101", 2)) # 5 (将二进制字符串转换为十进制)

5. 位运算

::

    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101

    print(a & b)   # 按位与: 12 = 0000 1100
    print(a | b)   # 按位或: 61 = 0011 1101
    print(a ^ b)   # 按位异或: 49 = 0011 0001
    print(~a)      # 按位取反: -61
    print(a << 2)  # 左移: 240 = 1111 0000
    print(a >> 2)  # 右移: 15 = 000
