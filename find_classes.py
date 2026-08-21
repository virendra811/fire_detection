import os
import xml.etree.ElementTree as ET

annotation_folder = r"C:\Users\VIRENDRA KUMAR\.cache\kagglehub\datasets\dataclusterlabs\fire-and-smoke-dataset\versions\3\Annotations\Annotations"

classes = set()

for file in os.listdir(annotation_folder):
    if file.endswith(".xml"):
        xml_path = os.path.join(annotation_folder, file)

        tree = ET.parse(xml_path)
        root = tree.getroot()

        for obj in root.findall("object"):
            classes.add(obj.find("name").text)

print("Classes found:")
print(classes)