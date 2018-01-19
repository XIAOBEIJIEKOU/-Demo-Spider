# 引入的时候存在一个module（baike_spider）的概念，module下面再分Class，Class与文件（.py）没有必然关联
from baike_spider import urls_manager, html_downloader, html_outputer, html_parser


class Spiderman(object):
    # self代表类的实例，而非类
    def __init__(self):
        # url管理器
        self.urls = urls_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParser()
        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 将需要爬虫的url放进待操作set中
        self.urls.add_new_url(root_url)
        # 从待操作set中取
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('loading : ', count)
                # 下载页面html
                html_content = self.downloader.download(new_url)
                # 提取页面html中需要的字段，按返回name自动匹配
                new_urls, new_datas = self.parser.parse(new_url, html_content)
                # 将页面关联的href增加到待爬虫set
                # 这个程序的url传入有问题
                print(new_urls)
                self.urls.add_new_urls(new_urls)
                # 输出
                self.outputer.collect_data(new_datas)
                count += 1
                if count == 1001:
                    break
            except Exception as e:
                print("failure!")

        # 一次性全部写入
        self.outputer.output_html()


if __name__ == '__main__':
    # 实例化本身，省略了main函数
    obj_spider = Spiderman()
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider.craw(root_url)
