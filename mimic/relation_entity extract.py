#-*- encoding:utf-8 -*-
__author__ = ''

#{3310} => {29410}
import csv
import re
def source2dist (sour_f,disc_f,icd_f,reportline=1000):
    fs = open(sour_f, 'r')
    fd = open(disc_f, "w")
    ficd = open(icd_f,'r')


icd_dic_f = "F:\\dictionary\\ICD9\ICD9-master\\icd9.txt"
source_f = "F:\\R\\mimic\\DIAGNOSES_ICD.csv"
disc_f = "F:\\R\\mimic\\DIAGNOSES_DisName.csv"

def icd2dis_name (icd_dic_f,source_f,disc_f):
    fi = open(icd_dic_f,'r')
    fs = open(source_f,'r')
    fs_csv =csv.reader(fs)
    fd = open(disc_f,'w')
    #build icd to disease name dictionary
    icd_dict = {}
    for line in fi:
        line = line.strip('\n')
        line = re.sub(",", "&", line)
        tem = line.split('\t')
        icd_code = tem[0]
        dis_name = tem[1]
        icd_dict[icd_code] = dis_name
    #trans icd code to they names
    counter = 0
    for line in fs_csv:
        if line[1] in icd_dict:
            fd.write(line[0])
            fd.write(',')
            fd.write(str(icd_dict[line[1]]))
            fd.write('\n')
    fi.close()
    fs.close()
    fd.close()

icd2dis_name (icd_dic_f,source_f,disc_f)
