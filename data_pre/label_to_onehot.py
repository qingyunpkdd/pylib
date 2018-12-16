#-*- encoding:utf-8 -*-
__author__ = ''
import tensorflow as tf
def label_to_onehot(labels):
    # label_unique = {}.fromkeys(labels).keys()
    label_set = set(labels)
    label_dictionary ={}
    for i, ele in enumerate(label_set):
        label_dictionary[ele] = i
    label_index_list = [label_dictionary[l] for l in labels]
    print("number of class:%s" %str(len(label_dictionary)))
    label_onehot = tf.one_hot(label_index_list, len(label_dictionary), 1, 0)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        sess.run(label_onehot)
        label_onehot_np = label_onehot.eval()
        print("label_onehot done")
    return label_onehot_np
if __name__ == "__main__":
    labels = ["abce","fjiew","jsifei","jifej","open","open","abce","sfjie","sjfiew","sfjie"]
    one_hot = label_to_onehot(labels)
    print(one_hot)