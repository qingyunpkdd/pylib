#-*- encoding:utf-8 -*-
__author__ = ''

#E:\\coral reefs data\\NCBI\\text\\abc.txt

import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S',
#                     filename='E:\\coral reefs data\\NCBI\\text\\abc.txt', filemode='w')
#
# logger = logging.getLogger(__name__)
# logging.debug('this is debug message')
# logging.info('this is info message')
# logging.warning('this is warning message')

# logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
#                     filename='E:\\coral reefs data\\NCBI\\text\\abcd.txt',
#                     filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
#                     #a是追加模式，默认如果不写的话，就是追加模式
#                     format=
#                     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
#                     #日志格式
#                     )
import logging
from logging.handlers import HTTPHandler
import sys

logger = logging.getLogger("test.txt")
logger.setLevel(level=logging.DEBUG)

# # StreamHandler
# stream_handler = logging.StreamHandler(sys.stdout)
# stream_handler.setLevel(level=logging.DEBUG)
# logger.addHandler(stream_handler)
#
# # FileHandler
# file_handler = logging.FileHandler('E:\\coral reefs data\\NCBI\\text\\abcd.txt',mode='a')
# file_handler.setLevel(level=logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)
logger.addHandler(ch)


fh = logging.FileHandler("E:\\coral reefs data\\NCBI\\text\\abcd.txt",mode='a')
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')