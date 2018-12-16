#-*- encoding:utf-8 -*-
__author__ = ''
import tensorflow as tf
import gensim
import numpy as np
def calculate_accuracy_new(label_predicted, labels, eval_counter=0, top_number=3):
    # label_predicted is model output label is real data label, top_number is cut off number of how many labels
    label_predicted = np.array(label_predicted)
    labels = np.array(labels)
    tem = label_predicted
    # argsort return the sorted array index of narray,order by ascendent the return object first element is the smallest number's index of prime array
    label_predicted = np.argsort(label_predicted, axis=1)
    label_index = label_predicted[:, :top_number]
    shape_1, shape_2 = label_index.shape
    # count the all data numbers
    all_count = shape_1 * shape_2

    length_label = label_index.shape[0]
    correction = 0
    for i in range(length_label):
        correction = correction + np.sum(labels[i,label_index[i, :]])
    return correction / all_count
test = np.arange(36).reshape(6,6)
test = np.random.randint(0,100,size=(6,6))
print(test)
labels = np.zeros((6,6),dtype=np.int32)
labels[:,1:]=1
acc = calculate_accuracy_new(label_predicted=test,labels=labels)
print(acc)