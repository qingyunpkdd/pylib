#-*- encoding:utf-8 -*-
__author__ = ''
from gensim.models import word2vec
import logging
import numpy as np

def building_w2v_model(file_name,model_file="D:\\chinese\\word2vec_corpus\\gensim_train.model",ndim=100):
    sentence = word2vec.Text8Corpus(file_name)
    model = word2vec.Word2Vec(sentence, size=ndim)
    model.save(model_file)
def load_w2v_model(model_file):
    from gensim.models import word2vec
    model_2 = word2vec.Word2Vec.load(model_file)
    y1 = model_2.most_similar(u'气管炎', topn=6)
    y2 = model_2.wv[u'气管炎']
    print(y1)
    print(y2)
if __name__ == "__main__":
    ndim = 256
    file_name = "D:\\chinese\\word2vec_corpus\\merged_ehr_2_segdone.txt"
    model_file = "D:\\chinese\\word2vec_corpus\\gensim_train{0}.model".format(ndim)
    building_w2v_model(file_name,model_file,ndim=ndim)
    load_w2v_model(model_file)