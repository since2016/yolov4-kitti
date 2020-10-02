#-------------------------------------#
#       mAP所需文件计算代码
#       具体教程请查看Bilibili
#       Bubbliiiing
#-------------------------------------#
import sys
import os
import glob
from tqdm import tqdm

image_ids = open('VOCdevkit/VOC2007/ImageSets/Main/test.txt').read().strip().split()

if not os.path.exists("./input"):
    os.makedirs("./input")
if not os.path.exists("./input/ground-truth"):
    os.makedirs("./input/ground-truth")

#---------------------------------------------------#
#   coco的val集xml放在annotations里
#   kitti 通过读取label生成文件
#---------------------------------------------------#
for image_id in tqdm(image_ids):
    with open("./input/ground-truth/"+image_id+".txt", "w") as new_f:
        with open("label_2/"+image_id+".txt", "r") as read_f:
            lines = read_f.readlines()
            for line in lines:
                items = line.split()
                obj_name = items[0]
                left = items[4]
                top = items[5]
                right = items[6]
                bottom = items[7]

            new_f.write("%s %s %s %s %s\n" % (obj_name, left, top, right, bottom))
print("Conversion completed!")
