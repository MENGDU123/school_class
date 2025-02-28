while True:
    try:
        n = int(input("请输入一个整数："))
    except  ValueError:
        print("这不是一个整数！")
    else:
        break

t = n % 2
if n == 0:
    print(f"数字{n}既不是奇数也不是偶数！")
    exit(0)

if t == 0:
    print(f"数字{n}是一个偶数！")
else:
    print(f"数字{n}是一个奇数！")
