from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8n.pt")

cap = cv2.VideoCapture("data/store1/CAM 1 - zone.mp4")

zone_count = 0
seen_ids = set()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0]
    )

    if results[0].boxes.id is not None:

        ids = results[0].boxes.id.cpu().numpy()

        for id_num in ids:

            if id_num not in seen_ids:
                seen_ids.add(id_num)

    zone_count = len(seen_ids)

    annotated = results[0].plot()

    cv2.putText(
        annotated,
        f"ZONE VISITORS: {zone_count}",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Zone Analytics", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print("\nTOTAL ZONE VISITORS:", zone_count)

cap.release()
cv2.destroyAllWindows()