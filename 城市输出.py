def enter():
    global province
    global city
    province = str(input("请输入省份："))
    city = str(input("请输入城市："))

def show():
    print(f"省份为；{province}，城市为：{city}") #如果只是访问其它函数的变量，无需写global，如果要改写新数据，需要global

enter()
show()

#####################################################################

