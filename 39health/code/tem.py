#-*- encoding:utf-8 -*-
__author__ = ''
from lxml import etree
from io import StringIO
import urllib2
import requests


url = "https://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?rs=429358"
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {'User-Agent': user_agent}
init_page = requests.get(url).text

parser = etree.HTMLParser()
html = etree.parse(StringIO(init_page), parser)


itme1 = html.xpath('//div[@id="imaps-result"]//tbody/text()')
itme1 = html.xpath('//div[@id="imaps-result"]//tbody[1]/tr[1]/td[3]/a/text()')
#//*[@id="ui-ncbigrid-1"]/tbody/tr[1]/td[3]/a
item1 = html.xpath('//div[@class="ui-ncbigrid-inner-div"]//tbody/tr[1]/td[3]/a/text()')
item2 = html.xpath('//*[@class="ui-ncbigrid-inner-div"]//tbody/tr[1]/td[4]/a/text()')
item3 = html.xpath('//*[@class="ui-ncbigrid-inner-div"]//tbody/tr[2]/td[3]/a/text()')
item4 = html.xpath('//*[@class="ui-ncbigrid-inner-div"]//tbody/tr[2]/td[3]/a/text()')

item_gene = html.xpath('//*[@id="gv-gene-container"]/div[1]/span/a/@title')
# 标号是从1开始的
# //*[@id="ui-ncbigrid-1"]/tbody/tr[1]/td[3]/a/text()
# //*[@id="ui-ncbigrid-1"]/tbody/tr[1]/td[4]/a/text()
# //*[@id="ui-ncbigrid-1"]/tbody/tr[2]/td[3]/a/text()
# //*[@id="ui-ncbigrid-1"]/tbody/tr[2]/td[4]/a/text()
#
#
#
# //*[@id="gv-gene-GRCh38_p7-348"]/h4/span[1]/a
# 基因名称
# //*[@id="gv-gene-container"]/div[1]/span/a/@title
# //*[@id="gv-gene-container"]/div[1]/span/a/@title/text()

