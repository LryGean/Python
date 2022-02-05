# 面向对象
# 有意义的面向对象代码
# 类 = 面向对象
# 类、对象
#类的最基本作用：封装代码

# 定义类
class Student():
    # 特征
    # 类变量
    # 一个班级里所有的学生的总数
    sum = 0
    # name = '七月'
    # age = 0 


    # 构造函数（特殊的）
    # 通过模板生成不同的对象
    def __init__(self,name,age):
        # 初始化对象的属性（特征）
        # 第一个name是定义的，第二个name是传入的参数name
        # (局部变量不会覆盖全局变量，作用于只作用于函数内部)


        # 定义实例变量
        self.name = name
        self.age = age

        # 操作实例变量（最好带上self）
        # print(self.name)
        
        # 访问类变量sum
        # （1）
        # print(Student.sum)
        # （2）
        # print(self.__class__.sum)

        # 判断创建对象的个数
        # self.__class__.sum += 1
        # print('当前班级学生总数为：' + str(self.__class__.sum)) 

        # 外部调用时才能存入字典中
        # print(self.__dict__)
        # 读取形参name
        # print(name)

        # print('student')
        # 只能返回None，默认返回None
        # return None

    # 行为
    # 普通方法
    def do_homework(self):
        print('homework')

    # self：表示对象本身
    # cls：表示类本身

    # 定义类方法（用来操作类变量）
    # @：装饰器
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        # print('当前班级学生总数为：' + str(cls.sum))

    #定义静态方法
    @staticmethod
    def add(x,y):
        # print(Student.sum)
        print()
        print('This is a static method')


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

# 调用类中方法
# student.print_file()

# 先实例化对象
# 调用构造方法
student1 = Student('小明',18)
student1.add(1,2)
Student.add(1,2)
# 对象调类方法（不建议使用）
# student1.plus_sum()
# 推荐使用类调用类方法
# Student.plus_sum()
# student2 = Student('小亮',19)
# Student.plus_sum()
# student3 = Student('小红',20)
# Student.plus_sum()

# 调用普通方法
# student1.do_homework()
# print(student1.name)
# print(student2.name)
# print(Student.sum)


#    方法：设计层面（面向对象）
#    函数：程序运行、过程式的一种称谓（面向过程）

# 类是现实世界或思维世界中的实体在计算机中的反映
# 它将数据以及这些数据上的操作封装在一起