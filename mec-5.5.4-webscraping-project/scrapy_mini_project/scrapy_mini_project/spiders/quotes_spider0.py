import scrapy

# This is the first class.  this class just get the page and don't parse it.
# Run this class from command line
#   scrapy crawl quotes0
#
class QuotesSpider0(scrapy.Spider):
    name = "quotes0"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


#  This should get the 2 HTML pages in the current directory as quotes-1.html and quotes-2.html