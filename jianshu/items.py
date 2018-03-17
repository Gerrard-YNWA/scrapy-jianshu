# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    article_abstract = scrapy.Field()
    article_link = scrapy.Field()
    author = scrapy.Field()
    author_link = scrapy.Field()
    post_time = scrapy.Field()
    category = scrapy.Field()
    views = scrapy.Field()
    comments = scrapy.Field()
    like = scrapy.Field()
    reward = scrapy.Field()
