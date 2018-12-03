# -*- coding: utf-8 -*-
import pymongo
from zhihuUser.settings import mongo_host, mongo_port, mongo_db_name, mongo_db_collection
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhihuuserPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        # update方法,第一个参数传入查询条件，这里用的是url_token，第二个参数传入字典类型的对象，就是item，
        # 第三个参数传入True，如果查询数据存在的话就更新，不存在的话就插入。这样就可以保证去重
        self.post.update({'url_token': item['url_token']}, {'$set': data}, True)
        return item
