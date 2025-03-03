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

c = a
if a < b:
    c = b
print(f"最大值为：{c}")
