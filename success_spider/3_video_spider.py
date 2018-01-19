import re
# Requests 是用Python语言编写，基于 urllib
import os
import requests
from bs4 import BeautifulSoup


def get_html_content(url):
    request_header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    }
    # 伪装请求header
    html_content = requests.get(url, headers=request_header).text
    # 加‘b’的方式是二进制方式，于是没有编码的错误，类似于str和byte的错误
    file_out = open('video_html_content.html', 'wb')
    file_out.write(html_content.encode('utf-8'))
    return html_content


def get_video_urls_by_node(html_cotent):
    links = []
    soup = BeautifulSoup(html_cotent, 'html.parser', from_encoding='utf-8')
    # class_是方法自带的参数，表示以类名过滤，text表示ctrl+f，href表示url，id表示id属性
    all_video = soup.find_all(class_=" j-video")
    for link in all_video:
        url = link.attrs.get('data-mp4')
        links.append(url)
    return links


def get_video_by_re(html_cotent):
    soup = BeautifulSoup(html_cotent, 'html.parser', from_encoding='utf-8')
    # all_video = soup.find_all('div', text= re.compile(r"^http://mvideo\.spriteapp\.cn/video/2018/0115/?\.mp4$"))
    # 可以通过find_all()方法的attrs参数定义一个字典参数来搜索包含特殊属性的tag
    all_video = soup.find_all(attrs={'data-mp4': re.compile(r"^http://mvideo.spriteapp.cn/video/2018/0115/?.mp4$")})
    return all_video


def download_video(all_video_links):
    count = 1
    path = 'D:/video/'
    if not os.path.exists(path):
        os.makedirs(path)
    for link in all_video_links:
        # open打开文件后将返回的文件流对象赋值给forder，然后在with语句块中使用
        # with语句块完毕之后，会隐藏地自动关闭文件。
        # with后的方法执行完之后会自动关闭，因为是以流的形式进行的所以结束请求后关闭节约资源
        # 以chunk（128k的一个字节流块）的方式循环写入
        # response = requests.get(link, stream=True)
        from contextlib import closing
        with closing(requests.get(link, stream=True, timeout=100)) as response:
            with open(path + str(count) + ".mp4", 'wb') as forder:
                for chunk in response.iter_content(128):
                    forder.write(chunk)
        print('done :',  count)
        count += 1
    print('all done!')


def main():
    url = 'http://www.budejie.com/'
    html_cotent = get_html_content(url)
    all_video_links = get_video_urls_by_node(html_cotent)
    # get_video_by_re(html_cotent)
    download_video(all_video_links)


# 让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行。
if __name__ == '__main__':
    main()
