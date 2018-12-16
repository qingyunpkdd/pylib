#! /usr/bin/env python
# encoding=utf-8

from __future__ import unicode_literals

from multiprocessing.dummy import Pool as ThreadPool
import threading

import os
import sys
import cPickle
from collections import namedtuple
import urllib2
from urlparse import urlsplit
import time


# global lock
lock = threading.Lock()


# default parameters
defaults = dict(
    thread_count=10,
    buffer_size=500 * 1024,
    block_size=1000 * 1024)


def progress(percent, width=50):
    print "%s %d%%\r" % (('%%-%ds' % width) % (width * percent / 100 * '='), percent),
    if percent >= 100:
        print "文件下载成功"
        sys.stdout.flush()


def write_data(filepath, data):
    with open(filepath, 'wb') as output:
        cPickle.dump(data, output)


def read_data(filepath):
    with open(filepath, 'rb') as output:
        return cPickle.load(output)


FileInfo = namedtuple('FileInfo', 'url name size lastmodified')


def get_file_info(url):
    class HeadRequest(urllib2.Request):

        def get_method(self):
            return "HEAD"
    res = urllib2.urlopen(HeadRequest(url))
    res.read()
    headers = dict(res.headers)
    size = int(headers.get('content-length', 0))
    lastmodified = headers.get('last-modified', '')
    name = None
    if headers.has_key('content-disposition'):
        name = headers['content-disposition'].split('filename=')[1]
        if name[0] == '"' or name[0] == "'":
            name = name[1:-1]
    else:
        name = os.path.basename(urlsplit(url)[2])

    return FileInfo(url, name, size, lastmodified)


def download(url, output,
             thread_count=defaults['thread_count'],
             buffer_size=defaults['buffer_size'],
             block_size=defaults['block_size']):
    # get latest file info
    file_info = get_file_info(url)

    # init path
    if output is None:
        output = file_info.name
    workpath = '%s.ing' % output
    infopath = '%s.inf' % output

    # split file to blocks. every block is a array [start, offset, end],
    # then each greenlet download filepart according to a block, and
    # update the block' offset.
    blocks = []

    if os.path.exists(infopath):
        # load blocks
        _x, blocks = read_data(infopath)
        if (_x.url != url or
                _x.name != file_info.name or
                _x.lastmodified != file_info.lastmodified):
            blocks = []

    if len(blocks) == 0:
        # set blocks
        if block_size > file_info.size:
            blocks = [[0, 0, file_info.size]]
        else:
            block_count, remain = divmod(file_info.size, block_size)
            blocks = [[i * block_size, i * block_size,
                       (i + 1) * block_size - 1] for i in range(block_count)]
            blocks[-1][-1] += remain
        # create new blank workpath
        with open(workpath, 'wb') as fobj:
            fobj.write('')

    print 'Downloading %s' % url
    # start monitor
    threading.Thread(target=_monitor, args=(
        infopath, file_info, blocks)).start()

    # start downloading
    with open(workpath, 'rb+') as fobj:
        args = [(url, blocks[i], fobj, buffer_size)
                for i in range(len(blocks)) if blocks[i][1] < blocks[i][2]]

        if thread_count > len(args):
            thread_count = len(args)

        pool = ThreadPool(thread_count)
        pool.map(_worker, args)
        pool.close()
        pool.join()

    # rename workpath to output
    if os.path.exists(output):
        os.remove(output)
    os.rename(workpath, output)

    # delete infopath
    if os.path.exists(infopath):
        os.remove(infopath)
    try:
        assert all([block[1] >= block[2] for block in blocks]) is True
        state_d = True
    except:
        state_d = False
    return state_d


def _worker((url, block, fobj, buffer_size)):
    req = urllib2.Request(url)
    req.headers['Range'] = 'bytes=%s-%s' % (block[1], block[2])
    res = urllib2.urlopen(req)

    while 1:
        chunk = res.read(buffer_size)
        if not chunk:
            break
        with lock:
            fobj.seek(block[1])
            fobj.write(chunk)
            block[1] += len(chunk)


def _monitor(infopath, file_info, blocks):
    while 1:
        with lock:
            percent = sum([block[1] - block[0]
                           for block in blocks]) * 100 / file_info.size
            progress(percent)
            if percent >= 100:
                break
            write_data(infopath, (file_info, blocks))
        time.sleep(2)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='多线程文件下载器.')
    parser.add_argument('url', type=str, help='下载连接')
    parser.add_argument('-o', type=str, default=None,
                        dest="output", help='输出文件')
    parser.add_argument(
        '-t', type=int, default=defaults['thread_count'], dest="thread_count", help='下载的线程数量')
    parser.add_argument(
        '-b', type=int, default=defaults['buffer_size'], dest="buffer_size", help='缓存大小')
    parser.add_argument(
        '-s', type=int, default=defaults['block_size'], dest="block_size", help='字区大小')

    argv = sys.argv[1:]

    if len(argv) == 0:
        argv = ['https://eyes.nasa.gov/eyesproduct/EYES/os/win']

    args = parser.parse_args(argv)

    start_time = time.time()
    state_d = download(args.url, "D:\\pylib\\my_lib\\testsss.ext")
    # download(args.url, args.output, args.thread_count,
             # args.buffer_size, args.block_size)
			 
    import sys
    print '下载时间: %ds' % int(time.time() - start_time)