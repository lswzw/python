import requests
import os
import re
from selenium import webdriver
from time import sleep
from lxml import etree
from multiprocessing.dummy import Pool

def get_date(num):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        browser = webdriver.Firefox(options=option)
        #browser = webdriver.Firefox()
        browser.get('https://huaban.com/boards/'+str(c)+'/')
        if num == 0:
                date = browser.page_source
                browser.quit()
                return(date)
        else:
                for i in range(num):
                        browser.execute_script('window.scrollTo(0,10240)')
                        sleep(1)
                date = browser.page_source
                browser.quit()
                return(date)

def get_url(url):
        url = 'https://huaban.com'+url
        req = requests.get(url)
        img_url = re.findall('"key":"(.*?)", "type":"image/jpeg", "height":',req.text)[0]
        img_url = 'http://hbimg.huabanimg.com/'+ img_url
        save_img(img_url)
            
def save_img(url):
        name = url[-30:-13]
        print(url)
        date = requests.get(url)
        with open(b+'/'+name+'.jpg', 'wb') as f:
            f.write(date.content)  

####开始####
if __name__ == '__main__':
        c = int(input('输入链接码: '))
        a = int(input('输入下载的页数: '))
        b = input('创建目录名： ')
        os.makedirs(b)
        list_old=[]
        list=[]
        for i in range(a):
                date = get_date(i)
                soup = etree.HTML(date)
                list_old += soup.xpath('//*[@id="waterfall"]/div/a/@href')
        for i in list_old:
                if i not in list:
                        list.append(i)
        pool = Pool(4)
        pool.map(get_url,list)
        pool.close()
        pool.join()
        print('\n'+'....下载完成....')

