import requests

cookies = {
    'route': '65389440feb63b53ee0576493abca26d',
    'SECKEY_ABVK': 'C8286kJRAVlwUcLhrilC0WPswSPvoHywgCBLaL8UWeU%3D',
    'BMAP_SECKEY': 'h3RZxVzaJW4GCj9Q4dQD1lIF7QCy8gasdp3UOhRJncpiM0ObWLhs8V3e89Au14RH3EIn4xUH7NWyZVi1fDUfKHFBMVxHqZd0Nb0neHO1iJUXBIQLDTZwdU0TmgvJ0WQ5RTeEKIvYh5immKS9XYYOIVNw_5cb741N2GgQTIiqzRtARnhBeMDxcyffVPx9Hib8',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'route=65389440feb63b53ee0576493abca26d; SECKEY_ABVK=C8286kJRAVlwUcLhrilC0WPswSPvoHywgCBLaL8UWeU%3D; BMAP_SECKEY=h3RZxVzaJW4GCj9Q4dQD1lIF7QCy8gasdp3UOhRJncpiM0ObWLhs8V3e89Au14RH3EIn4xUH7NWyZVi1fDUfKHFBMVxHqZd0Nb0neHO1iJUXBIQLDTZwdU0TmgvJ0WQ5RTeEKIvYh5immKS9XYYOIVNw_5cb741N2GgQTIiqzRtARnhBeMDxcyffVPx9Hib8',
    'Origin': 'https://ys.endata.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ys.endata.cn/BoxOffice/Ranking',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'r': '0.668356297214868',
    'top': '50',
    'type': '0',
}

response = requests.post(
    'https://ys.endata.cn/enlib-api/api/home/getrank_mainland.do',
    # cookies=cookies,
    headers=headers,
    data=data,
).json()
print(response)