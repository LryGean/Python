import requests

kw = input("请输入：")
url = f'https://tieba.baidu.com/f?fr=wwwt&ie=utf-8&dyTabStr=MCw2LDMsMSwyLDQsNSw4LDcsOQ%3D%3D&kw={kw}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}

resp = requests.get(url, headers=headers)

# print(resp.text)
with open('百度跳吧.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)

f.close()
resp.close()
