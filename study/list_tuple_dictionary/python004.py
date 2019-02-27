"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
分析：
    首先判断当前是否为闰年？闰年为366，平年是365
    明确输入年份的每个月的天数(分为平年和闰年两种)

"""

p_nian = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
r_nian = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 判断平年还是闰年
def isP_nina(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return False
    return True


year = input("请输入年份:")
month = input("请输入月份:")
day = input("请输入日子:")

year = int(year)
month = int(month)
day = int(day)

flag = isP_nina(year)
monthOfDay_sum = 0
if flag:
    for i in range(0, 12):
        if month > i + 1:
            monthOfDay_sum += p_nian[i]
    print(year, "年是平年")
else:
    for i in range(0, 12):
        if month > i + 1:
            monthOfDay_sum += r_nian[i]
    print(year, "年是闰年")

print("是该年的第", monthOfDay_sum + day, "天")