import scrapy

# This is the fifth class from the tutorial.
# Run this class from command line
#   scrapy crawl quotes4
#
# A shortcut for creating Requests
# --------------------------------
#
# As a shortcut for creating Request objects you can use
# :meth:`response.follow <scrapy.http.TextResponse.follow>`::


class QuotesSpider4(scrapy.Spider):
    name = "quotes4"
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
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)
        # pass a selector to response.follow instead of string
        for href in response.css('ul.pager a::attr(href)'):
            yield response.follow(href, callback=self.parse)

        # For `` < a > `` elements there is a shortcut: ``response.follow`` uses their href attribute automatically.
        # So the code can be shortened further::
        for a in response.css('ul.pager a'):
            yield response.follow(a, callback=self.parse)

        # To create multiple requests from an iterable, you can use
        # :meth:`response.follow_all <scrapy.http.TextResponse.follow_all>` instead::
        anchors = response.css('ul.pager a')
        yield from response.follow_all(anchors, callback=self.parse)
