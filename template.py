#-*- encoding:utf-8 -*-
import os
import urllib.request
import time
import random
from lxml import etree
import lxml.html


creature = ["coral","symbiodinium","Scleractinia","Alcyonacea","endosymbiont","dinoflagellate","cnidarian"]
func_rna = ["microrna","mirna","sirna","lncrna"]
evolution = ["phylogenetic","evolutionary"]
url_init = "https://www.ncbi.nlm.nih.gov/pubmed/?term={key_words}"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
i = 0
#def html_parse(data):
def parse_w(creature,func):
    global i
    for c in creature:
        for f in func:
            time.sleep(random.randint(1,10))
            keyws =c + "+" + f
            url = url_init.format(key_words=keyws)
            print("search for ",url)
            req = urllib.request.Request(url=url,headers=headers)
            res = urllib.request.urlopen(req)
            data = res.read()
            html = lxml.html.fromstring(data)
            count = html.xpath('//*[@id="resultcount"]/@value')
            if count:
                print(count)
                fp.write(keyws)
                fp.write("\t")
                fp.write(count[0])
                fp.write("\n")
                i+=1
                print("done!",i)
            else:
                raise "count error"
if __name__ == "__main__":
    with open("E:\\result.txt", 'w') as fp:
        parse_w(creature,func_rna)
        parse_w(creature,evolution)
