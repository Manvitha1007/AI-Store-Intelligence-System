from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.track(
    source="data/store1/CAM 3 - entry.mp4",
    persist=True,
    show=True,
    tracker="bytetrack.yaml"
)