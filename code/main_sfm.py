import sys
import os
import glob
import numpy as np
import pdb
import re
import cv2
import matplotlib.pyplot as plt
from GLOBAL_VARS import *

imageFile_list = glob.glob(INPUT_IMAGE_DIR + '*.bmp')
number_of_images = len(imageFile_list)

XPTS = np.load(NUMPY_MATCH_MATRIX_DIR+'x_matches.npy')
YPTS = np.load(NUMPY_MATCH_MATRIX_DIR+'y_matches.npy')
RGBPTS = np.load(NUMPY_MATCH_MATRIX_DIR+'rgb_matches.npy')

point_mask = (XPTS > 0)*1
pdb.set_trace()

for im1_idx in range(1,number_of_images):
	for im2_idx in range(im1_idx+1,number_of_images+1):
		print(im1_idx,im2_idx)
