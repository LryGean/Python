#函数返回两个值
'''
def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 *2 + 10
    return damage1,damage2

# damages = damage(3,6)
# print(damages)              #(9,22)
# print(type(damages))        #元组
# print(damages[0])
skill_damage1,skill_damage2 = damage(3,6)
print(skill_damage1,skill_damage2)
'''

'''
#序列解包 （a,b,c = d）
a = 1
b = 2
c = 3
#等价于
a,b,c = [1,2,3]
#一个变量接收三个数值表示一个元组
d = 1,2,3
a,b,c = d
print(type(d))
print(d)

#补充
a = 1
b = 1
c = 1
# 等价于
a=b=c=1 
'''

'''
# 让实参变成可选的
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)
'''

'''
# 返回字典
def build_person(first_name,last_name,age=''):
    """返回一个字典，其中包括有关的一个人的信息"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=27)
print(musician)
'''

'''
# 结合使用函数和while循环
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    if f_name == 'q':
        break
    l_name = input("last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHellow, " + formatted_name + "!")
'''

# 传递列表
'''
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannnah','ty','margot']
greet_users(usernames)
'''     

'''
def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #模拟根据设计制作3D打印模型的过程
        print("Printing models: " + current_design)
        completed_models.append(current_design)                                         
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
# 若禁止修改列表可用：print_models(unprinted_designs[:],completed_models)
# 注释：切片[:]用来创建列表副本
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
'''


# 可变参数
'''
# 传递任意数量的参数
def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print("\nMaking a  " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
'''

# 使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)