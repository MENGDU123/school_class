import turtle
import time
 
t = turtle
t.up()          #移动位置
t.goto(-200,200)

t.pensize(5)  # 定义画笔的宽度
t.pencolor("purple")  # 定义画笔颜色
t.fillcolor("pink")  # 定义填充颜色
turtle.down()   #落笔后出现线条
t.begin_fill()  # 开始填充图像

for i in range(4):  # 五角星循环五次
    t.forward(500)
    t.right(90)  # 右转144°
t.end_fill()  # 停止填充
time.sleep(2)   #阻塞两秒
 
