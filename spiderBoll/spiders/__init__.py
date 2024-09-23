# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapy.http import HtmlResponse

from spiderBoll.items import SpiderbollItem


class BollSpider(scrapy.Spider):
    name = 'spiderBoll'
    index = 1
    origin_url = "https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=&dayEnd=&pageNo=%s&pageSize=30&week=&systemType=PC"

    def start_requests(self):
        from_url = "https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=&dayEnd=&pageNo=1&pageSize=30&week=&systemType=PC"
        yield scrapy.Request(url=from_url, callback=self.parse, dont_filter=True)
        pass

    def parse(self, response: HtmlResponse, **kwargs):
        sel = response.json()
        # 解析返回的JSON数据
        for i in sel['result']:
            tw = SpiderbollItem()
            tw['code'] = i['code']
            tw['red'] = i['red']
            tw['blue'] = i['blue']
            yield tw
        self.index = self.index + 1
        url = self.origin_url % self.index
        if len(sel['result']) < 30:
            pass
        else:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
