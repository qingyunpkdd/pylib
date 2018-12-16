# -*- encoding:utf-8 -*-
__author__ = ''
import re
import sys

sys.path.append('../')
import os
import itertools
from databases import my_pymysql
from my_lib.Logger_my import Logger


def url_processing():
    sqln = my_pymysql.SqlCon(host="10.194.181.128", db_name="corals_db")
    sqln.connect()
    sql = "select count(*) from GEO_series"
    res = sqln.runfetchall(sql)[0][0]
    for i in range(res):
        sql = "select FTP,SRA from GEO_series where id={i}".format(i=i + 1)
        _res = sqln.runfetchall(sql)
        try:
            _FTP = _res[0][0]
            _SRA = _res[0][1]
        except:
            print("fetch data error!")

        # 'FTP download: GEO (PDF, XLSX) ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE70nnn/GSE70185/'
        # 'SRA Run Selector: https://www.ncbi.nlm.nih.gov/Traces/study/?acc=PRJNA290330'
        if _FTP != "":
            _pat = re.compile(r'(ftp:.*?$)', re.I)
            _pat_res = re.search(_pat, _FTP).group(1)
            log.logger.info(_pat_res)
            sql = "update GEO_series set FTP = '{ftp}' where id={i}".format(ftp=_pat_res, i=i + 1)
            result = sqln.run(sql)
            print("aa")
            log.logger.info(str(i) + "FTP" + str(result))
        if _SRA != "":
            _pat = re.compile(r'(https:.*?$)', re.I)
            _pat_res = re.search(_pat, _SRA).group(1)
            sql = "update GEO_series set SRA = '{sra}' where id={i}".format(sra=_pat_res, i=i + 1)
            result = sqln.run(sql)
            print("aa")
            log.logger.info(str(i) + "SRA" + str(result))
    sqln.dbclose()


if __name__ == "__main__":
    log = Logger('E:\\coral reefs data\\NCBI\\text\\geo_url_process.txt', level='debug')
    url_processing()
