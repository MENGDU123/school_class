'''
编写一个程序，要求检查一个字符串中大写字母的个数。
【选做】分别输出大写、小写和数字的个数。
'''
s = str(input("谁便输入点什么："))

# count = 0
# for i in range(len(s)):
#     test = ord(s[i])
#     if ord("A") <= test <= ord("Z"):
#         count += 1
#
# print(f"发现了{count}个大写字母")

a = 0
b = 0
c = 0
d = 0
for i in range(len(s)):
    test = ord(s[i])
    if ord("A") <= test <= ord("Z"):
        a += 1
    elif ord("a") <= test <= ord("z"):
        b += 1
    elif ord("0") <= test <= ord("9"):
        c += 1
    else:
        d += 1

print(f"发现了{a}个大写字母")
print(f"发现了{b}个小写字母")
print(f"发现了{c}个数字")
print(f"还有{d}个不知道是啥玩意")