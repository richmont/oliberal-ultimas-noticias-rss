# -*- coding: utf-8 -*-
import scrapy
from liberal.items import LiberalItem

class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    allowed_domains = ['www.oliberal.com']
    start_urls = ['https://www.oliberal.com/']

    def parse(self, response):
        for item in response.css("div.item"):
            link    = item.css('p.titulo a::attr(href)').extract_first()
            title   = item.css('p.titulo a::attr(title)').extract_first()
            head    = item.css('p.chapeu::text').extract_first()
            noticia = LiberalItem(title=title, head=head, link=link)
            print(noticia['title'])
            yield noticia
