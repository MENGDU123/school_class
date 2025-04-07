#print(5%3,5%-3,-5%-3)
# from email.quoprimime import body_check

# ask = str(input("你想要和谁打招呼?"))
# print("你好",ask,end="")
# print("再见",ask)
# while True:
#     try:
#         n = int(input("n="))
#     except ValueError:
#         pass
#     else:
#         break
#
# i = 1
# s = 1
#
# while i < n:
#     i = i + 1
#     s = s + i
#
# print(f"1+2+……+{n}={s}")
# for i in [1,0]:
#     print(i+1)
# y = 0
#
# for i in range(0, 10, 2):
#
#     y += i
#
# print(y)

# def fun(x,y):
#     print("In fun:",x,y)
#     x = 1
#     y = 2 #局部函数x，y仅仅在函数中有x，y
#     return x
#     return y
#
# x = 100
# y = 200
# fun(x,y)
# print(x,y) #这里输出的是主程序的x，y

# print("baka",9,sep="-")
# print(1,2,end="*")
# print()
# print(2025,"03",31,sep=":",end=" ")
# print(13,51,10,sep=":")

y = 2025
m = 3
d =31
h = 13
minute = 51
sec = 10
print("%04d"%y,"%02d"%m,"%02d"%d,sep = "-",end = " ")
print("%02d"%h,"%02d"%minute,"%02d"%sec,sep = ":",end = "")
