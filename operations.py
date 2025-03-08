import config
import copy
import numpy as np

#Define a inverse operation for binary matrix over F_{2}
def inv(mat):
	size = mat.shape[0]
	identity = np.eye(size, dtype=int)
	
	B = copy.deepcopy(mat)
	augmented = np.hstack((B, identity))

	for i in range(size):
		if augmented[i, i] == 0:
			for j in range(i+1, size):
				if augmented[j, i] == 1:
					augmented[[i, j]] = augmented[[j, i]]
					break
			else:
				raise ValueError("Matrix is not invertible in F_{2}")
		
		for k in range(size):
			if k != i and augmented[k, i] == 1:
				augmented[k, :] = np.logical_xor(augmented[k, :], augmented[i, :]).astype(int)

	if not np.array_equal(augmented[:, :size], np.eye(size, dtype=int)):
		raise ValueError("Matrix is not invertible in F_{2}")

	inverse = augmented[:, size:]

	return inverse
#The function execute the row operation for row i with row j
def row_i2j(mat, i, j):
	#copy the input matrix for calculate the row operation
	ret_mat = copy.deepcopy(mat)
	#select the rows i to xor with row j
	ret_mat[j, :] = np.logical_xor(ret_mat[i, :], ret_mat[j, :])
	#return the calculated matrix
	return ret_mat

#The function execute the column operation for row i with row j
def col_i2j(mat, i, j):
	#copy the input matrix for calculate the column operation
	ret_mat = copy.deepcopy(mat)
	#Find the column i has 1s
	for k in range(config.SIZE):
		if ret_mat[k][i] == 1:
			ret_mat[k][j] = ret_mat[k][j] ^ 1 #flip the column j through xor with 1
	#return the calcualted matrix
	return ret_mat
