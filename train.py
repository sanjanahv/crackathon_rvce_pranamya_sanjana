from ultralytics import YOLO
import yaml

# Load dataset config
DATA_YAML = "dataset.yaml"

# Load existing weights for refinement
OLD_WEIGHTS_PATH = "/kaggle/input/crackathon-rvce/runs/detect/train/weights/best.pt"

model = YOLO(OLD_WEIGHTS_PATH)

# Train / refine model
model.train(
    data=DATA_YAML,
    epochs=50,
    imgsz=800,
    batch=-1,
    patience=20,
    optimizer="AdamW",
    project="crackathon_final",
    name="v8s_refined"
)
