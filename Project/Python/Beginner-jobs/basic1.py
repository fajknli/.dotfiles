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

# print(*objects, sep=' ', end='\n', file=None, flush=False)

# sep='' 指定多个对象之间的分隔符（默认为空格）
# print(1, 2, 3)              # 输出: 1 2 3
# print(1, 2, 3, sep='-')     # 输出: 1-2-3
# print(1, 2, 3, sep=' -> ')  # 输出: 1 -> 2 -> 3
# print(1, 2, 3, sep='')      # 输出: 123（无分隔符）

# end='' 指定输出结尾的字符（默认为换行符 \n）
#print(end="\n") # end="\n" 表示以换行符结尾, end="" 表示以空字符结尾

# file= 指定输出到文件或其他流（默认为 sys.stdout）
# 输出到文件
# with open('output.txt', 'w') as f:
#     print("Hello File", file=f)
#
# # 输出到标准错误
# import sys
# print("Error message", file=sys.stderr)

# flush=True 刷新缓冲区,默认flush=False
# import time
#
# # 不使用 flush
# print("Loading...", end='')
# time.sleep(2)  # 这2秒内可能看不到输出
# print("Done")
#
# # 使用 flush
# print("Loading...", end='', flush=True)
# time.sleep(2)  # 立即显示 "Loading..."
# print("Done")

# 这里涉及到 输出缓冲 的概念

#在大多数情况下，标准输出是行缓冲的：
#遇到换行符 \n 时会立即刷新缓冲区,但上面代码里没有换行符，所以内容在缓冲区里，没有刷新
#下面那个代码，里面有flush=True会强制刷新，所以在运行时就会马上输出缓冲区的内容
#缓冲区满时会自动刷新
#程序正常结束时会自动刷新

# ljust() rjust()

# for i in range(1, 10):
#     j = 1
#     while j <= i:
#         result = f"{j}*{i} = {i*j}"
#         #print(result.ljust(10), end="")
#         print(result.ljust(10), end="")
#         j += 1
#     i += 1
#     print()
#
# print(resullt.ljust(10), end='') # 左对齐，长度为10的字符串，空格填充
# print(resullt.rjust(10), end='') # 右对齐

name = "Steve"
age = 19
print(f"Name:{name},Age:{age}")

print("--------------------------")

# bool 布尔值

x = 10
y = 9
print(x > y) # True

# True 和 False 本质上是1,0的别名
print(True == 1) # True
print(False == 0) # True
print(int(True)) # 1
print(int(False)) # 0
print(True + True) # 2
print(False + 3) # 3

# and 运算（与）
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# or 运算（或）
print(True or True)     # True
print(True or False)    # True
print(False or False)   # False

# not 运算（非）
print(not True)         # False
print(not False)        # True

# 以下值在布尔上下文中被视为 False：
# False, None, 0, 0.0, '', [], (), {}, set(), range(0)
print(bool(False))      # False
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(''))         # False
print(bool([]))         # False
print(bool(()))         # False
print(bool({}))         # False
print(bool(set()))      # False
print(bool(None))       # False
# 其他所有值都被视为 True
print(bool(1))          # True
print(bool(-1))         # True
print(bool(0.1))        # True
print(bool('hello'))    # True
print(bool([1, 2, 3]))  # True
print(bool({'a': 1}))   # True

# 比较运算
# 数值比较
a, b = 10, 20
print(a == b)   # False (等于)
print(a != b)   # True  (不等于)
print(a < b)    # True  (小于)
print(a > b)    # False (大于)
print(a <= b)   # True  (小于等于)
print(a >= b)   # False (大于等于)

# Python 支持链式比较
x = 15
print(10 < x < 20)      # True
print(10 <= x <= 20)    # True
print(5 < x < 10)       # False
# 相当于
print(10 < x and x < 20)  # True

# 字符串比较（按字典序）
print("apple" < "banana")   # True
print("cat" == "cat")       # True
print("dog" > "cat")        # True
# 列表比较
print([1, 2] < [1, 2, 3])   # True
print([1, 3] > [1, 2])      # True

# 传统写法
score = 85
if score >= 60:
    result = "及格"
else:
    result = "不及格"
# 三元表达式写法
result = "及格" if score >= 60 else "不及格"
print(result)  # 及格
# 复杂示例
age = 20
category = "成人" if age >= 18 else "未成年"
print(category)  # 成人

# any() all() 函数
# any() - 任意一个为 True 就返回 True
numbers = [0, 1, 0, 0]
print(any(numbers))  # True
conditions = [False, False, True]
print(any(conditions))  # True
# all() - 所有都为 True 才返回 True
numbers = [1, 2, 3, 4]
print(all(numbers))  # True
conditions = [True, True, False]
print(all(conditions))  # False

print("--------------------------")

# list 列表
# 有序，可变，[]表示，逗号分隔元素

# 创建
nums = [1, 2, 3]

