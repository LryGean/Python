# 43、
# 以123位随机数种子，随机生成10个在1（含）到999（含）之间的随机整数，
# 每个随机数后跟随一个逗号进行分隔，厅幕输出这10个随机数。



# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

import random
random.seed(123)
for i in range(10):
    print(random.randint(1,999), end=",")