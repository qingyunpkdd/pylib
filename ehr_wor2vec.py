#-*- encoding:utf-8 -*-
__author__ = ''
from gensim.models import word2vec
import logging
import numpy as np
filename = "D:\\chinese\\word2vec_corpus\\merged_ehr_2_segdone.txt"
sentence =  word2vec.Text8Corpus(filename)
n_dim =100
model =word2vec.Word2Vec(sentence,size=n_dim)
model.save(u"abc.model")


#test
from gensim.models import word2vec
model_2 = word2vec.Word2Vec.load("gensim_train.model")

y1 = model_2.most_similar(u'肝脏',topn = 6)
y2 = model_2.wv[u'肝脏']



#import word2vec

# segment word part
import jieba
import struct
filePath='merged.txt'
fileSegWordDonePath ='corpusSegDone.txt'
# read the file by line
fileTrainRead = []
#fileTestRead = []
with open(filePath) as fileTrainRaw:
    for line in fileTrainRaw:
        fileTrainRead.append(line)

# define this function to print a list with Chinese
def PrintListChinese(list):
    for i in range(len(list)):
      pass
        #print list[i]
# segment word with jieba
fileTrainSeg = []
for i in range(len(fileTrainRead)):
    fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i],cut_all=False)))])
    if i % 100 == 0 :
        print (i)

# to test the segment result
#PrintListChinese(fileTrainSeg[10])

# save the result
with open(fileSegWordDonePath,'wb') as fW:
    for i in range(len(fileTrainSeg)):
        fW.write(fileTrainSeg[i][0].encode('utf-8'))
        fW.write("\n".encode(encoding='utf-8'))


#不分词，对于每一个词都用空格隔开。
import re
text = ""
text = re.sub(r'(.*?)','\g(1) ',text)
text = text.strip()
