import os
import sys

xmls_path = sys.argv[1] #xml files path

xml_files = []

#r = root, d = directories, f = xml_files

for r,d,f in os.walk(xmls_path):
	for file in f:
		if '.png' in file:
			xml_files.append(os.path.join(r, file)) #Gets the whole file xmls_path
			#xml_files.append(os.path.splitext(file)[0]) # Gets only the name of the file without extension,path etc.	

file_num = len(xml_files)
print("Length of the .xml xml_files: ", file_num)

if not open('traffic_lights.txt','w'):
	os.makefile('traffic_lights.txt')

labels = open('traffic_lights.txt','w')

for xml in xml_files:
	labels.write(xml + '\n')

labels.close()

#for f in xml_files:
	#print(f)