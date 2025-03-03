while True:
    try:
        ach = float(input("请输入成绩："))
    except ValueError:
        print("成绩应该是一串数字，请重新输入")
    else:
        if 0 <= ach <= 100:
            break
        else:
            print("成绩应当为0~100区间内的数字！")
            continue

ach = int(ach // 10)
#print (ach)

if ach >= 9:
    print("您的等级为A")
elif ach == 8:
    print("您的等级为B")
elif ach == 7:
    print("您的等级为C")
elif ach == 6:
    print("您的等级为D")
else:
    print("很抱歉，你的等级为E")