import scrapy

from my_scrapy.items import MyScrapyItem


class SpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'spider4'
    # 允许爬取的范围 域名限制
    allowed_domains = ['quotes.toscrape.com']
    base_url = 'https://quotes.toscrape.com/page/{}/'
    # 初始请求
    start_urls = ['https://quotes.toscrape.com/']

    # 方法5：方法重写
    def start_requests(self):
        for page in range(1, 6):
            url = self.base_url.format(page)
            yield scrapy.Request(url, callback=self.parse)

    # 解析方法，默认调佣，自动执行
    def parse(self, response):
        # print(response.text)

        quotes = response.xpath('//div[@class="quote"]')

        for quote in quotes:
            # 旧方法
            # extract_first()返回一条数据
            # extract() 返回多条数据

            # 新方法
            # get()返回一条数据
            item = MyScrapyItem()
            item['text'] = quote.xpath('./span[@class="text"]/text()').get()
            # print(text)
            item['author'] = quote.xpath('.//small[@class="author"]/text()').get()
            # print(author)
            # 获取多条数据
            item['tags'] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
            # print(item)
            yield item

