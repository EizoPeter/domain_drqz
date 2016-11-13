#coding:utf-8

import os,csv,re,time,sys



'''检测搜狗SR'''
os.system('cd /Users/sunjian/Desktop/hc项目/domain_drqz/sgsr ; rm jieguo.csv ; scrapy crawl sgsr -o jieguo.csv')
time.sleep(10)

'''删除SR<3 和 长度>14的域名'''
os.system("cat /Users/sunjian/Desktop/hc项目/domain_drqz/sgsr/jieguo.csv|egrep ',(3|4|5)'|awk -F\",\" '{if(length($1)<15)print $0}'  > ~/Desktop/hc项目/domain_drqz/111 ")
time.sleep(10)

'''提取当日域名，判断是否做过违禁内容、英文站、泛域名，查询百度收录、倒排索引、搜狗SR'''
os.system('cd /Users/sunjian/Desktop/hc项目/domain_drqz/domain_filter ; rm jieguo.csv ; scrapy crawl domain -o jieguo.csv')
time.sleep(10)

'''剔除包含违禁内容、泛解析和英文站的域名'''
os.system("cat /Users/sunjian/Desktop/hc项目/domain_drqz/domain_filter/jieguo.csv|egrep -v '违禁词|english|泛解析'|awk -F\",\" '{print $1\",\"$NF}' > ~/Desktop/hc项目/domain_drqz/222")
time.sleep(10)


'''检测360安全数据，及360收录是否包含违禁内容'''
os.system('cd /Users/sunjian/Desktop/hc项目/domain_drqz/so360 ; rm 360.csv ; scrapy crawl 360 -o 360.csv')
time.sleep(10)

'''删除360有安全提示的域名'''
os.system(" cat /Users/sunjian/Desktop/hc项目/domain_drqz/so360/360.csv|grep -v '不安全'|awk -F\",\" '{print $2}' > ~/Desktop/hc项目/domain_drqz/333 ")
time.sleep(10)


print '请运行切换代理，并运行index2.py'

