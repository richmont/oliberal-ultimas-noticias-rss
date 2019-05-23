# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import json
#from xml.etree.ElementTree import Element, SubElement, Comment
#from ElementTree_pretty import prettify
from lxml import etree as ET
base_url = 'https://www.oliberal.com'
root = ET.Element('rss',version="2.0" )
# define as tags para criar o XML
channel = ET.SubElement(root,'channel')
title = ET.SubElement(channel,'title')
link = ET.SubElement(channel,'link')
description = ET.SubElement(channel,'description')
language = ET.SubElement(channel,'language')
link = ET.SubElement(channel,'link')
atom = ET.SubElement(channel,'atom', href='https://www.oliberal.com', type='application/rss+xml')

title.text = 'O Liberal'
link.text = base_url
description.text = 'O Liberal é um jornal brasileiro que circula em Belém e maior parte do Pará desde o ano de 1946'
language.text = 'pt-BR'


# image
image = ET.SubElement(channel,'image')
url = ET.SubElement(image,'title')
title = ET.SubElement(image,'title')
link = ET.SubElement(image,'link')
width = ET.SubElement(image,'width')
heigh = ET.SubElement(image,'heigh')

url.text = 'https://www.oliberal.com/img/ol-logo.png'
title.text = 'O Liberal'
link = base_url
width.text = '144'
heigh.text = '144'


# template da notícia em si, item
item = ET.SubElement(channel,'item')
title = ET.SubElement(item,'title')
link = ET.SubElement(item,'link')
description = ET.SubElement(item,'description')
media = ET.SubElement(item,'media')
#category = ET.SubElement(item,'category')
pubDate = ET.SubElement(item,'pubDate')




class LiberalPipeline(object):
    def open_spider(self, spider):
        pass
    def close_spider(self, spider):
        tree = ET.ElementTree(root)
        tree.write('liberal.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")


    def process_item(self, item, spider):
        # preencher
        title.text = item['title']
        link.text = item['link']
        description.text = '<img src="'+  base_url + item['imagem_url']  + '" /><br />' + item['texto']
        pubDate.text = item['data_pub']

        return item
