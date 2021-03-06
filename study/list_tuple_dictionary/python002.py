"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
程序实现分析：
    此项实际上是一个分段函数，另输入的金额为X
    条件                  算法规则
    X>1000000             (X-1000000)*0.01
    600000<X<=1000000     (X-600000)*0.015
    400000<X<=600000      (X-400000)*0.03
    200000<X<=400000      (X-200000)*0.05
    100000<X<=200000      (X-100000)*0.075
    X<=100000             X*0.1

    此处做的时候错误的对分段函数进行了处理，需要加强注意，迭代的时候利润值的更新
"""

# 存储阶段和提成率
profit_number = [1000000, 600000, 400000, 200000, 100000, 0]
profit_rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]


profit = input("请输入利润")

profit_sum = 0.0

print(len(profit_number))
profit = float(profit)
for index in range(0, len(profit_number)):
    if profit > profit_number[index]:
        profit_sum = profit_sum + (profit - profit_number[index]) * profit_rate[index]
        print((profit - profit_number[index]) * profit_rate[index])
        profit = profit_number[index]  # 此项迭代是根据第一次输入的值，如果进入某一阶段之后，需要将后一阶段的最大值赋值给当前值进行下一次迭代

print("根据利润比例抽成，年收入", profit_sum, "元")

