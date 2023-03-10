import urllib.request
from http import cookiejar

filename = 'cookie.txt'


# 获取cookie
def get_cookie():
    # （1）实例化一个MozillaCookieJar （用于保存cookie）
    cookie = cookiejar.MozillaCookieJar(filename)
    # （2）创建handler对象
    handler = urllib.request.HTTPCookieProcessor(cookie)
    # （3）创建opener对象
    opener = urllib.request.build_opener(handler)
    # （4）请求网址
    url = 'https://tieba.baidu.com/'

    resp = opener.open(url)
    # （5）储存cookie文件
    cookie.save()


# 读取cookie
def use_cookie():
    # 实例化MozillaCookieJar
    cookie = cookiejar.MozillaCookieJar()
    # 加载cookie文件
    cookie.load((filename))
    print(cookie)


if __name__ == '__main__':
    # get_cookie()
    use_cookie()
