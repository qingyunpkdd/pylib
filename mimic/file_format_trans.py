#-*- encoding:utf-8 -*-
__author__ = ''
import re

#tsv to csv
def tsv2csv (tsv_f,csv_f,reportline=1000):
    tsv = open(tsv_f, 'r')
    csv_file = open(csv_f, "w")
    times = 0
    tem = 0
    for line in tsv:
        times = times+1
        len_detect = line.split('\t')
        if times==1: tem = len(len_detect)
        if times>=2:
            if len(len_detect)!=tem:
                raise "unequal length"
            if times%reportline==0:
                print times
        line =  re.sub("\t", ",", line)
        line = re.sub(".txt","",line)
        line = line.strip('\n')
        csv_file.write(line)
        csv_file.write('\n')
    csv_file.close()
    tsv.close()
tsv_f = "F:\\R\\mimic\\noble_metathesaurus_all_sid.tsv"
csv_f = "F:\\R\\mimic\\noble_metathesaurus_all_sid.csv"
tsv2csv (tsv_f,csv_f)
