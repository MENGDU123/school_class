'''
编写一个程序，判断字符串该字符串是否对称。
示例：输入“abcba”输出“对称”，输入“abbca”输出不对称。
'''
from os import rename

s = str(input("s="))
for i in range(len(s)):
    if s[len(s)-1-i] == s[i]:
        pass
    else:
        print("不对称")
        exit(0)

print("对称")

#官方一些的答案,但老师做的似乎有误。
def issymmtry(s):
    i = 0
    j = len(s)-1
    while(i<=j):
        if s[i]!=s[j]:
            return 0
        i += 1
        j += 1
    return 1
s = str(input("s="))
if issymmtry(s) == 1:
    print("对称")
else:
    print("不对称")