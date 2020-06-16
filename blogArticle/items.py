# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogArticleItem(scrapy.Item):
    # 文章标题
    a_title = scrapy.Field()

    # 文章分类
    a_category = scrapy.Field()

    # 文章的发布时间
    a_release_time = scrapy.Field()

    # 文章的阅读量
    a_read_number = scrapy.Field()

    # 文章的类容
    a_content = scrapy.Field()

    # 源地址
    a_origin = scrapy.Field()

    # 文章的简介
    a_introduce = scrapy.Field()

    # 文章简介图片
    a_introduce_img = scrapy.Field()


