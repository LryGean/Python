from enum import Enum

# 所有的枚举类都需要继承Enum类
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# # 枚举类型的等值比较
# result1 = VIP.GREEN == VIP.BLACK
# print(result1)
# # 结果：False

# result2 = VIP.GREEN == 2
# print(result2)
# # 结果：False


# 枚举类型的等值比较（不支持）
# result3 = VIP.GREEN > VIP.BLACK
# print(result3)


# # 枚举类型的is比较
# result4 = VIP.GREEN is VIP.BLACK
# print(result4)
# # 结果：False


class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# 不同枚举类型的等值比较
result5 = VIP.GREEN == VIP1.GREEN
print(result5)
# 结果：False