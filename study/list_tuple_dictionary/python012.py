"""
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　
"""

import math

list_sushu = []
for i in range(101, 201):
    flag = False
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j != 0:
            flag = True
            continue
        else:
            flag = False
            break
    if flag == True:
        list_sushu.append(i)
        flag = False

print(list_sushu)
print(len(list_sushu))