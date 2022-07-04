import scrapy
import random


class SpiderSpider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['www.httpbin.com']
    # 或
    # allowed_domains = ['www.httpbin.org']
    # get:请求
    start_urls = ['https://www.httpbin.org/get']
    # start_urls = ['https://www.httpbin.org/post']

    # 定义本爬虫的相关配置
    # custom_settings = {'DEFAULT_REQUEST_HEADERS': {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    # }}

    headerds = [
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'},
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'},
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'},
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Safari/537.36'}
    ]

    cookies = {'name': 'LinFei'}
    data = {'age': '18'}

    # 重写请求
    def start_requests(self):
        num = 1
        # 构造请求(随机)
        yield scrapy.Request(url=self.start_urls[0],
                             callback=self.parse,
                             headers=random.choice(self.headerds),
                             cookies=self.cookies,
                             # 额外参数
                             cb_kwargs={'num': num})

        # yield scrapy.http.FormRequest(url=self.start_urls[0],
        #                               callback=self.parse,
        #                               formdata=self.data)

        # json携带参数
        yield scrapy.http.JsonRequest(url=self.start_urls[0],
                                      callback=self.parse,
                                      data=self.data)

    def parse(self, response, num):
        print(num)
        print(response.text)
        print(response.status)
        print(response.ip_address)
        print(response.headers)

        # response.urljoin()
        # response.follow_all()
        #
        # response.xpath()
        # response.css()

        print('----'*10)
