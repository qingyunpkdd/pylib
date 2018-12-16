from __future__ import division
from __future__ import print_function

import gzip
import csv
import numpy

from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
from flags import FLAGS
import os
import pdb

pdb.set_trace()

def dense_to_one_hot(labels_dense, num_classes=10):
  """Convert class labels from scalars to one-hot vectors."""
  num_labels = labels_dense.shape[0]
  index_offset = numpy.arange(num_labels) * num_classes
  labels_one_hot = numpy.zeros((num_labels, num_classes))
  labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
  return labels_one_hot

class DataSetPreTraining():
  def __init__(self, sample_sets):
    self._num_examples = sample_sets.shape[0]

    # Convert shape from [num examples, rows, columns, depth]
    # to [num examples, rows*columns] (assuming depth == 1)
    assert sample_sets.shape[3] == 1
    # Convert from [0, 255] -> [0.0, 1.0].
    sample_sets = sample_sets.astype(numpy.float32)
    self._sample_sets = sample_sets
    self._epochs_completed = 0
    self._index_in_epoch = 0

  @property
  def sample_sets(self):
    return self._sample_sets

  @property
  def num_examples(self):
    return self._num_examples

  @property
  def epochs_completed(self):
    return self._epochs_completed

  def next_batch(self, batch_size):
    """Return the next `batch_size` examples from this data set."""
    start = self._index_in_epoch
    self._index_in_epoch += batch_size
    if self._index_in_epoch > self._num_examples:
      # Finished epoch
      self._epochs_completed += 1
      # Shuffle the data
      perm = numpy.arange(self._num_examples)
      numpy.random.shuffle(perm)
      self._images = self._images[perm]
      # Start next epoch
      start = 0
      self._index_in_epoch = batch_size
      assert batch_size <= self._num_examples
    end = self._index_in_epoch

    return self._sample_sets[start:end], self._sample_sets[start:end]
class DataSet():
 def __init__(self, sample_sets, labels):
  assert sample_sets.shape[0] == labels.shape[0], (
          "sample_sets: %s labels.shape: %s" % (sample_sets.shape,
                                                labels.shape))
  self._num_examples = sample_sets.shape[0]
      # Convert shape from [num examples, rows, columns, depth]
      # to [num examples, rows*columns] (assuming depth == 1)  
  assert sample_sets.shape[3] == 1
  self._sample_sets = sample_sets
  self._labels = labels
  self._epochs_completed = 0
  self._index_in_epoch = 0
 @property
 def sample_sets(self):
    return self._sample_sets

 @property
 def labels(self):
   return self._labels

 @property
 def num_examples(self):
   return self._num_examples

 @property
 def epochs_completed(self):
   return self._epochs_completed

 def next_batch(self, batch_size):
   """Return the next `batch_size` examples from this data set."""
   start = self._index_in_epoch
   self._index_in_epoch += batch_size
   if self._index_in_epoch > self._num_examples:
     # Finished epoch
     self._epochs_completed += 1
     # Shuffle the data
     perm = numpy.arange(self._num_examples)
     numpy.random.shuffle(perm)
     self._sample_sets = self._sample_sets[perm]
     self._labels = self._labels[perm]
     # Start next epoch
     start = 0
     self._index_in_epoch = batch_size
     assert batch_size <= self._num_examples
   end = self._index_in_epoch
   return self._sample_sets[start:end], self._labels[start:end]
#this class inint shalled be in the autoencoder.py

class ExtractData():
 def __init__(self):
    datafilepath = FLAGS.data_dir + "\\" + FLAGS.datafilename
    labelfilepath = FLAGS.data_dir + "\\" + FLAGS.labelfilename
    self.data_csvfile = csv.reader(open(datafilepath))
    self.label_csvfile = csv.reader(open(labelfilepath))
    #self.data_sets_num = 0 # data_sets_num represent the data file in which bitch.
    self.num_examples = FLAGS.num_examples
    self.data_label_rows = []
		
 def fetch_data_sets(self):
  data_rows = []
  label_rows = []
  data_rows = self.fetch_data().next()
  label_rows = self.fetch_label().next()
  self.data_label_rows = [data_rows,label_rows]
  return self.data_label_rows
 def fetch_data(self):
  for data_row in self.data_csvfile:
   if len(data_rows) == self.num_examples:
    data_rows = np.array(data_rows)
    yield data_rows
    data_rows = []
   else:
    data_rows.append(data_row)
 def fetch_label(self):
  for label_row in self.label_csvfile:
   if len(label_rows) == self.num_examples:
    label_rows = np.array(label_rows)
    label_rows.reshape(self.num_examples)
    yield label_rows
    label_rows = []
   else:
    label_rows.append(label_row)   

