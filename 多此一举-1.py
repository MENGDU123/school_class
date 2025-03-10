i = 0
s = 0

while i < 5:
    i = i + 1
    while True:
        try:
            b = float(input(f"请输入第{i}位的成绩："))
        except ValueError:
            print("输入有误，请重新输入！")
        else:
            if b<0 or b>100:
                print("数值有误，请重新输入！")
            else:
                break

    s = s + b

print(f"平均成绩为：{s/5:.2f}")