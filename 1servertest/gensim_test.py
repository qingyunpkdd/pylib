"run the program in a personal channel"
from gensim.models import word2vec
model_2 = word2vec.Word2Vec.load("gensim_train.model")
#import logging
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

word_vectors = model_2.wv
#del model

y1=model_2.most_similar(u'肝脏',topn=60)
y2=model_2.wv[u'肝脏']

print(y1,y2)