chars = list("Python") # ['P', 'y', 't', 'h', 'o', 'n']

squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]

# 访问和修改
print(nums[1]) # 2
print(nums[-1]) # 3
nums[-1] = 30
print(nums) # 修改

# 切片
nums = [0, 1, 2, 3, 4, 5]

print(nums[1:4]) # [1, 2, 3] 左闭右开区间
print(nums[:3]) # [0, 1, 2] 左闭右开区间
print(nums[3:]) # [3, 4, 5] 左闭右开区间
print(nums[::2]) # [0, 2, 4] 整个列表，但是从0开始步长为2
print(nums) # 返回完整列表，切片不会修改原列表

print("列表常用方法:")
# 列表常用方法
# append(x)	        在末尾添加元素	                lst.append(5)
# extend(iterable)	合并另一个序列	                lst.extend([6,7])
# insert(i, x)	    在指定位置插入	                lst.insert(1, 99)
# remove(x)	        删除第一个匹配元素	            lst.remove(99)
# pop([i])	        删除并返回指定元素（默认最后）	lst.pop()
# clear()	        清空列表	                    lst.clear()
# index(x)	        返回元素下标	                lst.index(3)
# count(x)	        统计出现次数	                lst.count(2)
# sort()	        原地排序	                    lst.sort()
# reverse()	        原地反转	                    lst.reverse()
# copy()	        浅拷贝	                        lst2 = lst.copy()

print("append():") # 末尾插入
nums.append(6)
print(nums)

print("len():")
print(len(nums))

print("extend():")
# 扩展列表
nums.extend([8,8]) # extend()没有返回值，直接修改原列表,而且得是可迭代对象，不能extend(5),单个数字
print(nums)
# 扩展元组到列表里
nums.extend((9,9)) # 不能是(9),一个不能迭代，就不是可迭代对象
print(nums)
# 扩展字典的键或值到列表里
d = {'a':10, 'b':20, 'c':30}
nums.extend(d.keys())
print(nums)
nums.extend(d.values())
print(nums)

print("insert():") #没有返回值，原列表修改
lst = [2, 3, 4]
lst.insert(0, 1)
print(lst) # [1, 2, 3, 4] ,在index=0处插入1
lst = [1, 3, 4]
lst.insert(1, 2)
print(lst)
lst = [1, 2, 3]
lst.insert(len(lst), 4) # 相当于append()在列表最后位置添加元素
print(lst)
# insert()还可以给列表里插入字符串，列表，字典，方法一样
# 超过索引会默认插入最后，负索引超出开头就插入开头,没超出就正常负索引插入

# 对比理解，insert()在指定位置插入一个元素，一个元素可以是一整个列表，字典。
# 而expend()则是可以将列表里的元素附加给目标对象

# insert()对于插入列表开头的效率不高，时间复杂度为O(n),因此使用collections.deque双端队列
# 可以在两端高效插入和删除的线性数据结构,主要是为了开头添加/删除效率高
# from collections import deque
#
# # 创建 deque
# dq = deque()                    # 空 deque
# dq = deque([1, 2, 3])          # 从列表初始化
# dq = deque("hello")            # 从字符串初始化
# dq = deque(range(5))           # 从 range 初始化

# 添加元素
dq.append(4) # 右端添加，和基础列表方法的append()一样
dq.appendleft(0) # 左端添加，比基础列表方法的insert(0,0)效率高

# 删除元素
right = dq.pop() # 右端删除，一样的效率
left = dq.popleft() # 左端删除，效率高

# 扩展元素
dq.extend([4, 5]) # 在后面依次添加
dq.extend([1, 0]) # 在前面依次添加，先1,再0 依次加入在第一个，相当于把[0, 1]添加在前面了

# 旋转元素
dq.rotate(1) # 将列表全部元素往右移一格，最后一个元素到第一来
dq.rotate(-1) # 差不多，不过是全部元素往左，第一个到最后去

# 统计元素数量(有返回值)
print(dq.count(2)) # 统计2这个元素，一共出现几次

# 删除指定的元素(第一个)
dq.remove(2) # 只删除一次，也就是找到的的一个元素,循环判断可全部删除

# 清空元素
dq.clear()

# 队列： FIFO first in first out
# from collections import deque
#
# class Queue:
#     def __init__(self):
#         self._items = deque() # 类实例创建一个双端空列表
#
#     def enqueue(self, item):
#         self._items.append(item)
#
#     def dequeue(self):
#         return self._items.popleft()
#
#     def is_empty(self):
#         return len(self._items) == 0
#
# # 使用示例
# q = Queue()
# q.enqueue(1)
# q.enqueue(2) # 类似管道通过，先进去先出来
# print(q.dequeue())  # 输出: 1

