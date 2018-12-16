#-*- encoding:utf-8 -*-
__author__ = ''
import os
#this class are used to count the file in same catalogue
class Count_DirFile():
    def __init__(self,dir,workpath,save_dir,save_filenm):
        self.dir = dir
        self.workpath = workpath
        self.save_dir = save_dir
        self.save_filenm = save_filenm
    def count_case(self):
        count_dir = {}
        for root, dirs, files in os.walk(self.workpath):
            if root.split("\\")[-1]==self.dir:
                file_c = len(files)
                p_dir = os.path.dirname(root).split("\\")[-1]
                count_dir[p_dir]=file_c
        return count_dir
    #dis_case = count_case("D:\\chinese\\d120ask_pro")
    def save_file(self,count_dir):
        print(len(count_dir))
        fp = open(self.save_filenm, 'a')
        for key, value in count_dir.items():
            fp.write(str(key))
            fp.write(":")
            fp.write(str(value))
            fp.write("\n")
        fp.close()
if __name__ == '__main__':
    count = Count_DirFile(dir = "case",workpath = "D:\\chinese\\d120ask_pro", save_dir = "d:\\",save_filenm = "d:\\dis_case.txt")
    count_dir = count.count_case()
    count.save_file(count_dir)
