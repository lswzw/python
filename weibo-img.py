import requests
import os
import json
from multiprocessing.dummy import Pool

uid = '1669879400'
containerid = '1076031669879400'

headers = {
           #'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
           #'cookie': ''
           }

def save_img(url):
    name = url[-36:]
    date = requests.get(url)
    with open(c+'/'+name, 'wb') as f:
        f.write(date.content)
    print(name+'\n')

if __name__ == '__main__':
    list=[]
    a = int(input('输入开始页 ：'))
    b = int(input('输入结束页 ：'))
    c = input('创建目录名 ：')
    os.makedirs(c) if os.path.exists(c) == False else None  
    for Page in range(a,b + 1):
        target='https://m.weibo.cn/api/container/getIndex?uid='+uid+'&containerid='+containerid+'&page='+str(Page)
        req = requests.get(target,headers=headers)
        items  = req.json().get('data').get('cards')
        for pics in items:
            url_text = dict(pics).get('mblog')
            if url_text != None:
                if url_text.get('pics') != None:
                    for large_url in url_text.get('pics'):
                        url = large_url.get('large').get('url')
                        list.append(url) 
    pool = Pool(44)
    pool.map(save_img,list)
    pool.close()
    pool.join()
    print('\n'+'....下载完成....')

