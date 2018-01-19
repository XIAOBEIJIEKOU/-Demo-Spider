#-*- coding:utf-8 -*-
import re
import urllib.request, urllib.error

from bs4 import BeautifulSoup

url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1460997499750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%B0%8F%E9%BB%84%E4%BA%BA'


html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
picture_links = soup.find_all('img', src=re.compile(r'src="([.*\S]*\.jpg)"'))
i = 0
for each in picture_links:
    print(each)
    try:
        pic = urllib.request.urlretrieve(each, timeout=10)
    except urllib.error:
        print('【错误】当前图片无法下载')
        continue
    string = 'pictures\\'+str(i) + '.jpg'
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1