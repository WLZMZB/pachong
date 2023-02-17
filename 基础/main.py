import requests
from lxml import etree

def send_requst():
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid' \
          '=8858151673f941e9b1a4d2c7214b2b52&psort=3&click=0 '
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    resp = requests.get(url, headers=headers)
    return resp.text
def gettext():
    ulxpath = '//*[@id="J_goodsList"]/ul/li/text()'


def start():
    print(send_requst())


if __name__ == '__main__':
    start()
