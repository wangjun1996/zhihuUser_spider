from scrapy import cmdline

# cmdline.execute('scrapy crawl zhihu_spider'.split())
cmdline.execute('scrapy crawl zhihu_spider -o zhihuUser.csv'.split())