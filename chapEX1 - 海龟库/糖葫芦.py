import turtle                # 导入 turtle 库
turtle.bgcolor("pink")   # 设置背景颜色为seagreen
turtle.pencolor("red")   # 设置画笔颜色为darkred
turtle.pensize(3)            # 设置画笔的粗细为3
turtle.speed(1)              # 设置海龟的绘图速度，参数为0时最快，参数为1时最慢。
#turtle.delay(50)             # 设置延迟时间。如果speed参数为1时，速度还不够慢，就要设置delay。数值越大，绘图越慢。
turtle.penup()               # 画笔抬起，海龟移动时不画线
turtle.goto(0,-200)          # 海龟移动到坐标(0,-200)
turtle.pendown()             # 画笔落下，海龟移动时将画线
turtle.left(90)              # 海龟向左旋转90度
turtle.forward(50)
i=1                        # 计数器变量
while i<=6:                # 循环体要执行5次
    turtle.forward(55)     # 海龟前进55步
    turtle.dot(50)         # 海龟画直径为50像素的圆点
    i=i+1                  # 改变计数器（计数器加1）
turtle.penup()              # 画笔抬起，海龟移动时不画线
turtle.forward(70)          # 海龟前进70步
turtle.pendown()            # 画笔落下，海龟移动时将画线
turtle.write("冰糖葫芦",align="center",font=("隶书",30))  # 书写文本
turtle.hideturtle()         # 隐藏海龟