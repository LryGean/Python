#文件路径
#with open('text_file\filename.txt') as file_object：


'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
'''

#逐行读取
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
'''


'''
#创建一个包含晚间各行内容的列表
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    #删除末尾的空行
    print(line.rstrip())
'''

