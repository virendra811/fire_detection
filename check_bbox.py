import xml.etree.ElementTree as ET

xml_file = r"C:\Users\VIRENDRA KUMAR\.cache\kagglehub\datasets\dataclusterlabs\fire-and-smoke-dataset\versions\3\Annotations\Annotations\Datacluster Fire and Smoke Sample (1).xml"

tree = ET.parse(xml_file)
root = tree.getroot()

for obj in root.findall("object"):
    print("Class:", obj.find("name").text)

    bbox = obj.find("bndbox")

    print("xmin:", bbox.find("xmin").text)
    print("ymin:", bbox.find("ymin").text)
    print("xmax:", bbox.find("xmax").text)
    print("ymax:", bbox.find("ymax").text)