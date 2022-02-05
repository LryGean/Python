#继承
class Car():
    #一次模拟汽车的简单尝试
    def __init__(self,make,model,year):
        #初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odmeter_reading = 0

    def get_descriptive_name(self):
        #返回整洁的描述信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        #打印出一条指出期初里程的消息
        print("This car has " + str(self.odmeter_reading) + " miles on it.")
    def update_odometer(self,mileage):
        #将里程数设置位为指定值
        #禁止将里程表里读数往回调
        if mileage >= self.odmeter_reading:
            self.odmeter_reading = mileage
        else:
            print("You can't roll back an odmeter!")
    def increment_odometer(self,miles):
        #将里程表读书增加指定的量
        self.odmeter_reading += miles

class ELectricCar(Car):
    #电动汽车的独特之处

    def __init__(self,make,model,year):
        #电动汽车的独特之处
        #初始化父类的属性，再初始化电动汽车特有的属性
        
        #super()用于将父类和子类关联起来
        super().__init__(make,model,year) 
        self.battery_size = 70
    
    def dedescribe_battery(self):
        #打印一条描述电瓶容量的消息
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    
my_tesla = ELectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.dedescribe_battery()