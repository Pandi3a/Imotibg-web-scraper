# -*- coding: utf-8 -*-
import scrapy


class ImotSpider(scrapy.Spider):
    name = 'imot'
    allowed_domains = ['imoti.bg']
# Here you add the URL's use the following syntax to add them.
# 'http://imoti.bg/bg/adv/view:203303',
# 'http://imoti.bg/bg/adv/view:222058',
# 'http://imoti.bg/bg/adv/view:231970',
start_urls = [
        'http://imoti.bg/bg/adv/view:203303',
        'http://imoti.bg/bg/adv/view:222058',
        'http://imoti.bg/bg/adv/view:231970',
        'http://imoti.bg/bg/adv/view:210130',
        'http://imoti.bg/bg/adv/view:230234',
        'http://imoti.bg/bg/adv/view:222269',
        'http://imoti.bg/bg/adv/view:203303',

    ]

    def parse(self, response):
        for imoti in response.css("div.left_desc"):
            yield {
                "Цена на квадрат": response.css("div.price_for_meter::text").get(),
                "Наем/Продажба": response.css("p.action::text").get(),
                "Вид Имот": response.xpath('/html/body/div[3]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/h2[1]/text()').get(),
                "Локация": response.css("div.place::text").getall(),
                "Цена": response.xpath('/html/body/div[3]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/h2[2]/text()').get(),
                "Площ": response.xpath('/html/body/div[3]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/table/tr[1]/td[2]/text()').get(),
                "Особености": response.xpath('/html/body/div[3]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/table/tr[2]/td[2]/text()').get(),
                "Етаж": response.xpath('/html/body/div[3]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/table/tr[3]/td[2]/text()').get(),
                "Добавена на": response.xpath('/html/body/div[3]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/table/tr[4]/td[2]/text()').get(),

            }

