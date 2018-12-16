#-*- encoding:utf-8 -*-
__author__ = ''
import lxml.html
from lxml import etree


html = "<book>\
    <author>Tom <em>John</em> cat</author>\
    <pricing>\
        abc \
        <price>20</price>\
        <discount>0.8</discount>\
    </pricing>\
</book>"

selector = etree.HTML(html)
cont = selector.xpath('//pricing/strint(.)')
#cont = cont.xpath('string(.)')
cont = str(cont)
print(type(cont))
print(cont)



