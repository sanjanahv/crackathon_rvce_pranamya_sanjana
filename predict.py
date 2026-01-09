from ultralytics import YOLO

# Load best trained model
model = YOLO("/kaggle/input/latest-output/runs/detect/train/weights/best.pt")

# Run inference on test images
model.predict(
    source="/kaggle/input/crackathon-data/randomized_dataset/test/images",
    save_txt=True,
    save_conf=True,
    conf=0.25,
    imgsz=640,
    project="predictions",
    name="test_results"
)
