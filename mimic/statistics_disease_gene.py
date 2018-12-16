#-*- encoding:utf-8 -*-
__author__ = ''
__author__ = ''
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
#F:\dictionary\dis_gene\curated_gene_disease_associations.tsv
#方案一，对于每一个疾病构建一个基因集合，如果两个疾病的基因集合有交集，则说明问题。



#dis_gene_co.csv header is #geneSymbol #diseaseId #diseaseName #score
file_dir  = ""







#build the dictionary
disease_gene_set = {}
with open(file_dir,'r') as fp:
    for line in fp:
        tem = line.split(',')
        geneSymbol = tem[0]
        diseaseId = tem[1]
        diseaseName = tem[2]
        if not disease_gene_set[diseaseId]:
            disease_gene_set[diseaseId] = set()
            disease_gene_set[diseaseId].add(str(geneSymbol))
        else:
            disease_gene_set[diseaseId].add(str(geneSymbol))
# if two disease are share one gene

#duild Icd9 to SNOMATCT multiply the file.





file_dir  = ""
with open(file_dir,'r') as fp:
    for line in fp:
        tem = line.split(',')
        dis_1 = tem[0]
        dis_2 = tem[1]



#build icd dictionary


#icd to CUI

dis2icd dictionary = {}
