# 递归
'''
counter = 1
while counter <= 10:
    counter += 1
    print(counter)
else:
    print("终于打上了王者！")
'''
lis = []
for i in [2,8,3,6,5,3,8]:
    lis.append(i)
lis = lis(set(lis))
lis.sort()
print(lis)