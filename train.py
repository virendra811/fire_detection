from ultralytics import YOLO

# Load pretrained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Train
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    name="fire_detector"
)