import requests

url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1760318&mrd=0.6085973234963866'


# 防盗链
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    'Referer': 'https://www.pearvideo.com/video_1760318'
}

resp = requests.get(url, headers=headers)

print(resp.text)
