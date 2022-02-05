'''
prompt = "\nTell me something,and I willreapt it back to you:"
prompt += "\nEnter \'quit\' to end the program.\n"
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
         print(message)
'''
'''
pizza = "\n请输入你想添加的配料:"
pizza += "\nEnter \'quit\' to end the program.\n"
Sweet = True
while Sweet:
    Try = str(input(pizza))
    if Try == 'quit':
        Sweet = False
    else:
         print("请确认你添加的配料： " + pizza)
'''
print('欢迎来到金钱豹电影院！')
print("下面是收费标准：")
active = True
over = ''
while active:
    age = eval(input("你的年龄:"))
    if age <= 3 and age >= 0:
        print("免费")
    elif age >3 and age <= 12:
        print("10$")
    elif age >12:
        print("15$")
    elif age == -1:
        over = input('输入结束')
        if over == '结束':
            pass
        active = False     
         