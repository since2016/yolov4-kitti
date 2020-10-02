import os

images_path = ""
with open("VOCdevkit/VOC2007/ImageSets/Main/test.txt", "w") as image_f:
    for root, dirs, files in os.walk(images_path):
        image_id = files[:-4]
        image_f.write("%s\n", %(image_id))

print("conversion complete!!")



