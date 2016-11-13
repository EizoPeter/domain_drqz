#coding:utf-8
import os,csv,re,time

'''提取历史快照地址'''
print '------> 提取历史快照地址'
os.system(' python archive_url.py  ')
print '------> done'

time.sleep(10)


'''检测历史快照是否包含违禁词'''
print '------> 检测历史快照是否包含违禁词'
os.system(' cd /Users/sunjian/Desktop/hc项目/domain_drqz/archive/ ; scrapy crawl lskz ')
time.sleep(10)
print '------> done'

'''过滤不包含违禁词的domain'''
print '------> 过滤不包含违禁词的domain'
os.system('cd /Users/sunjian/Desktop/hc项目/domain_drqz/')


data_dict = {}
for line in open('/Users/sunjian/Desktop/hc项目/domain_drqz/555'):
	line = line.strip()

	domain = line.split(',')[0]
	tezheng = line.split(',')[1]

	if data_dict.has_key(domain):
		data_dict[domain].append(tezheng)
	else:
		data_dict[domain] = [tezheng]

current_time = time.strftime("%Y%m%d",time.localtime(time.time()))
outfile = open('/Users/sunjian/Desktop/%s_当日过期_人肉筛选.csv' % current_time,'wb')

for k,v in data_dict.items():
	if 'weijin' not in v:
		print '检测%s -----> 正常' % k
		data = []
		data.append(k)
		writer = csv.writer(outfile,dialect='excel')
		writer.writerow(data)
	else:
		print '检测%s -----> 违禁' % k

print '------> done'
print '------> 删除历史数据...'
os.system('cd /Users/sunjian/Desktop/hc项目/domain_drqz/ ; rm 111 222 333 444 555')
print '------> 进入人工筛选环节'


