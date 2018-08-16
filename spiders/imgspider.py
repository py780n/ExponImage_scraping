from ExpoCrawler.items import ExponeaImages
import scrapy


class ImageSpider(scrapy.Spider):
    name ="exponeaImage"
    start_urls = ["https://exponea.com/"] 

    def parse(self,response):
        urls = response.css('img').xpath('@src').re('https://.*') #will collect the source location
        for url in urls:
            yield scrapy.Request(url,self.parse_image)
     
        page_urls = response.css("a").xpath('@href').re("https://exponea.com/.*")
        for page_url in page_urls:
            yield scrapy.Request(page_url,self.parse)
    
    def parse_image(self,response):
        yield ExponeaImages(image_urls=[response.url])