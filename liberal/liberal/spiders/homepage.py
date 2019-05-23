# -*- coding: utf-8 -*-
import scrapy
from liberal.items import LiberalItem
import sys

class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    allowed_domains = ['www.oliberal.com']
    start_urls = ['https://www.oliberal.com/']

    # coleta os links de notícias na página principal
    def parse(self, response):
        for item in response.css("div.item"):
            link    = item.css('p.titulo a::attr(href)').extract_first()
            yield response.follow(link,self.parse_artigo)

    # é executado para cada link coletado na página principal
    def parse_artigo(self,response):
        link = response.url
        title =  response.css("h1.title::text").extract_first()
        author = response.css("div.author::text").extract_first()
        imagem_url = response.css('div.fullwidth img::attr(src)').extract_first()
        img_sub = response.css("span.image-byline::text").extract_first()
        data_pub = response.css("time.publishing-date::text").extract_first()
        texto = response.css("div.textbody p::text").extract()
        texto = "".join(texto)
        # armazena tudo que foi coletado em um item do tipo "notícia"
        notice = LiberalItem(title=title,link=link,author=author,imagem_url=imagem_url,img_sub=img_sub,texto=texto,data_pub=data_pub)
        # retorna o item ao scrapper
        yield notice