from enum import Enum

# 所有的枚举类都需要继承Enum类
class VIP(Enum):
    # 不能有相同的标签名
    YELLOW = 1
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3
    RED = 4



class Common():
    YELLOW = 1

# print(VIP.YELLOW)
# 结果：VIP.YELLOW


# print(VIP.YELLOW_ALIAS)
# 结果：VIP.YELLOW
# 解释：第二个YELLOW_ALIAS因为值和YELLOW相等，所以被看做是YELLOW的别名



# 遍历
for v in VIP:
    print(v)
# 别名不会被直接遍历出

print('-----------------------')

for i in VIP.__members__.items():
    print(i)

# 结果
# ('YELLOW', <VIP.YELLOW: 1>)
# ('YELLOW_ALIAS', <VIP.YELLOW: 1>)
# ('GREEN', <VIP.GREEN: 2>)
# ('BLACK', <VIP.BLACK: 3>)
# ('RED', <VIP.RED: 4>)

print('-----------------------')

for p in VIP.__members__:
    print(p)

# 结果
# YELLOW
# YELLOW_ALIAS
# GREEN
# BLACK
# RED