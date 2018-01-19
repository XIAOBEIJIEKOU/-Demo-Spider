class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_datas):
        if new_datas is None:
            return
        # 将所有的数据都存在内存中然后循环结束后一起输出
        self.datas.append(new_datas)

    def output_html(self):
        file_out = open('output.txt', 'wb')
        for data in self.datas:
            file_out.write(data['url'].encode('utf-8'))
            file_out.write(data['title'].encode('utf-8'))
            file_out.write(data['content'].encode('utf-8'))
        file_out.close()

    def output_txt_once(self, data):
        file_out = open('output1.txt', 'wb')
        file_out.write(data['url'].encode('utf-8'))
        file_out.write(data['title'].encode('utf-8'))
        file_out.write(data['content'].encode('utf-8'))
        file_out.close()

