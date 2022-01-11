dimensions = (200,50)

'''
print(dimensions[0])
print(dimensions[1])
'''

#不能给元祖元素赋值
'''
dimensions[0] = 250
'''

print("Original dimension:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)