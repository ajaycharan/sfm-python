import sys
import os
import glob
import numpy as np
import pdb
import re
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
# This script will build a list of correspondences and save the results as 
# three NUMPY files for X co-ordinates, Y co-ordinates and RGB features of 
# the resulting matches respectively.
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
imageFile_list = glob.glob(INPUT_IMAGE_DIR + '*.bmp')
XPts = []
YPts = []
RGB_Features = []
imageNumber = 0

def is_number(s):
	'''
	Function to take input string and check if give string is a number (int or float).
	This function is used while iteratively reading lines from input text file.
	'''
	try:
		float(s)
		return True
	except:
		return False

def check_file(filepath):
	'''
	Function to take an input filepath and check whether the file exists or not
	'''
	return os.path.isfile(filepath)

for correspondence_file in matchFile_list:
	if check_file(correspondence_file):
		filehandle = open(correspondence_file)
	# Read the first line from the correspondence file and extract the number of features
	line1 = filehandle.readline()
	features_inImage = [int(s) for s in line1.split() if s.isdigit()][0]
	# Initialize a matrix block for matches of the form (features x image_no)
	x_Matches = np.zeros([features_inImage,len(imageFile_list)])
	y_Matches = np.zeros([features_inImage,len(imageFile_list)])
	rgb_Matches = np.zeros([features_inImage,CLR_CHANNELS_COUNT])

	# Iterate over each feature in the given image
	for feature in range(features_inImage):
		feature_line = [float(s) for s in filehandle.readline().split() if is_number(s)]
		match_count = feature_line[0]
		# Append respective matches to match matrices
		rgb_Matches[feature,:] = feature_line[1:4]
		x_Matches[feature,imageNumber] = feature_line[4]
		y_Matches[feature,imageNumber] = feature_line[5]
		for i in range(6,len(feature_line),3):
			match_file_idx = int(feature_line[i])
			x_Matches[feature,match_file_idx-1] = feature_line[i+1]
			y_Matches[feature,match_file_idx-1] = feature_line[i+2]
	imageNumber += 1
	# Append to list of overall matches across all images
	XPts.append(x_Matches)
	YPts.append(y_Matches)
	RGB_Features.append(rgb_Matches)
	filehandle.close()

# Flatten out match list into a single NUMPY array
X_Matches_Final = np.concatenate(XPts)
Y_Matches_Final = np.concatenate(YPts)
RGB_Matches_Final = np.concatenate(RGB_Features)

# Save NUMPY arrays
if not os.path.isdir(NUMPY_MATCH_MATRIX_DIR):
	os.makedirs(NUMPY_MATCH_MATRIX_DIR)
np.save(NUMPY_MATCH_MATRIX_DIR+'x_matches.npy',X_Matches_Final)
np.save(NUMPY_MATCH_MATRIX_DIR+'y_matches.npy',Y_Matches_Final)
np.save(NUMPY_MATCH_MATRIX_DIR+'rgb_matches.npy',RGB_Matches_Final)