# 栈 LIFO last in first out
# from collections import deque
#
# class Stack:
#     def __init__(self):
#         self._items = deque()
#
#     def push(self, item):
#         self._items.append(item)
#
#     def pop(self):
#         return self._items.pop()
#
#     def is_empty(self):
#         return len(self._items) == 0
#
# # 使用示例
# s = Stack()
# s.push(1)
# s.push(2) # 类似堆书本，最后放的，先拿走
# print(s.pop())  # 输出: 2

# depue 和列表的转化
# from collections import deque
# dq = deque([1, 2, 3])
# lst = list(dq)
#
# lst = [4, 5, 6]
# dq = deque(lst)

# 回文检查
# from collections import deque
#
# def is_palindrome(word):
#     dq = deque(word.lower())
#
#     while len(dq) > 1:
#         if dq.popleft() != dq.pop():
#             return False
#     return True
#
# print(is_palindrome("radar"))    # True
# print(is_palindrome("python"))   # False

# 滑动窗口问题
# from collections import deque
#
# def max_sliding_window(nums, k):
#     """求滑动窗口最大值"""
#     if not nums:
#         return []
#
#     result = []
#     dq = deque()  # 存储索引
#
#     for i in range(len(nums)):
#         # 移除超出窗口的元素
#         if dq and dq[0] < i - k + 1:
#             dq.popleft()
#
#         # 移除比当前元素小的元素
#         while dq and nums[dq[-1]] < nums[i]:
#             dq.pop()
#
#         dq.append(i)
#
#         # 当窗口形成时记录结果
#         if i >= k - 1:
#             result.append(nums[dq[0]])
#
#     return result
#
# # 示例
# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# print(max_sliding_window(nums, 3))  # 输出: [3, 3, 5, 5, 6, 7]

print("remove():")

print("--------------------------")

# tuple 元组

t = (1, 2, 3, 4, 5)
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
print(a - b) # {1, 2} 差集
print(a ^ b) # {1, 2, 4, 5} 对称差集(只在其中一个集合里出现的,剔除两个集合里都有的元素)
# 集合里的元素是无序的
# 集合里的元素是唯一的

print("--------------------------")

# dict 字典

# 字典的创建
persion1 = {"name":"Alice", "age":"22", "city":"Changsha"}
print(persion1["city"])

persion2 = dict(name="Bob", age=23, city="Luki")
print(persion2)

persion3 = dict([("name", "Haili"), ("age",24)])
print(persion3)

# 访问 修改
print(persion2["name"]) #访问
persion2["name"] = "Big Bob"
print(persion2["name"]) #修改后访问
# 不能在表达式里进行赋值
# print(persion2["name"] = "Big Bob") # error

# print(persion2["height"]) # error,没有这个键
print(persion2.get("height", "173")) # 没有这个键,返回None,不会引起报错,如果.get()有第二个参数
# 第二个参数就当做默认，进行返回

# 删除字典元素

del persion1["city"]
print(persion1) # 没city 这个键了

persion1.pop("age")
print(persion1) # 没city 这个键了

print(persion3)
persion3.clear() # 清空persion3字典所有内容
print(persion3)

# 遍历字典
user = {"name":"Tom", "age":25, "city":"Beijing"}

for k in user:
    print(k, user[k], sep='', end='')
# 键-值对全部打印，一个元素一个元素来，键-值默认空格分隔，每个元素(每个键-值对)默认换行符结尾
print() # 默认打印换行符

# k,v 代表单个元素内的key-value,如果没有items(),就会报错，因为字典是单元素的,有items()就会把一个元素分为key,value两个
for k, v in user.items():
    print(k, v)

# 字典的方法
# 方法                        | 说明                          | 示例                                 |
# dict.get(key, default)      | 获取键值，若不存在返回默认值  | `user.get("age", 0)`                 |
# dict.keys()                 | 获取所有键                    | `user.keys()`                        |
# dict.values()               | 获取所有值                    | `user.values()`                      |
# dict.items()                | 获取键值对                    | `user.items()`                       |
# dict.pop(key)               | 删除并返回指定键值            | `user.pop("age")`                    |
# dict.popitem()              | 删除并返回最后一个键值对      | `user.popitem()`                     |
# dict.update(other)          | 合并另一个字典                | `user.update({"gender": "M"})`       |
# dict.clear()                | 清空字典                      | `user.clear()`                       |
# dict.setdefault(key, value) | 如果 key 不存在则设置默认值   | `user.setdefault("city", "Beijing")` |

# 嵌套字典(值为字典)

students = {
        "1":{"name":"Tom", "age":20},
        "2":{"name":"Mark", "age":21}
}

print(students["2"]["name"]) # Mark

# 遍历嵌套字典用两个变量，一个查键，一个查值，所以得使用.items()

# 字典推导式

# 创建字典
squares = {x:x**2 for x in range(5)}
print(squares)

# 筛选条件
nums = {"a":1, "b":2, "c":3, "d":4}
even = {k:v for k, v in nums.items() if v % 2 == 0}
print(even) # 2 4
