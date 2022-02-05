# 面向对象
# 有意义的面向对象代码
# 类 = 面向对象
# 类、对象
#类的最基本作用：封装代码

# 定义类
class Student():
    # 特征
    # 类变量

    name = '七月'
    # age = 0 


    # 构造函数
    # 通过模板生成不同的对象
    # 实例方法中第一个参数必须指定为self（可以更改成this）:实例可以调用的方法
    def __init__(self,name,age):
        # 初始化对象的属性（特征）
        # 第一个name是定义的，第二个name是传入的参数name
        # (局部变量不会覆盖全局变量，作用于只作用于函数内部)
        # name = name


        # 定义实例变量
        self.name = name
        self.age = age
        print(name)
        print(age)

        # print('student')
        # 只能返回None，默认返回None
        # return None


    # 构造函数
    # 行为
    def do_homework(self):
        print('homework')


# class Printer():
    
#    # 在类中编写函数需强制传入参数self，固定的特征
#    def print_file(self):
#         print('name:' + self.name)
#         print('age:' + str(self.age))

# a = student1.__init__()
# print(a,'\n',type(a))

# print(id(student1))
# print(id(student2))
# print(id(student3))

# 调用类中的方法
# student.print_file()

# 先实例化对象
student1 = Student('小明',18)

student1.do_homework()

# __dict__内置实例变量的存储用字典来存储
# print(student1.__dict__)
# print(Student.__dict__)

# student2 = Student('小亮',19)
# student3 = Student()

# print(student1.name)
# print(student2.name)
# print(Student.name)


#    方法：设计层面（面向对象）
#    函数：程序运行、过程式的一种称谓（面向过程）