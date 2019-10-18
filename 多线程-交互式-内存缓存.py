import requests
import os
from lxml import etree
from multiprocessing.dummy import Pool

'''
更换网站须要更改的几个地方：

字符集 GBK  更改  UTF-8

__main__
1. 	print('仅支持：http://www.62ma.com'+'\n')
2. 	target='http://www.62ma.com/s/'+c+'_'+a+'/'
3.	list_tag = soup.xpath('/html/body/div[1]/ul/span')
4.	name = str(soup.xpath('/html/body/div[1]/p/a/@title')[0])[0:-2]

cache_chapter & get_chapter
1.	chapter_url='http://www.62ma.com'+dd_tag.xpath('./a/@href')[0]

cache_download & get_download
1.	content_name = tree.xpath('/html/body/div[4]/text()')[0]
2.	content_text = tree.xpath('//*[@id="content"]/text()')

'''

name = None
dict = {}

####缓存下载--章节列表####
def cache_chapter(list_tag,chapter_unm,pool_num):
	pool = Pool(pool_num)
	chapter_url_list = []
	for dd_tag in list_tag:
		chapter_url='http://www.62ma.com'+dd_tag.xpath('./a/@href')[0]
		chapter_url_list.append(chapter_url)
	if pool_num == 88:
		pool.imap(cache_download,chapter_url_list[chapter_unm:])
		print('\n'+'正在应用缓存下载中。。。')
		pool.close()
		pool.join()
	elif pool_num == 1:
		pool.imap(cache_text,chapter_url_list[chapter_unm:])
		pool.close()
		pool.join()

####缓存下载--多线程下载章节####
def cache_download(url):
	dictname = url[-13:-5]
	chapter_req = requests.get(url)
	chapter_req.encoding = 'gbk'
	tree = etree.HTML(chapter_req.text)
	content_name = tree.xpath('/html/body/div[4]/text()')[0]
	content_text = tree.xpath('//*[@id="content"]/text()')
	content_text = ''.join(content_text)
	dict[dictname] = [content_name,content_text]
	print(content_name)


####缓存下载--顺序合并多线程下载章节####
def cache_text(url):
	dictname = url[-13:-5]
	content_name = dict[dictname][0]
	content_text = dict[dictname][1]
	with open('./bak','a',encoding='utf-8') as f:
		f.write(content_name+'\n')
		f.write(content_text+'\n')

####正常下载--章节列表####
def get_chapter(list_tag,chapter_unm,pool_num):
	pool = Pool(pool_num)
	chapter_url_list = []
	for dd_tag in list_tag:
		chapter_url='http://www.62ma.com'+dd_tag.xpath('./a/@href')[0]
		chapter_url_list.append(chapter_url)
	pool.imap(get_download,chapter_url_list[chapter_unm:])
	pool.close()
	pool.join()

####正常下载--顺序下载章节####
def get_download(url):
	chapter_req = requests.get(url)
	chapter_req.encoding = 'gbk'
	tree = etree.HTML(chapter_req.text)
	content_name = tree.xpath('/html/body/div[4]/text()')[0]
	content_text = tree.xpath('//*[@id="content"]/text()')
	content_text = ''.join(content_text)
	print(content_name)
	with open('./bak','a',encoding='utf-8') as f:
		f.write(content_name+'\n')
		f.write(content_text+'\n')

####清洗换行符####
def clearBlankLine():
	file1 = open('./bak', 'r', encoding='utf-8')
	file2 = open(name+'.txt', 'w', encoding='utf-8')
	try:
		for line in file1.readlines():
			if line == '\n':
				line = line.strip('\n')
			file2.write(line)
	finally:
		file1.close()
		file2.close()
	os.remove('./bak')

####开始####
if __name__ == '__main__':
	print('仅支持：http://www.62ma.com'+'\n')
	a = input('输入要下载的链接码：')
	b = len(str(a))
	if b > 5:
		c=str(a)[0:3]
	else:
		c=str(a)[0:2]
	target='http://www.62ma.com/s/'+c+'_'+a+'/'
	req=requests.get(url=target)
	req.encoding = 'gbk'
	soup = etree.HTML(req.text)
	list_tag = soup.xpath('/html/body/div[1]/ul/span')
	name = str(soup.xpath('/html/body/div[1]/p/a/@title')[0])[0:-2]
	print('\n'+'你须要下载的小说是：'+name+'\n')
	chapter_unm = int(input('请输入开始章节：')) -1
	print('\n'+'是否须要缓存技术?')
	cacheif = int(input('是:1   否:2   :'))
	if cacheif == 1:
		pool_num = 88
		cache_chapter(list_tag,chapter_unm,pool_num)
		pool_num = 1
		cache_chapter(list_tag,chapter_unm,pool_num)
	else:
		pool_num = 1
		get_chapter(list_tag,chapter_unm,pool_num)
	clearBlankLine()
	print('\n'+'....下载完成....')

