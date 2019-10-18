import requests
import re
target="https://www.vodtw.com/Html/Book/59/59089/"

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}

req_text = requests.get(url=target,headers=headers)
req_text.encoding='gbk'
li_list = re.findall('i><a href="(.*?)" title=',req_text.text)
count = 1
for li in li_list:
    chapter=requests.get(url=target+li,headers=headers).text
    name = re.findall('ex.html">(.*?)</a>',chapter)[0]
    chapter_title = re.findall('id="htmltimu"> (.*?) </span></h1>',chapter)[0]
    chapter_text=(re.findall('3px;"></div>([\W\w]*?)<div class="button_con">',chapter)[0]).replace('</div>','').replace('<br>','').replace('&nbsp;','')
    percent = count / len(li_list) * 100
    print('%s 下载进度 %0.1f %%'%(name,percent),end='\r')
    count = count + 1
    with open(name+'.txt', 'a',encoding='utf-8') as f:
        f.write(chapter_title+'\n'+chapter_text+'\n')
        
print('\n'+'下载完成...')

