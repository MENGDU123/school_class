while True:
    try:
        n = str(input("请输入你的名字："))
        if n.strip()=="":
            raise Exception("无效的姓名")

        Gender = str(input("请输入你的性别："))
        if "男" in Gender or "女" in Gender:
            pass
        else:
            raise Exception("无效的性别")

        age = int(input("请输入你的年龄："))
        if age < 18 or  age > 30 :
            raise Exception("无效的年龄")

    except Exception as err:
        print(err)
        print("请重新输入！")
    else:
        break

print(n,Gender,age)