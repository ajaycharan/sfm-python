import sys
import os
import glob
import numpy as np
import pdb
import re
import cv2
import matplotlib.pyplot as plt
from GLOBAL_VARS import *

from SFM_UTILS import *

imageFile_list = glob.glob(INPUT_IMAGE_DIR + '*.bmp')
number_of_images = len(imageFile_list)

# Load feature point correspondences generated by preprocessing script.
try:
	XPTS = np.load(NUMPY_MATCH_MATRIX_DIR+'x_matches.npy')
	YPTS = np.load(NUMPY_MATCH_MATRIX_DIR+'y_matches.npy')
	RGBPTS = np.load(NUMPY_MATCH_MATRIX_DIR+'rgb_matches.npy')
except IOError:
	print('One or more numpy correspondences files could not be loaded.')

# Evaluate feature point correspondences, i.e check if X,Y co-ordinates align.
X_mask = XPTS>0
Y_mask = YPTS>0
assert(np.array_equal(X_mask,Y_mask)), "Error in (x,y) co-ordinate matches in preprocessing."

# Create a point mask to identify feature correspondences
point_mask = X_mask*1
del X_mask,Y_mask

for im1_idx in range(1,number_of_images):
	for im2_idx in range(im1_idx+1,number_of_images+1):

		print(im1_idx,im2_idx)

		# Extract indices of valid features from both image frames
		indices_image1 = np.nonzero(point_mask[:,im1_idx-1])
		indices_image2 = np.nonzero(point_mask[:,im2_idx-1])

		# Identify a set of initial feature correspondences,
		# These will be refined using RANSAC.
		common_indices = np.intersect1d(indices_image1,indices_image2).tolist()
		#pdb.set_trace()
		if len(common_indices) < MIN_RANSAC_POINTS:
			print("Error: Not enough feature correspondences for RANSAC between frame #%d and frame #%d",im1_idx,im2_idx)
			continue

		# Arrange feature point correspondences for both frames into two [x,y] matrices
		Image1_PTS = np.transpose(np.array([XPTS[common_indices,im1_idx-1],YPTS[common_indices,im1_idx-1]]))
		Image2_PTS = np.transpose(np.array([XPTS[common_indices,im2_idx-1],YPTS[common_indices,im2_idx-1]]))

		(F_temp,indices_RANSAC) = get_inliers_RANSAC()
		pdb.set_trace()
