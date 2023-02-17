import requests
from lxml import etree
import csv
import pandas as pd

def get_html():
    url = 'https://api.bilibili.com/pgc/web/rank/list?day=3&season_type=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    resp = requests.get(url, headers=headers)
    # html = etree.HTML(resp.text)
    json= resp.json()
    return json


# pricels = []
namels = []


def get_xpath(html):
    s = len(html.xpath('//*[@id="app"]/div[2]/div[1]/ul[2]/li'))
    for i in range(1, s + 1):
        # pricexpath = html.xpath('//*[@id="app"]/div[2]/div[1]/ul[2]/li[1]/text()'.format(i))
        # pricels.append(pricexpath)
        namexpath = html.xpath('//*[@id="app"]/div[2]/div[1]/ul[2]/li[{}]/text()'.format(i))
        namels.append(namexpath)


def csvwriter():
    count = 1
    file = open('bilibili恋爱动画.csv', 'a+', encoding='gbk', newline='')
    writer = csv.writer(file)
    for name in namels:
        row = '第{}名'.format(count), name
        writer.writerow(row)
        count += 1
        # 一次写多行
        # writer.writerows()


def savedata(json):
    badge_list = []
    rating_list = []
    season_id_list = []
    title_list = []
    url_list = []
    list0 = json['result']['list']
    for item in list0:
        badge_list.append(item['badge'])
        rating_list.append(item['rating'])
        season_id_list.append(item['season_id'])
        title_list.append(item['title'])
        url_list.append(item['url'])
    dict0 = {
        'badge': badge_list,
        'rating': rating_list,
        'season_id': season_id_list,
        'title': title_list,
        'url': url_list
    }
    df = pd.DataFrame(dict0)

    df.to_excel('bilibili番剧排行.xlsx', index=True, header=True)

    print(df)

if __name__ == '__main__':
    # get_xpath(get_html())
    print(get_html()['result']['list'])
    savedata(get_html())
