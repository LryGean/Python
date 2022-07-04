import scrapy
import re

from BeiKe_scrapy.items import BeikeScrapyItem


class SpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'spider'
    # 允许爬取的范围 域名限制
    allowed_domains = ['cs.zu.ke.com/zufang/rs/']
    base_url = 'https://cs.zu.ke.com/zufang/pg{}/#contentList'
    # 初始请求
    start_urls = ['https://cs.zu.ke.com/zufang/rs/']

    pg = 1

    # 方法重写
    def start_requests(self):
        for page in range(1, 11):
            if page == 1:
                url = self.start_urls[0]
            else:
                url = self.base_url.format(page)
            yield scrapy.Request(url, callback=self.parse)

    # 解析方法，默认调佣，自动执行
    def parse(self, response):
        # print(response.text)
        quotes = response.xpath('//div[@class="content__list--item--main"]')
        print(f'获取{len(quotes)}')
        lst = []
        for quote in quotes:
            item = BeikeScrapyItem()
            item['title'] = quote.xpath('.//p/a[@class="twoline"]/text()').get().strip('\n').strip(' ')
            # print(item['title'])
            item['region'] = f"{quote.css('.content__list--item--des > a:nth-of-type(1)::text').get()}区"
            item['block'] = quote.xpath('.//p[@class="content__list--item--des"]/a[2]/text()').get()
            item['community'] = quote.css('.content__list--item--des > a:nth-of-type(3)::attr(title)').get()

            area = quote.xpath('.//p[@class="content__list--item--des"]').get()
            area = re.search('<p class="content__list--item--des">(.*?)</p>', area, re.S).group(1)
            content = re.match('.*?<a target="_blank" href="/zufang/.*?<i>/</i>(.*?)<i>/</i>(.*?)<i>/</i>(.*?)'
                               '<span class="hide">.*?<i>/</i>(.*?)</span>', area, re.S)
            area = content.group(1).strip('\n').strip(' ').strip('\n')
            item['area'] = area
            item['toward'] = content.group(2).strip(' ')
            type1 = content.group(3).strip('\n').strip(' ')
            type2 = content.group(4).strip('\n').strip(' ').strip('\n').replace(' ', '')
            item['type'] = type1 + ' ' + type2

            rent_num = quote.xpath('./span[@class="content__list--item-price"]/em/text()').get()
            rent_units = quote.xpath('./span[@class="content__list--item-price"]/text()').get().strip(' ')
            rent = rent_num + rent_units
            item['rent'] = rent

            item['time'] = quote.css('.content__list--item--brand .content__list--item--time::text').get()
            # print(item)
            # lst.append(item)
            yield item
