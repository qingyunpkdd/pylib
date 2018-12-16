#-*- encoding:utf-8 -*-
__author__ = ''
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

#disease_gene_dic = {}
file_dir = "F:\\dictionary\\PATHWAY\\reactome_pathway\\ReactomePathways.gmt"
processed_file = "F:\\dictionary\\PATHWAY\\reactome_pathway\\pawhway_processed.txt"
with open(processed_file,'w') as fw:
    with open(file_dir,'r') as fp:
        for line in fp:
            line = line.strip('\n')
            tem = line.split("\t")
            pa_id = tem[1]
            gene_set = tem[2:]
            #disease_gene_dic[tem[1]] = tem[1:]
            for gene in gene_set:
                fw.write(str(pa_id))
                fw.write('\t')
                fw.write(str(gene))
                fw.write("\n")
print "finished"

