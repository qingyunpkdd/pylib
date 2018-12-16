#-*- encoding:utf-8 -*-
import urllib

import os, sys
from LTML import LTML
import sys
import urllib, urllib2
__author__ = ''
reload(sys)
sys.setdefaultencoding("utf-8")

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
    def fenci(self):
        ltml = LTML()
        ltml.build_from_words(["自定义", "分词", "结果", "的", "示例"])
        xml = ltml.tostring()

        uri_base = "http://ltpapi.voicecloud.cn/analysis/?"

        data = {
            "api_key": "11x3Q768B0mY9KGZ2sZlinNc1n0jFVwfSW2GVVPx",
            "text": xml,
            "format": "plain",
            "pattern": "pos",
            "xml_input": "true"
        }

        params = urllib.urlencode(data)

        try:
            request = urllib2.Request(uri_base)
            response = urllib2.urlopen(request, params)
            content = response.read().strip()
            print content
        except urllib2.HTTPError, e:
            print >> sys.stderr, e.reason
        return content



if __name__ == '__main__':
    des_dir = "D:\\chinese\\d120ask_all_case_merge"
    count = 0
    for filename in os.listdir(des_dir):
        filename = des_dir + "\\" + filename
        with open(filename,'r') as fp:
            cont = fp.read()
            fenci_ins = HaGongDaLTP(cont,pattern="ws",formats="plain")
            cont = fenci_ins.fenci()
        with open(filename, 'w') as fp:
            fp.write(cont)
