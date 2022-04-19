import requests

url = 'https://movie.douban.com/j/chart/top_list'

# url参数过长，重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

resp = requests.get(url, params=param, headers=header)

# print(resp.request.url)

# 查看python默认的headers
# print(resp.request.headers)

print(resp.json())

# 关闭请求
resp.close()
