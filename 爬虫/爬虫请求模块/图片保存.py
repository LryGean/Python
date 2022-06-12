import urllib.request

url = 'https://img0.baidu.com/it/u=1278618774,2401043221&fm=253&fmt=auto&app=138&f=JPEG?w=575&h=500'

urllib.request.urlretrieve(url, './picture/2.jpg')

