from ultralytics import YOLO

yolo=YOLO("yolov8s.pt")

yolo.train(
    data="trash-can-1/data.yaml",
    epochs=15,
    imgsz=416,
    batch=16,
    patience=3,
    device="cpu",
    workers=4
)
