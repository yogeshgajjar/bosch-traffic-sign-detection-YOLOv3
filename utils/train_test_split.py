"""
Copyright © 2020 Yogesh Gajjar. All rights reserved.
"""

import glob, os
import numpy as np
from sklearn.model_selection import train_test_split
import sys


def split_test_train(image_paths_file, percentage):
	"""
	This function splits the image .txt file to test and train .txt file. The
	ratio depends on the percentage selected by the user.

	args:
		1. image_paths_file 	: The image .txt file path
		2. percentage	 		: Value in the range (0,1)

	"""

	img_paths = []
	img_paths = open(image_paths_file).read().strip().split()

	X_train, X_test= train_test_split(img_paths, test_size=percentage, random_state=31)

	with open('train.txt', 'a') as train_file:
		for train in X_train:
			train_file.write(train + '\n')

	with open('test.txt', 'a') as test_file:
		for test in X_test:
			test_file.write(test + '\n')

def main():
	image_paths_file = sys.argv[1]
	percentage_test = float(sys.argv[2]);


if __name__ == '__main__':
    main()
