while True:
    try:
        n = int(input("n="))
    except ValueError:
        print("这不是一个数字！")
    else:
        if n >= 0 :
            break
        else:
            print("请输入一个正整数！")

m = 2
while m < n:
    if  n % m == 0:
        break
    else:
        m = m + 1

if m == n:
    print("这是素数")
else:
    print("这不是一个素数")


