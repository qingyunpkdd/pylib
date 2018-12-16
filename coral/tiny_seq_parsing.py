# -*- encoding:utf-8 -*-
__author__ = ''
from lxml import etree
import re
import os
import sys

sys.path.append('../')
from my_lib import Logger_my


class TinySeq():
    def __init__(self, file_path="", des_file_path="", mysql_table_name=""):
        self.filepath = file_path
        self.des_file_path = des_file_path
        self.table_name = mysql_table_name
        self.re_start = re.compile(r'^<TSeq>$')
        self.re_end = re.compile(r'^</TSeq>$')
        # self.field_seqtype = [""]
        # self.field_accver =[""]
        # self.field_taxid =[""]
        # self.field_orgname =[""]
        # self.field_defline =[""]
        # self.field_length =[""]
        # self.field_sequence =[""]
        self.fp = ""
        self.i = 0

    def generate_lxml(self):
        with open(self.filepath, 'r', encoding='utf-8') as fp:
            _batch = ""
            while True:
                self.i += 1
                if self.i % 10000 == 0:
                    print(self.i)
                line = fp.readline()
                if line == '\n':
                    _batch = _batch.replace('\t', ' ')
                    yield _batch
                    _batch = ""
                elif not line:
                    yield _batch
                    break
                else:
                    _batch += line

    def xml_parse(self, xml_f):
        xml_dict = {}
        try:
            xml_p = etree.XML(xml_f)
        except:
            print("parsing error!")
            log_.logger.warning("parsing error!" + "in line" + str(self.i) + str(xml_f))
            # print(str(xml_f))
            return {}
        # root = xml_p.getroot()
        for _tag in xml_p:
            if _tag.tag == "TSeq_seqtype":
                xml_dict[str(_tag.tag)] = str(_tag.get("value"))
            else:
                xml_dict[str(_tag.tag)] = str(_tag.text)
        return xml_dict

    def tsv_open(self, file_path):
        self.fp = open(file_path, 'a+')

    def tsv_close(self):
        self.fp.close()

    def save_to_file(self, xml_dict):
        field_order = ["TSeq_seqtype", "TSeq_accver", "TSeq_taxid", "TSeq_orgname", "TSeq_defline", "TSeq_length",
                       "TSeq_sequence"]
        if not self.fp:
            try:
                os.remove(self.des_file_path)
            except:
                print("output file clear ok")
            self.tsv_open(self.des_file_path)
        if not os.path.getsize(self.des_file_path):
            tit = ""
            for e in field_order:
                if tit:
                    tit = tit + "\t" + e
                else:
                    tit = e
            tit.strip('\t')
            tit = tit + "\n"
            self.fp.write(tit)
            self.fp.flush()
        content = []
        for _f in field_order:
            if _f in xml_dict:
                content.append(xml_dict[_f])
            else:
                info = [str(k) + "\t" + str(v) for k, v in xml_dict.items()]
                info = "--".join(info)
                log_.logger.warning(str(_f) + info)
                content.append("")
        _line = "\t".join(content)
        self.fp.write(_line)
        self.fp.write('\n')
        if self.i % 100 == 0:
            self.fp.flush()

    def save_to_mysql(self):
        pass


if __name__ == "__main__":
    source_file_path = "E:\\coral reefs data\\NCBI\\text\\tiny_sequence.fasta.xml"
    def_file_path = "E:\\coral reefs data\\NCBI\\text\\tiny_sequence.fasta.tsv"
    tinyseq = TinySeq(file_path=source_file_path, des_file_path=def_file_path, mysql_table_name="")
    log_ = Logger_my.Logger("E:\\coral reefs data\\NCBI\\text\\abc.log", level="debug")
    for _xml in tinyseq.generate_lxml():
        xml_dict = tinyseq.xml_parse(_xml)
        if xml_dict:
            tinyseq.save_to_file(xml_dict)
    tinyseq.fp.close()
