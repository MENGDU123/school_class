'''
验证歌德巴赫猜想，写一个程序列出100以内所有大于6的偶数的分解式。
'''
def fun(m):
    for n in range(2,m):
        if m % n == 0:
            return 0
        else:
            return 1

for n in range(6,101,2):
    for p in range(3,n+1,2):
        q = n - p
        if fun(p) == 1 and fun(q) == 1:
            print(f"{n}={p}+{q}")
            #break  #去掉该注释，每个偶数只列出一个。