'''
本文件用于演示如何读取字符串。
各个字符串是不允许被修改的。
'''
import time

s = "我们abc"
print(len(s)) #len用于检测字符串长度。
print(s[2]) #读取字符串的顺序应该是从0开始。
print(s)

for i in range(len(s)):
    time.sleep(1)
    print(s[i],end='')
#一种播放式输出的方式。

print()
print(ord('A'))
print(ord('a'))
print(chr(65))

#ord可以检查字符在字库中的编码。
#chr则是在字库中检索字母。