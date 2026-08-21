import kagglehub

path = kagglehub.dataset_download(
    "dataclusterlabs/fire-and-smoke-dataset"
)

print("Dataset Path:", path)