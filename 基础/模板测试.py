import re

from 基础 import crawlermodel as cm
from 基础.crawlermodel import gettext, geturl
import pandas as pd

# text/html; charset=gb2312
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb2312')


def zhihutest():
    url0 = f"https://www.zhihu.com/people/mt36501"
    header0 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/109.0.0.0Safari/537.36 Edg/109.0.1518.70'}  # 请求头

    dataxpath = '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div/span[2]'
    hrefxpath = '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div/div/h2/span/a'
    textxpath = '/html/body/div[1]/div/main/div/article/div[1]/div/div/div/p[{}]'
    textxpathcount = '/html/body/div[1]/div/main/div/article/div[1]/div/div/div/p'
    data = gettext(url0, header0, dataxpath)
    print(data)
    article_link = geturl(url0, header0, hrefxpath)
    print(article_link)
    b2 = W.getlxml(article_link, header0)
    textlablenumbers = W.lablecount(b2, textxpathcount)
    text = ''
    for zt in range(0, textlablenumbers):
        play_count = W.xpathtext(b2, textxpath.format(zt))
        if play_count:
            text = text + play_count[0] + '\n'
    text = re.sub(r"在这里，每天60秒读懂世界！\n", '', text) + '\n——by知乎'
    print(text)


def xinan():
    url0 = 'https://yz.swufe.edu.cn/chaxun/yzbwww/tjss/ss_searchout.asp?currentpage={}&c_year=ON&year=2022'
    kongdf = pd.DataFrame()
    for i in range(1, 6):
        url1 = url0.format(i)
        table = pd.read_html(url1, header=0, encoding='gb2312')
        kongdf = pd.concat([kongdf, table[-1]], ignore_index=True)
    kongdf.to_excel('123.xlsx', index=True, header=True)

def test():
    url = 'https://mp.weixin.qq.com/s/EclitmUXQV0y0CplmzM4ow'
    header0 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/109.0.0.0Safari/537.36 Edg/109.0.1518.70'}  # 请求头
    xpath = '//*[@id="js_content"]/p[1]'
    text = gettext(url, header0, xpath)
    print(text)
if __name__ == '__main__':
    R = cm.Request()
    W = cm.Webparse()
    # zhihutest()
    # xinan()
    test()