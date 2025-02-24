#print(5%3,5%-3,-5%-3)
from email.quoprimime import body_check

ask = input()
if ask >= "a" and ask <= "z":
    print("这是一个英文字母")
else:
    if ask >= "A" and ask <= "Z":
        print("这是一个英文字母")
    else:
        print("这不是一个英文字母")


ask = str(input("你想要和谁打招呼?"))
print("你好",ask,end="")
print("再见",ask)