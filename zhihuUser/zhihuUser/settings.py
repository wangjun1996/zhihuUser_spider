# -*- coding: utf-8 -*-

# Scrapy settings for zhihuUser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuUser'

SPIDER_MODULES = ['zhihuUser.spiders']
NEWSPIDER_MODULE = 'zhihuUser.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihuUser (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)'
USER_AGENT = 'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                 'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuUser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'zhihuUser.middlewares.ZhihuuserDownloaderMiddleware': 543,
    'zhihuUser.middlewares.my_useragent': 544,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihuUser.pipelines.ZhihuuserPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


mongo_host = 'localhost'
mongo_port = 27017
mongo_db_name = 'spider'
mongo_db_collection = 'zhihu_user'


# 使输出的csv文件按照设定好的标题顺序输出，这里假设你的project名字为zhihuUser
FEED_EXPORTERS = {
    'csv': 'zhihuUser.spiders.itemCsvExporter.itemcsvexporter',
}

FIELDS_TO_EXPORT = [
    'name',
    'headline',
    'description',
    'url',
    'url_token',
    'gender',
    'badge',

    'locations',
    'educations',
    'employments',
    'business',
    'job',

    'answer_count',
    'articles_count',
    'favorite_count',
    'favorited_count',
    'follower_count',
    'following_columns_count',
    'following_count',
    'pins_count',
    'question_count',
    'thanked_count',
    'voteup_count',
    'following_favlists_count',
    'following_question_count',
    'following_topic_count',
    'marked_answers_count',
    # 'hosted_live_count',
    # 'participated_live_count',
]