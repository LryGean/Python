import csv
# 1. 读取数据
# with open('./csv/person.csv', 'r', encoding='utf-8') as f:
#     # 1.创建对象
#     csvreader = csv.reader(f)
#     for i in csvreader:
#         print(i)   # 数据存放在列表中

# 2. 方式二
with open('./csv/personDic.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.DictReader(f)
    for i in csvreader:
        print(i['name'])
        print(i)
