"""
Copyright © 2020 Yogesh Gajjar. All rights reserved.
"""

import os
import sys


def combine_xmls(xmls_path):
	"""
	This function reads the .xml file and converts into a form requried
	for training.

	args:
		1. xmls_path : The .xml file path

	"""
	xml_files = []
	for r,d,f in os.walk(xmls_path):
		#r = root, d = directories, f = xml_files
		for file in f:
			if '.xml' in file:
				xml_files.append(os.path.join(r, file)) #Gets the whole file xmls_path

	file_num = len(xml_files)
	print("Length of the xml_files: ", file_num)

	if not open('traffic_lights_xmls.txt','w'):
		os.makefile('traffic_lights_xmls.txt')

	labels = open('traffic_lights_xmls.txt','w')

	for xml in xml_files:
		labels.write(xml + '\n')

	labels.close()

def main():
	xmls_path = sys.argv[1] #xml files path
	combine_labels(xmls_path)

if __name__ == '__main__':
    main()
