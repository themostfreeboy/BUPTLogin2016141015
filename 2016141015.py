#!/usr/bin/env python  
# coding=utf-8
# 北邮网关登陆

import urllib2
import urllib
import re
import os

class Loginer():
    def __init__(self, username, password):
        self.loginUrl = 'http://10.3.8.211/'
        self.username = username
        self.password = password
        self.openner = urllib2.build_opener()

    def login(self):
        postdata = {
            'DDDDD': self.username,
            'upass': self.password,
            'savePWD': 0,
            '0MKKey': ''
        }
        postdata = urllib.urlencode(postdata)
        myRequest = urllib2.Request(url=self.loginUrl, data=postdata)
        #         myRequest.add_header('Referer','http://10.3.8.211/')
        #         myRequest.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 UBrowser/1.0.739.0 Safari/537.36')

        result = self.openner.open(myRequest).read()
        unicodePage = result.decode('gb2312')
        #         print unicodePage
        msg = re.findall('<title>(.*?)</title>', unicodePage)[0]
        if msg.encode('utf-8') == '登录成功窗':
            print 'user: ', self.username, '    login success! '
        else:
            print 'user: ', self.username, '    login fail! '


def main():
    l = Loginer('2016141015', '02884197169') #用户在这里输入自己的学号与密码
    l.login()


if __name__ == '__main__':
    main()

os.system("pause")