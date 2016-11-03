import sys
import os
import glob
import numpy as np
import pdb
import re
import cv2
import matplotlib.pyplot as plt
import random

def normalise_homogeneous_pts(points_x):
	'''
	Normalise the matrix of homogeneous points
	'''
	assert(points_x.shape[0]==3, "Points must be in homogeneous form (3,Xi)")
	mean_xi = np.mean(points_x[0,:])
	mean_yi = np.mean(points_x[1,:])
	pXi = points_x[0,:] - mean_xi
	pYi = points_x[1,:] - mean_yi
	meandist = np.mean(np.sqrt(np.multiply(pXi,pXi)+np.multiply(pYi,pYi)))
	scale = np.sqrt(2)/meandist
	T = np.array([[scale,0,-scale*mean_xi],[0,scale,-scale*mean_yi],[0,0,1]])
	norm_homo_pts = np.dot(T,points_x)
	return (norm_homo_pts,T)

def EstimateFundamentalMatrix(input_points):
	'''
	To estimate the fundamental matrix F from a set of 8
	point correspondences between two images

	Input:
	This method takes the points in (xi,yi) format from Image1
	and Image2 such that they are in a matrix of the form
	[[X1,Y1];[X2,Y2]] with dimensions [6 x num_points]

	Output:
	This method returns the fundamental matrix F
	'''
	