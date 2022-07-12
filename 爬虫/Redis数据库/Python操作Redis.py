import redis


# 创建连接对象 与redis服务简历链接
sr = redis.StrictRedis()
# sr.set('u4', 'LinFei')
# sr.lpush('u5', '1', '2', '3', '4')
# print(sr.lrange('u5', 0, -1))

class StringRedis:
    def __init__(self):
        self.conn = redis.StrictRedis(host='127.0.0.1', port=6379, db=1, decode_responses=True)

    def string_set(self, k, y):
        # 写入
        res = self.conn.set(k, y)
        print(res)

    def string_get(self, k):
        # 读取
        res = self.conn.get(k)
        print(res)


s = StringRedis()
s.string_set('u6', '陈凡')
s.string_get('u6')

