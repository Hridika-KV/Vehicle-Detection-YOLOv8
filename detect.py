from ultralytics import YOLO
import os

model = YOLO("runs/detect/train/weights/best.pt")

file_name = input("Enter image or video name: ")

if os.path.isfile(file_name):

    model.predict(
    source=file_name,
    save=True,
    name="output",
    exist_ok=True
    )
    print("Detection completed! Results saved in 'results/output'")
else:
    print("File not found!")