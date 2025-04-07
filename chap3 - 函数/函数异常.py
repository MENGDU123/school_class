'''
此程序用于测试异常处理在函数或主程序不同位置的区别。
任务1-调用A函数，主程序异常处理。
任务2-在A函数中异常处理。
任务3-在B函数中异常处理。
'''


def A():
    print("start A")
    # try:
    #     N = 1 / 0
    # except Exception as err:
    #     print("除数不能为0")

    N = 1 / 0

    print("end A")


def B():
    print("start B")
    A()
    print("end B")


try:
    B()
except Exception as err:
    print("主程序error")

# B()

print("finsh")