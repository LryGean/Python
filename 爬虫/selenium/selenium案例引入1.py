import requests

url = 'http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn=1&rn=30&httpsStatus=1&reqId=0306dd31-d908-11ec-b104-b5826ed548fe'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    'csrf': 'SC9WDBBYF4H',
    'Cookie': '_ga=GA1.2.943117738.1647433269; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1651146831,1652183760,1653138827; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1653138827; _gid=GA1.2.1473897111.1653138827; kw_token=SC9WDBBYF4H'
}

resp = requests.get(url, headers=headers)
# print(resp.text)
data = resp.json()
lis = data['data']['musicList']
for i in lis:
    print(i['artist'], i['name'])
    