import numpy as np
import sys
from Greedy import Greedy
from verify import Verify
np.set_printoptions(threshold=sys.maxsize) #setting for print full numpy matrix
'''
This main function execute the square cost function and product cost function respectively, using 0 and 1 to select
'''
def main():
	matrix = np.loadtxt('AES.txt', usecols=range(32), dtype=int)
	print("The Load Block Cipher Data: ")
	print(matrix)
	Greedy(matrix, 0)
	Greedy(matrix, 1)
	Verify(matrix, 0)
	Verify(matrix, 1)
if __name__ == "__main__":
	main()
