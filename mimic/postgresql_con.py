#-*- encoding:utf-8 -*-
__author__ = ''

#应该尽可能的在python中处理好所有的过程，通过调用系统进程处理每一个文本，然后将结果也在这里进行处理。
#
#connect to postgres databases;
import psycopg2
import zipfile
from mimic import rm_dir



def fetch_the_disease_note_all(disease_icd = ""):
    sql = "select text from noteevents as nt\
              where nt.hadm_id in (select di.hadm_id from diagnoses_icd as di  where di.icd9_code='{disease_icd}');".format(disease_icd=disease_icd)
    cursor.execute(sql)
    text_list = list(cursor.fetchall())
    return text_list
def fetch_the_disease_note_one(disease_icd = ""):
    sql = "select text from noteevents as nt\
              where nt.hadm_id in (select di.hadm_id from diagnoses_icd as di  where di.icd9_code='{disease_icd}');".format(disease_icd=disease_icd)
    cursor.execute(sql)
    numrows = int(cursor.rowcount)
    for i in range(numrows):
        text_one = list(cursor.fetchone())
        yield text_one

def fetch_else_disease_note_one(disease_icd=""):
    sql = "select text from noteevents as nt\
              where nt.hadm_id not in (select di.hadm_id from diagnoses_icd as di  where di.icd9_code='{disease_icd}');".format(disease_icd=disease_icd)
    cursor.execute(sql)
    numrows = int(cursor.rowcount)
    for i in range(numrows):
        text_one = list(cursor.fetchone())
        yield text_one


#写入文件函数
def all_write(disease_icd="",file_dir=""):
    text_list = fetch_the_disease_note_all(disease_icd=disease_icd)
    i = 0
    for item in text_list:
        f = open(file_dir.format(num=i), "w")
        f.write(item[0])
        f.close()
        i = i + 1
        if i%100==0:
            print("write file{i}".format(i=i))

def one_write(disease_icd="",file_dir=""):
    init_i = 0
    for text_one in fetch_the_disease_note_one(disease_icd=disease_icd):
        f = open(file_dir.format(num=init_i), "w")
        f.write(text_one[0])
        f.close()
        init_i = init_i + 1
        if init_i%100==0:
            print("write file{i}".format(i=init_i))

def one_else_write(disease_icd="",file_dir=""):
    init_i = 0
    for text_one in fetch_else_disease_note_one(disease_icd=disease_icd):
        f = open(file_dir.format(num=init_i), "w")
        f.write(text_one[0])
        f.close()
        init_i = init_i + 1
        if init_i%100==0:
            print("write file{i}".format(i=init_i))

def one_zip(disease_icd="",file_disease_zip="",file_dir=""):
    azip = zipfile.ZipFile(file_disease_zip,'a')
    init_i = 0
    for text_one in fetch_the_disease_note_one(disease_icd=disease_icd):
        azip.writestr(file_dir.format(num=init_i),data=text_one[0],compress_type=zipfile.ZIP_DEFLATED)
        init_i = init_i + 1
        if init_i%100==0:
            print("write file{i}".format(i=init_i))
    azip.close()
def one_else_zip(disease_icd="",file_else_disease_zip="",file_dir=""):
    azip = zipfile.ZipFile(file_else_disease_zip,'a')
    init_i = 0
    for text_one in fetch_else_disease_note_one(disease_icd=disease_icd):
        azip.writestr(file_dir.format(num=init_i),data=text_one[0],compress_type=zipfile.ZIP_DEFLATED)
        init_i = init_i + 1
        if init_i%100==0:
            print("write file{i}".format(i=init_i))
    azip.close()

if __name__ == "__main__":
    #test connection
    connection = psycopg2.connect(database="mimic", user="postgres", password="lyh123,.A", host="10.194.181.128",
                                  port="5432")
    cursor = connection.cursor()
    cursor.execute("set search_path to mimiciii;")
    cursor.execute("select * from diagnoses_icd LIMIT 10;")
    result = cursor.fetchall()
    print(result)
    print("test sussesfull")


    # config
    disease_icd = '4019'
    #rm dir
    #file_dirs = "F:\\clinical_NLP\\hypertention\\"
    #rm_dir.del_file(file_dirs)
    file_dir = "F:\\clinical_NLP\\hypertention\\file{num}.txt"
    zip_file_dir = "hypertention\\file{num}.txt"
    not_zip_file_dir = "non_hypertention\\file{num}.txt"
    file_dir_else = "F:\\clinical_NLP\\hypertention_NEG\\file{num}.txt"
    # fetchone or all   the value is "one" ,"all","one_else","one_zip","one_else_zip"
    method = "one_else_zip"
    file_disease_zip = "F:\\clinical_NLP\\hypertention_all.zip"
    file_else_disease_zip = "F:\\clinical_NLP\\non_hypertention_all.zip"


    if method == "one":
        one_write(disease_icd=disease_icd, file_dir=file_dir)
    elif method=="all":
        all_write(disease_icd=disease_icd, file_dir=file_dir)
    elif method=="one_else":
        one_else_write(disease_icd=disease_icd, file_dir=file_dir_else)
    elif method=="one_zip":
        one_zip(disease_icd=disease_icd, file_disease_zip=file_disease_zip, file_dir=zip_file_dir)
    elif method=="one_else_zip":
        one_else_zip(disease_icd=disease_icd, file_else_disease_zip=file_else_disease_zip, file_dir=not_zip_file_dir)
    else:
        raise Exception("metho error you must input 'one'or 'all'")

#for each_text in fetch_the_disease_note_one(disease_icd=disease_icd):

