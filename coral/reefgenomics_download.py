#-*- encoding:utf-8 -*-
#python version = 2.7
__author__ = ''
import sys
import subprocess
import os
import logging
#sys.path.append('package addtress')
sys.path.append('../')
from my_lib import download_kits


# urls = ['https://eyes.nasa.gov/eyesproduct/EYES/os/win']
# dirs = "D:\\pylib\\my_lib\\testdir\\abc.txt"
# cwd = os.getcwd()
# print cwd


logger = logging.getLogger('reefgenome_download')
logger.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)
logger.addHandler(ch)


fh = logging.FileHandler("E:\\coral reefs data\\reef genome sumup\\reefgenomics_download.log")
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)



#识别文件中的url地址，同时将文件存储为相应的网址文件，文件名如何命名呢？
# md5
import hashlib
# def md5(str):
#     import hashlib
#     m = hashlib.md5()
#     m.update(str)
#     return m.hexdigest()

#遍历文件夹，并将每个文件新建一个文件夹，将文件名分离出来，然后新建文件
import multiprocessing
import time



def main(path,data_path):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path,filename)):
            if not os.path.exists(os.path.join(path,data_path,filename)):
                os.mkdir(os.path.join(path,data_path,filename))
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path,filename)):
            file_dic = process_file(os.path.join(path,filename))
            for _url,_file in file_dic.items():
                _dir = os.path.join(path,data_path,filename,_file)
                if os.path.exists(_dir):
                    logging.info("file already exists")
                print "download file{url}".format(url=_url)
                # pool.apply_async(download_kits.download, (_url,_dir))
                # n_p += 1
                # if n_p%10 == 0:
                #     pool.close()
                #     pool.join()
                state_d = False
                try:
                    state_d = download_kits.download(_url,_dir)
                except:
                    logging.info(_url + "download failed")
                message = "\t".join([_url, _file, str(state_d)])
                logging.info(message)

def process_file(file_name):
    file_dic = {}
    with open(file_name,'r') as fp:
        for line in fp:
            urls = extract_url(line.strip('\n'))
            if urls:
                for url in urls:
                    file_dic[url] = url.split('/')[-1]
    return file_dic
def extract_url(str):
    urls = []
    tems = str.split('\t')
    for t in tems:
        if t.startswith('http://'):
            urls.append(t)
    return urls

if __name__ == "__main__":
    list_file_path = "E:\\coral reefs data\\reef genome sumup\\reefgenomics"
    data_path = "data_path"
    main(path=list_file_path,data_path=data_path)











# for url in urls:
#     #cmds = "python2 ..\\my_lib\\download_kits.py {u} -o {d}".format(u = url, d = dirs)
#     state_d = download_kits.download(url,dirs)
#     print state_d
#     #os.system(cmds)









