#coding:utf-8

import scrapy,re,urllib,os,time,sys,random
from sgsr.items import SgsrItem
from scrapy import Request
import MySQLdb as mdb
import StringIO,pycurl

reload(sys)
sys.setdefaultencoding('utf-8')

current_time = time.strftime("%Y-%m-%d",time.localtime(time.time()))
#current_time = '2016-10-24'


if current_time != time.strftime("%Y-%m-%d",time.localtime(time.time())):
    print '''
@@@@@@@@@@@@                                             @@@@@@@@@@@@
@@@@@@@@@@@@                                             @@@@@@@@@@@@
@@@@@@@@@@@@                                             @@@@@@@@@@@@
@@@@@@@@@@@@      Error   ,查询时间非当前                  @@@@@@@@@@@@
@@@@@@@@@@@@    请检测时间 current_time 是否有误！！         @@@@@@@@@@@@
@@@@@@@@@@@@                                             @@@@@@@@@@@@
@@@@@@@@@@@@                                             @@@@@@@@@@@@
'''
    time.sleep(120)

def search(req,html):
     text = re.search(req,html)
     if text:
         data = text.group(1)
     else:
         data = 'no'
     return data

query_file = open('/Users/sunjian/Desktop/hc项目/domain_drqz/sgsr/domain.txt','w')
con = mdb.connect(host="127.0.0.1",user="root",passwd="",db="heichan",charset='utf8');
with con:
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("select domain from domain_original where delete_time = '%s'" % current_time)
    rows = cur.fetchall()
    for row in rows:
        query = row['domain']
        query_file.write(query + "\n")
con.close()
query_file.close()

req = open('/Users/sunjian/Desktop/hc项目/weijin.txt').read().strip()

class DmozSpider(scrapy.Spider):
    name = "sgsr"
    start_urls = []
    for word in open('/Users/sunjian/Desktop/hc项目/domain_drqz/sgsr/domain.txt'):
        word = word.strip()
        url = 'http://rank.ie.sogou.com/sogourank.php?ur=http://www.%s/' % word
        start_urls.append(url)

    def parse(self,response):
        word = search(r'http:\/\/www.(.*)\/',response.url)
        sgsr = search(r'sogourank=(\d+)',response.body)

        item = SgsrItem()
        item['domain'] = word
        item['sgsr'] = sgsr
        yield item


