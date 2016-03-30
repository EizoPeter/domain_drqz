#coding:utf-8

import os,csv,re,time


'''提取当日域名，判断是否做过违禁内容、英文站、泛域名，查询百度收录、倒排索引、搜狗SR'''
os.system('cd /Users/sunjian/Desktop/hc项目/domain_drqz/domain_filter ; rm jieguo.csv ; scrapy crawl domain -o jieguo.csv')
time.sleep(10)

'''剔除包含违禁内容、泛域名和英文站，取出SR>1 或 百度收录>0的域名'''
os.system('cd /Users/sunjian/Desktop/hc项目/domain_drqz/ ; python 1_fiter.py')
time.sleep(10)

'''检测360安全数据，及360收录是否包含违禁内容'''
os.system('cd /Users/sunjian/Desktop/hc项目/domain_drqz/so360 ; rm 360.csv ; scrapy crawl 360 -o 360.csv')
time.sleep(10)

'''删除360有安全提示的域名'''
os.system(' cd /Users/sunjian/Desktop/hc项目/domain_drqz/ ; python 2_fiter.py')
time.sleep(10)

'''过滤archive历史快照'''
os.system(' python archive_url.py  ')



