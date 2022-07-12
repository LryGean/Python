from pymongo import MongoClient


class MongoDBConn:
    def __init__(self):
        self.conn = MongoClient()
        # 数据库
        self.db = self.conn['Gean']['a']

    # 添加一条数据
    def add_one(self, v):
        self.db.insert_one(v)

    # 添加多条数据
    def add_many(self, v):
        self.db.insert_many(v)

    # 查询一条数据
    def get_one(self, query):
        res = self.db.find_one(query)
        return res

    # 查询一条数据
    def get_more(self, query):
        more = self.db.find(query)
        return more


if __name__ == '__main__':
    m = MongoDBConn()
    # m.add_one({'name': 'b'})
    # m.add_many([{'name': 'd'}, {'name': 'e'}])
    # r = m.get_one({'name': 'b'})
    # print(r)
    mo = m.get_more({'name': 'd'})
    for i in mo:
        print(i)


# 创建连接
# 默认链接本机电脑的数据库
# conn = pymongo.MongoClient()
#    数据库    表
# 一条数据：字典
# conn['Linfei']['陈凡'].insert_one({'name': '陈凡'})
# 插入多条数据：列表
# conn['Linfei']['陈凡'].insert_many([{'name': '林非'}, {'name': 'Gean'}])


# conn = pymongo.MongoClient()
# conn['Gean']['a'].insert_one({'name': 'a'})
