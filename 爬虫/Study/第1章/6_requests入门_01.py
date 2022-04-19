import requests
query = input("请输入一个你喜欢的明星：")


# url = 'https://www.sogou.com/web?query={}'.format(query)
url = f'https://www.sogou.com/web?query={query}'

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

resp = requests.get(url, headers=head)         # 处理一个小小的反爬

# print(resp)
print(resp.text)  # 获取源代码

resp.close()

