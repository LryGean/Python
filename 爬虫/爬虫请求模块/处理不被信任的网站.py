import requests

url = "https://inv-veri.chinatax.gov.cn/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}


# requests向一个网站发请求， 会主动
resp = requests.get(url, headers=headers, verify=False)
print(resp.text)
