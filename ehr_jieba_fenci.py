#-*- encoding:utf-8 -*-
__author__ = ''
import re
import jieba
class jiebafenci():
    def __init__(self,method = "word",filePath='D:\\chinese\\ehr_zhihu_format_sample_size5.txt',fileSegWordDonePath ='D:\\chinese\\corpusSegDone'):#method = word or charactor
        self.method = method
        self.filePath=filePath
        self.fileSegWordDonePath =fileSegWordDonePath
        jieba.load_userdict("D:\\chinese\\word2vec_corpus\\dictionary.txt")
    def segment(self):
        self.fileTrainRead = []
        with open(self.filePath,'r') as fileTrainRaw:
            for line in fileTrainRaw:
                self.fileTrainRead.append(line)
        if self.method =="word":
            self.content = self.word_segment()
        elif self.method =="charactor":
            self.content = self.char_segment()
        else:
            raise NameError("method must be <word> or <charactor> ")

    def word_segment(self):
        fileTrainSeg = []
        for i in range(len(self.fileTrainRead)):
            texts =  self.fileTrainRead[i].split("__label__")
            texts,label = texts[0],texts[1]
            #def user define dictionary
            text = ' '.join(list(jieba.cut(texts, cut_all=False)))
            text = re.sub('[a-zA-Z0-9]{10,}', '', text)
            text = text.strip()
            text = text + "__label__" + label
            fileTrainSeg.append([text])
            if i % 100 == 0:
                print(i)
        return fileTrainSeg
    def char_segment(self):
        fileTrainSeg = []
        for i in range(len(self.fileTrainRead)):
            texts =  self.fileTrainRead[i].split("__label__")
            texts,label = texts[0],texts[1]
            text = re.sub('(.*?)', '\g<1> ',texts)
            text = re.sub('[a-zA-Z0-9]','',text)#this place should no be use any alphabra
            text = text.strip()
            text = text + "__label__" + label
            fileTrainSeg.append([text])
        return fileTrainSeg
    def write_to_file(self):
        with open(self.fileSegWordDonePath, 'wb') as fW:
            for i in range(len(self.content)):
                fW.write(self.content[i][0].encode('utf-8'))
                #fW.write("\n".encode(encoding='utf-8'))
if __name__ == '__main__':
    methon = "word"
    jifen = jiebafenci(method=methon,fileSegWordDonePath ='D:\\chinese\\corpusSegDone_{method}.txt'.format(method=methon))
    jifen.segment()
    jifen.write_to_file()