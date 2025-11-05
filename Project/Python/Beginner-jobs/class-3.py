#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-11-02 09:48


# class A:
#     def __init__(self,x):
#         self.x = x
#     def __add__(self,other):
#         return A(self.x + getattr(other, 'x', 0))
#
# class B:
#     def __init__(self,x):
#         self.x = x
#
# a = A(1)
# b = B(2)
#
# print((a + b).x)

# ---------------------------

# class A:
#     def __init__(self,x):
#         self.x = x
#
# class B:
#     def __init__(self,x):
#         self.x = x
#
# a = A(1)
# b = B(2)
#
# #print((a + b).x)
# print(a + b)
#
# ---------------------------

class A:
    def __init__(self,x):
        self.x = x

class B:
    def __init__(self,x):
        self.x = x
    def __radd__(self,other):
        return B(other.x + self.x)
    def __repr__(self):
        return f"{self.x}"

a = A(1)
b = B(2)

print(a + b)
#print((a + b).x)
#result = a + b
#print(result.x)
