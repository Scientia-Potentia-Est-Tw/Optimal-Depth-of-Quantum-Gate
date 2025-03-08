import config
import math
import numpy as np

#The function execute the cost function for h_sq
def cost_sq(mat):
	ret = 0.0
	for i in range(config.SIZE):
		for j in range(config.SIZE):
			ret += mat[i][j] * mat[i][j]

	#return the calculated square row's Hamming weight
	return ret

#The function execute the cost function for h_prod
def cost_prod(mat):
	ret = 0.0
	row_counts = np.sum(mat, axis=1)
	non_zero_counts = row_counts[row_counts > 0]

	#return the calculated product row's Hamming weight
	return np.sum(np.log2(non_zero_counts))
