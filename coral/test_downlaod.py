#-*- encoding:utf-8 -*-
__author__ = ''
import sys
import os
from pySmartDL import SmartDL


dirs = "E:\\coral reefs data\\reef genome sumup\\"
urls = "http://mirror.ufs.ac.za/7zip/9.20/7za920.zip"
#sys.path.append('../')
# from my_lib import download_kits
# state_d = download_kits.download(urls,dirs)
obj = SmartDL(urls, dirs)
obj.start()
path = obj.get_dest()