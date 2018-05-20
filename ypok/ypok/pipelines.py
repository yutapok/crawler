# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from logging import getLogger, FileHandler

class YpokPipeline(object):

    def __init__(self, settings):
        self.logger = self.set_logger(settings)

    def set_logger(self, settings):
        logger = getLogger(__name__)
        fh = FileHandler(settings['SCRAPED_LOG_PATH'])
        logger.addHandler(fh)
        return logger

    def _check_filepath(self, file_name):
        if not os.path.isfile(file_name):
            with open(fine_name, 'w') as f:
                f.write('')

    def process_item(self, item, spider):
        if not item['FLAG'] == 0:
            return "Not found new rss information"
        
        for t, l, p in zip(item['TITLE'], item['LINK'], item['PUBDATE']):
            self.logger.debug('{0}{1}{2}'.format(item['DOMAIN'], t, l, p))
        spider.server.hset("pubdate", item['DOMAIN'], item['LATEST'])
        return None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
