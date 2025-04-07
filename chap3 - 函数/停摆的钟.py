'''
输入一个有效的时间，并利用格式化输出显示该时间。
如果输入的时间有误，请抛出异常。
'''
while True:
    try:
        h = int(input("请调整时针："))
        if 0 <= h < 24:
            break
        else:
            raise Exception("地球的一天是24小时！")
    except Exception as err:
        print(err)
        print("请重新输入！")

while True:
    try:
        m = int(input("请调整分针："))
        if 0 <= m < 60:
            break
        else:
            raise Exception("一小时只有60分钟！")
    except Exception as err:
        print(err)
        print("请重新输入！")

while True:
    try:
        s = int(input("请调整秒针："))
        if 0 <= s < 60:
            break
        else:
            raise Exception("一分钟只有60秒！")
    except Exception as err:
        print(err)
        print("请重新输入！")

print()
print("显示时间：",f"{h}:{m}:{s}")