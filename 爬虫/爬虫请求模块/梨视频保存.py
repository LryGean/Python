import requests
r_url = "https://www.pearvideo.com/video_1760884"
id1 = r_url.split("_")[-1]
url = "https://www.pearvideo.com/videoStatus.jsp?contId=1760884&mrd=0.3786766218092379"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'Referer': url
}

resp = requests.get(url, headers=headers)
dic_data = resp.json()
# print(dic_data)

video_url = dic_data['videoInfo']['videos']['srcUrl']
# print(video_url)

systemTime = dic_data['systemTime']
v_url = video_url.replace(systemTime, f'cont-{id1}')
# print(v_url)

re = requests.get(v_url)
with open('./video/v1.mp4', 'wb') as f:
    f.write(re.content)
f.close()
re.close()
resp.close()
