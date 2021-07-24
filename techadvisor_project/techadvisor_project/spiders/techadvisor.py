import scrapy


class TechadvisorSpider(scrapy.Spider):
    name = 'techadvisor'
    start_urls = ['https://www.techadvisor.com/review/']
    page = 2

    def parse(self, response):
        for link in response.xpath("//a[@class='thumb']/@href").getall():
            yield scrapy.Request(link, callback = self.categories)

            next_page = "https://www.techadvisor.com/review/?p=" + str(TechadvisorSpider.page)
            if TechadvisorSpider.page <= 202:
                TechadvisorSpider.page += 1
                yield scrapy.Request(next_page, callback = self.parse)
        
    def categories(self, response):
        for item in response.xpath("//*/div[@class='content-area']"):
            title = item.xpath("//header/h1/text()").get()
            path = title.replace('review', '')
            yield{
                'title' : path,
                'url' : response.url ,
                'image url' : item.xpath("//div//figure/img/@src").get(),
                'description' : item.xpath("//header/h3[1]/text()").get(),
                'verdict' : item.xpath("//div[@class='reviewVerdict__contents']/div/p/text()").get(),
                'pros' : item.xpath("//section[2]/ul[1]//li//text()").getall(),
                'cons' : item.xpath("//section[2]/ul[2]//li//text()").getall(),
                'price' : item.xpath("//*/div[@class='content-area']//span[@class='geo-price']/@data-price-us").get() 
            }

        
