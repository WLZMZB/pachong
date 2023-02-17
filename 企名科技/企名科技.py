import requests
import execjs
# payload = execjs.compile(open('巨潮咨询mcode.js', 'r', encoding='utf-8').read()).call('run123')
# print(payload)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.qimingpian.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'num': '20',
    'time_interval': '',
    'unionid': '',
}

response = requests.post('https://vipapi.qimingpian.cn/Activity/combineList', headers=headers, data=data).json()
# print(response)
data = response['encrypt_data']
# print(data)
decryptData = execjs.compile(open('企名科技.js', 'r', encoding='utf-8').read()).call('main123', data)
print(decryptData)