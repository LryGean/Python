import requests
from lxml import etree

# 第一部确定
if __name__ == '__main__':
    url = 'https://www.qbiqu.com/0_305/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    # 发请求
    resp = requests.get(url, headers=headers)
    resp.encoding = "gbk"
    # 获取Q源码
    html = resp.text
    # print(html)
    # 采用xpath解析
    html_element = etree.HTML(html)
    lis = html_element.xpath('//div[@id="list"]/dl/dd')[9:]
    # print(lis)
    for i in lis:
        title = i.xpath('.//a/text()')[0]
        href = 'https://www.qbiqu.com' + i.xpath('.//a/@href')[0]
        # print(title, href)
        res = requests.get(href, headers=headers)
        res.encoding = 'gbk'
        htmlText = res.text
        htm = etree.HTML(htmlText)
        content = htm.xpath('//div[@id="content"]/text()')
        # print(content)
        with open(f'./book/{title}.txt', 'w', encoding='utf-8', newline='') as f:
            f.writelines(content)   # 写入多行
        break
