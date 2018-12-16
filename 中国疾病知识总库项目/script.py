# -*- coding:utf-8 -*-
#import urllib2
import urllib2
import re
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

#build url
idexs = ["00000"]
for i in range(99999):
    if len(str(i)) < 5:
        idn = "0" * (5 - len(str(i))) + str(i)
    else:
        idn = str(i)
    idexs.append(idn)
for j in idexs[39298:40000]:
    url = "http://pmmp.cnki.net/cdd/Disease/dis_detail.aspx?id=" + str(j) + "&SearchType=1"
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    #the_page = response.read().decode('gbk')
    the_page = response.read().decode('gbk')
    soup = BeautifulSoup(the_page)
    a = soup.title.string
    text = soup.get_text()
    if a != (u'温馨提示'):
        print "yes"+ str(j)
        dir = "e:\\medical\\" + str(j) + ".txt"
        f = open(dir,'wt')
        #f.write(text.encode('gbk'))
        f.write(text.encode())
        f.close()
    else:
        print "no find" + str(j)