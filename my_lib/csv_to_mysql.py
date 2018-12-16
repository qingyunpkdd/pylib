#-*- encoding:utf-8 -*-
__author__ = ''
import pandas as pd
import numpy as np
import sys
import os
sys.path.append('../')
from databases import my_pymysql
import collections


class NsvToMysql():
    def __init__(self,filepath,mysql_db,table_name,field_terminated=",",filet="csv"):
        self.filepath = filepath
        self.my_db = mysql_db
        self.line_no = 0
        self.field_terminated = field_terminated
        self.filetype = filet
        self.field_dic = collections.OrderedDict()
        self.max_value = []
        self.table_name = table_name
        #self.mysql =
    def check_field_length(self):
        if self.filetype == "csv":
            with open(self.filepath,'r',encoding='utf-8') as fp:
                import csv
                csv_file = csv.reader(fp)
                l_no =0
                for line in csv_file:
                    l_no+=1
                    if l_no==1:
                        for _fieled in line:
                            self.field_dic[_fieled] = 0
                            self.max_value.append(0)
                    else:
                        line = self.get_length(line)
                        for l_len, k in zip(line,self.field_dic.keys()):
                            if self.field_dic[k] < l_len:
                                self.field_dic[k] = l_len
                        # ss = [v for v in self.field_dic.values()]
                        # len_fieled = self.get_length(line)
                        # self.max_value = self.lis_cmp(self.max_value,len_fieled)
    def get_length(self,lis):
        s_l = [len(s) for s in lis]
        return s_l
    # def lis_cmp(self,l1,l2):
    #     l_max = []
    #     for i,j in zip(l1,l2):
    #         if i < j:
    #             l_max.append(j)
    #         else:
    #             l_max.append(i)
    #     return l_max
        # if not len(l1)==len(l2):
        #     raise RuntimeError("two list not equal!")
        # for i in range(len(l1)):
        #     if l1[i] < l2[i]:
        #         l1[i] = l2[i]
        # return l1
    def parse_csv(self):
        import csv
        with open(self.filepath, 'r',encoding='utf-8') as fps:
            csv_file = csv.reader(fps)
            for line in csv_file:
                self.line_no+=1
                yield line
    def parsing_nsv(self):
        with open(self.filepath,'r',encoding='utf-8') as fp:
            while True:
                line = fp.readline()
                self.line_no += 1
                if line == '':
                    break
                else:
                    _batch = line.strip().split(self.field_terminated)
                    yield _batch
    def create_table(self):
        _i = 0
        sql_s = "create table {table_name} (".format(table_name=self.table_name)
        sql_string = "{fieled}  varchar({lens})"
        sql_fie = []
        for k in self.field_dic.keys():
            if self.field_dic[k] < 60:
                s = sql_string.format(fieled=str(k),lens=str(60))
            elif self.field_dic[k] < 90:
                s = sql_string.format(fieled=str(k),lens=str(90))
            elif self.field_dic[k] < 256:
                s = sql_string.format(fieled=str(k),lens=str(256))
            else:
                s = str(k) + " " + "text"
            sql_fie.append(s)
        sql_ = ",".join(sql_fie)
        sql_s = sql_s + sql_ + ")"
        res = self.my_db.run(sql_s)
        print(res)
    @staticmethod
    def get_db(host="10.194.181.128",db_name="corals_db"):
        my_db = my_pymysql.SqlCon(host="10.194.181.128",db_name="corals_db")
        my_db.connect()
        return my_db
    def save_to_mysql(self,_batch):
        _batch = [b.replace(',',';') for b in _batch]
        _batch = [b.replace('"', '') for b in _batch]
        _batch = [b.replace("'", '') for b in _batch]
        #_batch = [b.replace('', ';') for b in _batch]

        vals = ['"' + val + '"' for val in _batch]
        #vals = [str(val) for val in _batch]
        vals = ",".join(vals)
        _sql = 'insert into {table_name} values({vals})'.format(table_name=self.table_name,vals=vals)
        res = self.my_db.run(_sql)
        print(res)
    def run(self):
        self.check_field_length()
        for _batch in self.parse_csv():
            if self.line_no == 1:
                #continue
                self.create_table()
            else:
                self.save_to_mysql(_batch)
if __name__ == "__main__":
    filepath  = "E:\\coral reefs data\\NCBI\\anthozoa\\SraRunInfo_cp.csv"
    my_db = NsvToMysql.get_db(db_name="corals_db")
    nsvtomysql = NsvToMysql(filepath=filepath,mysql_db=my_db,table_name="SraRunInfo_cp", filet="csv")
    nsvtomysql.run()
