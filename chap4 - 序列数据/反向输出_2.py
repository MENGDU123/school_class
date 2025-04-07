'''
设计一个程序，是的输入的字符串在输出时颠倒。
比如——输入：abc，输出：cba
如果有多种方法，请写在函数里，以便后期调用。
'''

def fun1():
    s = str(input("谁便输入点什么："))
    a = int(len(s))
    for i in range(len(s)):
        print(s[a-1],end="")
        a = a - 1

fun1()