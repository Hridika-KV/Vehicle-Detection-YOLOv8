# Vehicle Detection using YOLOv8

## Project Overview

This project is a custom Vehicle Detection system developed using the YOLOv8 object detection model. A custom dataset was collected, annotated, and used to train the model to detect different types of vehicles in images.

## Classes Detected

* Ambulance
* Bike
* Auto Rickshaw
* Car
* Bus

## Dataset

The dataset was manually annotated using LabelImg and divided into training and validation sets for model training and evaluation.

## Model Used

* YOLOv8n (Ultralytics)
* Training Epochs: 50

## Results

The trained model can detect:

* Ambulance
* Bike
* Auto Rickshaw
* Car
* Bus

with good accuracy on test images.

## Project Files

* `vehicle_dataset/` – Dataset images and labels
* `data.yaml` – Dataset configuration
* `detect.py` – Vehicle detection script
* `runs/` – Training and prediction results
* `best.pt` – Trained YOLOv8 model

## How to Run

Run the detection script:

```bash
python detect.py
```

Enter the image path when prompted, and the detected output image will be saved automatically.

## Technologies Used

* Python
* YOLOv8
* Ultralytics
* OpenCV
* LabelImg

## Author

## Author

**Name:** Hridika K V

**Course:** B.Tech Computer Science and Engineering

**College:** Government Engineering College, Wayanad
