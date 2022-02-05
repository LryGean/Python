'''
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
'''

#使用break退出循环
'''
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
'''

#在循环中使用continue
'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#Ctrl + C结束无限循环
'''

#使用while循环来处理列表和字典
'''
#在列表之间移动元素
#首先，创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brian','candace']       #unconfirmed user:未经验证的用户
confirmed_users = []

#验证每个用户，直到没有未验证用户为止
#将每个经过验证的用户都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()            #current:现在的、当前的
    print("Verifying user: " + current_user.title())  #verifying:验证、核查
    confirmed_users.append(current_user)

#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''

'''
#删除包含特定值得所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
'''

#使用用户输入来填充字典
responses = {}

'''
#设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    #将答卷存储在字典中
    responses[name] = response

    #看看是否还有人要参与调查
    repeat = input("Would you like to let another person resond?(yes/no)")
    if repeat == 'no':
        polling_active = False
    #调查结果，显示结果
    print("\n--- Poll Result ---")
    for name,response in responses.items():
        print(name + " would like to climb " + response + ".")
'''

#补充：for循环主要是用来遍历/循环：序列或者集合字典
'''
a = [['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    for y in x:
        print(y,end=' ')
#else:
#    print("\nfruit is gone")
#else也属于for循环的成分
'''

#for i in range(0,10,2):
#    print(i,end = " | ")

#for i in range(10,0,-2):
#    print(i,end = " | ")


#打印相间隔的数字 
a = [1,2,3,4,5,6,7,8]
'''for i in range(0,len(a),2):
    print(a[i],end = ' | ')
'''
#或者利用切片：
b = a[0:len(a):2]
print(b)
