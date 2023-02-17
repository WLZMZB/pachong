import base64

import requests


url = 'https://rl01-sycdn.kuwo.cn/f24c91b8ba2cbf3d81c7b290ce4751a0/63eb231f/resource/n3/23/85/2346642937.mp3'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
resp = requests.get(url).content
with open('../너의 의미.mp3', 'wb') as f:
    f.write(resp)
