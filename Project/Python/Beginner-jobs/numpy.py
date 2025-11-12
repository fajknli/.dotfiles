#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-11-10 15:26


import numpy as np
import time

# 大数据量测试
large_data_np = np.random.rand(1000000)
large_data_list = large_data_np.tolist()

# NumPy 方式
start = time.time()
result_np = large_data_np[large_data_np > 0.5]
time_np = time.time() - start

# 原生 Python 方式
start = time.time()
result_py = [x for x in large_data_list if x > 0.5]
time_py = time.time() - start

print(f"NumPy 耗时: {time_np:.4f}秒")
print(f"Python 耗时: {time_py:.4f}秒")
