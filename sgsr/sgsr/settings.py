# -*- coding: utf-8 -*-

# Scrapy settings for sgsr project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sgsr'

SPIDER_MODULES = ['sgsr.spiders']
NEWSPIDER_MODULE = 'sgsr.spiders'

# -*- coding: utf-8 -*-

# Scrapy settings for domain_filter project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import random

'''读取代理文件中的ip，写入PROXIES'''
PROXIES = []
for line in open('/Users/sunjian/Desktop/hc项目/proxy/hege_daili.txt'):
    line = line.strip()
    PROXIES.append({'ip_port':'%s' % line ,'user_pass':''})

# 随机cookie
def getCookie():
    cookie_list = [
    'SUID=3D8C7A7B2208990A0000000056F52D06; SUV=1458908474288236822890988; IPLOC=CN1100; SMYUV=1459321495442932; sct=6; fromwww=1; SUIR=834C78453A3F165D6AA75C353A7C0D58; wuid=AAFQ24WLEAAAAAqTGFb8WAcAAAA=; usid=IJT1H1XK9xXVEMuT; SNUID=AA64516C10143EA94C8882AD110D465A; ppinf=5|1459848081|1461057681|Y2xpZW50aWQ6NDoxMTIwfGNydDoxMDoxNDU5ODQ4MDgxfHJlZm5pY2s6MDp8dHJ1c3Q6MToxfHVzZXJpZDoxOToxMzkyMDExMzI1M0AxNjMuY29tfHVuaXFuYW1lOjA6fA; pprdig=fpb8y1hPocHqxslwHl2CcK41BV6b80m5QlHqaGUFHJY8e4h81Iif7e_ULWkvzEIMBVpRS2VA4HoScRBpeASlF_ZKmy3AW3AHa2nqdpJ8hNN1yZWFEF2CnHnwGocEgRDUBKBR9djwhAB50aja9Hjo5MVh_u22hTx_ZkdiCsT1wTc; ld=wkllllllll2QM5YXlllllVtVDIZlllllK9VCmkllll9lllllxZlll5@@@@@@@@@@'
    ]
    cookie = random.choice(cookie_list)
    return cookie

# 定义ua列表
USER_AGENTS =[
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        #'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    ]

RETRY_TIMES = 10
RETRY_HTTP_CODES = [ 500 , 503 , 504 , 400 , 403 , 404 , 408 ,302]

# 假如中间件
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware' : 90 ,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    'sgsr.middlewares.RandomUserAgent':400,

    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    # 'sgsr.middlewares.ProxyMiddleware': 100,
}

# '''降低log级别，取消注释则输出抓取详情'''
# LOG_LEVEL = 'INFO'

# 禁止cookie
COOKIES_ENABLED = False

# cookie debug
# COOKIES_DEBUG = False

# DEFAULT_REQUEST_HEADERS ，定义请求的头信息
DEFAULT_REQUEST_HEADERS = {
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
	"Cache-Control":"no-cache",
	"Connection":"keep-alive",
	"Cookie":"%s" % getCookie(),
	"Host":"rank.ie.sogou.com",
	"Pragma":"no-cache",
	"Upgrade-Insecure-Requests":1,
}

# 禁止显示<urlopen error timed out>告警
DOWNLOAD_HANDLERS = {
  's3': None,
}

# 下载延迟，既下载两个页面之间的等待时间
# DOWNLOAD_DELAY = 0.5

# 并发最大值
CONCURRENT_REQUESTS = 10

# 对单个网站的并发最大值
CONCURRENT_REQUESTS_PER_DOMAIN = 10

# #启动自动限速
# AUTOTHROTTLE_ENABLED = False

# 设置下载超时
DOWNLOAD_TIMEOUT = 60

#配置数据库
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'heichan'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''


# #启用PIPELINES
# ITEM_PIPELINES = {
#     'domain_filter.pipelines.DomainFilterPipeline': 300,
#     'domain_filter.pipelines.MySQLDomainFilterPipeline': 400,
# }




