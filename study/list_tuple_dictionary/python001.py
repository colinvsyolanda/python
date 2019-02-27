# coding = UTF-8

"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
问题分析：
    此项考察组成一个三位数，且数字不重复+各个数值不相同
    用到三重for循环i,j,k,判断条件为三个数值不相同；i,j,k要得到按照固定的规则，i代表百位，j代表十位，k代表各位
"""

number_sum = 0

number_list = []

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                number_list.append(i * 100 + j * 10 + k)
                number_sum = number_sum + 1

print("得到的无重复的互不相同的三位数总数为", number_sum)
print("所有的数为", number_list)

for list_item in range(0, len(number_list)):
    print("%2d"%list_item, ":", number_list[list_item])
