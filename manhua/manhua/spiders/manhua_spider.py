#coding=utf-8
'''
/*
 * @Author: brandon 
 * @Date: 2019-01-08 17:15:12 
 * @Last Modified by: brandon
 * @Last Modified time: 2019-01-09 14:25:52
 */
 '''
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from manhua.items import ManhuaItem

class manhua(scrapy.Spider):
    name = 'tengxunmanhua'

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        # self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(30)
    
    def closed(self,spider):
        print 'spider closed'
        self.browser.close()

    def start_requests(self):
        # 'http://ac.qq.com/ComicView/index/id/536332/cid/1'
        # 'https://ac.qq.com/ComicView/index/id/536332/cid/120?fromPrev=1'
        urls = [
            'http://ac.qq.com/ComicView/index/id/536332/cid/1'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        item = ManhuaItem()
        imgs = response.xpath('//*[@id="comicContain"]/li')
        pattern=r'https://manhua.qpic.cn/manhua_detail'
        xiayiyexpath='//*[@id="mainControlNext"]/@href'
        imgtitle = response.css('title::text').extract()[0].split(u'-')[0]
        count = 1
        for i in imgs:
            if len(i.xpath('img/@src').extract()) >= 1:
                imgurl = i.xpath('img/@src').extract()[0]
            else:
                imgurl=''
            if imgurl != '' and imgurl.startswith(pattern):
                item['title'] = imgtitle.encode("utf-8")
                item['url'] = imgurl.encode("utf-8")  
                item['imgname'] = 'img' + str(count)
                count = count + 1
                yield item
        next_page=response.xpath(xiayiyexpath).extract_first()
        if next_page is not None: 
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        
        # self.log('保存文件: %s' % filename)


