from enum import Enum

# 所有的枚举类都需要继承Enum类
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class Common():
    YELLOW = 1


# print(VIP.YELLOW)
# print(type(VIP.YELLOW))
# # VIP类型

# # 获取标签名
# print(VIP.YELLOW.name)
# print(type(VIP.YELLOW.name))
# # 标签名是一个字符串

# # 获取枚举类型的值
# print(VIP.YELLOW.value)

# # 通过枚举名称获取枚举类型
# print(VIP['GREEN'])


# 遍历枚举类型
for v in VIP:
    print(v)