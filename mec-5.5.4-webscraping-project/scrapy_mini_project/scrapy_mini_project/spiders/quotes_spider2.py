import scrapy

# This is the third class from the tutorial.
# Run this class from command line
#   scrapy crawl quotes2
#
# Until now, it doesn't extract any data in
# particular, just saves the whole HTML page to a local file. Let's integrate the
# extraction logic above into our spider.
# A Scrapy spider typically generates many dictionaries containing the data
# extracted from the page. To do that, we use the ``yield`` Python keyword
# in the callback, as you can see below::


class QuotesSpider2(scrapy.Spider):
    name = "quotes2"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
