#-*- encoding:utf-8 -*-
__author__ = ''
import re,os
des_dir="D:\\chinese\\d120ask_all_case_merge"
count = 0
for filename in os.listdir(des_dir):
    filename = des_dir + "\\" + filename
    with open(filename,'r',encoding='utf-8') as fp:
        cont = fp.read()
        cont = re.sub(r'<img.*?jpg\">',r' ',cont)
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(cont)
    count = count + 1
    print(count)