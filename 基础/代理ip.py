from urllib.request import build_opener
from urllib.request import ProxyHandler

proxy = ProxyHandler({'http': '120.24.76.81:8123'})
opener=build_opener(proxy)
url = 'https://www.baidu.com/'
resp = opener.open(url)
print(resp.read().decode('utf-8'))
