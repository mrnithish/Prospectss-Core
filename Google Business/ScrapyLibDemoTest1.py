import scrapy


class FirstSpider(scrapy.Spider):
    name = "first"

    def __init__(self, group=None, *args, **kwargs):
        super(FirstSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["https://www.google.com/maps/search/grocery+store/@11.0938415,77.0218907,15z/data=!3m1!4b1"]
