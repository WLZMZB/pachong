# i = (new Date).getTime()
# j = h(d.token + "&" + i + "&" + g + "&" + c.data)
import time

import execjs
import requests

i = round(time.time()*1000)
# print(i)
g = "12574478"
# i = '1676618605455'
token = 'a46557322dbbb34f9a5b5768120fea6e'
data = '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"query\\":\\"mainCate=54&leafCate=\\",\\"sort\\":\\"mix\\",\\"pageNo\\":\\"1\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"trafficSource\\":\\"pc_index_recommend\\"}"}'
cdata = '{"fcGroup":"cbu-seller-fc","fcName":"zgc-promotion-component","serviceName":"categoryBaseInfoService","params":"{\\"cateId\\":\\"54\\",\\"leafCateId\\":\\"\\"}"}'
sign = token + "&" + str(i) + "&" + g + "&" + cdata
ctx = execjs.compile(open('1688sign加密.js', 'r', encoding='utf-8').read()).call('h', sign)
print(ctx)

cookies = {
    '_m_h5_tk': 'a46557322dbbb34f9a5b5768120fea6e_1676618940250',
    '_m_h5_tk_enc': 'b73289d2a3d1d7a2767c2f12575a9612',
    'cookie2': '15fc5af4dc0ba9e12c30ef9370844883',
    't': 'a76a5c2293ed206e0ef588be2647ead8',
    '_tb_token_': '3fb53e3d945be',
    '__cn_logon__': 'false',
    'xlly_s': '1',
    'cna': '8v51HImNHWACAa303UgkINb0',
    'alicnweb': 'touch_tb_at%3D1676615883061',
    'tfstk': 'c7tfB9wavSVbBgigmsMrQR0JUWSVZ4cCUr1vhj0r9aa-uQvfiDZFOrxPS7jNBT1..',
    'l': 'fBSslZxrTt52t1ToBOfwPurza77OSIRAguPzaNbMi9fPO_fk5wuCW6-HaA8DC3GVFsdHR3SYy-iBBeYBqnDhzC_njsx8SPDmnmOk-Wf..',
    'isg': 'BDU169pkuhsKgd6nN5YbvF6uRLHvsunEbrLzErda8az6jlWAfwL5lEMM2FK4zgF8',
}

headers = {
    # 'authority': 'h5api.m.1688.com',
    # 'accept': '*/*',
    # 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': '_m_h5_tk=a46557322dbbb34f9a5b5768120fea6e_1676618940250; _m_h5_tk_enc=b73289d2a3d1d7a2767c2f12575a9612; cookie2=15fc5af4dc0ba9e12c30ef9370844883; t=a76a5c2293ed206e0ef588be2647ead8; _tb_token_=3fb53e3d945be; __cn_logon__=false; xlly_s=1; cna=8v51HImNHWACAa303UgkINb0; alicnweb=touch_tb_at%3D1676615883061; isg=BPHxpOgQNm9Zypp7UyoniHI6AH2L3mVQ0oY3btMG7bjX-hFMGy51IJ8YHI6cMv2I; tfstk=cL3NBVcwZFLa59Gvey4q4nUimdXOaUwgpePzjKw7lOZcZHqgUsXlHWm9MXlVTtqG.; l=fBSslZxrTt52tb7CBOfwPurza77OSIRAguPzaNbMi9fPOHfw5sqFW6-H17TeC3GVFsxMR3SYy-iBBeYBq3xonxvtjsx8SPDmngzr905..',
    'referer': 'https://sale.1688.com/',
    # 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'script',
    # 'sec-fetch-mode': 'no-cors',
    # 'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
}

params = {
    'jsv': '2.6.1',
    'appKey': '12574478',
    't': i,
    'sign': ctx,
    'v': '1.0',
    'type': 'jsonp',
    'isSec': '0',
    'timeout': '20000',
    'api': 'mtop.taobao.widgetService.getJsonComponent',
    'dataType': 'jsonp',
    'jsonpIncPrefix': 'mboxfc',
    'callback': 'mtopjsonpmboxfc3',
    'data': '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"query\\":\\"mainCate=54&leafCate=\\",\\"sort\\":\\"mix\\",\\"pageNo\\":\\"1\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"trafficSource\\":\\"pc_index_recommend\\"}"}',
}
#
response = requests.get(
    'https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)

