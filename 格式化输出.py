import time

name = str(input("Teacher?"))
print("hello,teacher"+name)

s1 = 123
s2 = 123
print(s1+s2)

print("%05d"%s1)
print("%-05d"%s1)
print("%2d"%s1)
print("s1 = %7d,s2 = %7d"%(s1,s2))

year = 2025
mouth = 2
day = 20
print("%05d-%02d-%02d"%(year,mouth,day)) #格式化输出，理解为 %<填充物品><预>

m = int(12)
print("|%d|"%m)
print("|%4d|"%m)
print("|%-4d|"%m)
print("|%04d|"%m)
print("|%-04d|"%m) #0是不会补在变量右侧的

a = float(123.456)
print("%f"%a) #输出小数后六位
print("|%8.1f|"%a) #靠右，共计8个字符，小数保留1位
print("|%8.2f|"%a) #靠右，共计8个字符，小数保留2位
print("|%-8.1f|"%a)
print("|%-8.1f|"%a)#左，共计8个字符，小数保留2位
print("|%8.0f"%a)#四舍物入靠左

ack = str("Hello")
print("|%s|"%ack)
print("|%8s|"%ack)
print("|%-8s|"%ack)

print("kwymengdu","online",sep=".")

for _ in range(10):
    print(".",end="")
    time.sleep(1)