## This script is written and improved by Malou Arvidsson, Salma Kazemi Rashed and do convert images to 16bit png, then normalized and cast to 8-bit png format
## The plate number could be passed to it as input arguments

import argparse
import os
import os.path
import subprocess
from tqdm import tqdm
from pathlib import Path
import numpy as np
import skimage.io
from skimage.util import img_as_ubyte

#################################### ARGPARSE ##################################
usage = 'Enter the directory name where the files to convert are located, what format to convert the files to \
and name a directory where you want the converted files to end up.'
parser = argparse.ArgumentParser(description=usage)
parser.add_argument(
    '-i',
    dest = 'infile',
    metavar = 'INDIR',
    type = str,
    help = 'set the directory where the input files are located',
    required = True
    )
parser.add_argument(
    '-o',
    dest = 'outfile',
    metavar = 'OUTDIR',
    type = str,
    help = 'set the directory to store the converted files',
    required = True
    )
parser.add_argument(
    '-ift',
    dest = 'input_filetype',
    metavar = 'IN_FILETYPE',
    type = str,
    help = 'Set what format the input files are: C01',
    required = True
    )
parser.add_argument(
    '-oft',
    dest = 'output_filetype',
    metavar = 'OUT_FILETYPE',
    type = str,
    help = 'Chose format to convert to: tiff',
    required = True
    )
args = parser.parse_args()
################################################################################
# CONVERSION TO TIFF

# Convert the input to the absolute path
input_dir = os.path.abspath(args.infile)
output_dir = os.path.abspath(args.outfile)


out_filetype = '.{}'.format(args.output_filetype)
in_filetype = args.input_filetype

# If the output directory does not exist,
# a directory will be created with that name.
my_file = Path(output_dir)
if not my_file.exists():
    os.mkdir(output_dir)

# If the path provided is not a directory, raise error
if not os.path.isdir(input_dir):
    raise argparse.ArgumentTypeError('Input must be a directory')
if not os.path.isdir(output_dir):
    raise argparse.ArgumentTypeError('Output must be a directory')

input_files = []
converted_files = []
os.chdir(input_dir)
for i in os.listdir(input_dir):
    if i.split('.')[-1] == in_filetype: # Checks that filename ends with format chosen
        input_files.append(input_dir + '/' + i)
        converted_files.append(output_dir + '/' + i.split('.')[0] + out_filetype)

for i,j in tqdm(zip(input_files,converted_files), total = len(input_files)): # tqdm creates a progressbar to see the progress.
    subprocess.run(['bfconvert', '-overwrite', '-nogroup',i,j],stdout = subprocess.PIPE, stderr = subprocess.DEVNULL) #Runs bftools which needs to be preinstalled, output to DEVNULL.
    subprocess.run(['convert', i, '-auto-level', '-depth', '16', '-define', 'quantum:format=unsigned', '-type', 'grayscale', j],stdout = subprocess.PIPE, stderr = subprocess.DEVNULL) #Convert images to 16-bits tiff images


################################################################################
# NORMALIZATION AND CONVERSION TO PNG

filelist = sorted(os.listdir(output_dir))

# run over all raw images
for filename in tqdm(filelist):
    # load image and its annotation
   
    tif_img = skimage.io.imread(output_dir +'/' +filename)       
    
    # normalize to [0,1]
    percentile = 99.9
    high = np.percentile(tif_img, percentile)
    low = np.percentile(tif_img, 100-percentile)

    img = np.minimum(high, tif_img)
    img = np.maximum(low, img)

    img = (img - low) / (high - low) # gives float64, thus cast to 8 bit later
    img = skimage.img_as_ubyte(img) 
    
    current_format = filename.split('.')[-1]
    img_name       = filename.split('.')[0]
    skimage.io.imsave(output_dir + '/' +img_name + '.png', img)  