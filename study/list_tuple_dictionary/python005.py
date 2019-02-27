"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
分析：
    比较大小
"""


def bjijao(x, y, z):
    temp = 0.0
    if x > y:
        temp = x
        x = y
        y = temp
    if x > z:
        temp = x
        x = z
        z = temp
    if y > z:
        temp = y
        y = z
        z = temp
    return x, y, z


x = input("输入x的值：")
y = input("输入y的值：")
z = input("输入z的值：")

x = float(x)
y = float(y)
z = float(z)

'''
自定义函数比较
'''
x, y, z = bjijao(x, y, z)
print(x, ":", y, ":", z)


'''
方法二：利用列表的特性进行排序
'''
list1 = [x, y, z]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
