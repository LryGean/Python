# 字符串替换
import re
language = 'PythonC#JavaC#PHPC#'


# r = re.sub('C#', 'Go', language)
# 结果：Python Go Java Go PHP Go

# 参数：count(默认值取0，表示指定替换的字符串在原字符串中全部被替换,1表示替换的最大个数为1)
# r = re.sub('C#', 'Go', language, 1)
# 结果：Python Go Java C# PHP C#

# 内置字符串替换函数replace
# 注意：由于字符串是不可变的，所以使用replace时需重新赋值一个变量
# s = language.replace('C#', 'Go', 1)
# print(s)
# 结果：Python Go Java C# PHP C#



# 第二个参数可以为函数
def convert(value):
    
    # value是一个对象
    print(value)
    # span=<前面有几位，指定字符串最后一位的位置>
    # <re.Match object; span=(6, 8), match='C#'>
    # <re.Match object; span=(12, 14), match='C#'>
    # <re.Match object; span=(17, 19), match='C#'>

    matched = value.group()

    return ' ' + matched + ' '
# 解释：C#作为参数传入函数中
# 利用函数作为参数进行动态替换 
r = re.sub('C#', convert, language)
#结果：Python  Java C# PHP C#



print(r)