'''
bicyclers = ['trek','cannondale','redine','specialized']
#print(bicyclers)
#print(bicycles[0])
#print(bicycles[0].title())
#print(bicycles[1])
#print(bicycles[3])
#print(bicycles[-1])
#print(bicycles[:-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
'''

'''
#修改列表元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
'''

'''
#①添加元素
motorcycles = ['honda','yamaha','suzuki']
#motorcycles.append('ducati')
#print(motorcycles)

#②插入元素
motorcycles.insert(1,'ducati')
print(motorcycles)
'''

#motorcycles = ['honda','yamaha','suzuki']
#删除元素

#一、del 删除
#del motorcycles[0]
#del motorcycles[1]
#del motorcycles[0:2]
#print(motorcycles)

#二、pop ①括号为空删除末尾元素
#print(motorcycles)
#poped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(poped_motorcycle)

#②指定位置删除元素
#print(motorcycles)
#first_owned = motorcycles.pop(0)
#print(motorcycles)

#三、remove 根据值删除
""" 
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)   
"""   


#组织列表
cars = ['bmw','audi','toyota','subaru']
""" 
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
"""

#临时排序
"""
 print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars,reverse=True))

print("\nHere is the original list again:")
print(cars)
"""

#倒着打印列表
cars.reverse()
print(cars)
print(cars[-2])
print(len(cars))