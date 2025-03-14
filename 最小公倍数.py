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
# while n % a == 0 and n % b == 0:
#     n = n + 1
# print(f"a和b的最小公倍数为{n}")

for _ in range(a * b):
    if n % a == 0 and n % b == 0:
        print(f"a和b的最小公倍数为{n}")
        exit(0)
    else:
        n = n + 1