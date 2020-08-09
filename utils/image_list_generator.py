"""
Copyright © 2020 Yogesh Gajjar. All rights reserved.
"""

import os
import sys


def combine_images(img_path):
	"""
	This function reads the .png image file and converts into a form requried
	for training. Later this can be converted to test and train .txt files.

	args:
		1. img_path : The image file path

	"""

	image_files = []
	for r,d,f in os.walk(img_path):
		#r = root, d = directories, f = image_files
		for file in f:
			if '.png' in file:
				image_files.append(os.path.join(r, file)) #Gets the whole file img_path

	file_num = len(image_files)
	print("Length of the image_files: ", file_num)

	if not open('traffic_lights_images.txt','w'):
		os.makefile('traffic_lights_images.txt')

	labels = open('traffic_lights_images.txt','w')

	for xml in image_files:
		labels.write(xml + '\n')

	labels.close()

def main():
	image_path = sys.argv[1] #image files path
	combine_images(image_path)

if __name__ == '__main__':
    main()
