#coding:utf-8

import csv,re

csvfile = file('/Users/sunjian/Desktop/hc项目/domain_drqz/so360/360.csv', 'rb')
reader = csv.reader(csvfile)

outfile = open('/Users/sunjian/Desktop/hc项目/domain_drqz/二轮待选.csv','wb')

def search(req,html):
     text = re.search(req,html)
     if text:
         data = text.group(1)
     else:
         data = 'no'
     return data

n = 0
m = 0
for line in reader:
	sr = line[0]
	bd_index = line[1]
	daopai = line[2]
	score = line[3]
	word = line[4]

	m += 1
	if score != '不安全':
		data = []
		data.append(word)
		data.append(bd_index)
		data.append(daopai)
		data.append(sr)
		writer = csv.writer(outfile,dialect='excel')
		writer.writerow(data)
		n += 1
csvfile.close()
print '二轮过滤数据：查询总数：%s，删除：%s' % (m,m-n)
