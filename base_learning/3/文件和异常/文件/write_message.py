#写入空文件
#写入多行
filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

#附加到文件
filename = 'programming.txt'

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that run in a browser.\n")