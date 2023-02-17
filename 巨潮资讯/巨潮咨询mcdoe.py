import execjs
import requests
from os.path import realpath,dirname
import js2py
def get_js():
    payload = execjs.compile(open('巨潮咨询mcode.js', 'r', encoding='utf-8').read()).call('run123')
    print(payload)
    return payload
mocde = get_js()


cookies = {
    'JSESSIONID': '75A0A7B8BBB912D66435E97C3FCA35B6',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=75A0A7B8BBB912D66435E97C3FCA35B6',
    'Origin': 'http://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://webapi.cninfo.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'X-Requested-With': 'XMLHttpRequest',
    'mcode': mocde,
}

data = {
    'tdate': '2023-02-14',
    'market': 'SZE',
}

response = requests.post(
    'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007',
    # cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)
print(response.json())
# if __name__ == '__main__':

