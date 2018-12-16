#-*- encoding:utf-8 -*-
__author__ = ''
import tensorflow as tf
import numpy as np
import matplotlib as mp
import codecs
import numpy as np
#load data of zhihu
import os
import pickle
PAD_ID = 0
_GO="_GO"
_END="_END"
_PAD="_PAD"

file_name_list = ["a.txt","b.txt","c.txt"]
filename_queue = tf.train.string_input_producer(file_name_list)

def read_my_file_format(filename_queue,vocabulary_word2index,vocabulary_word2index_label,traning_data_path="",seq2seq_label_length=6,use_seq2seq=False,multi_label_flag=True):
    reader = tf.TextLineReader()
    key, value = reader.read(filename_queue)
    #processing the file content
    x, y = value.split('__label__')
    y = y.strip().replace('\n', '')
    x = x.strip()
    x = [vocabulary_word2index.get(e, 0) for e in x]
    if use_seq2seq:  # 1)prepare label for seq2seq format(ADD _GO,_END,_PAD for seq2seq)
        ys = y.replace('\n', '').split(" ")  # ys is a list
        _PAD_INDEX = vocabulary_word2index_label[_PAD]
        ys_mulithot_list = [_PAD_INDEX] * seq2seq_label_length  # [3,2,11,14,1]
        ys_decoder_input = [_PAD_INDEX] * seq2seq_label_length
        # below is label.
        for j, y in enumerate(ys):
            if j < seq2seq_label_length - 1:
                ys_mulithot_list[j] = vocabulary_word2index_label[y]
        if len(ys) > seq2seq_label_length - 1:
            ys_mulithot_list[seq2seq_label_length - 1] = vocabulary_word2index_label[_END]  # ADD END TOKEN
        else:
            ys_mulithot_list[len(ys)] = vocabulary_word2index_label[_END]

        # below is input for decoder.
        ys_decoder_input[0] = vocabulary_word2index_label[_GO]
        for j, y in enumerate(ys):
            if j < seq2seq_label_length - 1:
                ys_decoder_input[j + 1] = vocabulary_word2index_label[y]
    else:
        if multi_label_flag:  # 2)prepare multi-label format for classification
            ys = y.replace('\n', '').split(" ")  # ys is a list
            ys_index = []
            for y in ys:
                y_index = vocabulary_word2index_label[y]
                ys_index.append(y_index)
            ys_mulithot_list = transform_multilabel_as_multihot(ys_index)
        else:  # 3)prepare single label format for classification
            ys_mulithot_list = vocabulary_word2index_label[y]
    label = ys_mulithot_list
    processed_example = x
    return processed_example, label
def input_pipeline(filenames, batch_size, num_epochs=None):
  filename_queue = tf.train.string_input_producer(
      filenames, num_epochs=num_epochs, shuffle=True)
  example, label = read_my_file_format(filename_queue)
  # min_after_dequeue defines how big a buffer we will randomly sample
  #   from -- bigger means better shuffling but slower start up and more
  #   memory used.
  # capacity must be larger than min_after_dequeue and the amount larger
  #   determines the maximum we will prefetch.  Recommendation:
  #   min_after_dequeue + (num_threads + a small safety margin) * batch_size
  min_after_dequeue = 10000
  capacity = min_after_dequeue + 3 * batch_size
  example_batch, label_batch = tf.train.shuffle_batch([example, label], batch_size=batch_size, capacity=capacity,min_after_dequeue=min_after_dequeue)
  return example_batch, label_batch





#processing multilabels
def transform_multilabel_as_multihot(label_list,label_size=1999): #1999label_list=[0,1,4,9,5]
    """
    :param label_list: e.g.[0,1,4]
    :param label_size: e.g.199
    :return:e.g.[1,1,0,1,0,0,........]
    """
    result=np.zeros(label_size)
    #set those location as 1, all else place as 0.
    result[label_list] = 1
    return result


#should increase in the main train steps
with tf.Session() as sess:
  # Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)
