import csv

# 第一种
# persons = [('张三', 18, 180), ('胡军', 23, 182), ('张庆大', 19, 178)]
# # 标题
# headers = ('name', 'age', 'height')
# # wps: utf-8 office: utf-8-sig
# with open('./csv/person.csv', 'w', encoding='utf-8', newline='') as f:
#     # 创建对象
#     csvwriter = csv.writer(f)
#     # 写入
#     csvwriter.writerow(headers)
#     csvwriter.writerows(persons)
#     for i in persons:
#         csvwriter.writerow(i)

# 第二种

persons = [
    {'name': '李四', 'age': 18, 'height': 180},
    {'name': '张三', 'age': 22, 'height': 178},
    {'name': '王五', 'age': 24, 'height': 188},
]

# 标题
headers = ('name', 'age', 'height')
with open('./csv/personDic.csv', 'w', encoding='utf-8', newline='') as f:
    csvwriter = csv.DictWriter(f, headers)   # 标题
    csvwriter.writeheader()     # 写入标题
    csvwriter.writerows(persons)  # 写入数据

# 不用导入模块写入csv
# f.write(f'{x},{y}\n')
# f.write('{},{}'.format(x, y))

