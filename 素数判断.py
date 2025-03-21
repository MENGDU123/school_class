# while True:
#     try:
#         n = int(input("n="))
#     except ValueError:
#         print("这不是一个数字！")
#     else:
#         if n >= 0 :
#             break
#         else:
#             print("请输入一个正整数！")
#
# m = 2
# while m < n:
#     if  n % m == 0:
#         break
#     else:
#         m = m + 1
#
# if m == n:
#     print("这是素数")
# else:
#     print("这不是一个素数")

count = 0 #计数器

for n in range(1,101): # 100以内的素数

    f = 1
    for m in range(2,n):
        if n % m == 0:
            f = -1
            break
        m = m + 1
    if f == 1:
        print(n,end=' ')
        count = count + 1
        if count == 5:
            print()
            count = 0