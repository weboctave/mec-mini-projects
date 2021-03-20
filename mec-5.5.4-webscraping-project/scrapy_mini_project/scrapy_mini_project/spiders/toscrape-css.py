import scrapy

# This is the final class from the tutorial for submit.
# Run this class from command line
#   scrapy crawl quotes
#
# You can provide command line arguments to your spiders by using the ``-a``
# option when running them::
#
#     scrapy crawl toscrape-css -o css-scraper-results.json
#     scrapy crawl toscrape-css -o css-scraper-results.json -a tag=humor
#


class ToScrapeCssSpider(scrapy.Spider):
    name = "toscrape-css"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
