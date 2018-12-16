#-*- encoding:utf-8 -*-
__author__ = ''
import os
import time
import shutil
def del_files(path):
    #[copy_file for root, dirs, copy_file in os.walk(path)]
    for root , dirs, files in os.walk(path):
        try:
            for name in files:
                 if name.endswith(""):
                    try:
                        os.remove(os.path.join(root, name))
                        print("Delete File: " + os.path.join(root, name))
                    except:
                        print('can\'t remove file')
                        continue
        except:
            break
# test
def copy_undump_file(src_path, ref_paht, des_path):
    src_files = set(os.listdir(src_path))
    ref_files = set(os.listdir(ref_paht))
    not_processed_files = list(src_files - ref_files)
    if not os.listdir(des_path):
        for file_i in not_processed_files:
            shutil.copy2(os.path.join(src_path,file_i),des_path)
        print('{lens} files copyed'.format(lens=len(not_processed_files)))
if __name__ == "__main__":
    path = 'F:/clinical_NLP/ClampCmd_1.4.0/output_1/'
    ref_path = 'F:/clinical_NLP/ClampCmd_1.4.0/output_1/'
    des_path = 'F:/clinical_NLP/ClampCmd_1.4.0/input_tem/'
    src_path = 'F:/R/mimic/seg_files_doc/'
    copy_undump_file(src_path=src_path,ref_paht=ref_path,des_path=des_path)
    while (True):
        print('checking dir...')
        del_files(path)
        time.sleep(60)