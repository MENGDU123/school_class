p = 0
q = 0
n = 0

while True:
    try:
        p = int(input("Enter p:"))
    except ValueError:
        print("输入有误请重新输入！")
    else:
        if p >= 0:
            break
        else:
            print("p不应该是个负数！")
            continue

while True:
    try:
        q = int(input("Enter q:"))
    except ValueError:
        print("输入有误请重新输入！")
    else:
        if p >= 0:
            break
        else:
            print("q不应该是个负数！")
            continue

while True:
    try:
        n = int(input("Enter n:"))
    except ValueError:
        print("输入有误请重新输入！")
    else:
        if n >= 0:
            break
        else:
            print("n不应该是个负数！")
            continue

s = str(p // q)
r = p % q
if r != 0:
    s = s + "."
i = 0
while r != 0 and i < n:
    r = r * 10
    s = s + str(r//q)
    r = r % q
    i = i + 1
print(f"{p}/{q}精确到小数点{n}位：{s}")

#输出有问题，稍后检查！