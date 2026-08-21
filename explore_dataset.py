
import os

path = r"C:\Users\VIRENDRA KUMAR\.cache\kagglehub\datasets\dataclusterlabs\fire-and-smoke-dataset\versions\3"

print("Contents of dataset folder:\n")

for item in os.listdir(path):
    print(item)