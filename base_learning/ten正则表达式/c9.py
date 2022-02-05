# 组 
import re
a = 'PythonPythonPythonPythonPythonJS'


# 小括号表示组
# r = re.findall('PythonPythonPython',a)
r = re.findall('(Python){3}(JS)',a)


# print(r)

# 区别
# ()内是且的关系
# []内是或的关系
