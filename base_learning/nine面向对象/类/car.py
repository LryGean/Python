#一组用于表示燃油汽车和电动汽车的类
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
        self.odmeter_reading += mile

class Battery():
    #一次模拟电动汽车的简单尝试

    def __init__(self,battery_size=70):
        #初始化电瓶的属性
        self.battery_size = battery_size

    def describe_battery(self):
        #打印一条描述电瓶容量的消息
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        #打印一条消息，指出电瓶的续航里程
        if self.battery_size == 70:
            range = 240
        else:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge." 
        print(message)    

class ELectricCar(Car):
    #电动汽车的独特之处

    def __init__(self,make,model,year):
        #初始化父类的属性，再初始化电动汽车特有的属性
        super().__init__(make,model,year) 
        self.battery = Battery()