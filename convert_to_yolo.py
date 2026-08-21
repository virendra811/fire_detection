# import xml.etree.ElementTree as ET

# xml_file = r"C:\Users\VIRENDRA KUMAR\.cache\kagglehub\datasets\dataclusterlabs\fire-and-smoke-dataset\versions\3\Annotations\Annotations\Datacluster Fire and Smoke Sample (1).xml"

# tree = ET.parse(xml_file)
# root = tree.getroot()

# print("Width:", root.find("size/width").text)
# print("Height:", root.find("size/height").text)
# this was the code to check the length and width of the images 
#****************this is the code to convert the dataset to yolo format****************
import os
import shutil
import random
import xml.etree.ElementTree as ET

# Dataset paths
IMG_DIR = r"C:\Users\VIRENDRA KUMAR\.cache\kagglehub\datasets\dataclusterlabs\fire-and-smoke-dataset\versions\3\Datacluster Fire and Smoke Sample\Datacluster Fire and Smoke Sample"

XML_DIR = r"C:\Users\VIRENDRA KUMAR\.cache\kagglehub\datasets\dataclusterlabs\fire-and-smoke-dataset\versions\3\Annotations\Annotations"

# Output folders
TRAIN_IMG = "dataset/images/train"
VAL_IMG = "dataset/images/val"

TRAIN_LABEL = "dataset/labels/train"
VAL_LABEL = "dataset/labels/val"

for folder in [
    TRAIN_IMG,
    VAL_IMG,
    TRAIN_LABEL,
    VAL_LABEL
]:
    os.makedirs(folder, exist_ok=True)

# Image list
images = [
    f for f in os.listdir(IMG_DIR)
    if f.endswith(".jpg")
]

random.shuffle(images)

split_index = int(len(images) * 0.8)

train_images = images[:split_index]
val_images = images[split_index:]

def convert(xml_path, txt_path):

    tree = ET.parse(xml_path)
    root = tree.getroot()

    width = float(root.find("size/width").text)
    height = float(root.find("size/height").text)

    with open(txt_path, "w") as f:

        for obj in root.findall("object"):

            bbox = obj.find("bndbox")

            xmin = float(bbox.find("xmin").text)
            ymin = float(bbox.find("ymin").text)
            xmax = float(bbox.find("xmax").text)
            ymax = float(bbox.find("ymax").text)

            x_center = ((xmin + xmax) / 2) / width
            y_center = ((ymin + ymax) / 2) / height

            box_width = (xmax - xmin) / width
            box_height = (ymax - ymin) / height

            f.write(
                f"0 {x_center} {y_center} {box_width} {box_height}\n"
            )

for image_list, img_dest, label_dest in [
    (train_images, TRAIN_IMG, TRAIN_LABEL),
    (val_images, VAL_IMG, VAL_LABEL)
]:

    for image_name in image_list:

        xml_name = image_name.replace(".jpg", ".xml")

        shutil.copy(
            os.path.join(IMG_DIR, image_name),
            os.path.join(img_dest, image_name)
        )

        convert(
            os.path.join(XML_DIR, xml_name),
            os.path.join(
                label_dest,
                xml_name.replace(".xml", ".txt")
            )
        )

print("Conversion Complete!")