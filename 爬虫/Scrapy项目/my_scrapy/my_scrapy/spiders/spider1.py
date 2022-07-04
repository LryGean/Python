import scrapy

from my_scrapy.items import MyScrapyItem


class SpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'spider1'
    # 允许爬取的范围 域名限制
    allowed_domains = ['quotes.toscrape.com']
    # 初始请求
    start_urls = ['https://quotes.toscrape.com/']

    page = 1

    # 解析方法，默认调佣，自动执行
    def parse(self, response):
        # print(response.text)

        quotes = response.xpath('//div[@class="quote"]')

        for quote in quotes:
            # extract_first()返回一条数据
            # extract() 返回多条数据

            # 新方法
            # get()返回一条数据
            item = MyScrapyItem()
            item['text'] = quote.xpath('./span[@class="text"]/text()').get()
            # print(item['text'])
            item['author'] = quote.xpath('.//small[@class="author"]/text()').get()
            # print(author)
            # 获取多条数据
            item['tags'] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
            # print(item)
            yield item

        # 方法1
        # self.page += 1
        # url = self.start_urls[0] + f'page/{self.page}'
        # if self.page <= 5:
        #    yield scrapy.Request(url=url, callback=self.parse)

        # 方法二
        # （1）
        next1 = response.css('.pager .next a::attr(href)').get()
        print(next1)
        # url = 'https://quotes.toscrape.com' + next1  # 需要考虑为空的情况
        # yield scrapy.Request(url=url, callback=self.parse)

        # (2)
        url = response.urljoin(next1)
        yield scrapy.Request(url=url, callback=self.parse)



