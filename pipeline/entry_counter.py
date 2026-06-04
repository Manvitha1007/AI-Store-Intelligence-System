from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("data/store1/CAM 3 - entry.mp4")

seen_ids = set()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml"
    )

    if results[0].boxes.id is not None:

        ids = results[0].boxes.id.cpu().numpy().astype(int)

        for track_id in ids:

            if track_id not in seen_ids:
                seen_ids.add(track_id)

                print(
                    f"VISITOR ENTERED -> ID {track_id}"
                )

    annotated = results[0].plot()

    cv2.imshow("Entry Counter", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print()
print("TOTAL VISITORS:", len(seen_ids))

cap.release()
cv2.destroyAllWindows()