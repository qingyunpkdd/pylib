#-*- encoding:utf-8 -*-

#python = 3.5 Aconda 虚拟环境
__author__ = ''
from urllib.parse import urljoin
import urllib.request
import time
import random
from lxml import etree
import lxml.html
import os
import re
init_url = ""


class ReefGenomeSpider():
    #info_file: save the information about the coral
    def __init__(self,init_url,base_path="E:\\coral reefs data"):
        self.init_url = init_url
        self.base_path = base_path
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
        self.page = ""
        self.pub_info = ""
        self.table_content = {}
    def get_page(self):
        req = urllib.request.Request(self.init_url, headers=self.headers)
        res = urllib.request.urlopen(req)
        self.page = res.read()
        page_content = self.page.decode('utf-8')
        selector = etree.HTML(page_content)
        #self.html_page = lxml.html.fromstring(self.page)
        self.html_page = selector
    def get_pub_info(self):
        _xpath = '//p[2]/a/@href'
        hrefs = self.html_page.xpath(_xpath)
        self.pub_info = urljoin(self.init_url,hrefs[0])  #?

    def get_content_title(self):
        try:
            _xpath = '//h1'
            cont = self.html_page.xpath(_xpath)[0].xpath('string(.)')
            self.table_content["title"] = str(cont) #?
            self.info_file = self.table_content["title"] + ".txt"
        except:
            print("parse error!")
    def table_info(self):
        _xpath = '//table'
        tables = self.html_page.xpath(_xpath)
        sub_titles = self.html_page.xpath('//h2/text()')
        h3 = self.html_page.xpath('//h3/text()')
        del sub_titles[1]
        for h3_t in h3:
            sub_titles.append(h3_t)
        # reconstruct the compare data
        # s_t = self.html_page.xpath('//h2')
        # s_f_b = s_t.xpath('local-name(./following-sibling::*)')
        # [str(s) for s in s_f_b if str(s) in ["table","h3"]]



        #sub_titles_cont = self.html_page.xpath('//h2/text()')
        #ssub_tiles = sub_titles.xpath('./following-sibling::*')[0]
        #if str(ssub_tiles.xpath('.')) == "h3":

        #new to deal
        # sub_titles = self.html_page.xpath('//h2 | //h3')
        # tem = []
        # for st in sub_titles:
        #     if  str(st.xpath('local-name(./following-sibling::*)')[0]) != "table":
        #         sub_titles
        if sub_titles:
            i = 0
            for _s in sub_titles:
                self.table_content[str(_s)] = self.parse_table_detail(tables[i])
        else:
            if len(tables) == 1:
                self.table_content["default"] = self.parse_table_detail(tables[0])
    def parse_table_detail(self,table):
        items = []
        _trs = table.xpath('//tr')
        for _tr in _trs:
            _ths = _tr.xpath('.//th | .//td')
            item = []
            for _th in _ths:
                try:
                    content = str(_th.xpath('.//text()')[0])
                except:
                    content = "NULL"
                try:
                    link = str(_th.xpath('.//a/@href')[0])
                except:
                    link = ""
                item.append(content)
                if link:
                    link = urljoin(self.init_url, link)
                    item.append(link)
            items.append(item)
        return items

    def writt_to_file(self):
            file_path = os.path.join(self.base_path,self.info_file)
            with open(file_path, 'w') as fp:
                if self.pub_info:
                    fp.write("public_if:")
                    fp.write("\n")
                    fp.write(self.pub_info)
                    fp.write("\n")
                for _key in self.table_content:
                    if isinstance(self.table_content[_key],list):
                        for _l in self.table_content[_key]:
                            tem = '\t'.join([str(ele) for ele in _l])
                            fp.write(tem)
                            fp.write("\n")
                        fp.flush()
                    elif isinstance(self.table_content[_key],str):
                        pass
                        #fp.write(self.table_content[_key])

if __name__ == "__main__":
    base_path="E:\\coral reefs data"
    url = "http://reefgenomics.org/sitemap.html"
    rgs = ReefGenomeSpider(init_url=url,base_path=base_path)
    rgs.get_page()
    #rgs.get_pub_info()
    rgs.get_content_title()
    rgs.table_info()
    rgs.writt_to_file()







