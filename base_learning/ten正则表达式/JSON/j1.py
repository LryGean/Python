# 反序列化

import json

# JSON object
# json字符串格式
# 外部用单引号，内部用双引号
# key和value(除了数字)
json_str = '{"name":"gean", "age":18}'

# JSON array
json_arr = '[{"name":"gean", "age":18, "flag":false}, {"name":"qiyue", "age":19}]'


# # 将JSON字符串转换成python对应的数据结构
# student = json.loads(json_str)
# print(type(student))
# # 字典格式：<class 'dict'>
# # 说明：不同语言转化的格式不同，python是字典格式
# print(student)
# # {'name': 'gean', 'age': 18}
# print(student['name'])
# print(student['age'])


students = json.loads(json_arr)
print(type(students))
# 列表格式：<class 'list'>
print(students)
# 注意：python会将小写的布尔值转化为大写
