'''
利用两个函数，将一个字符串中大写和小写分别列出。
注意，如果输入的字符串有非字母，请保留它。
'''

print(ord('a')-ord('A'))
a = ord('a')-ord('A')

# print(chr(ord('E')+ord('a')-ord("A")))
# print(chr(ord('E')+32))
# print(chr(ord('T')+32))
#示例

def toupper(s):
    t = ''
    for i in range(len(s)):
        if 'a'<=s[i]<='z':
            chr(ord(s[i])-a)
        else:
            t = t + s[i]

    return t

def tolower(s):
    t = ''
    for i in range(len(s)):
        if 'A'<=s[i]<='Z':
            chr(ord(s[i])+a)
        else:
            t = t + s[i]

    return t

s = input("s=")
print("大写：",toupper(s))
print("小写：",tolower(s))