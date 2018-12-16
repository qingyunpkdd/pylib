#-*- encoding:utf-8 -*-
__author__ = ''
#list all the file segment all the file.

from gensim import corpora,models,similarities
import jieba
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import re


# #stoplist = open("D:\\chinese\\word2vec_corpus\\stop_word_dictionary.txt",'r',encoding='utf-8').readlines()
#
# def building_documents(seg_done_file):
#    with open(seg_done_file,'r',encoding='utf-8') as pre_file:
#        for case in pre_file:
#            tem =case.split("__label__")
#            case,label = tem[0],tem[1]
#            yield [case,label]
# def preprocessing_text(documents,stoplist = set("1","2")):
#     stoplist = stoplist
#     texts = [[word for word in document.lower().split() if word not in stoplist]
#              for document in documents]
#     # remove words that appear only once
#     all_tokens = sum(texts, [])
#     tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
#     texts = [[word for word in text if word not in tokens_once]
#              for text in texts]
#     return texts
#
# def building_dictionary(texts):
#     dictionary = corpora.Dictionary(texts)
#     corpus = [dictionary.doc2bow(text) for text in texts]
#     dictionary.save('.//case_lib.dict')  # store the dictionary, for future reference
#     # dictionary.token2id
#     # {'minors': 11, 'graph': 10, 'system': 5, 'trees': 9, 'eps': 8, 'computer': 0,
#     #  'survey': 4, 'user': 7, 'human': 1, 'time': 6, 'interface': 2, 'response': 3}
#     return corpus
# def tfidf(corpus):
#     tfidf_model = models.TfidfModel(corpus)
#     doc_bow = [(0, 1), (1, 1)]
#     #print(tfidf_model[doc_bow])  # [(0, 0.70710678), (1, 0.70710678)]
#     corpus_tfidf = tfidf_model[corpus]
#     #for every word in dictionary return the word id tfidf score
#     # print(tfidf[corpus[0]])
#     # [(0, 0.5773502691896257), (1, 0.5773502691896257), (2, 0.5773502691896257)]
#     return corpus_tfidf
#
#     #save and load tfidf models
#     # tfidf.save("./model.tfidf")
#     # tfidf = models.TfidfModel.load("./model.tfidf")



def re_build_tf_idf_file(seg_done_file,method,n):
    disease_dict = {}
    documents =[]
    disease_list = []
    with open(seg_done_file,'r',encoding='utf-8') as pre_file:
        for case in pre_file:
           tem =case.split("__label__")
           case,label = tem[0],tem[1].strip()
           if not(label in disease_dict):
               disease_dict[label] = case
           else:
               disease_dict[label] = disease_dict[label] + case
    #http://blog.csdn.net/liuxuejiang158blog/article/details/31360765
    #building tf-idf for each disease

    #disease corpus
    for dis,dis_content in disease_dict.items():
        documents.append(dis_content)
        disease_list.append(dis)
    corpus = documents
    # corpus = ["我 来到 北京 清华大学",  # 第一类文本切词后的结果，词之间以空格隔开
    #           "他 来到 了 网易 杭研 大厦",  # 第二类文本的切词结果
    #           "小明 硕士 毕业 与 中国 科学院",  # 第三类文本的切词结果
    #           "我 爱 北京 天安门"]  # 第四类文本的切词结果
    vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
    tfidf = transformer.fit_transform(
        vectorizer.fit_transform(corpus))  # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    words = vectorizer.get_feature_names()  # 获取词袋模型中的所有词语
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
    # for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    #     print
    #     u"-------这里输出第", i, u"类文本的词语tf-idf权重------"
    #     for j in range(len(word)):
    #         print
    #         word[j], weight[i][j]
    #从原始文本中将前N个词构提取出来，并写入新的文件。
    def top_n(n =100,file_to_write="",seg_done_file=""):
        write_files = open(file_to_write, 'w', encoding='utf-8')
        with open(seg_done_file, 'r', encoding='utf-8') as pre_file:
            i = 0
            for case in pre_file:
                tem = case.split("__label__")
                case, label = tem[0], tem[1].strip()
                case_list = case.split()
                dis_index_i = disease_list.index(label)
                tem_content_dict = {}
                for dis_word in case_list:
                    if dis_word in words:
                        word_index_j = words.index(dis_word)
                        tem_content_dict[dis_word] = weight[dis_index_i][word_index_j]
                    else:
                        tem_content_dict[dis_word] = 0
                top_n_word = sorted(tem_content_dict.items(),key=lambda item:item[1],reverse=True)
                top_n_word = [word_each[0] for word_each in top_n_word]
                while len(top_n_word)< n:
                    top_n_word.append("0")
                top_n_word = " ".join(top_n_word[:n])
                write_files.write(top_n_word)
                write_files.write("__label__")
                write_files.write(label)
                write_files.write("\n")
                write_files.flush()
                i = i + 1
                print("file {0} done,{1}".format(label,i))
        write_files.close()
    if method == "top_n":
        n  = n
        file_to_write = "D:\\chinese\\top_{0}.txt".format(n)
        top_n(file_to_write=file_to_write,seg_done_file=seg_done_file)
# def tem_seg(file_path,des_path):
#     with open(file_path,'r',encoding='utf-8') as files:
#         contents = files.read()
#         contents = re.sub(r'(__label__[a-zA-Z]+)','\1\n',contents)
#     with open(des_path, 'w', encoding='utf-8') as files:
#         files.write(contents)
if __name__ == "__main__":
    n = 50
    method = "top_n"
    seg_done_file = "D:\\chinese\\corpusSegDone_word.txt"
    re_build_tf_idf_file(seg_done_file = seg_done_file,method = method,n = n)
    # file_path = "D:\\chinese\\top_{0}.txt".format(n)
    # des_path = "D:\\chinese\\top_{0}_seg.txt".format(n)
    # tem_seg(file_path=file_path, des_path=des_path)