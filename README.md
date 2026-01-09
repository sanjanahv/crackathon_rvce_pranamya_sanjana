# Road Damage Detection (RDD2022) – YOLOv8

Object detection model developed for the RDD2022 hackathon to identify and classify road surface damages.

## Classes
0 – Longitudinal Crack  
1 – Transverse Crack  
2 – Alligator Crack  
3 – Other Corruption  
4 – Pothole  

## Model
- YOLOv8 Small (YOLOv8s)
- COCO pretrained weights
- Framework: Ultralytics YOLOv8

## Dataset
- Road Damage Detection 2022 (RDD2022)
- Only organizer-provided dataset used

## Training
- Epochs: 50
- Image size: 640
- Validation mAP@50 ≈ 0.52

## Inference & Submission
Predictions are generated for test images in YOLO format with confidence scores and packaged as `submission.zip` as per competition guidelines.
