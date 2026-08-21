# import os

# path = r"C:\Users\VIRENDRA KUMAR\.cache\kagglehub\datasets\dataclusterlabs\fire-and-smoke-dataset\versions\3"

# for item in os.listdir(path):
#     full_path = os.path.join(path, item)

#     print("\n", item)

#     if os.path.isdir(full_path):
# #         print(os.listdir(fullpath)[:20])  # show first 20 items
# import os

# path = r"C:\Users\VIRENDRA KUMAR\.cache\kagglehub\datasets\dataclusterlabs\fire-and-smoke-dataset\versions\3"

# for root, dirs, files in os.walk(path):
#     print("\nROOT:", root)
#     print("DIRS:", dirs[:10])
#     print("FILES:", files[:10])

import os

path = r"C:\Users\VIRENDRA KUMAR\.cache\kagglehub\datasets\dataclusterlabs\fire-and-smoke-dataset\versions\3\Annotations\Annotations"

files = os.listdir(path)

print("Number of files:", len(files))
print(files[:10])