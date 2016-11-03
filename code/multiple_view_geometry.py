import sys
import os
import numpy as np
import pdb
import re
import cv2
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
	pdb.set_trace()
	x1_points = input_points[0:3,:]
	x2_points = input_points[3:6,:]
	num_points = x1_points.shape[1]

	(x1_pts,T1) = normalise_homogeneous_pts(x1_points)
	(x2_pts,T2) = normalise_homogeneous_pts(x2_points)

	# Building the A matrix for SVD
	a11 = np.reshape(np.multiply(x2_pts[0,:],x1_pts[0,:]),[num_points,1])
	a12 = np.reshape(np.multiply(x2_pts[0,:],x1_pts[1,:]),[num_points,1])
	a13 = np.reshape(x2_pts[0,:],[num_points,1])
	row1 = np.column_stack((a11,a12,a13))
	pdb.set_trace()
	a21 = np.reshape(np.multiply(x2_pts[1,:],x1_pts[0,:]),[num_points,1])
	a22 = np.reshape(np.multiply(x2_pts[1,:],x1_pts[1,:]),[num_points,1])
	a23 = np.reshape(x2_pts[1,:],[num_points,1])
	row2 = np.column_stack((a21,a22,a23))
	a31 = np.reshape(x1_pts[0,:],[num_points,1])
	a32 = np.reshape(x1_pts[1,:],[num_points,1])
	a33 = np.ones([num_points,1])
	row3 = np.column_stack((a31,a32,a33))
	pdb.set_trace()

	A = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])

	(U,s,V) = np.linalg.svd(A,full_matrices=True)


