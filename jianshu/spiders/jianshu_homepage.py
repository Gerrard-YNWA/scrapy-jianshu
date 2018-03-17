#!/bin/python
#-*-coding:utf8-*-

import scrapy
import urllib
from jianshu.items import JianshuItem


class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    allowed_domains=['www.jianshu.com']
    start_urls = [
        "https://www.jianshu.com"
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3067.6 Safari/537.36",
        "Accept": "text/html, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://www.jianshu.com/",
        "X-INFINITESCROLL": "true",
        "X-Requested-With": "XMLHttpRequest"
    }
    note_id_list = []
    page = 1

    def parse(self, response):
        if self.page == 1:
            articles = response.selector.xpath('//ul[@class="note-list"]/li')
        else:
            articles = response.selector.xpath('//li[@class="have-img"]')

        for article in articles:
            note_id = article.xpath('@data-note-id').extract()
            if len(note_id) > 0:
                self.note_id_list.append(note_id[0])
                
            title = article.xpath('div/a[@class="title"]/text()').extract()
            article_abstract = article.xpath('div/p[@class="abstract"]/text()').extract()
            article_link = article.xpath('div/a[@class="title"]/@href').extract()
            author = article.xpath('div/div/div/a[@class="nickname"]/text()').extract()
            author_link = article.xpath('div/div/div/a[@class="nickname"]/@href').extract()
            post_time = article.xpath('div/div/div/span/@data-shared-at').extract()
            category = article.xpath('div/div/a[@class="collection-tag"]/text()').extract()
            meta_a = article.xpath('div/div/a/text()').re(r' ([0-9]*)\n')
            meta_span = article.xpath('div/div/span/text()').re(r' ([0-9]*)')
            item = JianshuItem()
            item['title'] = title[0]
            item['article_abstract'] = article_abstract[0]
            item['article_link'] = article_link[0]
            item['author'] = author[0]
            item['author_link'] = author_link[0]
            item['post_time'] = post_time[0]
            item['category'] = ''
            item['views'] = int(meta_a[0])
            item['comments'] = int(meta_a[1])
            item['like'] = int(meta_span[0])
            item['reward'] = 0
            if len(category) > 0:
                item['category'] = category[0]
            if len(meta_span) > 1:
                item['reward'] = int(meta_span[1])
            yield item

        #最多加载15页
        if self.page < 15:
            self.page = self.page + 1
            params = urllib.urlencode({"page": self.page, "seen_snote_ids[]": self.note_id_list}, True)
            yield scrapy.Request("https://www.jianshu.com/?%s" % params, headers=self.headers,
                                 callback=self.parse)
