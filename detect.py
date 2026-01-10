from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train/weights/best.pt")

img = cv2.imread("test.jpg")
results = model(img)[0]

img_area = img.shape[0] * img.shape[1]

def severity(area):
    ratio = area / img_area
    if ratio < 0.01:
        return "LOW"
    elif ratio < 0.05:
        return "MEDIUM"
    else:
        return "HIGH"

for box in results.boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cls = int(box.cls[0])
    conf = float(box.conf[0])

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    area = (x2 - x1) * (y2 - y1)

    sev = severity(area)

    print({
        "defect": model.names[cls],
        "confidence": round(conf, 2),
        "center": (cx, cy),
        "severity": sev
    })

    label = f"{model.names[cls]} {conf:.2f} {sev}"
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    cv2.putText(img, label, (x1, y1-8),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
