# -*- coding: utf-8 -*-

import scrapy


class LiberalItem(scrapy.Item):

    title = scrapy.Field() # título da notícia
    author = scrapy.Field() # autor
    link = scrapy.Field() # link que leva a notícia
    texto = scrapy.Field() # conteúdo
    imagem_url = scrapy.Field() # endereço sem domínio da imagem exibida na notícia
    img_sub = scrapy.Field() # legenda da imagem
    data_pub = scrapy.Field() # data de publicação da notícia
