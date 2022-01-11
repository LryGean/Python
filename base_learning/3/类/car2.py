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

my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()