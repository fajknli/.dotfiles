#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-11-02 01:45

# 定义一个简单的类
class MyClass:
    pass  # 这个类什么也不做，仅用于演示

# 创建两个实例
a = MyClass()
b = MyClass()
c = a

# 比较 a 和 b 是否是同一个对象（即是否指向同一块内存地址）
print(a is b)  # 输出: False
# is 操作符比较的是对象的身份（identity）

# 补充：它们的类型是一样的
print(type(a) == type(b))  # 输出: True

# 补充：它们都是 MyClass 的实例
print(isinstance(a, MyClass))  # 输出: True
print(isinstance(b, MyClass))  # 输出: True

# 补充：查看它们的 id（内存地址）
print(id(a))  # 例如: 140234567890123
print(id(b))  # 例如: 140234567890456 （和 a 不同）

print(a == b)
print(a.__eq__(b))
print(a.__eq__(c))
