import os
import random
import shutil

dataset_path = r"C:\Users\hridika\Desktop\CustomObjectdetection2\vehicle_dataset"

class_folders = ["ambulance", "bike", "auto", "car", "bus"]

images_train = os.path.join(dataset_path, "images", "train")
images_val   = os.path.join(dataset_path, "images", "val")
labels_train = os.path.join(dataset_path, "labels", "train")
labels_val   = os.path.join(dataset_path, "labels", "val")

os.makedirs(images_train, exist_ok=True)
os.makedirs(images_val, exist_ok=True)
os.makedirs(labels_train, exist_ok=True)
os.makedirs(labels_val, exist_ok=True)

all_data = []

# Collect images from all class folders
for folder in class_folders:
    folder_path = os.path.join(dataset_path, folder)

    for file in os.listdir(folder_path):
        if file.endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(folder_path, file)
            txt_path = os.path.join(folder_path, file.rsplit(".", 1)[0] + ".txt")

            all_data.append((img_path, txt_path))

# Shuffle dataset
random.shuffle(all_data)

split = int(0.8 * len(all_data))
train_data = all_data[:split]
val_data = all_data[split:]

def move(data, img_dest, lbl_dest):
    for img_path, txt_path in data:
        shutil.copy(img_path, img_dest)

        if os.path.exists(txt_path):
            shutil.copy(txt_path, lbl_dest)

move(train_data, images_train, labels_train)
move(val_data, images_val, labels_val)

print("✅ Split complete!")