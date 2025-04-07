import random

num = int(random.uniform(0, 100))
print(num)

while True:

    while True:
        try:
            b = int(input("请猜一个数字:"))
        except ValueError:
            print("这不是一个数字！")
        else:
            break

    if num == b:
        print("你猜对了！")
        break
    else:
        if b > num:
            print("大了！")
            continue
        else:
            print("小了！")
            continue

exit(0)