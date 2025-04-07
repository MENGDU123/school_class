'''
编写一个程序，计算 "a + aa + aaa + …… + n个a ="
a的值介于0和10之间。
要求输出时包含算式。
'''
a = 0
while a <= 0 or a >= 10:
    a = int(input("a="))
while True:
    n = int(input("n="))
    if n > 0:
        break
m = int(0)
s = int(0)

for i in range(n):
    m = 10 * m + a
    if i < n - 1    :
        print(m,end="+")
    else:
        print(m, end="=")
    s = s + m
print(s)
exit(0)