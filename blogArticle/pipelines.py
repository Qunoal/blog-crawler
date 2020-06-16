# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi


class BlogArticlePipeline(object):

    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'a_project_blog',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor,
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)

    def process_item(self, item, spider):
        # 插入数据(异步：高效率)
        deferred = self.dbpool.runInteraction(self.insert_item, item)

        # 错误处理的函数
        deferred.addErrback(self.insert_error, item)

    # 插入数据的函数
    def insert_item(self, cursor, item):
        print("*" * 20 + "成功添加了一条数据" + "*" * 20)
        sql = "insert into article(" \
              "a_title," \
              "a_category," \
              "a_release_time," \
              "a_read_number," \
              "a_content," \
              "a_origin," \
              "a_introduce," \
              "a_introduce_img) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(sql, (
            item['a_title'],
            item['a_category'],
            item['a_release_time'],
            item['a_read_number'],
            item['a_content'],
            item['a_origin'],
            item['a_introduce'],
            item['a_introduce_img'],
        ))

    # 发送错误，执行的方法
    def insert_error(self, item, spider):
        print('=' * 90)
        # 把出错的源地址输出
        print(item['a_origin'])
        print(item)
        print('=' * 90)
        pass
