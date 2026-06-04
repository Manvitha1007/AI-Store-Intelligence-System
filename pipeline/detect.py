from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")

video = cv2.VideoCapture("data/store1/CAM 3 - entry.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Store Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()