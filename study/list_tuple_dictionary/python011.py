"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
"""


def calNumber(month):
    tuzi_month_number = []
    if month == 1 or month == 2:
        tuzi_month_number.append(1)
    else:
        tuzi_month_number = [1, 1]
        for i in range(2, month):
            tuzi_month_number.append(tuzi_month_number[-1] + tuzi_month_number[-2])
    return tuzi_month_number


print(calNumber(10))
tuzinumber = calNumber(50)
j = 1
for i in range(len(tuzinumber)):
    print("%12d" % tuzinumber[i], " ", end=" ")
    if j % 5 == 0:
        print()
        j = 1
        continue
    j += 1

