import scrapy


class AmznbookSpider(scrapy.Spider):
    name = 'amznbook'
    allowed_domains = []
    page_number = 2
    start_urls = [
        'https://www.amazon.in/s?k=books&page=1'
        ]

    def parse(self, response):
        book_title = response.css(".a-size-medium::text").get()
        book_author = response.css(".a-color-secondary .a-row .a-size-base+ .a-size-base::text").get()
        book_rating = response.css(".a-spacing-top-small .aok-align-bottom").css('::text').get()
        book_price = response.css(".a-spacing-top-small .s-price-instructions-style .a-price-whole").css('::text').get()

        yield{'Title':book_title, 'Author':book_author, 'Rating':book_rating, 'Price':book_price}

        next_page = 'https://www.amazon.in/s?k=books&page=' + str(AmznbookSpider.page_number) + '&qid=1657606851'
        if AmznbookSpider.page_number <= 20:
            AmznbookSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)


