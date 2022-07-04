# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 中间件
import random

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MiddlewaredemoSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """
        当 response 经过爬虫中间件时，调用该方法
        :param response:
        :param spider:
        :return:
        """
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        """

        :param response:
        :param result:
        :param spider:
        :return:
        """
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):

        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MiddlewaredemoDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        对Request进行处理
        :param request:  要被处理Request请求对象
        :param spider:   Request对应的爬虫对象
        :return:
        """

        # Called for each request that goes through the downloader
        # middleware.

        # Must either:

        # 当返回为None：scrapy继续处理请求，交给后面的人处理
        # - return None: continue processing this request

        # 当返回 Response 对象
        # - or return a Response object

        # 当返回 Request 对象
        # - or return a Request object

        # 当返回 IgnoreRequest 异常
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        """
        处理response响应方法
        :param request:
        :param response:
        :param spider:
        :return:
        """
        # Called with the response returned from the downloader.

        # Must either;

        # 更靠近下载器的中间件先处理
        # - return a Response object

        # 最靠近下载器的会将请求提交给调度器队列李
        # - return a Request object

        # 当返回 IgnoreRequest 异常， 处理异常
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 随机UA下载器中间件
class RandonUserAgentMiddleware:
    def __init__(self):
        self.user_agent = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'
        ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent)


# 修改状态码下载器中间件
class ChangeResponseMiddleware:
    def process_response(self, request, response, spider):
        response.status = 201
        return response


# 添加额外参数爬虫中间件
class NameMiddleware:
    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            url = r.url
            url += '&name=LinFei'
            request = r.replace(url=url)
            yield request


# 筛选响应
class HttpStatusMiddleware:
    def process_spider_input(self, response, spider):
        if response == 200:
            return response
        else:
            print('单独处理')
