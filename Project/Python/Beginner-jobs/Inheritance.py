#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-11-04 16:30

# 1. 基础继承
# **基类（父类）**定义时不需要加括号，除非你想显式地指定它继承自其他类（但通常默认继承自 object）。
# 子类定义时需要加括号来指定它继承自哪个父类。
class Animal: # 等于 class Animal(object)
    def __init__(self,name):
        self.name = name

    def speak(self):
        return f"{self.name} 发出声音"

class Dog(Animal):
    def speak(self):
        return f"{self.name} 汪汪叫"

dog = Dog("小黑")

#print(dog.speak())

# 输出 " 小黑 汪汪叫"
# dog对象是Dog类的实例，Dog类继承了Animal类的__init__方法和name属性
# 然后Dog类重写了Animal类里的speak,所以输出"汪汪叫"

# 2.super()调用父类方法
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self,brand,model,doors):
        super().__init__(brand,model)
        # 通过super()获取父类__init__方法里的属性,不然下面的实例没有brand,model
        self.doors = doors

    def info(self):
        return f"{super().info()},{self.doors}门"

car1 = Car("丰田","卡罗拉",4)

print(car1.info())

# 3.多重继承
# 多重继承的super()顺序为类的父类顺序，可通过实例.mro()查看
class Flyable:
    def fly(self):
        return "I can fly"
    def speak(self):
        return "wowo"

class Swimmable:
    def swim(self):
        return "I can swim"

#class Duck(Flyable,Animal,Swimmable):
class Duck(Animal,Flyable,Swimmable):
    def speak(self):
        #speak1 = super().speak()
        return f"{self.name},{super().speak()}" # 调用父类Animal的speak(),因为Duck类的继承顺序，的一个就是Animal
    # 另外只有Animal有speak

duck1 = Duck("Big Duck")

print(duck1.speak(),duck1.fly(),duck1.swim())
print(Duck.mro())
# mro()使用C3线性化算法，调用继承类的顺序，如果父类也继承了，将其父类继承类放父类之后，
# 从左到右，深度优先，但要保持一致性（C3 合并规则）。
# 当一个列表中只有一个元素时，这个元素被视为 “头部（head）”，而不是“尾部（tail）”

# 在合并过程中，Python 把每个继承链都视作一个「列表」，然后：
# 头部（head）：列表的第一个元素（即当前候选）。
# 尾部（tail）：列表中除第一个元素外的所有剩余元素。

# class X: pass
# class Y: pass
# class A(X): pass
# class B(Y): pass
# class C(A, B): pass
#
# 对于 class C(A, B)，C3 算法会做：
#
# C.mro = [C] + merge(A.mro, B.mro, [A, B])
#
# [C] + merge([A, X, object],
#             [B, Y, object],
#             [A, B])

# 保证局部顺序一致性（local precedence order），
# 也就是说，class C(A, B) 一定要让 A 出现在 B 之前。

# 因此[A, B] 的存在就是为了：
# 明确表达 “C 的直接父类顺序”；
# 确保 merge 阶段尊重这个顺序
# 如果不加 [A, B]，就会丢失这个「显式继承顺序」的信息。

# [A, B] 被放在 merge() 的最后，是因为它是“父类顺序约束”，不是“继承路径”。
#放在最后可以让 C3 优先尊重每个父类自身的 MRO，再用 [A, B] 来维持局部顺序（A 在 B 前）。

# 假设(正常)
# A.mro = [A, X, object]
# B.mro = [B, X, object]

# [A, X, object]
# [B, X, object]
# [A, B]

# [C, A, B, X, object]

# 假设([A, B] 在前)
# merge([A, B], A.mro, B.mro)
#
# [A, B]
# [A, X, object]
# [B, X, object]

print("----------------------")

# 4. 私有属性和方法
class Mind:
    def __init__(self,thought):
        self.__thought = thought

    def __thought_make(self):
        return self.__thought # 这里是私有变量的返回值

    def get_thought(self):
        return self.__thought_make() # 注意这里是私有函数的返回值

myself = Mind("I Like ***")
print(myself.get_thought())
print(myself._Mind__thought)

# 以单下划线 _ 开头 → 表示“受保护的”（protected）
# 以双下划线 __ 开头 → 表示“私有的”（private）

# class Parent:
#     def __init__(self):
#         self.__secret = "父类的秘密"
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__secret = "子类的秘密"
#
# c = Child()
# print(c._Parent__secret)  # 父类的私有变量
# print(c._Child__secret)   # 子类的私有变量

# 主要用于防冲突而不是安全
# 单下划线 _ 是提醒，双下划线 __ 是保护。
# _ 靠约定，__ 靠机制。

print("----------------------")

# 使用abc模块创建抽象基类，子类必须包含其全部指定方法才可以被创建实例
from abc import ABC, abstractmethod

class Sharp(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Rectangle类必须包含父类里的由@abstractmethod装饰的方法，才可以创建其实例rect
class Rectangle(Sharp):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 5)
print(f"面积: {rect.area()}")
print(f"周长: {rect.perimeter()}")

print("----------------------")

# isinstance() 和 issubclass()
class Animal:
    pass
class Cat(Animal):
    pass
kitty = Cat()

print(isinstance(kitty, Cat))
print(isinstance(kitty, Animal))
print(issubclass(Cat, Animal))
# isinstance 判断是否是类的实例
# issubclass 判断是否是父类的子类

# 代码复用: 继承避免重复代码
# 方法重写: 子类可以覆盖父类方法
# super(): 调用父类方法
# 多重继承: 谨慎使用,注意 MRO
# 抽象类: 定义接口规范
# 定义一组必须实现的接口规范，保证所有子类的行为一致。
#
# 换句话说：
# 抽象类不是为了“能运行”，而是为了防止别人写出不规范的类。

print("----------------------")

# 多态（Polymorphism）
# 通过一个方法，调用不同类的实例--“同一个接口，不同的实现”。

class Payment:
    def pay(self, amount):
        raise NotImplementedError

class Alipay(Payment):
    def pay(self, amount):
        print(f"使用支付宝支付 {amount} 元")

class WechatPay(Payment):
    def pay(self, amount):
        print(f"使用微信支付 {amount} 元")

# 这里的payment: Payment,Payment是指为Payment的类或子类的类的实例。这是类型注解，约定的，没有也可以运行，但是
# 通过mypy检查会出错
def process_payment(payment: Payment, amount):
    payment.pay(amount)

# 调用
process_payment(Alipay(), 100)
process_payment(WechatPay(), 100)

# 输出
# 使用支付宝支付 100 元
# 使用微信支付 100 元

# 鸭子类型
# Python 是动态语言，不要求必须继承同一个父类。
# 只要对象“长得像”就行（有相同的方法），也算多态。
#
# class FakePay:
#     def pay(self, amount):
#         print(f"我是假支付，也能支付 {amount} 元")
#
# process_payment(FakePay(), 88)  # ✅ 正常运行

# 在 Python 中，只要对象有相同的方法名，就能多态调用。
#
# 有抽象类时 → 强约束式多态
#
# 无抽象类时 → 鸭子类型式多态
