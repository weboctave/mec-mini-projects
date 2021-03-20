import scrapy

# This is the second class from the tutorial.  This class just get the page and don't parse it.
# shortcut to the start_requests method
# Run this class from command line
#   scrapy crawl quotes1
#
# Instead of implementing a :meth:`~scrapy.spiders.Spider.start_requests` method
# that generates :class:`scrapy.Request <scrapy.http.Request>` objects from URLs,
# you can just define a :attr:`~scrapy.spiders.Spider.start_urls` class attribute
# with a list of URLs. This list will then be used by the default implementation
# of :meth:`~scrapy.spiders.Spider.start_requests` to create the initial requests
# for your spider::
class QuotesSpider1(scrapy.Spider):
    name = "quotes1"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)


#  This should get the 2 HTML pages in the current directory as quotes-1.html and quotes-2.html