# -*- coding:utf-8 -*-
import re
import requests
import os
from bs4 import BeautifulSoup

url = 'https://pixabay.com/'
html = requests.get(url).text  # 获取网页内容
html_output = open("picture_html_content.html", 'wb')
html_output.write(html.encode('utf-8'))
html_output.close()
# 这里由于有些图片可能存在网址打不开的情况，加个5秒超时控制。
# data-objurl="http://pic38.nipic.com/20140218/17995031_091821599000_2.jpg"获取这种类型链接
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
# ^abc.*?qwe$
pic_url = soup.find_all('img', src=re.compile(r'^https://cdn.pixabay.com/photo/.*?jpg$'))
# pic_url = pic_node.get_text()
# pic_url = re.findall('"https://cdn.pixabay.com/photo/""(.*?)",',html,re.S)
print(pic_url)
i = 0
# 判断image文件夹是否存在，不存在则创建
if not os.path.exists('image'):
    os.makedirs('image')
for url in pic_url:
    img = url['src']
    try:
        pic = requests.get(img, timeout=5)  # 超时异常判断 5秒超时
    except requests.exceptions.ConnectionError:
        print('当前图片无法下载')
        continue
    file_name = "image/" + str(i) + ".jpg"  # 拼接图片名
    print(file_name)
    # 将图片存入本地
    fp = open(file_name, 'wb')
    fp.write(pic.content)  # 写入图片
    fp.close()
    i += 1

# import re
# import urllib.request
#
# class Picture_catch(object):
#     # ------ 获取网页源代码的方法 ---
#     def get_html_content(self, url):
#         return urllib.request.urlopen(url).read()
#
#     # ------ 获取帖子内所有图片地址的方法 ------
#     def get_img_url_list(self, html):
#         # ------ 利用正则表达式匹配网页内容找到图片地址 ------
#         reg = r'src="([.*\S]*\.jpg)"'
#         imgre = re.compile(reg);
#         imglist = re.findall(imgre, html)
#         return imglist
#
#     def save_pictures(self, img_list):
#         img_count = 0
#         for img_path in img_list:
#             # ------ 这里最好使用异常处理及多线程编程方式 ------
#             try:
#                 f = open('D:\\Python\\' + str(img_count) + ".jpg", 'wb')
#                 f.write((urllib.request.urlopen(img_path)).read())
#                 print(img_path)
#                 f.close()
#             except Exception as e:
#                 print(img_path + " error")
#                 img_count += 1
#         print("All Done!")
#
#
# object_spider = Picture_catch()
# # ------ getHtml()内输入任意帖子的URL ------
# html_content = object_spider.get_html_content("https://tieba.baidu.com/p/5352556650").decode('UTF-8')
# # ------ 修改html对象内的字符编码为UTF-8 ------
# img_list = object_spider.get_img_url_list(html_content)
# object_spider.save_pictures(img_list)
