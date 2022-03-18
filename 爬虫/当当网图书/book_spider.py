import requests
import parsel
import json

class Book_Spider(object):
    def __init__(self):
        self.data_url = "http://e.dangdang.com/classification_list_page.html?category=XS2&dimension=dd_sale&order=0"
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; __permanent_id=20220318201630480336681765467974315; __visit_id=20220318201630482782914849929313650; __out_refer=1647605790%7C!%7Cwww.baidu.com%7C!%7C; __rpm=%7Cmix_65152.403752%2C5360.1.1647605826037; MDD_channelId=70000; MDD_fromPlatform=307; producthistoryid=1900768012; __trace_id=20220318202748771205266166875768587",
            "Host": "e.dangdang.com",
            "Referer": "http://book.dangdang.com/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

    # 获取网页源代码
    def get_page_index(self):
        response = requests.get(url=self.data_url,headers=self.headers)
        if response.status_code==200:
            return response.text
        else:
            return None

    # 提取详情页链接
    def parse_url_iindex(self,html):
        selector = parsel.Selector(html)
        data_list = selector.xpath('//div[@class="new_aside"]/dl/dd')
        for data in data_list:
            href = data.xpath("./a/@href").get()
            book_url = "http:"+str(href)
            for item in self.parse_page_index(book_url):
                self.write_data(item)
                print(item)

    # 解析详情页，获取源代码，并且提取目标数据
    def parse_page_index(self,book_url):
        response = requests.get(url=book_url, headers=self.headers).text
        selector = parsel.Selector(response)
        book_list = selector.xpath('//div[@id="book_list"]')
        for book in book_list:
            title = book.xpath("./a/@title").get()
            author = book.xpath('./a/div/div[@class="author"]/text()').get()
            price = book.xpath('./a/div/div[@class="price"]/span/text()').get()
            yield {
                "书名":title,
                "出版社":author,
                "价格":price
            }

    # 保存数据
    def write_data(self,data):
        with open("图书.txt","a",encoding="utf-8") as f:
            f.write(json.dumps(data,ensure_ascii=False)+"\n")

    def run(self):
        html = self.get_page_index()
        self.parse_url_iindex(html)

if __name__ == '__main__':
    spider = Book_Spider()
    spider.run()








