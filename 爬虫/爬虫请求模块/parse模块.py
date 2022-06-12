# 编码
import urllib.request
import urllib.parse
# key = input('请输入')   # 不识别中文
# dic = {
#     'kw': key
# }
# # 对中文进行编码操作
# # 方法一 中文转 % 十六进制
# # value = urllib.parse.urlencode(dic)
# # 方法二
# value = urllib.parse.quote(key)
# print(value)
# url = f'https://tieba.baidu.com/f?ie=utf-8&kw={value}&fr=search'
# # resp = urllib.request.urlopen(url)
# print(url)

url = "https%3A%2F%2Fshp%2Eqpic%2Ecn%2Fishow%2F2735042915%2F1651219067%5F1265602313%5F7108%5FsProdImgNo%5F1%2Ejpg%2F200"
urls = urllib.parse.unquote(url)   # 解码
urllib.request.urlretrieve(urls, './picture/阿斗.jpg')

