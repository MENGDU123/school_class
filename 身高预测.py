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
        print("男孩身高为","%8.2f"%b,"cm")
        break
    elif  "女" in ask:
        f = f + 0.932
        g = (f + m) * 0.5
        print("男孩身高为", "%8.1f" %g, "cm")
        break
    else:
        print("输入有误，请重新输入！")

print("程序执行完毕！")
exit(0)
#纯手码，绝对没用Deepseek!