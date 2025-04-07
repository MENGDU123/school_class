'''
请设计一个程序完成 1+（1+2）+……+（1+2+……+n）的计算。
Please design a program to complete 1+(1+2)+...+(1+2+...+n).
'''

def sum(m):
    s = 0
    for n in range(1,m+1):
        s = s + n
    return s

def sumALL(n):
    s = 0
    for m in range(1,n+1):
        s = s + sum(m)
    return s

n = input("n=")
n = int(n)
print("总和是",sumALL(n))
