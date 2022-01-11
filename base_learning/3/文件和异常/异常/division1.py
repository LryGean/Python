#处理ZeoDivisionError
# print(5/0)

#使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")  #divide:分开，划分