# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
import time


class SeleniumDownloadMiddleware(object):
    # chromedriver插件路径
    path = r"G:\developer-tool\ChromeDriver\chromedriver"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.path)

    def process_request(self, request, spider):
        self.driver.get(request.url)

        time.sleep(1)

        source = self.driver.page_source

        # 封装response对象并返回
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return response
