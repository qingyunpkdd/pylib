import os
import sys
import logging
import argparse
from Bio import SeqIO
import subprocess

def logger_info(file_level, console_level = logging.INFO, logger_file='log.txt', outdir='./'):
    '''
    create log file when running pipeline
    :param file_level: file level
    :param console_level: console level (default=logging.INFO)
    :param logger_file: log file name (default=log.txt)
    :param outdir: output directory (default=./)
    :return logger
	
    '''
    function_name = os.path.join(outdir, logger_file)
    logger = logging.getLogger(function_name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(console_level)
    ch_format = logging.Formatter('%(asctime)s-%(message)s')
    ch.setFormatter(ch_format)
    logger.addHandler(ch)

    fh = logging.FileHandler("{0}.log".format(function_name), mode='w')
    fh.setLevel(file_level)
    fh_format = logging.Formatter('%(asctime)s - %(lineno)d - %(levelname) -4s- %(message)s')
    fh.setFormatter(fh_format)
    logger.addHandler(fh)
    return logger

def create_dir(root, subdir=None):
    '''
    create sub-directory in root directory
    :param root: root directory
    :param subdir: target create directory nam
    :return path
	
    '''
    if subdir:
	path = os.path.join(root, subdir)
    else:
	path = root

    0 if os.path.exists(path) else os.mkdir(path)
    return path

def search_tool(tool):
    '''
    search tool on the platform path or not
    :param tool: tool name
    :return tool_path
    
    '''
    cmd       = 'where' if 'WIN' in sys.platform.upper() else 'which'
    tool_path = subprocess.Popen([cmd, tool], stdout=subprocess.PIPE).communicate()[0].strip()
    return tool_path

def convert_seq_fmt(seq_fil, in_fmt, out_fmt):
    '''
    convert sequence file format
    :param seq_fil: input sequence file
    :param in_fmt: input sequence file format
    :param out_fmt: output format
    :return out_fmt_name
    
    '''
    out_handle = open(seq_fil.rsplit('.', 1)[0] + '.' + out_fmt, 'w')
    SeqIO.convert(seq_fil, in_fmt, out_handle, out_fmt)
    out_handle.close()

    return out_handle.name

def myround(x, base=10):
    '''
    round the input integer number
    :param x: input integer number
    :param base: binary or decimal (default=10)
    :return int

    '''
    return int(round(int(x), -1))

def parser_check(parser):
    '''
    check output path is specified or not
    :param parser: parser object
    :return: args
    '''
    if not isinstance(parser, argparse.ArgumentParser):
        parser = argparse.ArgumentParser()
        parser.add_argument('--fastq',
                            help    = 'Nanopore long-read RNASeq fastq format data',
                            metavar = '<FILE>',
                            type    = str,
                            default = None)
        parser.add_argument('--outdir',
                            help    = 'Output directory (default: ./)',
                            metavar = '<DIR>',
                            type    = str,
                            default = './')
    return parser


