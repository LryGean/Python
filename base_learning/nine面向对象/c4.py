# 成员可见性
# 定义私有的变量或方法需要在变量或方法前加双下划线__

from cgi import print_directory


class Student():
    
    sum = 0
    
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum += 1

    # 打分
    def marking(self, score):
        if score < 0:
            score = 0
            return '不能给别人打负分'        
        self.__score = score
        print(self.name + '同学本次考试分数为：' + str(self.__score))

    # 行为与特征
    def do_homework(self):
        # 类的内部调用
        self.do_english_homework()
        print('homework')

    def do_english_homework(self):
        print()

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)
        # print('当前班级学生总数为：' + str(cls.sum))

    @staticmethod
    def add(x,y):
        print(Student.sum)
        print('This is a static method')

student1 = Student('小明',18)
student2 = Student('小亮',19)
# 外部调用
# student1.do_homework()
# student1.__marking__(59)
result = student1.marking(59)
# print(result)


# 不安全、错误的打分方法
# 新添加的实例变量，并不是原来的属性值，是动态强行添加的私有变量
student1.__score = -1
# print(student1.__score)

#通过内置变量查看某一个对象的内部成员列表
print(student1.__dict__)
print(student2.__dict__)
print(student2._Student__score)

# print(student2.__score)