#coding:utf-8

import scrapy,re,urllib,os,time,sys,random
from domain_filter.items import DomainFilterItem
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

req = open('/Users/sunjian/Desktop/hc项目/weijin.txt').read().strip()

class DmozSpider(scrapy.Spider):
    name = "domain"
    start_urls = []
    for line in open('/Users/sunjian/Desktop/hc项目/domain_drqz/111'):
        line = line.strip()

        url = line.split(',')[0]
        sr = line.split(',')[1]

        url_bd = 'http://www.baidu.com/s?&tn=baidulocal&ie=utf-8&cl=3&wd=site:%s&class=%s' % (url,sr)

        start_urls.append(url_bd)

    def parse(self,response):

        # 提取查询domain
        word = search(r'site:(.*?)&',response.url)
        sr = search(r'class=(\d+)',response.url)

        item = DomainFilterItem()

        # 抓取百度
        baidu_html = response.body
        bd_index = search('百度为您找到相关网页(\d+)篇',baidu_html)
        if bd_index == 'no' or 'us1.wss.webroot.com' in response.url or 'search/error.html' in response.url:
            yield Request(url=response.url, callback=self.parse)
            #yield Request(url=response.url, callback=self.parse)
        else:

            # 检测首页结果进入倒排索引的数量
            size_list = re.findall(';(\d+)K&',baidu_html)
            reverse_index = len(size_list) - size_list.count(1)

            # 检测百度搜索标题是否包含中文（判断是否为中文站点）
            title_list = re.findall('<font size="3">(.*?)</font>',baidu_html)
            if len(title_list) == 0:
                chinese = 'no_language'
            else:
                title_set = ''.join(title_list)
                if len(re.findall(u'[\u4e00-\u9fa5]+',title_set.decode('utf8'))) > 0:
                    chinese = 'chinese'
                else:
                    chinese = 'english'

            # 检测是否泛解析过（二级域名>=3，则判定为泛解析）
            domain_list = re.findall(r'<font color=#008000>([^\.]*?)\.%s/' % word,baidu_html)
            if len(set(domain_list)) >= 3:
                pan_analysis = '泛解析'
            else:
                pan_analysis = '正常'

            # 检测是否做过非法违禁内容（检测html是否包含违禁关键词）
            if search('(%s)' % req,baidu_html) == 'no':
                illegal = '正常'
            else:
                illegal = '包含违禁词'    


            item['domain'] = word
            item['bd_index'] = bd_index
            item['reverse_index'] = reverse_index
            item['chinese'] = chinese
            item['pan_analysis'] = pan_analysis
            item['illegal'] = illegal
            item['sgsr'] = sr
            yield item


