while True:
    try:
        a = int(input("a="))
    except ValueError:
        print("这不是一个有效的数字")
    else:
        break

while True:
    try:
        b = int(input("b="))
    except ValueError:
        print("这不是一个有效的数字")
    else:
        break

n = 1
while n / a != 0 or n / b != 0:
    n = n + 1
print(f"a和b的最小公倍数为{n}")
