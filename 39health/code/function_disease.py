#-*- encoding:utf-8 -*-
__author__ = ''
__author__ = ''
# -*- coding:utf-8 -*-
#import urllib2
import urllib2
import re
import sys
import lxml
import html5lib
from bs4 import BeautifulSoup
from gzip import GzipFile
from StringIO import StringIO
import zlib
reload(sys)
sys.setdefaultencoding('utf-8')
#疾病部分
#测试代码
# ########################
# dir = "d:\\tem\\test.html"
# all_text = open(dir).read().decode('gbk')
# soup = BeautifulSoup(all_text)
#
# ############################################################################

dis = {}
dis_ref = {}
pages = 780
urllist = ["http://jbk.39.net/bw_t1"]
urlr = "http://jbk.39.net/bw_t1_p"
urllist.extend([urlr + str(pagei) + "#ps" for pagei in range(pages)[1:]])
def page_processing(url):
    url = url
    def gzip(data):
        buf = StringIO(data)
        f = GzipFile(fileobj=buf)
        return f.read()

    def deflate(data):
        try:
            return zlib.decompress(data, -zlib.MAX_WBITS)
        except zlib.error:
            return zlib.decompress(data)

    def loadData(url):
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        headers = {'User-Agent': user_agent}
        request = urllib2.Request(url, headers=headers)
        #request.add_header('Accept-encoding', 'gzip,deflate')
        response = urllib2.urlopen(request,timeout=3)
        content = response.read()
        encoding = response.info().get('Content-Encoding')
        if encoding == 'gzip':
            content = gzip(content)
        elif encoding == 'deflate':
            content = deflate(content)
        return content
    r = 1
    while r==1:
        try:
            the_page = loadData(str(url)).decode('gbk')
        except:
            r = 1
        else:
            r = 0
    soup = BeautifulSoup(the_page)
    distem = {}
    dis_reftem = {}
    disease_item = soup.select('div div[dtype="1"]')

    def find_id(stri,type=1):#1,代表疾病，2，代表症状
        if type == 1:
            id = re.match('http://jbk.39.net/(.*?)/', stri.get('href'), re.S).group(1)
        elif type == 2:
            id = re.match('http://jbk.39.net/zhengzhuang/(.*?)/', stri.get('href'), re.S).group(1)
        return id
    for d in disease_item:
        dd = d.select('a[title]')[0]
        sym = []
        resym = []
        if d.p:sym = [ds.get_text() for ds in d.p.find_all('a')]
        if d.p:resym = [find_id(res, type=2) for res in d.p.find_all('a')]
        distem[find_id(dd,type=1)] = resym
        dis_reftem[find_id(dd,type=1)] = [dd.get('title'),sym]
    return distem,dis_reftem
#网页处理入口
#def main():
for url in urllist[528:644]:
    print "processing page:"+url
    ds, df = page_processing(str(url))
    #dis = dict(ds.items()+dis.items())
    dis.update(ds)
    dis_ref = dict(df.items()+dis_ref.items())
    dis_ref.update(df)
    print url+":done!"
#return dis,dis_ref
dirdf = "d:\\tem\\disease_reference3.txt"
dirds = "d:\\tem\\disease3.txt"
with open(dirdf,"w") as f:
    print 'writefile...'
    for df in dis_ref.iteritems():
        f.write(df[0])
        f.write(':')
        f.write(df[1][0].encode('utf-8'))
        f.write(':')
        [f.write(rf.encode('utf-8')+',') for rf in df[1][1]]
        f.write('\n')
    f.close()
with open(dirds,"w") as f:
    for ds in dis.iteritems():
        f.write(ds[0])
        f.write(':')
        [f.write(dss + ',') for dss in ds[1]]
        f.write('\n')
    f.close()
###############################################################################