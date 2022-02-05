""" 
class Dog():
    #一次模拟小猴的简单尝试
    def __init__(self,name,age):
        #初始化属性name和age
        self.name = name
        self.age = age

    def sit(self):
        #模拟小狗被命令时蹲下
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        #模拟小狗被命令时打滚
        print(self.name.title() + " rolled over!")
"""
#根据类创建实例
"""
my_dog = Dog('willie',6)
you_dog = Dog('lucy',3)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " year old.")
my_dog.sit()
my_dog.roll_over()

print("\nYou dog's name is " + you_dog.name.title() + '.')
print("You dog is " + str(you_dog.age) + " year old.")
you_dog.sit() 
"""

