import urllib.request
# 1.创建请求对象
url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
}
# 2.获取响应结果
req = urllib.request.Request(url, headers=headers)
# 3.获取内容
resp = urllib.request.urlopen(req)
print(resp.read().decode("utf-8"))   # 解码
