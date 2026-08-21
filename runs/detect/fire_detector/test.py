from ultralytics import YOLO

model = YOLO(
    "runs/detect/fire_detector/weights/best.pt"
)

results = model.predict(
    source="dataset/images/val",
    save=True,
    conf=0.25
)


