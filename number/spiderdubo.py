# coding = utf-8
'''
/*
 * @Author: brandon 
 * @Date: 2019-01-08 10:27:25 
 * @Last Modified by: brandon
 * @Last Modified time: 2019-01-08 14:56:47
 * @爬取赌博网站
 */
'''
import requests
from lxml import etree
import re
import sys
import math


def progress_bar(portion, total):
    """
    total 总数据大小，portion 已经传送的数据大小
    :param portion: 已经接收的数据量
    :param total: 总数据量
    :return: 接收数据完成，返回True
    """
    part = total / 50  # 1%数据的大小
    count = math.ceil(portion / part)
    sys.stdout.write('\r')
    sys.stdout.write(('[%-50s]%.2f%%' % (('>' * count), portion / total * 100)))
    sys.stdout.flush()

    if portion >= total:
        sys.stdout.write('\n')
        return True
    
    
# 调用方式
portion = 0
total = 999999-1000+1

for i in range(1000,999999):
    f=open('urlresult.txt','a+')
    urltxt = open('urllist.txt','a+')
    url = 'http://www.%s.com' %str(i)
    try:
        r = requests.get(url, timeout=1)
        f.write(url+'\n')
        urltxt.write('\n'+url)
        html = etree.HTML(r.text)
        pattern = r"window.location.href='(.*?)'"
        hrefpat = r'<a href="(.*?)"'
        titlepat = r'<title>(.*?)</title>'
        title = re.findall(titlepat,r.text)
        if len(title) >= 1:
            f.write('标题:'+title[0]+'\n')
            urltxt.write('——————'+title[0])
        urllist = re.findall(pattern,r.text)
        urllist1 = re.findall(hrefpat,r.text)
        for urlurl in urllist1:
            if urlurl in urllist:
                pass
            else:
                urllist.append(urlurl)
        if len(urllist) > 0 :
            f.write('#####\n')
            for urlurl in urllist:
                if urlurl.startswith('http://') or urlurl.startswith('https://'):
                    f.write(urlurl+'\n')
            f.write('#####\n')
        f.write('-----------------------------\n')
    except:
        pass
    urltxt.close()
    f.close()
    portion += 1    
    sum = progress_bar(portion, total)
    if sum:
        break
    

print('end')