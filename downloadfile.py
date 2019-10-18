import time
import requests

def downloadFile(name, url):
    headers = {'Proxy-Connection':'keep-alive'}
    r = requests.get(url, stream=True, headers=headers)
    length = float(r.headers['content-length'])
    f = open(name, 'wb')
    count = 0
    count_tmp = 0
    time1 = time.time()
    for chunk in r.iter_content(chunk_size = 512):
        if chunk:
            f.write(chunk)
            count += len(chunk)
            if time.time() - time1 > 2:
                p = count / length * 100
                speed = (count - count_tmp) / 1024 / 1024 / 2
                count_tmp = count
                print(name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S')
                time1 = time.time()
    f.close()

def formatFloat(num):
    return '{:.2f}'.format(num)

if __name__ == '__main__':
	i = 1
	while i ==1:
    	url = input('输入要下载的文件地址：')
    	name = input('输入要下载的文件名字: ')
    	downloadFile(name,url)
    	print('下载完成...')

