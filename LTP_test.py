#-*- encoding:utf-8 -*-
__author__ = ''
import urllib2
#http://blog.csdn.net/churximi/article/details/51173297
#http://blog.csdn.net/mebiuw/article/details/52496920
# -*- coding:utf8 -*-
url_get_base = "http://api.ltp-cloud.com/analysis/?"
api_key = '01b1z382Y6QDFjxHup2Y4F3f3O8CxKzNAWlzgKsQ'      # 输入注册API_KEY

# 待分析的文本
text = "语言技术平台(LTP) 是由 哈工大社会计算与信息检索研究中心 11"

format0 = 'xml'  # 结果格式，有xml、json、conll、plain（不可改成大写）
pattern = 'srl'  # 指定分析模式，有ws、pos、ner、dp、sdp、srl和all

result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s"
                         % (url_get_base, api_key, text, format0, pattern))
content = result.read().strip()
print content

# -*- coding: utf-8 -*-
#!/usr/bin/env python

# This example shows how to use Python to access the LTP API to perform full
# stack Chinese text analysis including word segmentation, POS tagging, dep-
# endency parsing, name entity recognization and semantic role labeling and
# get the result in specified format.

# import urllib2, urllib
# import sys
#
# if __name__ == '__main__':
#     # if len(sys.argv) < 2 or sys.argv[1] not in ["xml", "json", "conll"]:
#     #     print >> sys.stderr, "usage: %s [xml/json/conll]" % sys.argv[0]
#     #     sys.exit(1)
#
#     uri_base = "http://ltpapi.voicecloud.cn/analysis/?"
#     api_key  = "01b1z382Y6QDFjxHup2Y4F3f3O8CxKzNAWlzgKsQ"
#     text     = "我爱北京天安门"
#     # Note that if your text contain special characters such as linefeed or '&',
#     # you need to use urlencode to encode your data
#     text     = urllib.quote(text)
#     #format   = sys.argv[1]
#     format = "plain"
#     pattern  = "all"
#
#     url      = (uri_base
#                + "api_key=" + api_key + "&"
#                + "text="    + text    + "&"
#                + "format="  + format  + "&"
#                + "pattern=" + "all")
#
#     try:
#         response = urllib2.urlopen(url)
#         content  = response.read().strip()
#         print content
#     except urllib2.HTTPError, e:
#         print >> sys.stderr, e.reason