#this function's peremeter is result of class ExtractData'fetch_data_sets method()
def read_data_sets_pretraining(data_label_rows):
 class Datasets():
  pass
 data_sets = DataSets()
 data_rows = data_label_rows[0]

 VALIDATION_SIZE = int(num_examples*0.1)
 TEST_SIZE = int(num_examples*0.1)
 
 #notice that the numpy.shape dim order (0,1,2,3),and for default np[1:2] means the dim 0's option
 validate_sample_sets = data_rows[:VALIDATION_SIZE]
 test_sample_sets = data_rows[VALIDATION_SIZE:VALIDATION_SIZE+TEST_SIZE]
 train_sample_sets = data_rows[VALIDATION_SIZE+TEST_SIZE:]
 
 data_sets.train = DataSetPreTraining(train_sample_sets)
 data_sets.validation = DataSetPreTraining(validate_sample_sets)
 data_sets.test = DataSetPreTraining(test_sample_sets)
 
 return data_sets

def read_data_sets(data_label_rows):
 class Datasets():
  pass
 data_sets = DataSets()
 data_rows = data_label_rows[0]
 label_rows = data_label_rows[1]
 
 VALIDATION_SIZE = int(num_examples*0.1)
 TEST_SIZE = int(num_examples*0.1)
 
 validate_label_sets = label_rows[:VALIDATION_SIZE]
 test_label_sets = label_rows[VALIDATION_SIZE:VALIDATION_SIZE+TEST_SIZE]
 train_label_sets = label_rows[VALIDATION_SIZE+TEST_SIZE:] 
 
 
 validate_sample_sets = data_rows[:VALIDATION_SIZE]
 test_sample_sets = data_rows[VALIDATION_SIZE:VALIDATION_SIZE+TEST_SIZE]
 train_sample_sets = data_rows[VALIDATION_SIZE+TEST_SIZE:]
 
 data_sets.train = DataSetPreTraining(train_sample_sets,train_label_sets)
 data_sets.validation = DataSetPreTraining(validate_sample_sets,validate_label_sets)
 data_sets.test = DataSetPreTraining(test_sample_sets,test_label_sets)
 
 



def _add_noise(x, rate):
  x_cp = numpy.copy(x)
  pix_to_drop = numpy.random.rand(x_cp.shape[0],
                                  x_cp.shape[1]) < rate
  x_cp[pix_to_drop] = FLAGS.zero_bound
  return x_cp
def read_data_sets_pretraining(train_dir):
 class Datasets():
  pass
 data_sets =DataSets() 
 def fetch_data_sets(self,num_examples = 500):
  self.data_rows = next_data
  self.label_rows = next_label
  yield [data_rows,label_rows]
  def fetch_data():
   data_rows = []
   label_rows = []
   for data_row in data_csvfile:
    if len(data_rows) == num_examples:
     data_rows = np.array(data_rows)
     yield data_rows
     data_rows = []
    else:
     data_rows.append(data_row)
  def fetch_label():
   for label_row in labels_csvfile:
    if len(label_rows) == num_examples:
     yield label_rows
     label_rows = []
    else:
     label_rows.append(label_row)
 
 return data_sets


 
 
 
def fill_feed_dict_ae(data_set, input_pl, target_pl, noise=None):
    input_feed, target_feed = data_set.next_batch(FLAGS.batch_size)
    if noise:
      input_feed = _add_noise(input_feed, noise)
    feed_dict = {
        input_pl: input_feed,
        target_pl: target_feed
    }
    return feed_dict

def fill_feed_dict(data_set, sample_sets_pl, labels_pl, noise=False):
  """Fills the feed_dict for training the given step.
  A feed_dict takes the form of:
  feed_dict = {
      <placeholder>: <tensor of values to be passed for placeholder>,
      ....
  }
  Args:
    data_set: The set of images and labels, from input_data.read_data_sets()
    sample_sets_pl: The images placeholder, from placeholder_inputs().
    labels_pl: The labels placeholder, from placeholder_inputs().
  Returns:
    feed_dict: The feed dictionary mapping from placeholders to values.
  """
#### Create the feed_dict for the placeholders filled with the next
#### `batch size ` examples.
  sample_sets_feed, labels_feed = data_set.next_batch(FLAGS.batch_size)
  if noise:
      sample_sets_feed = _add_noise(sample_sets_feed, FLAGS.drop_out_rate)
  feed_dict = {
      sample_sets_pl: sample_sets_feed,
      labels_pl: labels_feed,
  }
  return feed_dict

