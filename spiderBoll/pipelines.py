# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl

class SpiderbollPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.worksheet = self.wb.active
        self.worksheet.title = '双色球汇总'
        self.worksheet.append(['期号', '红球', '蓝球'])

    def close_spider(self, spider):
        self.wb.save('双色球汇总.xlsx')

    def process_item(self, item, spider):
        code = item['code'] or ''
        red = item['red'] or ''
        blue = item['blue'] or ''
        self.worksheet.append([code, red, blue])
        return item
