from enum import IntEnum,unique
from enum import Enum

# 所有的枚举类都需要继承Enum类
class VIP1(Enum):
    # 不能有相同的标签名
    YELLOW = 1
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3
    RED = 4
    COLOR = 'color'

# 将拿到的数据转换成枚举类型
# a = 1
# print(VIP1(a))


# 所有枚举类型的值必须是整形
# 不能有相同值
@unique
class VIP2(IntEnum):
    # 不能有相同的标签名
    YELLOW = 1
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 枚举类型不能进行实例化

# 23中设计模式 枚举类型用作单例模式