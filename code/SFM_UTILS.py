import sys
import os
import glob
import numpy as np
import pdb
import re
import cv2
import matplotlib.pyplot as plt
from GLOBAL_VARS import *


def get_inliers_RANSAC(points_x1,points_x2,ransac_threshold=0.00005):
	'''
	Function: 
	To find the best set of point correspondences from a set of 
	possible correspondences using RAndom Sampling And Consensus.

	Input Arguments:
	This method takes two point sets [X,Y] from two images along
	with a threshold to constrain the matching.

	Output:
	This method returns a mask of indices indicating which of the
	correspondences are inliers. This method also returns the best
	Fundamental Matrix estimated from the set of final inliers.
	'''
	
