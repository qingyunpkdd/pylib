#-*- encoding:utf-8 -*-
__author__ = ''

import os
import re
from tqdm import tqdm
def merge_english(file_dir,train_rate=0.8):
    ls = os.listdir(file_dir)
    pbar = tqdm(ls)
    count = 0
    for i in  pbar:
        c_path = os.path.join(file_dir,i)
        if os.path.isdir(c_path):
            merge_english(c_path,train_rate=0.8)
        elif os.path.isfile(c_path):
            count = count+1
            class_name = c_path.split("\\")[-2]
            with open(c_path,'r') as fr:
                text = fr.read()
            #text = text.decode()
            text = text.replace("\n"," ")
            text = text.replace("*","")
            text = text.replace("__","")
            text = re.sub('\s{2,}',' ',text)
            full_text = text + "\t__label__"+ str(class_name) +"\n"

            if count <= int(len(ls)*0.8):
                fw.write(full_text)
            else:
                f_test_w.write(full_text)
def merge_chinese(file_dir,train_rate=0.8):
    pass
if __name__=="__main__":
    file_dir = "F:\\clinical_NLP\\hyper_sample_filed"
    des_train_file = "F:\\clinical_NLP\\news_fasttext_train.txt"
    des_test_file = "F:\\clinical_NLP\\news_fasttext_test.txt"
    fw = open(des_train_file, 'w')
    f_test_w = open(des_test_file, 'w')
    train_rate = 0.8
    merge_english(file_dir=file_dir, train_rate=train_rate)
    fw.close()
    f_test_w.close()