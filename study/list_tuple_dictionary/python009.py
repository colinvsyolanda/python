"""
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
"""

# 学习使用字典类型
import time

mydict = {"id":1, "name":"zhangsan", "gender":"Female"}

for key, value in dict.items(mydict):
    print(key, ":", value)
    time.sleep(2)