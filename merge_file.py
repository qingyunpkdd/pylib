# text preprocessing
#import pymongo
#db = pymongo.MongoClient().baike.items

#reload(sys)
#sys.setdefaultencoding("utf-8")

import codecs
import sys, os

from collections import defaultdict
from itertools import tee
from tqdm import tqdm
import re


def texts():
    rootdir = "D:\\chinese\\word2vec_corpus\\corpus"
    #list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in tqdm(filenames):
            ful_filename = os.path.join(parent,filename)
            if os.path.isfile(ful_filename):
                try:
                  text = open(ful_filename, 'rb').read().decode('utf-8')
                except:
                   print('FILE OPEN ERROR!')
                yield text
def text_filter(texts):
    for content in tqdm(texts):
        # for t in re.split(u'[^\u4e00-\u9fa50-9a-zA-Z\u3002\uFF1F\uFF01\uFF0C]+', a):
        #     if t:
        #         yield t +'\n'
        content = re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z\u3002\uFF1F\uFF01\uFF0C\n\r]', '', content)# delete all none chinese word
        content = re.sub(u'[\n\r\f]{2,}','\n',content)#delete empty lines
        content = re.sub('[a-zA-Z0-9]{10,}', '', content) #delete alphabra
        content = re.sub('【.*?】', ' ', content)
        yield content
def save_to_file(words):
    file = codecs.open('D:\\chinese\\word2vec_corpus\\merged_ehr_2.txt', 'w', 'utf-8')
    for wd in words:
        file.write(wd)
    file.close()


texts = texts()
word = text_filter(texts)
save_to_file(word)