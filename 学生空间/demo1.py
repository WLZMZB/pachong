"""
password加密方式为一次MD5后两次sha1
"""
import hashlib

text = "123456"


def encrypt(t):
    """
    :param t:待加密内容
    :type t: str
    """
    print('需要加密的内容是：', t)
    md5 = hashlib.new('md5', t.encode(encoding='utf8')).hexdigest()
    print('md5加密结果：', md5.upper())
    sha1 = hashlib.new('sha1', md5.encode(encoding='utf8').upper()).hexdigest()
    print("sha1加密结果1：" + sha1.upper())
    sha2 = hashlib.new('sha1', sha1.encode(encoding='utf8').upper()).hexdigest()
    print("sha1加密结果2：" + sha2.upper())
    return sha2


if __name__ == '__main__':
    encrypt(text)
