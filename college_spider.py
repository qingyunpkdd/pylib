#-*- encoding:utf-8 -*-
__author__ = ''
from urllib.parse import urljoin
import urllib.request
import time
import random
from lxml import etree
import lxml.html
import re

# href = ""
# # 方法一，判断文件法
# file_type = href.split(".")[-1]
# if file_type == "htm" or file_type == "html":
#     "进入链接"
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/51.0.2704.63 Safari/537.36'}

# 方法二，只关心a标签法、
def html_generator(s_url,html_page):
    html = lxml.html.fromstring(html_page)
    _xpath = '//a/@href'
    hrefs = html.xpath(_xpath)
    for href in hrefs:
        final_url = urljoin(s_url, href)
        try:
            serv_domain = final_url.split("/")[2]
            domain = serv_domain
        except:
            print("url illegel")
            domain = None
        if domain == "bme.seu.edu.cn":
            yield final_url
def find_keywords(html_page, url_p, key_word):
    #html = lxml.html.fromstring(html_page)
    #_xpath = '//*/text()'
    page_content = html_page.decode('utf-8')
    pattern = re.compile(re.escape(key_word), re.I)
    if re.search(pattern, page_content):
        print(re.search(pattern, page_content))
        fp.write(url_p)
        fp.write("\n")
        fp.write(key_word)
        fp.write("\n")
        fp.flush()
        print(key_word)
def download_and_parse(s_url):
    req = urllib.request.Request(url=s_url, headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read()
    return data
def iter_open(_url, deep, max_deep):
    try:
        if _url not in url_used:
            url_used.append(_url)
            html_page = download_and_parse(_url)
            for keyword in key_words:
                find_keywords(html_page,_url, keyword)
            if deep < max_deep:
                try:
                    url_list = [_url for _url in html_generator(_url,html_page)]
                    if url_list:
                        if len(url_list) >= 1:
                            for url_2 in url_list:
                                iter_open(url_2, deep + 1, max_deep)
                except:
                    print("url not content urls")
                    # for url in url_list:
                    #     for keyword in key_words:
                    #         html_page = download_and_parse(url_list[0])
                    #         find_keywords(html_page, keyword)
            else:
                print("reach the max_deep")
    except:
        print("page cann't download")
if __name__ == "__main__":
    max_deep = 9
    key_words = ["千人", "1000 talents", "thousand talents"]
    s_url = "http://bme.seu.edu.cn/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    url_used = []
    with open("E:\\colle_task.txt",'w')as fp:
        iter_open(s_url, 0, max_deep)

