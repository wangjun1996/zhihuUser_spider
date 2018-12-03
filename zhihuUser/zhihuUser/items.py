# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ZhihuuserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 用户名
    name = Field()
    # 标题
    headline = Field()
    # 个人简介
    description = Field()
    # 个人主页url
    url = Field()
    # 用来制作url的用户名参数
    url_token = Field()
    # 性别。“1”表示男，“0”表示女
    gender = Field()
    # 个人成就
    badge = Field()

    # 居住地
    locations = Field()
    # 教育经历
    educations = Field()
    # 所在行业
    business = Field()
    # 公司
    employments = Field()
    # 工作岗位
    job = Field()

    # 回答数
    answer_count = Field()
    # 文章数
    articles_count = Field()
    # 收藏数
    favorite_count = Field()
    # 被收藏数
    favorited_count = Field()
    # 粉丝数
    follower_count = Field()
    # 关注的专栏数
    following_columns_count = Field()
    # 该用户关注了多少人
    following_count = Field()
    # 想法数
    pins_count = Field()
    # 提问数
    question_count = Field()
    # 获得感谢数
    thanked_count = Field()
    # 获赞数
    voteup_count = Field()
    # 关注的收藏夹数
    following_favlists_count = Field()
    # 关注的问题数
    following_question_count = Field()
    # 关注的话题数
    following_topic_count = Field()
    # 知乎收录的回答数
    marked_answers_count = Field()
    # # 举办的Live数
    # hosted_live_count = Field()
    # # 赞助的Live数
    # participated_live_count = Field()


