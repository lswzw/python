import requests
from bs4 import BeautifulSoup

if __name__=='__main__':
    target="http://192.168.5.55/1.html"
    save_path = 'Z:\\text'
    index_path='https://www.wuruo.com/126/126892/'
    req=requests.get(url=target,
                     headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        }  
                     )
    req.encoding = 'gbk'
    soup = BeautifulSoup(req.text,"html.parser")
    #print(soup)
    list_tag = soup.find('div',attrs={'id':'readerlist'})
    #print(list_tag)
        
for dd_tag in list_tag.find_all('li',attrs={'a':''}):
    chapter_name = dd_tag.a.string
    #print(chapter_name)
    chapter_url=index_path+dd_tag.a.get('href')
    #print(chapter_url)
    chapter_req = requests.get(
        url=chapter_url,
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
        }  
    )
    chapter_req.encoding = 'gbk'
    chapter_soup = BeautifulSoup(chapter_req.text, "html.parser")
    #print(chapter_soup)
    content_tag = chapter_soup.find('div',attrs={'id':'content'})
    content_name = chapter_soup.title.string
    print(content_name)
    content_text = str(content_tag.text.replace('\xa0','\n'))
    #print(content_text)
    with open('Z:\\0\\1.txt', 'a') as f:
            f.write(content_name)
            f.write(content_text)

