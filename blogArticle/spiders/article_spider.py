# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from blogArticle.items import BlogArticleItem


class ArticleSpiderSpider(CrawlSpider):
    name = 'article_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/p/61b9ef649461']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 文章的标题  a_title
        title = response.xpath("//h1[@class='_1RuRku']/text()").get()

        # 文章分类  对应item里面a_category
        category = 'Python'

        # 文章的发布时间 对应item里面的a_release_time  ajax请求的数据，，
        release_time = response.xpath("//div[@class='s-dsoj']/time/text()").get().replace(".", '-')

        # 文章的观看人数 对应item里面的a_watch_number   ajax请求的数据
        read_number = response.xpath("//div[@class='s-dsoj']/span[last()]/text()").get()
        read_number = int(read_number.split(" ")[1].replace(",", ''))  # 阅读 5,648 --> 5648 转成int

        # 文章的类容 对应item里面的a_content ajax请求的数据，
        content = "".join(response.xpath("//article[@class='_2rhmJa']").getall())

        # 源地址 对应item里面的 a_origin
        origin = response.url.split("?")[0]

        # 文章的简介  对应item里面a_introduce
        introduce = response.xpath("//article[@class='_2rhmJa']/blockquote/p/text()").get()
        if not introduce:
            # 为空默认从文章中摘取一段
            introduce = response.xpath("//article[@class='_2rhmJa']/p[5]/text()").get()

        # 文章简介图片 对应item里面a_introduce_img
        introduce_img = response.xpath("//article[@class='_2rhmJa']//img/@data-original-src").get()

        item = BlogArticleItem(
            a_title=title,
            a_category=category,
            a_release_time=release_time,
            a_read_number=read_number,
            a_content=content,
            a_origin=origin,
            a_introduce=introduce,
            a_introduce_img=introduce_img,
        )

        yield item
