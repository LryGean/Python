# 8.(必做题2)目标网站：http://www.bbsnet.com/doutu 需求： 1、用scrapy框架把"斗图"专题的所有表情包下载到images文件夹里面；
# 2、将scrapy项目和images文件夹安装指定格式提交至指定邮箱(邮箱不能直接发送文件夹，可以压缩之后添加至附件)。
import random
import scrapy

from DouTu.items import DoutuItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.bbsnet.com']
    start_urls = ['http://www.bbsnet.com/']

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
    page = 1

    def parse(self, response):
        lis = response.xpath('//div[@class="mainleft"]/ul/li')
        print(f'获取：{len(lis)}')
        for li in lis:
            item = DoutuItem()
            img_url = li.xpath('.//img/@src').extract_first()
            item['img_url'] = img_url
            img_name = '_' + li.xpath('.//div[@class="article"]/h2/a/text()').extract_first()
            img_name = img_name.replace('[', '').replace(']', '').replace(' ', '').replace('?', '')
            item['img_name'] = img_name
            yield item
        self.page += 1
        if self.page <= 9:
            next_url = response.xpath('//a[@class="next"]/@href').get()
            url = response.urljoin(next_url)
            yield scrapy.Request(url=url, callback=self.parse, headers=random.choice(self.headers))
