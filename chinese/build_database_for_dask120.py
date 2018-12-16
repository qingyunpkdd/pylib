#-*- encoding:utf-8 -*-
__author__ = ''

import pymysql
import re
import codecs
import os
from tqdm import tqdm


#构建文本数据库
def get_text(file_dir=""):
    ls = os.listdir(file_dir)
    ls = tqdm(ls)
    for i in ls:
        cpath = os.path.join(file_dir,i)
        if os.path.isfile(cpath):
            file_i = dict()
            with open(cpath, 'rb') as fr:
                text = fr.read().decode('utf-8')
            text = text.replace("\'","")
            text = text.replace("\"","")
            text = text.replace(",","")
            file_name = i.split("_")[0]
            file_name = file_name.encode('utf-8')
            file_i[file_name] = text.encode('utf-8')
            yield file_i
def insert_to_database(cursor,data,table):
    id = list(data.keys())
    id = id[0]
    content = data[id]
    param=(id,content)
    sql = "insert into {table}(disease_id,disease_content) values(%s,%s)".format(table=table)
    #sql="insert into {table}(disease_id,disease_content) values('{id}','{content})'".format(table=table,id=id,content=content)
    cursor.execute(sql,param)

#fetch data with sample size large than 100
def fetch_data(cursor,min_size=100,to_dir=""):
    sql="select disease_id ,disease_content from d120_corpus \
            where disease_id in (select disease_id from  d120_corpus group by disease_id HAVING count(*)>={min_size})".format(min_size=min_size)
    cursor.execute(sql)
    tems = list(cursor.fetchall())
    file_name_i = dict()
    for tem in tems:
        disease_id = tem[0]
        if disease_id in file_name_i:
            file_name_i[disease_id]+=1
        else:
            file_name_i[disease_id]=0
        disease_content = tem[1]
        s_i = str(file_name_i[disease_id])
        file_name = disease_id + "_"+ s_i+ ".txt"
        file_name = os.path.join(to_dir,file_name)
        with codecs.open(file_name, 'w', 'UTF-8') as fw:
            fw.write(disease_content)

#产生特定的数据集，去除诊断信息。要分几步走，首先要做的就是，分词和命名实体识别。
def clear_data(source_dir="",des_dir=""):
    ls = os.listdir(source_dir)
    ls =tqdm(ls)
    def clear_content_and_write(file_dict,des_dir):
        file_name = list(file_dict.keys())[0]
        content = file_dict[file_name]
        content = re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z\u3002\uFF1F\uFF01\uFF0C\n\r]', '',
                         content)  # delete all none chinese word
        content = re.sub(u'[\n\r\f]{2,}', '\n', content)  # delete empty lines
        content = re.sub('[a-zA-Z0-9]{10,}', '', content)  # delete alphabra
        content = re.sub('【.*?】', ' ', content)
        content = re.sub('【.{,3}诊断.{,3}】.*','',content)
        fw_name = os.path.join(des_dir,file_name)
        fw = codecs.open(fw_name,'w','UTF-8')
        fw.write(content)
        fw.close()
    for i in ls:
        cpath = os.path.join(source_dir, i)
        file_i = dict()
        if os.path.isfile(cpath):
            with open(cpath, 'rb') as fr:
                text = fr.read().decode('utf-8')
            file_i[i] = text
            clear_content_and_write(file_dict=file_i, des_dir=des_dir)
if __name__=="__main__":
    db = pymysql.connect("10.194.181.128", "root", "lyh123", "chinese_note",use_unicode=True,charset="utf8")
    cursor = db.cursor()
    cursor.execute("select version()")
    result = cursor.fetchall()

    #config
    pre_dir="D:\\chinese\\d120_mysql\\pre_clear"
    aft_dir="D:\\chinese\\d120_mysql\\clear"
    source_dir="D:\\chinese\\d120ask_all_case"
    table = "d120_corpus"

    #building mysql
    # for data in get_text(file_dir=source_dir):
    #     insert_to_database(cursor, data, table)
    #     db.commit()
    # print("update database done")

    #generate data
    # fetch_data(cursor, min_size=100, to_dir=pre_dir)
    # print("corpus build done")

    #clear data
    clear_data(source_dir=pre_dir, des_dir=aft_dir)




    db.close()





