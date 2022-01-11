from car import ELectricCar

my_tesla = ELectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()