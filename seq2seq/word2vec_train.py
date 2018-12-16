#-*- encoding:utf-8 -*-
__author__ = 'qingyun891'

#step 1 conject the text file for future processing iteration the dir to open the file.
import os
from tqdm import tqdm
filedir = os.getcwd()
filedir = "./sougou_news"

tem = os.walk(filedir)
out_put_file = "merged.txt"
f = open(out_put_file,"w")
for fpath,dirs,fi in tqdm(tem):
    for fn in fi:
        file_name = os.path.join(fpath, fn)
        try:
            for line in open(file_name,"r",encoding='gb2312'):
                f.writelines(line)
                f.write('\n')
        except:
            continue
f.close()

#step 2 run the word2vec program
#refresh the txt file

import word2vec
word2vec.word2vec('corpusSegDone.txt', 'corpusWord2Vec.bin', size=300,verbose=True)
