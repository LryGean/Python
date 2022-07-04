import scrapy

# post
class SpiderSpider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').get()
        timestamp = response.xpath('//input[@name="timestamp"]/@value').get()
        timestamp_secret = response.xpath('//input[@name="timestamp_secret"]/@value').get()

        data = {
            'commit': 'Sign in',
            'authenticity_token': authenticity_token,
            'login': 'LryGean',
            'password': 'lry981222@',
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'supported',
            'timestamp': timestamp,
            'timestamp_secret': timestamp_secret
        }

        # 携带表单数据post请求
        yield scrapy.FormRequest(
            url='https://github.com/session',
            formdata=data,
            callback=self.after_login
        )

    def after_login(self, response):
        with open('github.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

