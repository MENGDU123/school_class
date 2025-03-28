# def fun(x,y):
#     print("In fun:",x,y)
#     x = 1
#     y = 2 #局部函数x，y仅仅在函数中有x，y
#     print("In fun:", x, y)
#
#
# x = 100
# y = 200
# fun(x,y)
# print(x,y) #这里输出的是主程序的x，y
m = 0

def fun(m):
    global n #设置为全局变量，这样内外就可以统一了
    m = 0
    n = 0 #全局变量不需要在fun中声明

m = 1 #主程序变量
n = 2 #全局变量
fun(m)
print(m,n)