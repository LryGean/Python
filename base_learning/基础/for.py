"""
a = [["apple","banana","orange","grape"],(1,2,3)]
for i in a:
    for b in i:
        if b == "orange":
            break
        print(b)
else:
    print('fruit is gone')
     """

# a = [1,2,3]
# for i in a:
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("EOF")


#for循环和while循环：
#for i in range(0,10,2):
#    print("(",i,")",end = " | ")       #end:让变量一行的方式出现
for i in range(10,0,-2):
    print("(",i,")",end = " | ")

# i = 0
# while i < 10:
#     print(i)
#     i += 2
    