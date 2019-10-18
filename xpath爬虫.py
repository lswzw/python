import requests
from lxml import etree

target = "https://www.vodtw.com/Html/Book/48/48766/"
index_path = 'https://www.vodtw.com/Html/Book/48/48766/'

req_text = requests.get(url=target).text
# print(req_text)
list_text = etree.HTML(req_text)
li_list = list_text.xpath('/html/body/div[7]/div[5]/dl/dd/ul/li')

for li in li_list:
    chapter_url = index_path + li.xpath('./a/@href')[0]
    # print(chapter_url)
    chapter = requests.get(url=chapter_url).text
    xpath_text = etree.HTML(chapter)
    chapter_title = xpath_text.xpath('//*[@id="htmltimu"]/text()')[0]
    print(chapter_title)
    chapter_text = xpath_text.xpath('//*[@id="BookText"]/text()')
    chapter_text = ''.join(chapter_text)
    # print(chapter_text)
    with open('999.txt', 'a', encoding='utf-8') as f:
        f.write(chapter_title+'\n'+chapter_text+'\n')
        
print("下载完成...")


