import scrapy
import codecs
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CrawlerSpider.items import CrawlerspiderItem

class BookcrawlSpider(CrawlSpider):
    name = 'BookCrawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow=('catalogue/page'), callback='parsepage', follow=True),
    )
    def parsepage(self, response):
        B = CrawlerspiderItem()
        for book in response.css('article.product_pod '):
            B['name'] = book.css('h3 a').xpath('@title').get()
            B['price'] = book.css('p.price_color::text').get()
            B['picture']= book.css('div.image_container img').xpath('@src').get()
            yield B