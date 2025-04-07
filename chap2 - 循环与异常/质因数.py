while True:
    try:
        n = int(input("请输入一个数字："))
        if n <= 0:
            raise Exception("数字不能是一个负数！！")
    except Exception as err:
        print("请输入正整数！")
    else:
        break

first = True
print(n,end="")
i = 2
while i <= n:
    while n % i == 0:
        if first:
            print("=",i,end="")
            first = False
        else:
            print(" *",i,end="")
        n = n // i
    i = i + 1