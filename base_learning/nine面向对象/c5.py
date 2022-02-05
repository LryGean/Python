
class Human():
    
    sum = 0

    # 定义构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义实例方法
    def get_name(self):
        print(self.name)

    def do_homework(self):
        print('This is a parent method')