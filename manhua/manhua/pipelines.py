# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
from manhua.settings import IMAGES_STORE,USER_AGENT
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class ManhuaPipeline(object):
    def process_item(self, item, spider):
        fold_name = ''.join(item['title']).encode('gbk')
        header = {
            'USER-Agent': USER_AGENT
        }
        images=[]
        dir_path = '{}//{}'.format(IMAGES_STORE,fold_name)
        if not os.path.exists(dir_path) and item['url'] != '':
            os.mkdir(dir_path)
        if len(item['url']) == 0:
            with open('..//check.txt','a+') as fp:
                fp.write(''.join(item['title']))
                fp.write('\n')
        
      

        imgurl = item['url']
        file_name = item['imgname']
        file_path = '{}//{}'.format(dir_path,file_name)
        images.append(file_path)
        if os.path.exists(file_path) or os.path.exists(file_name):
            pass
        
        with open('{}//{}.jpg'.format(dir_path,file_name), 'wb') as f:
            req = requests.get(imgurl, headers=header)
            f.write(req.content)
            
        return item 
