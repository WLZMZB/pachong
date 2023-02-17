import requests
from lxml import etree
import csv


def get_html():
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid' \
          '=8858151673f941e9b1a4d2c7214b2b52&psort=3&click=0 '
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)
    return html


pricels = []
namels = []


def get_xpath(html):
    s = len(html.xpath('// *[ @ id = "J_goodsList"]/ul/li'))
    for i in range(1, s + 1):
        pricexpath = html.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[3]/strong/i/text()'.format(i))
        pricels.append(pricexpath)
        namexpath = html.xpath('//*[@id="J_goodsList"]/ul/li[{}]/div/div[4]/a/em/text()'.format(i))
        namels.append(namexpath)


def csvwriter():
    count = 1
    file = open('../demo.csv', 'a+', encoding='gbk', newline='')
    writer = csv.writer(file)
    for name, price in zip(namels, pricels):
        row = '第{}名'.format(count), name, '售价：', price, '元'
        writer.writerow(row)
        count += 1
        # 一次写多行
        # writer.writerows()


if __name__ == '__main__':
    get_xpath(get_html())
    csvwriter()
