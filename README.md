# ExponImage_scraping
#The following changes should be made in your settings.py .

#settings.py
#============

ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
}

#Note:Configure the location were you expect the images to be stored 
IMAGES_STORE='<your_project_location>\\ExpoCrawler\\ExpoCrawler\\output'

#To The maximum number of concurrent requests (improve the speed of the crawler)
CONCURRENT_REQUESTS_PER_IP = 100
