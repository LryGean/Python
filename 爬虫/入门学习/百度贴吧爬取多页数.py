import requests

kw = input("请输入贴吧主题：")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}

for i in range(1, 6):
    url = f'https://tieba.baidu.com/f?kw={kw}&ie=utf-8&pn={(i-1)*50}'
    resp = requests.get(url, headers=headers)
    with open(f'./data/百度跳吧{i}页.html', 'w', encoding='utf-8') as f:
        f.write(resp.text)
    f.close()
    resp.close()
