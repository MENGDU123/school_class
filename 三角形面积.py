while True:
    try:
        a = float(input("请输入三角形的底："))
    except ValueError:
        print("不合法的输入！")
    else:
        break

while True:
    try:
        h = float(input("请输入三角形的高："))
    except ValueError:
        print("不合法的输入！")
    else:
        break

s = a * h / 2

print(f"三角形面积为:{s:.2f}")