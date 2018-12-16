#-*- encoding:utf-8 -*-
__author__ = ''
import os,sys
import hashlib
import logging
import sys
class remove_dum():
    def __init__(self,dir,md5="yes"):
        self.dir = dir
        self.md5 = md5
    def file_lists(self):
        for root,dirs,files in os.walk(self.dir):
            #print(root)
            base = root
            file_urls = []
            if files:
                for file in files:
                    file_url=base+"\\"+file
                    file_urls.append(file_url)
            if (len(file_urls)>1):
                 yield file_urls
    def get_md5(self,filename):
        m = hashlib.md5()
        mfile = open(filename, 'rb')
        m.update(mfile.read())
        mfile.close()
        md5_value = m.hexdigest()
        return md5_value
    def remove_dumps(self):
            for file_urls in self.file_lists():
                if file_urls:
                    #log = self.logger()
                    if self.md5 == "yes":
                        for file in file_urls:
                            md5List =[]
                            md5 = self.get_md5(file)
                            if (md5 in md5List):
                                os.remove(file)
                                print("重复：：%s"%file)
                                #log.info("重复：%s"%file)
                            else:
                                md5List.append(md5)
                    else:
                        content_list = []
                        for file in file_urls:
                            fp = open(file, 'r', encoding='utf-8')
                            try:
                                content = fp.read()
                                if (content in content_list):
                                    fp.close()
                                    os.remove(file)
                                    print("重复：：%s"%file)
                                else:
                                    fp.close()
                                    content_list.append(content)
                            except:
                                print("读文件错误")
                                print(str(file))
if __name__ == '__main__':
    rem = remove_dum("D:\\chinese\\d120ask_all_case",md5="no")
    rem.remove_dumps()

#reference:
# class remove_dum():
# 	def __init__(self,dir):
# 		self.dir=dir
# 	def file_lists(self):
# 		for root,dirs,files in os.walk(self.dir):
# 			base = root
# 			file_urls = []
# 			if files:
# 				for file in files:
# 					file_url=base+file
# 					file_urls= file_urls.append(file_url)
# 			yield file_urls
# 	def get_md5(self,filename):
# 		m = hashlib.md5()
# 		mfile = open(filename, "rb")
# 		m.update(mfile.read())
# 		mfile.close()
# 		md5_value = m.hexdigest()
# 		return md5_value
# 	def logger(self):
# 		logger = logging.getLogger()
# 		if not logger.handlers:
# 			# 指定logger输出格式
# 			formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
# 			# 文件日志
# 			file_handler = logging.FileHandler("d:\\test.log")
# 			file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
# 			# 控制台日志
# 			console_handler = logging.StreamHandler(sys.stdout)
# 			console_handler.formatter = formatter  # 也可以直接给formatter赋值
# 			# 为logger添加的日志处理器
# 			logger.addHandler(file_handler)
# 			logger.addHandler(console_handler)
# 			# 指定日志的最低输出级别，默认为WARN级别
# 			logger.setLevel(logging.INFO)
# 		return logger
# 	def remove_dumps(self):
# 		for file_urls in file_list():
# 			md5List =[]
# 			for file in file_urls:
# 				md5 = get_md5(filename)
# 				if (md5 in md5list):
# 					os.remove(file)
# 					pirnt("重复：：%s"%file)
# 					log.info("重复：%s"%a)
# 				else:
# 					md5List.append(md5)