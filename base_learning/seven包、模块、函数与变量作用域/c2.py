#不同级别的引入
#方法二:
# import t.c1
# print(t.c1.a)

#对于路径较长的引用
#方法三:
# import t.c1 as m
# print(m.a)

#方法四:
# from t.c1 import a
# print(a)

#方法五:
# from t import c1
# print(c1.a)

#引入多个变量
#方法六:
# from t.c1 import *
# print(a)
# print(b)
# print(c)

#方法七:
# from t.c1 import a,b,\   #\用来换行或者加括号
# c
# print(a,"\n",b,"\n",c)
import t 
