import pizza
#或 ：from pizza import make_pizza
#使用as给函数指定别名：from  pizza import make_pizza as mp
#使用as给模块指定别名： import pizza as p
#导入模块所有函数：from pizza import *

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')