from urllib.parse import urlparse
from scrapy_redis.spiders import RedisSpider
from ypok.modules import common
from ypok.items import YpokItem

class YpokSpider(RedisSpider):
    name = 'ypok'
    item = None

    def __init__(self):
        self.server = RedisSpider.server
        self.item = YpokItem()

    def parse(self, response):
        response.selector.remove_namespaces()
        self.item['FLAG'] = 1
        self.item['DOMAIN'] = common.parse_domain(response.url)
        link_list = []
        title_list = []
        pubdate_list = response.xpath('//item/pubDate/text()').extract()
        if pubdate_list is not None:
            latest =  common.rfc2822_to_unix(pubdate_list[0])
        
        date_code = self._check_update(self.item['DOMAIN'] , latest)

        if date_code != -1:
            title_list= response.xpath('//item/title/text()').extract()
            link_list = response.xpath('//item/link/text()').extract()
            if date_code == 0:
                latest = 0

        if len(pubdate_list) == ( len(title_list) + len(link_list) + len(pubdate_list))/ 3:                
                result_pubdate = []
                result_title = []
                result_link = []

                generator = [[common.rfc2822_to_unix(p), t, l] for p, t, l in zip(pubdate_list, title_list, link_list) \
                                         if common.rfc2822_to_unix(p) > latest]
                for li in generator:
                    result_pubdate.append(li[0])
                    result_title.append(li[1])
                    result_link.append(li[2])

                self.item['PUBDATE'] = result_pubdate
                self.item['TITLE'] = result_title
                self.item['LINK'] = result_link
                self.item['FLAG'] = 0
                self.item['LATEST'] = result_pubdate[0]

        yield self.item


    def _check_update(self, domain, latest_date):
        store_date = self.server.hget("pubdate", domain)
        if not store_date:
            return 0

        store_date = int(store_date.decode('utf-8'))
        if latest_date > store_date:
            return 1
        else:
            return -1

