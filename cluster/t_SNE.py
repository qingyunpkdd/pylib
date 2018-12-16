#-*- encoding:utf-8 -*-
__author__ = ''
import numpy as np
from sklearn.datasets import fetch_mldata
import pickle
import os





if os.path.exists('D:\\pylib\\cluster\\MNIST.pkl'):
    f2 = file('D:\\pylib\\cluster\\MNIST.pkl','rb')
    mnist = pickle.load(f2)
    f2.close()
else:
    mnist = fetch_mldata("MNIST original")
    f1 = file('MNIST.pkl', 'wb')
    pickle.dump(mnist, f1, True)
    f1.close()

X = mnist.data / 255.0
y = mnist.target
del mnist
print X.shape, y.shape
import pandas as pd

feat_cols = [ 'pixel'+str(i) for i in range(X.shape[1]) ]

df = pd.DataFrame(X,columns=feat_cols)
df['label'] = y
df['label'] = df['label'].apply(lambda i: str(i))
del X,y
X, y = None, None

print 'Size of the dataframe: {}'.format(df.shape)

rndperm = np.random.permutation(df.shape[0])

#matplotlib inline
import matplotlib.pyplot as plt

# Plot the graph
# plt.gray()
# fig = plt.figure( figsize=(16,7) )
# for i in range(0,30):
#     ax = fig.add_subplot(3,10,i+1, title='Digit: ' + str(df.loc[rndperm[i],'label']) )
#     ax.matshow(df.loc[rndperm[i],feat_cols].values.reshape((28,28)).astype(float))
# plt.show()

from sklearn.decomposition import PCA
#
# pca = PCA(n_components=3)
# pca_result = pca.fit_transform(df[feat_cols].values)
#
# df['pca-one'] = pca_result[:,0]
# df['pca-two'] = pca_result[:,1]
# df['pca-three'] = pca_result[:,2]
#
# print 'Explained variation per principal component: {}'.format(pca.explained_variance_ratio_)
#
#
from ggplot import *
#
# chart = ggplot( df.loc[rndperm[:3000],:], aes(x='pca-one', y='pca-two', color='label') ) \
#         + geom_point(size=75,alpha=0.8) \
#         + ggtitle("First and Second Principal Components colored by digit")
# chart

import time
from sklearn.manifold import TSNE

n_sne = 7000

time_start = time.time()
tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
tsne_results = tsne.fit_transform(df.loc[rndperm[:n_sne],feat_cols].values)

print 't-SNE done! Time elapsed: {} seconds'.format(time.time()-time_start)


df_tsne = df.loc[rndperm[:n_sne],:].copy()
df_tsne['x-tsne'] = tsne_results[:,0]
df_tsne['y-tsne'] = tsne_results[:,1]

chart = ggplot( df_tsne, aes(x='x-tsne', y='y-tsne', color='label') ) \
        + geom_point(size=70,alpha=0.1) \
        + ggtitle("tSNE dimensions colored by digit")
#chart

