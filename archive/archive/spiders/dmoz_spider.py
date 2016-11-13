#coding:utf-8

import scrapy,re,urllib,os,time,sys,random,StringIO,pycurl,csv
from archive.items import ArchiveItem
from scrapy import Request
import MySQLdb as mdb

current_time = time.strftime("%Y%m%d",time.localtime(time.time()))
a = open('/Users/sunjian/Desktop/hc项目/domain_drqz/555','wb')

reload(sys)
sys.setdefaultencoding('utf-8')

def search(req,html):
     text = re.search(req,html)
     if text:
         data = text.group(1)
     else:
         data = 'no'
     return data


req = open('/Users/sunjian/Desktop/hc项目/weijin.txt').read().strip()

class DmozSpider(scrapy.Spider):
    name = "lskz"
    start_urls = []
    for line in open('/Users/sunjian/Desktop/hc项目/domain_drqz/444'):
        domain = line.strip()
        ''' request archive csx api '''
        start_urls.append(domain)
        
    def parse(self,response):

        # 提取查询domain
        request = re.sub(':\d+$','',search(r'http://web.archive.org/.*?http://(.*)',response.url).replace('/','').replace('www.',''))

        if '00000000' in response.url:
            a.write('%s,%s\n' % (request,'无快照'))
        else:    
            archive_detail_html = response.body
            tezheng = search(r'(%s)' % req,archive_detail_html)
            if tezheng == 'no':
                illegal = 'zhengchang'
            else:
                illegal = 'weijin'

            a.write('%s,%s\n' % (request,illegal))


