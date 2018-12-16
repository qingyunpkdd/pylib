#-*- encoding:utf-8 -*-
__author__ = ''

import re,os,sys
import jieba
import jieba
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
des_dir="D:\\chinese\\d120ask_all_case_merge_wordsegment"
count = 0

disease = {}
copus = []
copus_name = []
for filename in os.listdir(des_dir):
    disease_id = filename.split(".")[0]
    filename = des_dir + "\\" + filename
    try:
        with open(filename,'r',encoding='utf-8') as fp:
            content = str(fp.read())
    except:
        print("read file err")
    #words  = jieba.cut(content)
    #seged = str(' '.join(words))
    #copus.append(seged)
    copus.append(content)
    copus_name.append(disease_id)
    count = count + 1
    print(count)
vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
tfidf=transformer.fit_transform(vectorizer.fit_transform(copus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
filename = "D:\\tfidf.txt"
with open(filename,'w',encoding='utf-8') as fp:
    for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
        for j in range(len(word)):
            if  ((float(weight[i][j]))>=0.0001):
                fp.write(str(word[j]))
                fp.write(' ')
                fp.write(str(weight[i][j]))
                fp.write(' ')
                fp.write(copus_name[i])
                fp.write('\n')
print("finis")