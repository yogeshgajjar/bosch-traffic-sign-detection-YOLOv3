"""
Copyright © 2020 Yogesh Gajjar. All rights reserved.
"""

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import sys

sets=['traffic_lights']
labels = ["RedLeft", "Red", "RedRight", "GreenLeft", "Green", "GreenRight", "Yellow", "off"]

def convert(size, box):
    """
    This function converts the bounding box dimensions into a yolo format.

    args:
        1. size : image size.
        2. box  : bounding box specification

    returns:
        1. (x,y,w,h) : the center point (x,y) and the width and height (w,h)
    """

    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(xml_path_input, file_folder, file_name):
    """
    This function converts the .xml format and fetches the bounding box to convert it to yolo format.

    args:
        1. xml_path_input   : input xml file directory/path
        2. file_folder      : output folder directiory/path
        3. file_name        : the current file being executed.

    """

    in_file = open('%s'%(xml_path_input))
    out_file = open('%s/%s.txt'%(file_folder,file_name), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        lbs = obj.find('name').text
        if lbs not in labels or int(difficult)==1:
            continue
        lbs_id = labels.index(lbs)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(lbs_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

def write_to_file(output_folder, xmls_list, images_folder):
    for image_set in sets:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        xml_paths = open(xmls_list).read().strip().split()
        list_file = open('%s.txt'%(image_set), 'w')
        for xml_path in xml_paths:
            #print("xml path: ",xml_path)
            xml_name = xml_path.split('/')[-1]
            #print("xml name:",xml_name)
            image_name = xml_name.split('.')[0]
            #print("image name: ",image_name)
            #print(images_folder+'/%s.png\n'%(image_name))
            list_file.write(images_folder+'/%s.png\n'%(image_name))
            convert_annotation(xml_path, output_folder, image_name)
        list_file.close()

def main():
    output_folder = str(sys.argv[1])
    xmls_list = str(sys.argv[2])
    images_folder = str(sys.argv[3])

if __name__ == '__main__':
    main()
