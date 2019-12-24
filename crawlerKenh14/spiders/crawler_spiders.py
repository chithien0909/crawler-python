from scrapy import Spider
from scrapy.selector import Selector
from crawlerKenh14.items import Crawlerkenh14Item

class CrawlerSpider(Spider):
  name = 'crawlerKenh14'
  allowed_domains = ["kenh14.vn"]
  start_urls = [
    "http://kenh14.vn"
  ]
  
  def parse(self, response):
    links = [
      '//div[@data-marked-zoneid="kenh14_home_bs1"]/li',
      '//div[@data-marked-zoneid="kenh14_home_bs2"]/li',
      '//div[@data-marked-zoneid="kenh14_home_bs3"]/li',
    ]
    for link in links:
      posts = Selector(response).xpath(link)
      for post in posts:
        item = Crawlerkenh14Item()
        item['title'] = post.xpath('div/h3//@title').extract()
        item['categories'] = post.xpath('div/div/a/text()').extract()

        item['time'] = post.xpath('div/div/span/@title').extract()
        item['image_url'] = post.xpath('div/a/@style').extract()
        item['description'] = post.xpath('div/span/text()').extract()
        yield item