# 序列化
# 将Python数据转化成JSON字符串
import json

students = [
            {'name':'gean', 'age':18, 'flag':False},
            {'name':'qiyue', 'age':19}
          ]

json_str = json.dumps(students)
# 检查是否转化成功
print(type(json_str))
# 结果：<class 'str'>
print(json_str)

# NOSQL MongDB