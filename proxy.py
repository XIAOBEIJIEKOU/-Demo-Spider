import requests
proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5:127.0.0.1:1080'
}
url = 'https://www.google.com'
response = requests.get(url, proxies=proxies, timeout=5)