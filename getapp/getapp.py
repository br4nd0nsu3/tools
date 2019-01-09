# coding=utf-8
'''
/*
 * @Author: brandon 
 * @Date: 2018-12-29 15:48:50 
 * @Last Modified by: brandon
 * @Last Modified time: 2018-12-29 17:38:14
 * @Get APP
 */
'''

from selenium import webdriver 
from time import sleep 

class autoscan():
    def __init__(self):
        options = webdriver.ChromeOptions()
        # prefs = {'profile.default_content_settings.popups': 0,'download.default_directory': config.SCANDOWNLOAD}  
        # options.add_experimental_option('prefs', prefs)
        self.browser = webdriver.Chrome()
        # self.browser.implicitly_wait(10)
        # self.wait=WebDriverWait(self.browser, 10) 
        self.delay=0.3
        # self.address=''
        self.tasklists=[]  
    def __del__(self):
        self.browser.quit()

    def getapp(self,url):
        temp=0
        # url='https://www.wandoujia.com/category/5018'
        self.browser.get(url)
        title=self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/h1/span').text
        try:
            for i in range(int(3000/24)+1):
                appnum=self.browser.find_elements_by_xpath('//*[@id="j-tag-list"]/li')
                if len(appnum) <= 3000 and temp != len(appnum):
                    self.browser.find_element_by_xpath('//*[@id="j-refresh-btn"]').click()
                    sleep(1)
                    temp = len(appnum)
                else:
                    break
        except:
            pass

        f=open('result.txt','a+')
        f.write('---------------------------------------------------\n')
        f.write(title+'\n')
        temp1={}
        for i in appnum:
            appname=i.find_element_by_xpath('div[2]/h2/a').text
            appdownloadnum=i.find_element_by_xpath('div[2]/div[1]/span[1]').text
            if '亿' in appdownloadnum:
                appdownloadnum=str(int(float(appdownloadnum[:-4])*100000000))
            elif '万' in appdownloadnum:
                appdownloadnum=str(int(float(appdownloadnum[:-4])*10000))
            # temp1[appname]=int(appdownloadnum)
            f.write(appname+';'+appdownloadnum+'\n')
        f.close()


        print('end')

if __name__=='__main__':
    auto = autoscan()
    lista=[5029,5018,5014,5024,5019,5016,5026,5017,5023,5020,5021,5028,5022,5027,6001,6003,6008,6004,6002,6007,6009,6005,6006,5015]
    for i in lista:
        url = 'https://www.wandoujia.com/category/'+str(i)
        auto.getapp(url)
