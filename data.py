#
# csv_reader = csv.reader(open('F:\\R\\expressiondata\\data_row_as_sample_label.csv'))
# dataarray = []
# for row in csv_reader:
#  for element in row:
#   row = []
#   row.extend(element)
#  dataarray.append(row)
#
# #read the label
#
#
# #read the data_array
#
# #data_array row as sample, colume as gene;
# import numpy as np
# data_ar=np.array(data_array)
# label_ar=np.array(label_array)
#
#
# #transform the data format
# data=data.astype(np.int32)
# data=data.astype(np.float32)
#
#
# for row in label_array:
#  if len(row)==2: label = row[1]
#  labels.extend(label)
# best way to doing the pipline is to split the data to some small files
 #split the fille into a small dataset
'''this is a python3 script'''
import os
#deal the header.

# remove the row header
import csv
filepath = "F:\\R\\expressiondata\\data_row_as_sample_normed.csv"
write_filepath = "F:\\R\\expressiondata\\data_row_as_sample_normed_e.csv"
csv_reader = csv.reader(open(filepath))
csv_writer = csv.writer(open(write_filepath,'w'),dialect="excel", lineterminator='\n')
i = 0
for row in csv_reader:
 if i == 0:
  i+=1
  continue
 row = row[1:]
 row = tuple(row)
 csv_writer.writerow(row)
print("abc")

import csv
import os
class CsvSplit():
 def __init__(self,filedir,apix = "_batch_{0}",num_of_each = 1000,delete_col = False):
  self.apix = apix
  self.filepath = filedir
  self.num_of_each = num_of_each
  #split the file content
  self.file_path,self.file_name_ex = os.path.split(self.filepath)
  self.file_name,self.extension = os.path.splitext(self.file_name_ex)
  self.delete_col = delete_col
 def split_data(self):
  csv_reader = csv.reader(open(self.filepath))
  rows = []
  counter = 0
  for row in csv_reader:
   if (len(rows)==self.num_of_each):
    with open(self.file_path + "\\" + self.file_name + self.apix.format(counter*self.num_of_each) + self.extension,'w') as fw:
     f_csv = csv.writer(fw,dialect="excel",lineterminator='\n')
     f_csv.writerows(rows)
     print("write file {filename}".format(filename = counter))
     counter =counter + 1
     rows = []
   else:
    if self.delete_col == True:
     row = tuple(row[1:])
    row = tuple(row)
    rows.append(row)
  #write the rest data into the left file
  if len(rows)!=0:
   with open(self.file_path + "\\" + self.file_name + self.apix.format(counter * self.num_of_each) + self.extension, 'w') as fw:
    f_csv = csv.writer(fw, dialect="excel", lineterminator='\n')
    f_csv.writerows(rows)
    print("write file {filename}".format(filename=counter))

filedir = "F:\\R\\expressiondata\\data_row_as_sample_label.csv"
sp_file = CsvSplit(filedir = filedir,num_of_each=1000)
sp_file.split_data()

filedir = "F:\\R\\expressiondata\\data_row_as_sample.csv"
sp_file = CsvSplit(filedir = filedir,num_of_each=1000,delete_col=True)
sp_file.split_data()



#label
#extend is very carefully.
import csv
import numpy as np
def read_labels(file_path):
 csv_reader = csv.reader(open('F:\\R\\expressiondata\\data_row_as_sample_label.csv'))
 label_array = []
 for row in csv_reader:
   label_array.append(row)
 label_array=label_array[1:]
 labels = []
 for i in range(len(label_array)):
  label = label_array[i][1]
  label = [int(label)]
  labels.extend(label)
 labels=np.array(labels)
 labels=labels.astype(np.int32)
 del label_array

#data
#read the split file and make a batch.calculate the sample location and then load it into
# import re
# class DataExtract():
#  def __init__(self,base_filename,sample_id):
#   self.base_filename = base_filename
#   self.sample_id = sample_id.sort()
#   self.file_path, self.file_name_ex = os.path.split(self.base_filename)
#   self.file_name, self.extension = os.path.splitext(self.file_name_ex)
#  def return_data(self):
#   batch = re.search(r'(\d+)',self.file_name,re.I|re.M)
#   self.batch = batch.group(1)
#   file_to_read = {}
#   for each_sample in self.sample_id;
#    file_id = int(each_sample/batch)*


# batch = 0 #
# sample_id = 0 #
# file_id = 0 #
# #sample_id to file_id
# file_id = int(sample_id/batch)*batch

#
#read each file for train, test, and validate
csv_reader = csv.reader(open('F:\\R\\expressiondata\\data_row_as_sample.csv'))
data_array = []
for row in csv_reader:
  data_array.append(row)
#make sure have enough memory size.
data_ar=np.array(data_array)
datas=data_ar.astype(np.float32)

import random
import numpy
class DataSplite():
 def __init__(self,labels,train_rate=0.8,test_rate=0.1,validate_rate=0.1):
  self.train_rate = train_rate
  self.test_rate = test_rate
  self.validate_rate = validate_rate
  self.labels = labels
 def class_label_id_set(self):
  class_name = "class_{0}"
  class_l = {}
  id_i = 0
  for id in self.labels:
   i_name  = class_name.format(id)
   if i_name in class_l:
    class_l[i_name].append(id_i)
   else:
    class_l[i_name] = [id_i]
   id_i = id_i + 1
  return class_l
 #@property
 def set_id(self,class_l):
  train_id = []
  test_id = []
  validate_id = []
  for lb in class_l:
   len_lb = len(class_l[lb])
   if len_lb>= 3:
    train_id.extend(class_l[lb][0:int(self.train_rate*len_lb)])
    test_id.extend(class_l[lb][int(self.train_rate*len_lb)+1:int((self.train_rate+self.test_rate)*len_lb)])
    validate_id.extend(class_l[lb][int(((self.train_rate+self.test_rate))*len_lb)+1:int(len_lb)])
   else:
    train_id = class_l[lb]
  return [train_id,test_id,validate_id]
# sp = DataSplite(labels)
# class_l = sp.class_label_id_set()
# [tr_id,te_id,val_id] = sp.set_id(class_l)

#data and label split
# train_data =
# test_data =
# validate_data =
# train_label =
# test_label =
# validate_label =
