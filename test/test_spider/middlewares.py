# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64
from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from test_spider.ip_pool import get_kdl_ip

ip, _ = get_kdl_ip()
# 快代理账号密码
kdl_admin = 'chuichui1901'
kdl_pass = 'vplygo03'
# 换ip阈值
threshold = 3
# 此ip异常次数
fail_time = 0


class TestSpiderMiddleware(object):
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
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
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


class TestSpiderDownloaderMiddleware(object):
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
        proxy_url = 'http://%s:%s@%s' % (kdl_admin, kdl_pass, ip)
        request.meta['proxy'] = proxy_url  # 设置代理
        spider.logger.debug("using proxy: {}".format(request.meta['proxy']))
        # 设置代理身份认证
        # Python3 写法
        auth = "Basic %s" % (base64.b64encode(('%s:%s' % (kdl_admin, kdl_pass)).encode('utf-8'))).decode('utf-8')
        # Python2 写法
        # auth = "Basic " + base64.b64encode('%s:%s' % (username, password))
        request.headers['Proxy-Authorization'] = auth

    def process_response(self, request, response, spider):
        global fail_time, ip, threshold
        if not (200 <= response.status < 300):
            fail_time += 1
            if fail_time >= threshold:
                proxy = get_kdl_ip()
                fail_time = 0
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


class AgentMiddleware(UserAgentMiddleware):
    """
        User-Agent中间件, 设置User-Agent
    """

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'
        request.headers.setdefault('User-Agent', ua)
