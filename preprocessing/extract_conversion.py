## This script is written by Salma Kazemi Rashed and Malou Arvidsson and Klara Esbo
## The whole purpose was to extract images from a .tar file and convert the format from .C01 microscopic format to .png or .tiff format
## This script is used for both training set and all images from full dataset in order to run train, prediction and postprocessing scripts on images
## Before running this script the path to .tar.gz file and the targeted plate number should be identified.


#libraries
import tarfile
import time 
import glob
import os 
import subprocess


RAW_DATA_DIR = '/proj/berzelius-2021-21/Segmentation/raw_data/'
TARGET_PLATE = 'MFGTMPcx7_170526090001.tar.gz'

os.chdir(RAW_DATA_DIR)


with tarfile.open(RAW_DATA_DIR + TARGET_PLATE) as file:
    names_files = file.getnames()
    for each in names_files:
        #specify suffix of files to be extracted
        if each.endswith('d0.C01'):   # in all plates we have three channels d0, d1, and d2
            start_1 = time.time()     # For measuring the time of extraction and conversion
            file.extract(each)
            
            #end timer test indentation?
            end_1 = time.time()
            print ('extraction time: ', end_1 - start_1) #time of extraction
            png_d0 = each.replace('.C01','.png')   # C01 should change to any other readable format (.jpg, .tiff, ...)
            
            #what is i j
            start_2 = time.time() 
            subprocess.run(['envs/bftools/bftools/bfconvert', '-overwrite', '-nogroup', each, png_d0]) ## This is for conversion
            subprocess.run(['convert', png_d0, '-auto-level', '-depth', '8', '-define', 'quantum:format=unsigned', '-type', 'grayscale', png_d0]) #This is for normalizing to 8-bit format
        #end timer 2
            end_2 = time.time()
            print ('conversion time: ', end_2 - start_2)  #time of conversion  
       
        