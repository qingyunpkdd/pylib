#-*- encoding:utf-8 -*-
__author__ = ''
#这个模块用来分析疾病的分类信息，如这个疾病是属于哪个大类的以及属于哪个小类的。
class D120ask():
    def __init__(self,disease_id,disease_name=None,main_id = None,sub_id = None):
        self.disease_id = disease_id
        self.disease_name = disease_name
        self.main_id = main_id
        self.sub_di = sub_id
    def tag_main_id(self):
    #read the D:\chinese\d120ask_dict\all_catalogue_info.txt,
    #then find the information about the hole files

