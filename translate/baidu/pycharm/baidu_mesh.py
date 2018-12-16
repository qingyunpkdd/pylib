#-*- encoding:utf-8 -*-
__author__ = ''
#form the mesh_data parsing the xml file
from lxml import etree
def xml_parse():
    xml_file = etree.parse(r'D:\translate\baidu\desc2017.xml')
    root_node = xml_file.getroot()
    concept_list = xml_file.xpath('//DescriptorRecord/DescriptorName/String/text()')
    return concept_list
#translate each concept for future parsing
import httplib
import hashlib
import urllib
import random
import sys, os
import re
reload(sys)
sys.setdefaultencoding( "utf-8" )
i = 0
concept_list = xml_parse()
def translate_p(concept):
    test_source_content = str(concept)
    appid = '20170816000074203'
    secretKey = 'dXos7IIsRCDiLPwk6a5i'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = test_source_content
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    m1 = hashlib.md5()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_td = response.read().decode('utf-8')
        response_en = re.findall(r'"src":"(.*?)"',result_td)[0]
        response_zh = re.findall(r'"dst":"(.*?)"',result_td)[0].decode('unicode_escape')
        #print response.read()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    resp = [response_en,response_zh]
    return resp
dir_translated = "D:\\translate\\baidu\\"
fp = open(dir_translated + 'exp.txt', 'a')
for concept in concept_list:
    #translate result for example as {"from":"en","to":"zh","trans_result":[{"src":"Temefos","dst":"\u66ff\u7f8e\u78f7"}]}
    resp = translate_p()
    response_en,response_zh = resp
    fp.write(response_en)
    fp.write("@")
    fp.write(response_zh)
    fp.write('\n')
fp.close()