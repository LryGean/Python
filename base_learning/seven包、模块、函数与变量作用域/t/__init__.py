
# ********* __init__模块名就是包名**************


# 自动生成的文件作用是课直接被导入
# 一般用来用作包和模块的初始化 
# a = 'This is __init__.py file'
# print(a)
##清屏用:cls

#系统内置内库
import sys
import datetime
import io

#其他模块导入该包下的模块时，__init__可以决定哪些模块被导入
__all__ = ['c1','c3']

print(sys.path)