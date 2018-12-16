#/usr/bin/env python
#coding=utf8
#ref : http://blog.csdn.net/haolexiao/article/details/54913740
import httplib
import hashlib
import urllib
import random
import sys
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )
appid = '20170816000074203'
secretKey = 'dXos7IIsRCDiLPwk6a5i'

def TranslateByBaidu(q = 'apple',fromLang = 'auto',toLang = 'zh'):
    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        #response是HTTPResponse对象
        response = httpClient.getresponse()
        result = response.read()
        data = json.loads(result)
        str_res = data["trans_result"][0]["dst"]
        return str_res
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
