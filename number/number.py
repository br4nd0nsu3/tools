# coding=utf-8
'''
/*
 * @Author: brandon 
 * @Date: 2019-01-04 18:04:49 
 * @Last Modified by: brandon
 * @Last Modified time: 2019-01-04 18:39:03
 * @查询号码运营商
 */
'''
from selenium import webdriver 
from time import sleep

class autoscan():
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # prefs = {'profile.default_content_settings.popups': 0,'download.default_directory': config.SCANDOWNLOAD}  
        # options.add_experimental_option('prefs', prefs)
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)
        # self.wait=WebDriverWait(self.browser, 1) 
        self.delay=0.3
        # self.address=''
        self.tasklists=[]  
    def __del__(self):
        self.browser.quit()

    def searchtnum(self,number):
        url = 'https://www.baidu.com/s?wd='+number
        self.browser.get(url)
        try:
            area = self.browser.find_element_by_xpath('//*[@id="1"]/div[1]/div/div[2]/div[1]/span[2]').text
            return area
        except:
            pass
        try:
            area = self.browser.find_element_by_xpath('//*[@id="1"]/div/div[2]/div[1]/div/div[2]/div[1]/span[3]').text
            return area
        except:
            pass
        area = '未知'
        return area

if __name__ == '__main__':
    auto = autoscan()
    f=open('yidong5000.txt','r')
    numbers = f.readlines()
    for number in numbers:
        f=open('result.txt','a+')
        number = number.strip()
        try:
            area = auto.searchtnum(number)
            f.write(number+'---'+area+'\n')
            if area.startswith('陕西'):
                f1=open('shanxiresult.txt','a+')
                f1.write(number+'---'+area+'\n')
                f1.close()
            sleep(2)
        except:
            f.write(number+'---未知\n')
        f.close()

    print('end')
