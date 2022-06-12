import requests

url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}
key = input("请输入：")
data = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16511533881732",
    "sign": "f1eb1be9a0dfa615233e76246c7bd467",
    "lts": "1651153388173",
    "bv": "70f10884355e7360fdfde6199e8b5094",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
}

# 会携带数据
resp = requests.post(url, headers=headers, data=data)
# print(resp.text)

data_json = resp.json()
# print(data_json)

d = data_json['translateResult'][0][0]['tgt']
print(d)

