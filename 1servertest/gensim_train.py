from gensim.models import word2vec
import logging
import numpy as np
filename = 'corpusSegDone.txt'
sentences = word2vec.Text8Corpus(filename)
n_dim = 100
model = word2vec.Word2Vec(sentences,size=n_dim)
model.save(u"gensim_train.model")
