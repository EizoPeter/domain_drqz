# -*- coding: utf-8 -*-

# Scrapy settings for archive project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'archive'

SPIDER_MODULES = ['archive.spiders']
NEWSPIDER_MODULE = 'archive.spiders'


# '''降低log级别，取消注释则输出抓取详情'''
# LOG_LEVEL = 'INFO'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 下载延迟，既下载两个页面之间的等待时间
# DOWNLOAD_DELAY = 0.5

# 并发最大值
CONCURRENT_REQUESTS = 20

# 对单个网站的并发最大值
CONCURRENT_REQUESTS_PER_DOMAIN = 20

# #启动自动限速
# AUTOTHROTTLE_ENABLED = False

# 设置下载超时
DOWNLOAD_TIMEOUT = 120
