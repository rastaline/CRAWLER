# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerspiderItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
    picture = scrapy.Field()