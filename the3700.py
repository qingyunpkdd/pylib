#-*- encoding:utf-8 -*-
__author__ = ''
#
import re
import sys
import os

#this class find_lable and save it
class find_lable():
    def __init__(self,ref_filepath,seper=',',desfilepath = "d:\\a.txt",desseper=','):
        self.path = ref_filepath
        self.speer = seper
        self.map_dic = {}
        self.desfilepath = desfilepath
        self.desseper = desseper
    def build_dict(self):
        try:
            f = open(self.path,'r')
            for line in f.readlines():
                try:
                    #asumpt that first elemnet is lable second is id
                    [d_value,d_key] = line.split(self.speer)
                    self.map_dic[d_key] = d_value
                except:
                    pass
        except:
            pass
        finally:
            f.close()
    def add_lable_line(self):
        with open(self.desfilepath,'r') as fs:
            for line in fs.readlines():
                if line.split(self.desseper)[0] == 'rid':
                    id_list = line.split(self.desseper)[1:]
                    break
            id_lable = "rid"+self.desseper
            for id in id_list:
                id_lable = self.map_dic.get(id) + self.desseper
            def DelLastChar(str):
                str_list = list(str)
                str_list.pop()
                return "".join(str_list)
            id_lable = DelLastChar(id_lable)
        with open(self.desfilepath,'a') as fs:
            fs.write(id_lable)

class gene_pathway_map ():
    #read the reaction pathway data and put it into a dict
    def __init__(self,s_filepath,d_filepath,s_sep = '\t',d_sep = '\t'):
        self.s_filepath = s_filepath
        self.s_sep = s_sep
        self.d_filepath = d_filepath
        self.d_sep = d_sep
        self.gene_dict = {}
        self.pathway_dict = {}
    def data_extract(self):
        with open(self.s_filepath,'r') as fs:
            for line in fs.readlines():
                ele_list = line.split(self.s_sep)
                pathway_name  = ele_list[1]
                gene_list = ele_list[3:]
        return pathway_name, gene_list
    def build_gene_dic(self):
        pathway_name, gene_list = self.data_extract()
        for gene in gene_list:
            if not(self.gene_dict.has_key(gene)):
                self.gene_dict[gene] = [pathway_name]
            if not(pathway_name in self.gene_dict[gene]):
                self.gene_dict[gene] = self.gene_dict[gene].append(pathway_name)
        return self.gene_dict
    def build_pathway_dic(self):
        pathway_name, gene_list = self.data_extract()
        self.pathway_dict[pathway_name] = gene_list
        return self.pathway_dict
    #this section below is try to save the dict to a file in need,which just store the import information and omit the rest.
    # def write_file(self):

