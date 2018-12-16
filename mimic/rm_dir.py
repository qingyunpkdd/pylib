#-*- encoding:utf-8 -*-
__author__ = ''
import os
from tqdm import tqdm
file_dir = ""
def del_file(file_dir):
    ls = os.listdir(file_dir)
    pbar = tqdm(ls)
    for i in  pbar:
        c_path = os.path.join(file_dir,i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
if __name__=="__main__":
    file_dir = "F:\\clinical_NLP\\hypertention\\"
    del_file(file_dir=file_dir)
    # import shutil
    # shutil.rmtree(file_dir)
    # print('ok')