'''
编写一个程序，输出九九乘法表。
'''
a = 0
b = 1
req = a * b
for i in range(1,10):
    a = a + 1
    b = 1
    for j in range(1,a+1):
       req = a * b
       print(f"{a} * {b} = {req} ",end = "")
       b = b + 1
    if a != 9:
        print("")