'''
请使用处理字符串的方式，从字库中读取26个英文字母。
将26个英文字母打印在同一行。
'''
for i in range(int(ord('A')),int(ord('A')+26)):
    print(chr(i),end="")

print()

for i in range(int(ord('a')),int(ord('a')+26)):
    print(chr(i),end="")