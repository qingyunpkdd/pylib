#-*- encoding:utf-8 -*-
__author__ = ''
import re
import pymysql
import sys
sys.path.append('../')
import os
import itertools
from databases import my_pymysql

#处理series 文件。
class GeoToSave():
    def __init__(self, s_file):
        self.s_file = s_file
        self.re_title = re.compile(r'^\d+\.')
        self.re_note = re.compile(r'^.Submitter supplied')
        self.re_Organism = re.compile(r'^Organism')
        self.re_Type = re.compile(r'^Type')
        self.re_Platform = re.compile(r'^Platform|^\d+\s')
        self.re_FTP = re.compile(r'^FTP')
        self.re_SRA = re.compile(r'^SRA')
        self.re_Series = re.compile(r'^Series')
        self.fp = ""
    def batch_process(self):
        with open(self.s_file,'r',encoding='utf-8') as fp:
            _start = False
            _end = False
            _batch = []
            while True:
                line = fp.readline()
                if line == '\n'and _end == False:
                    _end = True
                    continue
                elif line == '\n'and _end == True:
                    _end = True
                    yield _batch
                    _batch = []
                elif not line:
                    yield  _batch
                    break
                else:
                    content = line.strip('\n')
                    content = content.replace('\t',' ')
                    _batch.append(content)
    def field_process(self,_batch):
        fields = {}
        #init fields
        fields["title"] = [""]
        fields["note"] = [""]
        fields["Organism"] = [""]
        fields["Type"] = [""]
        fields["Platform"] = [""]
        fields["FTP"] = [""]
        fields["SRA"] = [""]
        fields["Series"] = [""]
        for line in _batch:
            if self.re_title.match(line):
                fields["title"] = [line]
            elif self.re_note.match(line):
                fields["note"] = [line]
            elif self.re_Organism.match(line):
                org = line.split(':')[-1]
                org = org.split(';')
                orgs = [o.strip() for o in org]
                fields["Organism"] = orgs
            elif self.re_Type.match(line):
                t = line.split(';')
                t = [o.strip() for o in t]
                fields["Type"] = t
            elif self.re_Platform.match(line):
                fields["Platform"] = [line]
            elif self.re_FTP.match(line):
                fields["FTP"] = [line]
            elif self.re_SRA.match(line):
                fields["SRA"] = [line]
            elif self.re_Series.match(line):
                fields["Series"] = [line]
        return fields
    def save_to_mysql(self,db_obj):
        #创建表格
        db_obj.run("")
        #将数据导入表格，通过物种分成多个表格
        db_obj.run("")
        #测试用例
    def tsv_open(self,file_path):
        self.fp = open(file_path, 'a+')
    def tsv_close(self):
        self.fp.close()
    def save_to_tsv(self,file_path,dic_field):
        write_titles = [ "title","note","Organism","Type","Platform","FTP","SRA","Series"]
        if not self.fp:
            try:
                os.remove(file_path)
            except:
                print("file not exist!")
            self.tsv_open(file_path)
        if not os.path.getsize(file_path):
            tit = ""
            for e in write_titles:
                if tit:
                    tit = tit + "\t" + e
                else:
                    tit = e
            tit.strip('\t')
            tit = tit + "\n"
            self.fp.write(tit)
            self.fp.flush()
        list_all = []
        for t in write_titles:
            if t in dic_field:
                list_all.append(dic_field[t])
            else:
                list_all.append([""])
        comb = list(itertools.product(*list_all))
        for ele in comb:
            _line = "\t".join(ele)
            self.fp.write(_line)
            self.fp.write("\n")
            self.fp.flush()
        # if  dic_field["Organism"]:
        #      for org in dic_field["Organism"]:
        #         each_line = ""
        #         for t in write_titles:
        #             if not each_line:
        #                 if t != "Organism":
        #                     each_line = dic_field[t]
        #             else:
        #                 if t == "Organism":
        #                     each_line = each_line + "\t" + org
        #                 elif t in dic_field:
        #                     each_line = each_line + "\t" + dic_field[t]
        #                 else:
        #                     each_line = each_line + "\t"
        #         self.fp.write(each_line.strip())
        #         self.fp.write('\n')
        #         self.fp.flush()


if __name__ == "__main__":
    #mydb = my_pymysql.SqlCon("")
    s_file = "E:\\coral reefs data\\NCBI\\symbiodinium\\ncbi_geo_series_symbiodinium.txt"
    file_path = "E:\\coral reefs data\\NCBI\\symbiodinium\\ncbi_geo_series_symbiodinium.tsv"
    geotosave = GeoToSave(s_file)
    for _batch in geotosave.batch_process():
        dic_field = geotosave.field_process(_batch)
        geotosave.save_to_tsv(file_path=file_path,dic_field=dic_field)

