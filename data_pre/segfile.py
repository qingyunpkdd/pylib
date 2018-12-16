#-*- encoding:utf-8 -*-
__author__ = ''
file_path = "D:\\chinese\\word2vec_corpus\\pre_segment\\merged_ehr_2.txt"
with open(file_path,'r',encoding='utf-8') as f:
    lines = []
    i = 0
    for line in f:
        lines.append(line)
        i = i + 1
        if i%100 == 0:
            file_name = "D:\\chinese\\word2vec_corpus\\pre_segment\\segfile{0}".format(i)
            fw = open(file_name,'w')
            [fw.write(line) for line in lines]
            fw.close()
            lines = []