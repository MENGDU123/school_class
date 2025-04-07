while True:
    try:
        a = int(input("a="))
    except ValueError:
        print("请输入数字！")
    else:
        break

while True:
    try:
        b = int(input("b="))
    except ValueError:
        print("请输入数字！")
    else:
        break


if a <= b:
    c = b
else:
    c = a

for i in range(c):
    if b % c == 0 and a % c == 0:
        print(f"{a}和{b}最大公约数为{c}")
        exit(0)
    else:
        c = c - 1

# while True:
#     if b % c == 0 and a % c == 0:
#         print(f"{a}和{b}最大公约数为{c}")
#         exit(0)
#     else:
#         c = c - 1
#         if c == 0:
#             exit(0)
#         else:
#             pass