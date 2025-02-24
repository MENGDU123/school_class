while True:
    try:
        y = int(input("请输入年份"))
    except ValueError:
        print("请输入正确的格式！")
    else:
        break

t = y%400
if y%4 == 0 and y%100!=0 or y%400==0:
    print("这是一个闰年！")
else:
    print=("这不是一个闰年！")