from ultralytics import YOLO

model = YOLO(
    "runs/detect/fire_detector/weights/best.pt"
)

model.predict(
    source="C:\Users\VIRENDRA KUMAR\Downloads\fire test.avif.jpg",
    save=True,
    conf=0.25
)