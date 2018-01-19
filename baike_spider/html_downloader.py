import urllib.request


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        else:
            response = urllib.request.urlopen(new_url)
            if response.getcode() != 200:
                return None
            read_back = response.read()
            return read_back

