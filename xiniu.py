import requests
import execjs

payload = execjs.compile(open('./xiniu.js', 'r', encoding='utf-8').read()).call('main123')
print(payload)
cookies = {
    'btoken': '2GDTC0RJFA6989V2TK5SEIQOLFXQE9D6',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1676378068',
    'hy_data_2020_id': '1864feb5554a55-03e673372aa9ae-74525476-1600000-1864feb5555133c',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%221864feb5554a55-03e673372aa9ae-74525476-1600000-1864feb5555133c%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%221864feb5554a55-03e673372aa9ae-74525476-1600000-1864feb5555133c%22%7D',
    'export_notice': 'true',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'btoken=2GDTC0RJFA6989V2TK5SEIQOLFXQE9D6; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1676378068; hy_data_2020_id=1864feb5554a55-03e673372aa9ae-74525476-1600000-1864feb5555133c; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%221864feb5554a55-03e673372aa9ae-74525476-1600000-1864feb5555133c%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%221864feb5554a55-03e673372aa9ae-74525476-1600000-1864feb5555133c%22%7D; export_notice=true',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
}

json_data = {
    'payload': payload['payload'],
    'sig': payload['sig'],
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
# print(response)
data = response['d']
# print(data)
decryptData = execjs.compile(open('./xiniu.js', 'r', encoding='utf-8').read()).call('decrypt123', data)
print(decryptData)

