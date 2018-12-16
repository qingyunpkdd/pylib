#-*- encoding:utf-8 -*-
__author__ = ''

import os


class SimpleCalculate():
    def __init__(self,dir,des_dir):
        self.dir = dir
        self.desdir = des_dir
        self.count = 0
    def file_merge(self):
        disease = {}
        for filename in os.listdir(self.dir):
            disease_id = filename.split("_")[0]
            filename = self.dir + "\\" + filename
            with open(filename,'r',encoding='utf-8') as fp:
                content = str(fp.read())
            dict_d = {str(disease_id):content}
            if (not disease_id in disease):
                disease.update(dict_d)
            else:
                disease[disease_id] = disease[disease_id] + content
        for key, cont in disease.items():
            desfile = self.desdir + "\\" + str(key) + ".txt"
            with open(desfile,'w',encoding='utf-8') as fp:
                fp.write(str(cont))
            self.count = self.count + 1
            print("%s file has write"%str(self.count))

if __name__ == '__main__':
    mergefile = SimpleCalculate(dir="D:\\chinese\d120ask_all_case",des_dir="D:\\chinese\\d120ask_all_case_merge")
    mergefile.file_merge()