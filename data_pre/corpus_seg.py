#-*- encoding:utf-8 -*-
__author__ = ''
import re
import jieba
file_path = "D:\\chinese\\word2vec_corpus\\merged_ehr_2.txt"
out_put_file_path = "D:\\chinese\\word2vec_corpus\\merged_ehr_2_segdone.txt"
jieba.load_userdict("D:\\chinese\\word2vec_corpus\\dictionary.txt")
with open(file_path,'r',encoding='utf-8') as f:
    with open(out_put_file_path,'w',encoding='utf-8') as fw:
        for line in f:
            text = ' '.join(list(jieba.cut(line, cut_all=False)))
            fw.write(text)
            fw.flush()
