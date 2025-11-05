#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-11-04 08:52


# int 整数
a = 2
b = 4
print(a + b, a * b, a ** b)
print("--------------------------")

# float 浮点数

pi = 3.14159
# round()内置函数，对浮点数进行四舍五入
print(round(pi)) # 对pi进行四舍五入
print(round(pi,2)) # 保留指导小数位(四舍五入)

# python 3 使用银行家舍入法(四舍六入五成双)
# 当舍弃的数字为5时，会舍入到最接近的偶数
print(round(2.5)) # 输出 2
print(round(3.5)) # 输出 4
print(round(1.5)) # 输出 2

# 浮点数的精度问题
print(round(2.675, 2))  # 输出: 2.67 而不是 2.68
print(0.1 + 0.2) # 输出 0.30000000000004

# ndigits为负数

# 可以舍入到十位、百位等
print(round(1234, -2))  # 输出: 1200
print(round(5678, -3))  # 输出: 6000

print("--------------------------")

# 字符串

s = "Python"
print(s[0],s[-1]) # 输出第一个字符P和最后一个字符n
print(s.upper(), s.lower()) # 全部大写和全部小写
print(s.replace("Py", "My")) # 替换

name = "Steve"
age = 19
print(f"Name:{name},Age:{age}")

print("--------------------------")

# bool 布尔值

x = 10
y = 9
print(x > y) # True
print(bool(0), bool(""), bool([]), bool(()), bool({})) # all False

print("--------------------------")

# list 列表

nums = [1, 2, 3]
nums.append(4)
print(nums) # [1, 2, 3, 4]
nums[2] = 30
print(nums, len(nums))

print("--------------------------")

# tuple 元组

t = (1, 2, 3)
print(t[2]) # 3
# t[2] = 2 # error

print("--------------------------")

# set 集合
s = {1, 2, 3, 4, 4, 4}
print(s) # {1, 2, 3, 4} 去除重复项目

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) # {1, 2, 3, 4, 5} 集合并集,去重，合并
print(a & b) # {3} 集合交集
