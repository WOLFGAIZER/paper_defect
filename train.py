from ultralytics import YOLO

#pretrained yolo model 
model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=30,
    imgsz=640,
    batch=8,
    project="runs",        
    name="paper_defect"    
)
