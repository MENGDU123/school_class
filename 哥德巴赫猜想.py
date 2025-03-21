while True:
    try:
        m = int(input("请输入一个大于6的偶数："))
        if m <6 or m % 2 != 0:
            raise ValueError("无效的数字")
    except ValueError as err:
        print(err)
        print("请重输！")
    else:
        break

maxp = m // 2
p = 2

while p <= maxp:
    flag = True
    for k in range(2,p):
        if p % k == 0:
            flag = False
            break

    if flag:
        q = m - p
        for k in range(2,q):
            if q % k == 0:
                flag = False
                break

    if flag:
        print(m,"=",p,"+",q)

    p = p + 1

print("Done!")



