# 一个模块定义一个类

# 一个子类允许多继承


from unittest.mock import seal
from c5 import Human

# 继承父类People

class Student(Human):
    
    # sum = 0
    
    def __init__(self, school, name, age):
        self.school = school
        # 子类调用父类的构造函数   (类调用实例方法，不推荐)
        # Human.__init__(self, name, age)
        # 主流调用方法
        super(Student, self).__init__(name, age)
        # self.__score = 0
        # self.__class__.sum += 1

    # 子类方法和父类方法同名，优先调用子类的方法
    def do_homework(self):
        # 子类调用父类普通方法
        super(Student,self).do_homework()
        print('english homework')


student1 = Student('贝壳大学','小明',18)
student1.do_homework()

# 对象调用实例方法Python自动将student1传入方法中
# student1.do_homework()

# Student.do_homework(student1)
# Student.do_homework('')
# print(student1.sum)
# print(Student.sum)

# 继承属性
# print(student1.name)
# print(student1.age)

# 继承方法
# student1.get_name()