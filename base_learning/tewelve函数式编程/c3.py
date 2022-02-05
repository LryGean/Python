# reduce

from functools import reduce

list_x = [1,2,3,4,5,6,7,8]

# 必须要有两个参数
r1 = reduce(lambda x,y:x+y, list_x)   # 连续取值，每一次的计算结果作为下一次的参数x,y取后面以为（例：①1+2 ②（1+2）+3 ...） 
print(r1)
# 结果：36

# 将10作为初始值传入
r2 = reduce(lambda x,y:x+y, list_x, 10)
print(r2)
# 结果：46

list_x1 = ['1','2','3','4','5','6','7','8']
r3 = reduce(lambda x,y:x+y, list_x1,'aaa')
print(r3)
# 结果：aaa12345678


# map  / reduce 编程模型 
# 映射 / 归约
# 并行计算