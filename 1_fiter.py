#coding:utf-8
import csv,re

csvfile = file('/Users/sunjian/Desktop/hc项目/domain_drqz/domain_filter/jieguo.csv', 'rb')
reader = csv.reader(csvfile)

outfile = open('/Users/sunjian/Desktop/hc项目/domain_drqz/待选.csv','wb')

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
	shijian = line[0]
	word = line[1]
	bd_index = line[2]
	reverse_index = line[3]
	chinese = line[4]
	illegal = line[6]
	pan_analysis = line[7]
	sgsr = line[8]

	m += 1

	if search('^(\d+)$',bd_index) == 'no' or search('^(\d+)$',sgsr) == 'no':
		
		continue

	if chinese != 'english' and pan_analysis != '泛解析' and illegal != '包含违禁词':
		if int(sgsr) > 1 or int(bd_index) > 0:

			data = []
			data.append(word)
			data.append(bd_index)
			data.append(reverse_index)
			data.append(sgsr)
			writer = csv.writer(outfile,dialect='excel')
			writer.writerow(data)
			n += 1
csvfile.close()
print '一轮过滤数据：查询总数：%s，提取：%s' % (m,n)