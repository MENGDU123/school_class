while True:
    try:
        h = float(input("请输入你的身高（单位：cm）："))
    except ValueError:
        print("数据格式错误！")
    else:
        if h > 0:
            h = h / 100
            print(h)
            break
        else:
            print("你的身高不可能是0或负数！")
            continue

while True:
    try:
        w = float(input("请输入你的体重（单位：kg）："))
    except ValueError:
        print("数据格式错误！")
    else:
        if w > 0:
            break
        else:
            print("你的体重不可能是0或负数！")
            continue

bmi = int(w / (h * h))
print(f"您的bmi为{bmi}，",end="")

if bmi < 18.5:
    print("您似乎有些偏瘦了……")
elif 18.5 <= bmi <= 24:
    print("恭喜，完美的身材！")
elif 24 <= bmi <= 28:
    print("有点小胖，但问题不大！")
else:
    print("肥胖体型，你该减肥啦！")

exit(0)