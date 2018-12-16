#-*- encoding:utf-8 -*-
__author__ = ''
#分别读取疾病名称和疾病的EHR描述，然后将疾病名称作为大类，将描述为文本，将每一个相关的内容做tf-idf 计算，调用python的包做，时间两个小时做完。
import os





class SimpleCalculate():
    def __init__(self,dir):
        self.dir = dir
    def file_merge(self):
        disease = {}
        for filename in os.listdir(self.dir):
            disease_id = filename.split("_")[0]
            with open(filename,'r',encoding="uff-8") as fp:
                content = str(fp.read())
            dict_d = {str(disease_id):content}
            if (not disease_id in disease):
                disease.update(dict_d)
            else:
                disease[disease_id] = disease[disease_id] + content
    def calculatetfidf(self):
        pass
    def




