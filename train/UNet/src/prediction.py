## This script is for predicting validation and test images using the best model trained by training.py
## The output files are probablity 3 class images as well as segmention images
## It gives a good sense of how well models can segment images

#!/usr/bin/env python
# coding: utf-8

# # Step 03
# # Predict segmentations
import os
import os.path
import matplotlib.pyplot as plt
import numpy as np
import skimage.io
import skimage.morphology
import tensorflow as tf
import keras
import utils.metrics
import utils.model_builder
import utils.dirtools
from config import config_vars
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from multiprocessing import cpu_count




# Partition of the data to make predictions (test or validation)
partition = "validation"

experiment_name = 'Cytosol_merged'

config_vars = utils.dirtools.setup_experiment(config_vars, experiment_name)

data_partitions = utils.dirtools.read_data_partitions(config_vars)

config_vars

# In[4]:


# Device configuration
# Configuration to run on GPU
configuration = tf.ConfigProto()
configuration.gpu_options.allow_growth = True
configuration.gpu_options.visible_device_list = "0"

session = tf.Session(config = configuration)

# apply session
keras.backend.set_session(session)


#image_names = [f for f in data_partitions[partition] if f.startswith("IXM")]
image_names = [os.path.join(config_vars["normalized_images_dir"], f) for f in data_partitions[partition]]

imagebuffer = skimage.io.imread_collection(image_names)

images = imagebuffer.concatenate()

dim1 = images.shape[1]
dim2 = images.shape[2]

images = images.reshape((-1, dim1, dim2, 1))

# preprocess (assuming images are encoded as 8-bits in the preprocessing step)
images = images / 255

# build model and load weights
model = utils.model_builder.get_model_3_class(dim1, dim2)
model.load_weights('experiments/Cytosol_merged/models/model_0.910.42.hdf5')

# Normal prediction time
predictions = model.predict(images, batch_size=1)

model.summary()



for i in range(len(images)):

    filename = imagebuffer.files[i]
    filename = os.path.basename(filename)
    print(filename)
    
    probmap = predictions[i].squeeze()
    
    skimage.io.imsave(config_vars["probmap_out_dir"] + filename, probmap)
    
    pred = utils.metrics.probmap_to_pred(probmap, config_vars["boundary_boost_factor"])

  
    label = utils.metrics.pred_to_label(pred, config_vars["cell_min_size"])
    

    skimage.io.imsave(config_vars["labels_out_dir"] + filename, label)




