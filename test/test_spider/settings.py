# -*- coding: utf-8 -*-

BOT_NAME = 'test_spider'

SPIDER_MODULES = ['test_spider.spiders']
NEWSPIDER_MODULE = 'test_spider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    # 下面对应我们自己编写的ProxyMiddleware, 其后数字越小表示优先级越高，越先执行
    "test_spider.middlewares.TestSpiderDownloaderMiddleware": 110,
    "test_spider.middlewares.AgentMiddleware": 2,
}