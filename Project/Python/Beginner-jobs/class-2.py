#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-11-02 02:03


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Marian", 24)
p2 = Person("Mark", 22)

print(p1.name)
print(p2.age)
