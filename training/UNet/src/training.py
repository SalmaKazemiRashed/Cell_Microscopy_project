## This script will run model.fit function for the number of epochs mentioned in config.py file
## The required directories are normalized_imgs, and boundary_label_dir
## The models will saved in models directory


#!/usr/bin/env python
# coding: utf-8


import sys
import os
import numpy as np
import skimage.io
import tensorflow as tf
import keras.backend
import keras.callbacks
import keras.layers
import keras.models
import keras.optimizers
import utils.model_builder
import utils.data_provider
import utils.metrics
import utils.objectives
import utils.dirtools
import random
random.seed(5)
from config import config_vars



experiment_name = 'Cytosol_M_merged'  ## This is experiment name

config_vars = utils.dirtools.setup_experiment(config_vars, experiment_name)

data_partitions = utils.dirtools.read_data_partitions(config_vars)

config_vars

# build session running on GPU 1  
configuration = tf.ConfigProto()
configuration.gpu_options.allow_growth = True
configuration.gpu_options.visible_device_list = "0"
session = tf.Session(config = configuration)

# apply session
keras.backend.set_session(session)

train_gen = utils.data_provider.random_sample_generator(
    config_vars["normalized_images_dir"],
    config_vars["boundary_labels_dir"],
    data_partitions["training"],
    config_vars["batch_size"],
    config_vars["pixel_depth"],
    config_vars["crop_size"],
    config_vars["crop_size"],
    config_vars["rescale_labels"]
)

val_gen = utils.data_provider.single_data_from_images(
     config_vars["normalized_images_dir"],
     config_vars["boundary_labels_dir"],
     data_partitions["validation"],
     config_vars["val_batch_size"],
     config_vars["pixel_depth"],
     config_vars["crop_size"],
     config_vars["crop_size"],
     config_vars["rescale_labels"]
)


## build_model
# build model
model = utils.model_builder.get_model_3_class(config_vars["crop_size"], config_vars["crop_size"], activation=None)
model.summary()

#loss = "categorical_crossentropy"
loss = utils.objectives.weighted_crossentropy

metrics = [keras.metrics.categorical_accuracy, 
           utils.metrics.channel_recall(channel=0, name="background_recall"), 
           utils.metrics.channel_precision(channel=0, name="background_precision"),
           utils.metrics.channel_recall(channel=1, name="interior_recall"), 
           utils.metrics.channel_precision(channel=1, name="interior_precision"),
           utils.metrics.channel_recall(channel=2, name="boundary_recall"), 
           utils.metrics.channel_precision(channel=2, name="boundary_precision"),
          ]

optimizer = keras.optimizers.RMSprop(lr=config_vars["learning_rate"])

model.compile(loss=loss, metrics=metrics, optimizer=optimizer)

# Performance logging
callback_csv = keras.callbacks.CSVLogger(filename=config_vars["csv_log_file"])
callback_mdlchk  = keras.callbacks.ModelCheckpoint('./experiments/Cytosol_M_merged/models/model_'+'{val_categorical_accuracy:.2f}'+'{val_boundary_precision:.2f}.hdf5', monitor='val_categorical_accuracy', verbose=0, save_best_only=False, save_weights_only=False, mode='max')
callbacks=[callback_csv,callback_mdlchk]


# TRAIN
statistics = model.fit_generator(
    generator=train_gen,
    steps_per_epoch=config_vars["steps_per_epoch"],
    epochs=config_vars["epochs"],
    validation_data=val_gen,
    validation_steps=int(len(data_partitions["validation"])/config_vars["val_batch_size"]),
    callbacks=callbacks
)

model.save_weights(config_vars["model_file"])

print('Done! :)')