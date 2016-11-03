import sys
import os
import glob
import numpy as np
import pdb
import re
import cv2
import matplotlib.pyplot as plt
import random
from global_variables import *
from multiple_view_geometry import *

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
	ransac_MAXITER = 1000
	estimationMaxCount = 100
	p = 0.99
	bestM = []
	trial_ctr = 0
	best_inlier_ctr = 0
	N = 1
	#pdb.set_trace()
	x1 = np.append(np.transpose(points_x1),np.ones(points_x1.shape[0]).reshape(1,points_x1.shape[0]),0)
	x2 = np.append(np.transpose(points_x2),np.ones(points_x2.shape[0]).reshape(1,points_x2.shape[0]),0)

	(x1pts,T1) = normalise_homogeneous_pts(x1)
	(x2pts,T2) = normalise_homogeneous_pts(x2)
	x = np.append(x1pts,x2pts,0)
	num_pts = x.shape[1]

	while N > trial_ctr:
		emptyCondition = 1
		ctr = 1
		while emptyCondition:
			rand_indices = random.sample(range(1, x.shape[1]), MIN_RANSAC_POINTS)
			emptyCondition = 0
			if emptyCondition == 0:
				F_mat_temp = EstimateFundamentalMatrix(x[:,rand_indices])
				if not F_mat_temp:
					emptyCondition = 1
			ctr += 1
			if ctr > estimationMaxCount:
				fprintf("Ransac failed at estimating Fundamental Matrix\n")
				break
		(bestMask,F_mat_temp) = evaluateDistance(F_mat_temp,x,ransac_threshold)
		num_inliers = len(bestMask)



	pdb.set_trace()
	return (10,10)
