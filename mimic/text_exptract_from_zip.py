#-*- encoding:utf-8 -*-
__author__ = ''
import random
import zipfile
import re
from tqdm import tqdm

def random_sample(data,size):
    data_size = len(data)
    data_seq = range(0,data_size)
    return random.sample(data_seq,size)

def extract_file(zip_file,ex_dir="",size=2000,size_threshold=1024,content="history"):
    print("read zip file...")
    zip_file = zipfile.ZipFile(zip_file,"r")
    file_nos = random_sample(zip_file.namelist(),size)
    file_nos = tqdm(file_nos)
    print("writing file")
    for file_i in file_nos:
        file_name = zip_file.namelist()[file_i]
        #test the file size and content
        file_info = zip_file.getinfo(file_name)
        file_size = file_info.file_size
        if file_size >= size_threshold:
            contents = zip_file.read(file_name)
            contents = contents.decode()
            match_result = re.search(content,contents, re.IGNORECASE)
            if match_result:
                zip_file.extract(file_name, ex_dir)
if __name__== "__main__":
    ex_dir = "F:\\clinical_NLP\\hyper_sample_filed"
    no_dir = "F:\\clinical_NLP\\non_hyper_sample_filed"
    zip_file = "F:\\clinical_NLP\\hypertention_all.zip"
    no_zip_file = "F:\\clinical_NLP\\non_hypertention_all.zip"
    size=100000
    size_threshold=1000
    content="chief"
    extract_file(zip_file=zip_file,ex_dir=ex_dir,size=size,size_threshold=size_threshold,content=content)
    extract_file(zip_file=no_zip_file,ex_dir=no_dir,size=size,size_threshold=size_threshold,content=content)