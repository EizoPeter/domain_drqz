# domain_drqz
Domain Filtering day

过滤当日删除域名，处理流程：

1、判断域名baidu_index、dp_index、sogou_sr、站点语言、是否泛解析、站点快照是否包含违禁词

2、删除英文站点 or 经过泛解析 or 包含违禁词的域名，提取bd_idnex > 0  or  sogou_sr > 2 的域名

3、检测360安全性

4、删除360安全评分 < 70的域名

5、检测archive，删除包含违禁词的域名

余下域名人工check
