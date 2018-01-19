import urllib
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse


class HtmlParser(object):
    def parse(self, new_url, html_content):
        if new_url is None or html_content is None:
            return
        # 将html转化成soup对象再进行处理，输入的页面内容是html_content，解释器是html.parser[解析html]，内容原本编码
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(new_url, soup)
        new_datas = self._get_new_datas(new_url, soup)
        return new_urls, new_datas

    # 处理页面中关联的href
    def _get_new_urls(self, new_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            need_add_new_url = link['href']
            # 将相对href转成绝对href
            new_full_url = urllib.parse.urlparse(new_url, need_add_new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 处理页面中的数据
    def _get_new_datas(self, new_url, soup):
        redis_datas = {}
        redis_datas['url'] = new_url
        # 需要字段的tag+class，定位
        node_title = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        redis_datas['title'] = node_title.get_text()
        # class ="lemma-summary"
        node_content = soup.find('div', class_="lemma-summary")
        redis_datas['content'] = node_content.get_text()
        return redis_datas
