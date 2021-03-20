import scrapy

# This is the final class from the tutorial for submit.
# Run this class from command line
#   scrapy crawl quotes
#
# You can provide command line arguments to your spiders by using the ``-a``
# option when running them::
#
#     scrapy crawl toscrape-xpath -o xpath-scraper-results.json
#


class ToScrapeXpathSpider(scrapy.Spider):
    name = "toscrape-xpath"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').get(),
                'author': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall(),
            }

