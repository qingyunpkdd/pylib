#-*- encoding:utf-8 -*-
__author__ = ''
import pymysql
try:
    db = pymysql.connect("10.194.181.128","root","lyh123","dictionary")
    cursor = db.cursor()
    cursor.execute("select count(*) from icd9")
    result = cursor.fetchall()
    print(result[0])
except:
    print("connect error!")
#icd9 file
f_icd_dir = "F:\\R\mimic\\疾病共现网络\\dis_gene_icd9_name.txt"
f_icd_to_name = "F:\\R\mimic\\疾病共现网络\\dis_gene_icd9_to_name.txt"
icd_list =[]
with open(f_icd_dir,"r") as f_icd:
    for line in f_icd:
        tem = line.strip().split("-")
        icd_list.append(tem)
with open(f_icd_to_name,"w") as f_name:
    for tem in icd_list:
        sql = "select SHORT_DESCRIPTION from icd9\
               where ICD9_CODE='{code}'"
        try:
            cursor.execute(sql.format(code=tem[0]))
            icd_1 = list(cursor.fetchall()[0])
            cursor.execute(sql.format(code=tem[1]))
            icd_2 = list(cursor.fetchall()[0])
        except:
            print("not find and ignore: {n1}-{n2}".format(n1=tem[0],n2=tem[1]))
            f_name.write("\n")
            continue
        f_name.write(icd_1[0])
        f_name.write("\t")
        f_name.write(icd_2[0])
        f_name.write("\n")
