# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from xml.etree.ElementTree import Element, SubElement, Comment
from ElementTree_pretty import prettify

class LiberalPipeline(object):
    def open_spider(self, spider):
      self.file = open('liberal.xml', 'w')

    def close_spider(self, spider):
      self.file.close()

    def process_item(self, item, spider):
        #line = json.dumps(dict(item)) + "\n"
        #self.file.write(line)
        
        return item
