import os
import shutil

src = "dataset"
train_img = "images/train"
val_img = "images/val"

os.makedirs(train_img, exist_ok=True)
os.makedirs(val_img, exist_ok=True)

images = sorted(os.listdir(src))

for i, img in enumerate(images):
    if not img.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    if i % 5 == 4:
        shutil.move(os.path.join(src, img), os.path.join(val_img, img))
    else:
        shutil.move(os.path.join(src, img), os.path.join(train_img, img))
