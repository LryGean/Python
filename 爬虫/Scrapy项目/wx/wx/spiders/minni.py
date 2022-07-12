import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MinniSpider(CrawlSpider):
    name = 'minni'
    allowed_domains = ['www.wxapp-union.com']
    start_urls = ['https://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    headers = [
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'},
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'},
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'},
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Safari/537.36'}
    ]

    rules = (
        # 规则
        # 翻页
        # follow=False:关闭重复爬去
        Rule(LinkExtractor(allow=r'https://www.wxapp-union.com/portal.php\?mod=list&catid=2&page=\d+'),
             callback='parse_item1', follow=False),
        # [1, 10]:1-10次
        # Rule(LinkExtractor(allow=r'https://www.wxapp-union.com/portal.php\?mod=list&catid=2&page=\d[1,10]'),
        #      callback='parse_item1', follow=False),
        # 文章链接
        Rule(LinkExtractor(allow=r'http://www.wxapp-union.com/article-\d+-1.html'), callback='parse_item', follow=True),
    )

    def parse_item1(self, response):
        print(response.url)

    def parse_item(self, response):
        print(response.text)

        name = response.xpath('//div[@class="c1"]/h1/text()').get()
        print(name)
