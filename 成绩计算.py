#定义三个变量（这里不写也没事）
math = 0
chinese = 0
english = 0

#成绩输入模块(时间紧，下次再尝试使用def简化）
while True:
    try:
        math = float(input("请输入数学成绩"))
    except ValueError:
        print("成绩应该是一串数字，请重新输入")
    else:
        break

while True:
    try:
        chinese = float(input("请输入语文成绩"))
    except ValueError:
        print("成绩应该是一串数字，请重新输入")
    else:
        break

while True:
    try:
        english = float(input("请输入英语成绩"))
    except ValueError:
        print("成绩应该是一串数字，请重新输入")
    else:
        break


sum = math + chinese + english
ave = sum / 3

math = int(math)
chinese = int(chinese)
english = int(english)

print(f"数学成绩:{math}")
print(f"语文成绩:{chinese}")
print(f"英语成绩:{english}")
print(f"你的总分为:{sum:.1f}分,",end="")
print(f"你的平均分为:{ave:.1f}分")

exit()