## This script is taken from carpenterlab and modified for this project.
## It will take annotations as masks and return nuclei(cells) as three class images (background, inside pixels and boundary pcs)
## there is a configuration file also which set specific parameters such as raw annotation directory or output folder as boundary 
## number of pixels as boundary size could be modified 


import os
import random
import matplotlib.pyplot as plt
import numpy as np
import pathlib
from tqdm import tqdm
import skimage.io
import skimage.segmentation
import utils.dirtools
import utils.augmentation
from config import config_vars



print(config_vars)
    
    
filelist = sorted(os.listdir(config_vars["raw_annotations_dir"]))
total_objects = 0

# run over all raw images
for filename in tqdm(filelist):
    
    # GET ANNOTATION
    annot = skimage.io.imread(config_vars["raw_annotations_dir"] + filename)
    
    # strip the first channel
    if len(annot.shape) == 3:
        annot = skimage.color.rgb2gray(annot)*255
        #annot = annot[:,:,0]
        
    
    # label the annotations nicely to prepare for future filtering operation
    annot = skimage.morphology.label(annot)
    total_objects += len(np.unique(annot)) - 1
    
    # filter small objects, e.g. micronulcei
    annot = skimage.morphology.remove_small_objects(annot, min_size=config_vars["cell_min_size"])
    
    # find boundaries
    boundaries = skimage.segmentation.find_boundaries(annot)

    for k in range(2, config_vars["boundary_size"], 2):
        boundaries = skimage.morphology.binary_dilation(boundaries)
        
    # BINARY LABEL
    
    # prepare buffer for binary label
    label_binary = np.zeros((annot.shape + (3,)))
    
    # write binary label
    label_binary[(annot == 0) & (boundaries == 0), 0] = 1
    label_binary[(annot != 0) & (boundaries == 0), 1] = 1
    label_binary[boundaries == 1, 2] = 1
    
    # save it - converts image to range from 0 to 255
    skimage.io.imsave(config_vars["boundary_labels_dir"] + filename, label_binary)
    
print("Total objects: ",total_objects)