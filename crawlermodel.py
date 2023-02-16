import requests
from lxml import etree

"""
1.发送请求
2.页面解析
3.数据分析
4.其他
"""


class Request:
    """
    请求类
    """

    def request_home(self, url, header):
        """
        用于获取resp.text
        :param url:
        :param header:
        :return:
        """
        resp = requests.get(url, header)
        return resp.text

    def request_json(self, url, header):
        """
        用于json数据获取，返回的是json
        :param url:
        :param header:
        :return:
        """
        resp = requests.get(url, header)
        json = resp.json()
        return json


class Webparse:
    """
    页面解析类
    """

    @staticmethod
    def tolxml(resp_text):
        """
        将resp.text转为lxml
        :param resp_text:
        :return:
        """
        lxml = etree.HTML(resp_text)
        return lxml

    @staticmethod
    def getlxml(url, header):
        """
        直接获取lxml
        :param url:
        :param header:
        :return:
        """
        lxml = etree.HTML(Request().request_home(url, header))
        return lxml

    def xpathtext(self, lxml, xpath):
        """
        获取文字
        :param lxml:
        :param xpath:
        :return:
        """
        text = lxml.xpath(xpath + '/text()')
        return text

    def xpathhref(self, lxml, xpath):
        """
        获取href标签
        :param lxml:
        :param xpath:
        :return:
        """
        href = lxml.xpath(xpath + '/@href')
        return href

    def xpathscr(self, lxml, xpath):
        """
        获取图片链接
        :param lxml:
        :param xpath:
        :return:
        """
        scr = lxml.xpath(xpath + '/@scr')
        return scr

    def lablecount(self, lxml, xpath):
        """
        统计标签数量
        :param lxml:
        :param xpath:标签的xpath路径
        :return:
        """
        count = len(lxml.xpath(xpath))
        return count

    pass


class DataAnalysis:
    """
    数据处理类
    """
    @staticmethod
    def delstring(text, delstr):
        """
        传入原字符串，删除不需要的字符后返回新字符串
        :param text:原字符串
        :param delstr:要删除的文字
        :return:
        """
        newstr = text.replace(delstr, '')
        return newstr
        pass

    def json_analyse(self):
        pass


def gettext(url, header, xpath):
    """
    用于直提取网页文字
    :param url:
    :param header:
    :param xpath:文字xpath路径
    :return:
    """
    html = Webparse().tolxml(Request().request_home(url, header))
    text = Webparse().xpathtext(html, xpath)
    return text


def geturl(url, header, xpath):
    """
    用于直接获取跳转页面url,已添加前缀'https:',返回link可直接使用
    :param url:
    :param header:
    :param xpath:href的xpath路径
    :return:
    """
    html = Webparse().tolxml(Request().request_home(url, header))
    link = Webparse().xpathhref(html, xpath)
    link = 'https:' + link[0]
    return link
