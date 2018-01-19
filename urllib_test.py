import urllib
import urllib.request
import re

# print('first method')
# response1 = urllib.request.urlopen(url)
# print(response1.getcode())
# print(len(response1.read))
#
# print('second method')


def download_image(url):
    # 采用封装成request的方式,返回url下载的html
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data


def get_image(html):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    images = re.findall(pattern, repr(html))
    num = 1
    for image in images:
        image = download_image(image)
        with open('%s.jpg'%num,'wb') as fp:
            num += 1
            print('downloading num %s'%num)
    return


url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=damon&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000'
html = download_image(url)
get_image(html)





