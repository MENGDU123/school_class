import math #math.sqrt是开根号
a = 0
b = 0
c = 0

def num(n):
    try:
        n = int(n)
    except ValueError:
        print("一个或多个数据格式错误!")
        exit(1)
    else:
        return n


a = input("请输入A的值：")
b = input("请输入B的值：")
c = input("请输入C的值：")

a = num(a)
b = num(b)
c = num(c)



if a != 0:
    print(a,b,c)
    pass
else:
    print("无解，因为分母不能为0")

#不会是因为数学不好=。=