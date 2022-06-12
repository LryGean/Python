import urllib.request
import urllib.parse

url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E8%91%AB%E8%8A%A6%E5%A8%83&fr=search'

# url = urllib.parse.unquote(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}

resp = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(resp)

print(resp.read().decode("utf-8"))
