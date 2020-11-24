import scrapy
import codecs
from CrawlerSpider.items import CrawlerspiderItem

class BookSpider(scrapy.Spider):
    name = 'Book'
    allowed_domains = ['http://books.toscrape.com/']
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        B = CrawlerspiderItem()
        for book in response.css('article.product_pod '):
            B['name'] = book.css('h3 a').xpath('@title').get()
            B['price'] = book.css('p.price_color::text').get()
            B['picture']= book.css('div.image_container img').xpath('@src').get()
            next_page = response.css('li.next a::attr("href")').get()
            if next_page is not None:
                yield response.follow(next_page, self.parse)
            else:
                yield B