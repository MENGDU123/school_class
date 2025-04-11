'''
~~~挑战关~~~
请编写一个程序，要求输入年份，输出今年的日历！
·必须使用函数
·日历不能有误
·公式自行查阅
~~~加油吧~~~
'''
from lib2to3.pgen2.tokenize import printtoken
from os import rename

y = 2024#年份
m = 12#月份
d = 0#日期

def isLeap(y):#闰年检测,输出的是布尔值
    return y % 400 == 0 or y % 4 == 0 and y % 100 != 0

def maxDay(y,m):#计算该年份一个月最大天数，输出值。
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        d = 31
    elif m == 2:
        if isLeap(y):
            d = 29
        else:
            d = 28
    else:
        d = 30

    return d

def countDays(y,m,d):#求日期是今年第几天，输出数字。
    days = d

    if m >= 2:
        days += 31

    if m >= 3:
        if isLeap(y):
            days += 29
        else:
            days += 28

    if m >= 4:
        days += 31

    if m >= 5:
        days += 30

    if m >= 6:
        days += 31

    if m >= 7:
        days += 30

    if m >= 8:
        days += 31

    if m >= 9:
        days += 31

    if m >= 10:
        days += 30

    if m >= 11:
        days += 31

    if m >= 12:
        days += 30

    return days

def countWeeks(y,m):#对应星期几，输出数字：
    w = (y-1) + (y-1)//400+(y-1)//4-(y-1)//100 + countDays(y,m,1)
    return w % 7

def printMonth(y,m):
    w = countWeeks(y,m)
    md = maxDay(y,m)

    print("Sum","Mon","Tue","Wed","Thu","Fri","Sat",sep="    ")
    for i in range(w):
        print("% -6s"%" ",end=" ")

    for d in range(1,md + 1):
        print("% -6d" % d,end=" ")
        w = w + 1
        if w% 7 == 0:
            print()

y = input("请输入年份：")
y = int(y)
for m in range(1,13):
    print()
    print("---------------",y,"年",m,"月 ---------------")
    printMonth(y,m)
    print()

