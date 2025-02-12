#!/usr/bin/python

import os

config_vars = {}

config_vars["home_folder"] = '../data/'

config_vars["model_file"]='../data/experiments/Cytosol_merged/'

config_vars["input_dimensions"] = 1

config_vars["root_directory"] = './'

config_vars["learning_rate"] = 1e-4

config_vars["epochs"] = 15

config_vars['cell_min_size'] = 16

config_vars["max_training_images"] = 30

config_vars["steps_per_epoch"] = 500

config_vars["pixel_depth"] = 8

config_vars["batch_size"] = 1

config_vars["val_batch_size"] = 1

config_vars["rescale_labels"] = True

config_vars["crop_size"] = 256

config_vars["boundary_boost_factor"] = 1  #Was 3

config_vars["boundary_size"] = 2

config_vars["object_dilation"] = 10


config_vars["csv_log_file"]     = '4_filelists/training.txt'

config_vars["raw_images_dir"] = config_vars["home_folder"] + "0_raw_images/"

config_vars["raw_annotations_dir"] = config_vars["home_folder"] + "1_raw_annotations/"

config_vars["normalized_images_dir"] = config_vars["home_folder"] + "2_norm_images_merged/"

config_vars["boundary_labels_dir"] = config_vars["home_folder"] + "3_boundary_labels/"

config_vars["path_files_training"] = os.path.join(config_vars["home_folder"], '4_filelists/training.txt')

config_vars["path_files_validation"] = os.path.join(config_vars["home_folder"], '4_filelists/VALIDATION.txt')

config_vars["path_files_test"] = os.path.join(config_vars["home_folder"], '4_filelists/TEST.txt')

