# -*- coding: utf-8 -*-
import json
from scrapy import Spider, Request
from zhihuUser.items import ZhihuuserItem


class ZhihuSpiderSpider(Spider):
    name = 'zhihu_spider'
    allowed_domains = ['www.zhihu.com']
    # 该用户的关注列表中的某个用户详细信息
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    # 该用户的关注列表
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?' \
                  'include={include}&offset={offset}&limit={limit}'
    # 该用户的粉丝列表
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}' \
                    '&limit={limit}'

    start_user = 'excited-vczh'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,' \
                 'following_count,following_topic_count,following_question_count,following_favlists_count,' \
                 'following_columns_count,answer_count,articles_count,pins_count,question_count,' \
                 'favorite_count,favorited_count,logs_count,marked_answers_count,' \
                 'marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,' \
                 'sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,' \
                 'thanked_count,' \
                 'description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,' \
                 'org_homepage,badge[?(type=best_answerer)].topics'
    # user_query = 'allow_message, is_followed, is_following, is_org, is_blocking, employments, answer_count,' \
    #              'follower_count, articles_count, gender, badge[?(type = best_answerer)].topics'

    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed' \
                    ',is_following,badge[?(type=best_answerer)].topics'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed' \
                      ',is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20),
                      self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20),
                      self.parse_followers)

    # 解析方法
    # 处理用户基本信息
    def parse_user(self, response):
        # print(response.text)
        # 在解析方法里面我们解析得到的 response 内容，然后转为 json 对象，然后依次判断字段是否存在，最后赋值
        result = json.loads(response.text)
        item = ZhihuuserItem()

        for field in item.fields:
            if field in result.keys():
                if field == 'locations' and len(result.get(field)) > 0:
                    item['locations'] = result.get(field)[0]['name']
                    continue
                if field == 'badge' and len(result.get(field)) > 0:
                    item['badge'] = result.get(field)[0].get('description')
                    continue
                if field == 'educations' and len(result.get(field)) > 0:
                    item['educations'] = result.get(field)[0]['school']['name']
                    continue
                if field == 'business':
                    item['business'] = result.get(field).get('name')
                    continue
                if field == 'employments' and len(result.get(field)) > 0:
                    item['employments'] = result.get(field)[0]['company']['name']
                    item['job'] = result.get(field)[0]['job']['name']
                    continue
                item[field] = result.get(field)
        yield item
        # 接下来还需要在这里获取这个用户的关注列表，所以需要再重新发起一个获取关注列表的 request
        yield Request(self.follows_url.format(user=result.get('url_token'), include=self.follows_query, offset=0, limit=20),
                      self.parse_follows)
        # 接下来还需要在这里获取这个用户的粉丝列表，所以需要再重新发起一个获取粉丝列表的 request
        yield Request(self.followers_url.format(user=result.get('url_token'), include=self.followers_query,
                                                limit=20, offset=0), self.parse_followers)

    # 处理关注列表
    def parse_follows(self, response):
        print("================parse_follows==================")
        # print(response.text)
        results = json.loads(response.text)
        # print("results:", results)
        if 'data' in results.keys():
            for result in results.get('data'):
                # 通过关注列表的每一个用户，对每一个用户发起请求，获取其详细信息。
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        # 处理分页，判断 paging 内容，获取下一页关注列表。
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            print("follows_next_page:", next_page)
            yield Request(next_page, self.parse_follows)

    # 处理粉丝列表
    def parse_followers(self, response):
        print("================parse_followers==================")
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            print("followers_next_page:", next_page)
            yield Request(next_page, self.parse_followers)
