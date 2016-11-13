#coding:utf-8

import scrapy,re,urllib,os,time,sys,random,csv
from so360.items import So360Item
from scrapy import Request
import MySQLdb as mdb
import StringIO,pycurl

reload(sys)
sys.setdefaultencoding('utf-8')

def search(req,html):
     text = re.search(req,html)
     if text:
         data = text.group(1)
     else:
         data = 'no'
     return data

class DmozSpider(scrapy.Spider):
    name = "360"
    start_urls = []

    for line in open('/Users/sunjian/Desktop/hc项目/domain_drqz/222'):
        line = line.strip()
        word = line.split(',')[0]
        sr = line.split(',')[1]
        url_so = 'http://www.so.com/s?a=index&q=site:%s' % word

        start_urls.append(url_so)

    def parse(self,response):

        # 提取查询domain
        print response.url
        word = search(r'site:(.*)',response.url)

        html = response.body

        aq_score = search(r'<p class="ele-score"><em>(\d+)</em><i>分',html)
        if aq_score != 'no':
            if int(aq_score) > 70:
                score = '较安全'
            else:
                score = '不安全'
        else:
            score = '无数据'

        item = So360Item()
        item['word'] = word
        item['score'] = score
        yield item


