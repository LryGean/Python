import requests
from lxml import etree


url = "https://beijing.zbj.com/search/f/?type=new&kw=saas"

resp = requests.get(url)

# print(resp.text)

# 解析原码
html = etree.HTML(resp.text)

# 拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")

for div in divs:
    price = div.xpath('./div/div[@id="utopia_widget_76"]/a[2]/div[2]/div[1]/span[1]/text()')[0].strip("¥")
    # print(price)
    title = "saas".join(div.xpath('./div/div[@id="utopia_widget_76"]/a[2]/div[2]/div[2]/p/text()'))
    print(title)
    com_name = div.xpath('./div/div[@id="utopia_widget_76"]/a[1]/div[1]/p/text()')
    del com_name[0]
    com_name[0] = com_name[0].replace('\n', '')
    # print(com_name)
    location = div.xpath('./div/div[@id="utopia_widget_76"]/a[1]/div[1]/div/span/text()')
    # print(location)

resp.close()
