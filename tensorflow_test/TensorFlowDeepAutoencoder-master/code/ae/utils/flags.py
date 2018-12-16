from __future__ import division
import os
from os.path import join as pjoin

import sys

import tensorflow as tf


def home_out(path):
  return pjoin(os.environ['HOME'], 'tmp', 'gene_expression', path)	

flags = tf.app.flags
FLAGS = flags.FLAGS

# Autoencoder Architecture Specific Flags
flags.DEFINE_integer("num_hidden_layers", 1, "Number of hidden layers")

flags.DEFINE_integer('hidden1_units', 500,
                     'Number of units in hidden layer 1.')
flags.DEFINE_integer('hidden2_units', 300,
                     'Number of units in hidden layer 2.')
flags.DEFINE_integer('hidden3_units', 200,
                     'Number of units in hidden layer 3.')

# flags.DEFINE_integer('image_pixels', IMAGE_PIXELS, 'Total number of pixels')
flags.DEFINE_integer('num_classes', 53, 'Number of classes')

flags.DEFINE_float('pre_layer1_learning_rate', 0.0001,
                   'Initial learning rate.')
flags.DEFINE_float('pre_layer2_learning_rate', 0.0001,
                   'Initial learning rate.')
flags.DEFINE_float('pre_layer3_learning_rate', 0.0001,
                   'Initial learning rate.')

flags.DEFINE_float('noise_1', 0.50, 'Rate at which to set pixels to 0')
flags.DEFINE_float('noise_2', 0.50, 'Rate at which to set pixels to 0')
flags.DEFINE_float('noise_3', 0.50, 'Rate at which to set pixels to 0')

#specific flags
flags.DEFINE_string('data_sets_dir', home_out('data'),
                    'Directory to put the training data.')
flags.DEFINE_string('datafilename', "data.csv",
                    'File name for data file.')
flags.DEFINE_string('labelfilename', "label.csv",
                    'File name for label file.')
flags.DEFINE_integer('num_examples',1000,
                     'quantity of data to use in a large datafiles')
flags.DEFINE_integer('number_genes',12000,
                     'how many genes in each sample(columns count)')

# Constants
flags.DEFINE_integer('seed', 1234, 'Random seed')
#flags.DEFINE_integer('image_size', 28, 'Image square size')

flags.DEFINE_integer('batch_size', 100,
                     'Batch size. Must divide evenly into the dataset sizes.')

flags.DEFINE_float('supervised_learning_rate', 0.1,
                   'Supervised initial learning rate.')

flags.DEFINE_integer('pretraining_epochs', 1,
                     "Number of training epochs for pretraining layers")
flags.DEFINE_integer('finetuning_epochs', 5,
                     "Number of training epochs for "
                     "fine tuning supervised step")

flags.DEFINE_float('zero_bound', 1.0e-9,
                   'Value to use as buffer to avoid '
                   'numerical issues at 0')
flags.DEFINE_float('one_bound', 1.0 - 1.0e-9,
                   'Value to use as buffer to avoid numerical issues at 1')

flags.DEFINE_float('flush_secs', 120, 'Number of seconds to flush summaries')

# Directories
flags.DEFINE_string('data_dir', home_out('data'),
                    'Directory to put the training data.')

flags.DEFINE_string('summary_dir', home_out('summaries'),
                    'Directory to put the summary data')

flags.DEFINE_string('chkpt_dir', home_out('chkpts'),
                    'Directory to put the model checkpoints')

# TensorBoard
flags.DEFINE_boolean('no_browser', True,
                     'Whether to start browser for TensorBoard')

# Python
flags.DEFINE_string('python', sys.executable,
                    'Path to python executable')
