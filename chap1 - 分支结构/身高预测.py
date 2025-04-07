import time

while True:
    try:
        m = float(input("请输入母亲的身高：（单位：cm）"))
    except ValueError:
        print("请输入数字！")
    else:
        break

while True:
    try:
        f = float(input("请输入父亲的身高：（单位：cm）"))
    except ValueError:
        print("请输入数字！")
    else:
        break

while True:
    ask = str(input("男孩还是女孩？"))
    if "男" in ask:
        b = (f + m) * 1.08 * 0.5
        print("计算中……")
        for _ in range(6):
            print(".",end="")
            time.sleep(1)
        print()
        print(f"男孩的身高为{b:.1f}cm")
        break
    elif  "女" in ask:
        f = f + 0.932
        g = (f + m) * 0.5
        print("计算中……")
        for _ in range(6):
            print(".",end="")
            time.sleep(1)
        print()
        print(f"女孩的身高为:{g:.1f}cm")
        break
    else:
        print("输入有误，请重新输入！")

time.sleep(1)
print("程序执行完毕！")
exit(0)
