#从一个模块中导入多个类
'''
from car import Car,ELectricCar

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ELectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
'''

#导入整个模块
import car

#导入模块中的所有类
#from car import *

my_beetle = car.Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ELectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())