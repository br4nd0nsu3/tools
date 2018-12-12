import os
import re
import math,sys

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

f=open('ipport.txt','r')
ipport=f.readlines()
total = len(ipport)
f.close()
pattern='VERSION\n(.*)\n\nSer'
f=open('result.txt','w')
count = 0
for i in ipport:
    ip,port = i.strip().split(',')
    content = os.popen("nmap %s -p %s -sV" %(ip,port)).read()
    try:
        result = re.findall(pattern,content)
        if len(result) >= 1:
            f.write(ip+':'+port+'   '+result[0]+'\n')
        else:
            f.write(ip+':'+port+'   '+'no result'+'\n')
    except:
        print('something wrong!')
    count = count+1
    progress = progress_bar(count, total)

print('ok!')

    

