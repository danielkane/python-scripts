from scrapy.spider import BaseSpider
from sc_craigslist.spiders.urls import url_list
from scrapy.http import Request
from scrapy.selector import Selector
#from sc_craigslist.items import Jobs


class ClSpider(BaseSpider):
    name = "ClSpider"
    allowed_domains = ["craigslist.org"]
    start_urls = url_list

    def parse(self, response):
        sel = Selector(response)
        for url in sel.xpath('//a/@href').extract():
            if "jjj" in url:
                yield Request(url, callback=self.parse)
