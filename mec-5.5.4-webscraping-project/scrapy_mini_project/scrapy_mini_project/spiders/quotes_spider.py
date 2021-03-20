import scrapy

# This is the sixth class from the tutorial.
# Run this class from command line
#   scrapy crawl quotes
#
# You can provide command line arguments to your spiders by using the ``-a``
# option when running them::
#
#     scrapy crawl quotes -o quotes-humor.json -a tag=humor
#
# These arguments are passed to the Spider's ``__init__`` method and become
# spider attributes by default.
#
# In this example, the value provided for the ``tag`` argument will be available
# via ``self.tag``. You can use this to make your spider fetch only quotes
# with a specific tag, building the URL based on the argument::


class QuotesSpider(scrapy.Spider):
    name = "quotes"

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
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
