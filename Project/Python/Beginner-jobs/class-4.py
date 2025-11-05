#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-11-03 21:21


class MyClass:
    class_variable = 42  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

    def instance_method(self):  # 实例方法
        print(f"Hello from instance method! My name is {self.name}")

    @classmethod
    def class_method(cls):  # 类方法
        print(f"Hello from class method! Class variable is {cls.class_variable}")

    @staticmethod
    def static_method():  # 静态方法
        print("Hello from static method! I don't need class or instance.")

# 创建一个 MyClass 的实例
obj = MyClass("Alice")

# 调用实例方法
obj.instance_method()  # 输出 "Hello from instance method! My name is Alice"

# 调用类方法
MyClass.class_method()  # 输出 "Hello from class method! Class variable is 42"

# 调用静态方法
MyClass.static_method()  # 输出 "Hello from static method! I don't need class or instance."

