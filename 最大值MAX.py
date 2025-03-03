while True:
    try:
        a = int(input("请输入第一个值："))
    except ValueError:
        print("这不是一个数字！")
    else:
        break

while True:
    try:
        b = int(input("请输入第二个值："))
    except ValueError:
        print("这不是一个数字！")
    else:
        break

if a > b:
    print(f"最大值为：{a}")
else:
    print(f"最大值为：{b}")
