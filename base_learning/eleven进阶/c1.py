# 类型
# 绿钻、黄钻、红钻、黑钻

# 枚举

from enum import Enum

# 所有的枚举类都需要继承Enum类
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW)
# 枚举的意义是标签名，不是值