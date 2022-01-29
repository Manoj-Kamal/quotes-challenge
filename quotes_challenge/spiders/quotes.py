import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # Splash Lua script
    script = '''
            function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(2))
            return {
                html = splash:html(),
            }
            end
    '''
    def start_requests(self):

        yield SplashRequest(url='http://quotes.toscrape.com/js/', endpoint='execute',
                            args={
                                'wait': 0.5,
                                'timeout': 90,
                                'lua_source': self.script
                            }, callback=self.parse)

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):

            quotes = quote.xpath('span[@class="text"]/text()').extract_first()

            author = quote.xpath('span/small[@class="author"]/text()').extract_first()

            tags = quote.xpath('div[@class="tags"]/a[@class="tag"]/text()').extract()

            yield {
                'Quote': quotes,
                'Author': author,
                'Tags': tags,
            }

        # This function is to navigate to the next page
        next_page = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            yield SplashRequest(response.urljoin(next_page))
