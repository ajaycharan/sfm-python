import sys
import os
import glob
import numpy as np
#import cv2
import pdb
#import matplotlib.pyplot as pyplot
from GLOBAL_VARS import *

# -------------------------------------------------------------------------
# SCRIPT NAME: preprocess_matches.py
#
# Purpose : To create a matrix of feature matches across all images in the
# data set.
#
# 1. Input Arguments: 
# This script takes the image directory and the matching
# points directory as input 
#
# 2. Output Arguments: 
# This script generates a numpy file of the individual matched matrices in
# [numberOfFeatures x numberOfImages] format for both X and Y co-ordinate
# positions respectively and also returns an array of RGB pixel values for
# each feature, the matrix is of size [numberOfFeature x 3]
#
# EXAMPLE:
# Xpts(1,:) = [454.7400,308.5700,0,447.5800,0,0];
# Ypts(1,:) = [392.3700,500.3200,0,479.3600,0,0];
# This means that the pixel in (454.74,392.37) found in IMAGE 1 can be
# found at (308.57,500.32) in IMAGE 2 and (447.58,479.36) in IMAGE 4 and is
# not found in IMAGE 3 and IMAGE 5. And this pixel value (in R,G and B
# components) can be found at RGBData(1,:)
# -------------------------------------------------------------------------

matchFile_list = glob.glob(FEATURES_DIR + '*.txt')

for correspondence_file in matchFile_matrix[:-1]:
	filehandle = open(correspondence_file)
	line1 = filehandle.readline()
	print line1
	features_inImage = [int(s) for s in line1.split() if s.isdigit()][0]
	print features_inImage
	# Initialize a matrix block for matches of the form (features x image_no)
	x_Matches = np.zeros([features_inImage,len(matchFile_list)])
	y_Matches = np.zeros([features_inImage,len(matchFile_list)])
	pdb.set_trace()
	#contents = open(correspondence_file).read()
	#print contents
