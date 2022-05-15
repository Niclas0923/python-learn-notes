#!/usr/bin/python3
import time

m = int(input("请输入质数输出的最高限制："))

time_start = time.time()  # 记录开始时间

i = 1
while i <= m:
    o = 2
    while i % o != 0 and o <= i:
        o += 1
    if i == o or i == 1:
        print(i, end=" ")
    i += 1

time_end = time.time()  # 记录结束时间
time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
print("\n总共用时：", time_sum)
