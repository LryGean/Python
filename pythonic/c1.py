# 字典映射代替switch

switchcher = {
    0 : 'Sunday',
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday'
}

# for day in range(7):
#     day_name = switchcher[day]
#     print(day_name)


day = 10
day_name = switchcher.get(day, 'UnKnow')
print(day_name)