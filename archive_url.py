#coding:utf-8

'''http://web.archive.org/cdx/search/cdx?url=oa24h.com&output=json&from=2014&to=2016&fl=timestamp,original'''
'''http://web.archive.org/web/20140625131200/http://www.kanzhun.com/'''


'''拼接archive检测url，默认提取该域名13-16年的快照'''

import StringIO,pycurl,time,random,re,os,csv,urllib,socket,sys,HTMLParser,whois
from threading import Thread,Lock
from Queue import Queue

current_time = time.strftime("%Y%m%d",time.localtime(time.time()))

def getHtml(url,headers):
    c = pycurl.Curl()    #通过curl方法构造一个对象
    #c.setopt(pycurl.REFERER, 'http://qy.m.58.com/')    #设置referer
    c.setopt(pycurl.FOLLOWLOCATION, True)    #自动进行跳转抓取
    c.setopt(pycurl.MAXREDIRS,5)            #设置最多跳转多少次
    c.setopt(pycurl.CONNECTTIMEOUT, 30)        #设置链接超时
    c.setopt(pycurl.TIMEOUT,60)            #下载超时
    c.setopt(pycurl.ENCODING, 'gzip,deflate')    #处理gzip内容，有些傻逼网站，就算你给的请求没有gzip，它还是会返回一个gzip压缩后的网页
    #c.setopt(c.PROXY,'cow.0.6180339.in:17225')    # 代理
    c.fp = StringIO.StringIO()    
    c.setopt(pycurl.URL, url)    #设置要访问的URL
    c.setopt(pycurl.HTTPHEADER,headers)        #传入请求头
    # c.setopt(pycurl.POST, 1)
    # c.setopt(pycurl.POSTFIELDS, data)        #传入POST数据
    c.setopt(c.WRITEFUNCTION, c.fp.write)    #回调写入字符串缓存
    c.perform()        

    code = c.getinfo(c.HTTP_CODE)    #返回状态码
    html = c.fp.getvalue()    #返回源代码
    return html

headers = [
    "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding:gzip, deflate, sdch",
    "Accept-Language:zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control:no-cache",
    "Host:web.archive.org",
    "Pragma:no-cache",
    "Proxy-Connection:keep-alive",
    "Upgrade-Insecure-Requests:1",
    "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
]

def search(req,html):
     text = re.search(req,html)
     if text:
         data = text.group(1)
     else:
         data = 'no'
     return data

api_url_list = []
for line in open('/Users/sunjian/Desktop/hc项目/domain_drqz/333'):
    domain = line.strip()
    ''' request archive csx api '''
    archive_url = 'http://web.archive.org/cdx/search/cdx?url=%s&output=json&from=2014&to=2016&fl=timestamp,original' % domain
    api_url_list.append((domain,archive_url))

a = open('/Users/sunjian/Desktop/hc项目/domain_drqz/444','w')

class Fetcher:
    def __init__(self,threads):
        self.lock = Lock() #线程锁
        self.q_req = Queue() #任务队列
        self.q_ans = Queue() #完成队列
        self.threads = threads
        for i in range(threads):
            t = Thread(target=self.threadget) #括号中的是每次线程要执行的任务
            t.setDaemon(True) #设置子线程是否随主线程一起结束，必须在start()
                              #之前调用。默认为False
            t.start() #启动线程
        self.running = 0 #设置运行中的线程个数
 
    def __del__(self): #解构时需等待两个队列完成
        time.sleep(0.5)
        self.q_req.join() #Queue等待队列为空后再执行其他操作
        self.q_ans.join()
 
    #返回还在运行线程的个数，为0时表示全部运行完毕
    def taskleft(self):
        return self.q_req.qsize()+self.q_ans.qsize()+self.running 

    def push(self,req):
        self.q_req.put(req)
 
    def pop(self):
        return self.q_ans.get()
 
    #线程执行的任务，根据req来区分 
    def threadget(self):
        while True:
            line = self.q_req.get()

            domain = line[0]
            url = line[1]

            with self.lock: 
                self.running += 1

            html = getHtml(url,headers)
            data_tupe = re.findall(r'"(\d+)", "(http://[^"]*?)"',html)
            if len(data_tupe) == 0:
                jieguo = '无历史快照'
                archive_url = 'http://web.archive.org/web/00000000000000/http://www.%s' % domain
                print archive_url  
                a.write('%s\n' % archive_url)
            else:
                black_url = []
                for line in data_tupe[:15]:
                    archive_url = 'http://web.archive.org/web/%s/%s' % (line[0],line[1])
                    print archive_url  
                    a.write('%s\n' % archive_url)
            
            self.q_ans.put(line)
            with self.lock:
                self.running -= 1
            self.q_req.task_done() # 在完成一项工作之后，Queue.task_done()
                                   # 函数向任务已经完成的队列发送一个信号
            time.sleep(0.1) # don't spam
 
'''获取api detail url'''
f = Fetcher(threads=50) #设置线程数
for url in api_url_list:
    f.push(url)         #所有url推入下载队列
while f.taskleft():     #若还有未完成的的线程
    f.pop()   #从下载完成的队列中取出结果



