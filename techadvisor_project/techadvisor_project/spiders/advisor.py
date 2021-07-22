import scrapy


class TechadvisorSpider(scrapy.Spider):
    name = 'advisor'
    start_urls = ['https://www.techadvisor.com/review/tp-link-deco-x60-3806803/']

    def parse(self, response):
        for item in response.xpath("//*/div[@class='content-area']"):
            path = item.xpath("//header/h1/text()").get()
            like = path.replace('review', '')
            yield{
                'title' : like ,

            }
        

