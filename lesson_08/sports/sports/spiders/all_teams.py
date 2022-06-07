import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

class AllTeamsSpider(scrapy.Spider):
    name = 'all_teams'
    allowed_domains = ['scrape.world']
    start_urls = ['https://scrape.world/login']

    def parse(self, response):
        csrf_token = response.xpath("//input[@id='csrf_token']/@value").get()
        yield scrapy.FormRequest.from_response(
            response,
            formxpath="//form/div[@class='form-group']",
            formdata={
                "csrf_token": csrf_token,
                "username": "admin",
                "password": "admin"
            },
            callback=self.after_login
        )

    def after_login(self, response):
        # logged_in = ''.join(response.xpath("//h3[contains(text(), 'Welcome to Scrape World')]/text()").getall()).strip()
        # print(logged_in)
        yield scrapy.Request(
            url='https://scrape.world/season',
            callback=self.table
        )

    def table(self, response):
        tables = pd.read_html(response.text, attrs={'id': 'stats_EAS'}, flavor='bs4')
        res = tables[0]
        tables = response.xpath("//tr")
        for row in tables:
            yield {
                'ranker': row.xpath(".//th[@data-stat='ranker']/text()").get(),
                'team_name': row.xpath(".//td[@data-stat='team_name']/text()").get(),
                'wins_avg': row.xpath(".//td[@data-stat='wins_avg']/text()").get(),
                'losses_avg': row.xpath(".//td[@data-stat='losses_avg']/text()").get(),
                'losses_ot_avg': row.xpath(".//td[@data-stat='losses_ot_avg']/text()").get(),
                'points_avg': row.xpath(".//td[@data-stat='points_avg']/text()").get()
            }

process = CrawlerProcess()
process.crawl(AllTeamsSpider)
process.start()
