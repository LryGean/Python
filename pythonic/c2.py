# 字典映射代替switch
# 用函数方法替代字典中的value

day = 7

def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_wednesday():
    return 'Wednesday'

def get_thursday():
    return 'Thursday'

def get_friday():
    return 'Friday'

def get_saturday():
    return 'Saturday'

def get_default():
    return 'UnKnow'

switchcher = {
    0 : get_sunday,
    1 : get_monday,
    2 : get_tuesday,
    3 : get_wednesday,
    4 : get_thursday,
    5 : get_friday,
    6 : get_saturday
}

day_name = switchcher.get(day, get_default)()
print(day_name)