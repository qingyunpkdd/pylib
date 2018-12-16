#-*- encoding:utf-8 -*-
import os, sys
import re

__author__ = 'qingyun891'
class CaseLibB():
    count = 0
    def __init__(self,dir_name,des_dir):
        self.dir = dir_name
        self.cpdir = des_dir
    def get_file(self):
        for root, dirs, files in os.walk(self.dir):
            if root.split("\\")[-1] == "case":
                base = root
                file_urls = []
                if files:
                    for file in files:
                        file_url = base + "\\" + file
                        file_urls.append(file_url)
                    yield file_urls
    def get_text(self):
        for file_urls in self.get_file():
            if file_urls:
                for file in file_urls:
                    fp = open(file, 'r', encoding='utf-8')
                    #read the html file and get the text file for the notes sections
                    try:
                        html_content = fp.read()
                        content = re.search(r'class=.p_siboxbor2(?:.*?)<p>(.*?)</p>',html_content,re.S).group(1)
                    except:
                        print("get file content err")
                    finally:
                        fp.close()
                    con = [file, content]
                    yield con

    def save_file(self,con):
        content = con[1]
        file_n = con[0]
        dir_name = file_n.split("\\")[-3]
        file_name = file_n.split("\\")[-1]
        con_filename = dir_name +"_" + file_name
        file_name = self.cpdir + "\\" + con_filename
        #test if the file has been exist
        while os.path.exists(file_name):
            file_name = str(re.search(r'(.*?)\.txt',file_name,re.S).group(1)) + "a.txt"
        with open(file_name,'w',encoding='utf-8') as fp:
            fp.write(content)
        CaseLibB.count = CaseLibB.count + 1
        print("%s file writed"%CaseLibB.count)
if __name__ == '__main__':
    instance_class = CaseLibB(dir_name="D:\\chinese\\d120ask_pro",des_dir="D:\\chinese\\d120ask_all_case")
    for con in instance_class.get_text():
        instance_class.save_file(con)



