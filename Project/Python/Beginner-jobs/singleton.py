#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-11-03 10:58


class Singleton(type):
    """单例元类"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
