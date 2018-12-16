#-*- encoding:utf-8 -*-
__author__ = ''
import os
import re
from functools import reduce
#F:\dictionary\dis_gene
#this script is to transform the all_gene to csv to avoid the dummy \t charactor


source_f = "F:\\dictionary\\dis_gene\\all_gene_disease_pmid_associations.tsv"
disc_f = "F:\\dictionary\\dis_gene\\all_gene_disease_pmid_associations.csv"

def tsv_to_csv(source_f,disc_f):
    fs = open(source_f,'r',encoding="utf-8")
    fd = open(disc_f,'w',encoding="utf-8")
    i = 0
    for line in fs:
        line = line.replace(",","@")
        tem = line.strip().split("\t")
        if len(tem) != 10:
            i = i + 1
            print("警告：非标准长度%s" %i)
        def joins(x,y):
            return x+","+y
        str = reduce(joins,[tem[i] for i in range(0,3,1)])
        fd.write(str)
        fd.write(",")
        str = reduce(joins, [tem[i] for i in range(-6, 0, 1)])
        fd.write(str)
        fd.write("\n")
        fd.flush()
    fs.close()
    fd.close()
tsv_to_csv(source_f=source_f,disc_f=disc_f)