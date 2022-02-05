'''name =  "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
'''

'''
#拼接字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hellow, " + full_name.title() + "!")

message = "Hellow, " + full_name.title() + "!"
print(message)
'''

'''
#删除末尾空白
favorite_language1 = 'python '
    #临时
favorite_language1.rstrip()
print(favorite_language1)
    #永久
favorite_language1 = favorite_language1.rstrip()
print(favorite_language1)
'''
'''
#开头空白
favorite_language2 = ' python'
    #临时
favorite_language2.lstrip()
print(favorite_language2)
    #永久
favorite_language2 = favorite_language2.lstrip()
print(favorite_language2)
'''

'''
#开头空白
favorite_language3 = ' python '
    #临时
favorite_language3.strip()
print(favorite_language3)
    #永久
favorite_language3 = favorite_language3.strip()
print(favorite_language3)
'''

# 正确使用引号
""" 
message = "One of the Python's strength is its diverse community."
print(message)

message = 'One of the Python\'s strength is its diverse community.'
print(message) 
"""

# 字符串换行
# 单引号和双引号用\
""" str1 = 'hellow world \
hellow world'
print(str1) """

# 三引号默认换行\n
""" str2 = '''hellow world
hellow world'''
print(str2) """

# 字符串切片
s = "hell world"
print(s[6:10])
print(s[6:-1])
print(s[6:0])
print(s[6:])
print(s[:-1])
print(s[:])

# id函数可以显示变量的内存地址
print(id(s))  # 2209744317424