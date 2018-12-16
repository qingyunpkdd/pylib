#-*- encoding:utf-8 -*-
__author__ = 'qingyun'
import urllib


class HaGongDaLTP():
#this class using LTP as word segmentation tools
#information
# Email:	qingyun891@126.com
# Api_key:	11x3Q768B0mY9KGZ2sZlinNc1n0jFVwfSW2GVVPx
# 本月流量使用：	0 bytes
# 本月剩余流量：	18.6 GB
    def __init__(self,text,pattern,formats):
        self.text = text
        self.pattern = pattern
        self.formats = formats
        url_get_base = "http://api.ltp-cloud.com/analysis/"
        args = {
            'api_key': '11x3Q768B0mY9KGZ2sZlinNc1n0jFVwfSW2GVVPx',
            'text': self.text,
            'pattern': self.pattern,
            'format': self.formats
        }
        result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
        content = result.read().strip()
        return content
class FuDanWS():
#this class using the result of the fudan word segmentation
    pass
if __name__ == '__main__':
