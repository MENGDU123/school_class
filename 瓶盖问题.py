m = int(input("你带了几块钱？"))#起始资金
beers = m//2 #酒的数量，啤酒两块一瓶
caps = 0 #瓶盖数量
bottle = 0 #空瓶数量
count = 0 #喝酒计数

while beers>0:
    beers = beers - 1
    bottle = bottle + 1
    caps = caps + 1
    count = count + 1
    if  bottle == 2:
        beers = beers + 1
        bottle = 0
    if caps == 4:
        beers = beers + 1
        caps = 0

print(f"一共获得了{count}瓶啤酒。")
print(f"还剩瓶盖{caps}个，还剩空瓶{bottle}个。")
