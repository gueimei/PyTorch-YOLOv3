import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=[('train_name','train'),('val_name','valid')]

classes = ["chicken"]

def convert(size, box):
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

def convert_annotation(image_id):
    print(image_id)
    #image_add = os.path.split(image_id)[1]
    #image_add = image_add[0:image_add.find('.',1)]
    #print(image_add)
    in_file = open('xml/'+ image_id + '.xml')
    out_file = open('/home/PyTorch-YOLOv3/data/custom/labels/%s.txt'%(image_id), 'w')

    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

#if not os.path.existd('/home/PyTorch-YOLOv3/data/custom/labels'):
#    os.makedirs('/home/PyTorch-YOLOv3/data/custom/labels')
#images_adds = open("train.txt")
#for image_add in image_add.strip()

for image_set, write_file_set in sets:
    if not os.path.exists('/home/PyTorch-YOLOv3/data/custom/labels'):
        os.makedirs('/home/PyTorch-YOLOv3/data/custom/labels')
    image_ids = open('/home/PyTorch-YOLOv3/data/custom/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s.txt'%(write_file_set), 'w')
    for image_id in image_ids:
        list_file.write('/home/PyTorch-YOLOv3/data/custom/images/%s.jpg\n'%(image_id))
        convert_annotation(image_id)
    list_file.close()

#os.system("cat 2019_train.txt 2019_val.txt > train.txt")
#os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")

