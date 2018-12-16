#-*- encoding:utf-8 -*-
__author__ = ''
import re
import os
from collections import defaultdict
from itertools import tee
from tqdm import tqdm
#将所有文件合并，方式是和知乎的相似，file.write(question_representation + " __label__" + str(topic_id_list_) + "\n")
def processing_file(rootdir="",file_to_write="",count = 10):
    disease_count = {}
    disease_file_name= {}
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in tqdm(filenames):
            ful_filename = os.path.join(parent,filename)
            if os.path.isfile(ful_filename):
                try:
                    filename_t = re.sub(r'\.txt','',filename)
                    tem = re.split(r'_', filename_t)
                    disease_name,rest_fn = tem[0],tem[1]
                except:
                    disease_name = filename
                    rest_fn = []
                if disease_name in disease_file_name:
                    disease_file_name[disease_name].append(ful_filename)
                else:
                    disease_file_name[disease_name] = [ful_filename]
                if disease_name in disease_count:
                    disease_count[disease_name] = disease_count[disease_name] + 1
                else:
                    disease_count[disease_name] = 1
                #if not re.search(r'\D',rest_fn) or rest_fn == []:
    with open(file_to_write, 'w') as fw:
        for fn in disease_file_name.keys():
           if disease_count[fn] >= count:
               for file_n in disease_file_name[fn]:
                  with open(file_n,'rb') as f:
                     try:
                       content = f.read().decode('utf-8')
                       content = re.sub('\n|\r',' ',content)
                       content = re.sub('【.*?】',' ',content)
                       content = re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z\u3002\uFF1F\uFF01\uFF0C]','',content)
                       fw.write(content)
                       fw.write(" __label__")
                       fw.write(str(fn))
                       fw.write('\n')
                     except:
                        print("file read error")
if __name__ == "__main__":
    count = 10
    file_to_write = "D:\\chinese\\ehr_zhihu_format_sample_size{size}.txt".format(size=count)
    processing_file(rootdir="D:\\chinese\\d120ask_all_case", file_to_write=file_to_write,count = count)