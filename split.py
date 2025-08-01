# Not recommended to use this method of splitting use tensorflow or torch libraries for generating test/train/val data

import os
import random
import shutil

# Seed for reproducibility
random.seed(42)

# Original dataset directory
source_dir = "Dataset/Brain Tumor MRI images"
# Target dataset directory
target_dir = "Dataset_Split"
# Classes
classes = ["Healthy", "Tumor"]
# Split ratios
split_ratio = (0.7, 0.15, 0.15)

for cls in classes:
    # Full path to class folder
    class_path = os.path.join(source_dir, cls)
    images = os.listdir(class_path)
    random.shuffle(images)

    total = len(images)
    train_end = int(split_ratio[0] * total)
    val_end = train_end + int(split_ratio[1] * total)

    splits = {
        "train": images[:train_end],
        "val": images[train_end:val_end],
        "test": images[val_end:]
    }

    for split_name, split_files in splits.items():
        split_folder = os.path.join(target_dir, split_name, cls)
        os.makedirs(split_folder, exist_ok=True)

        for file_name in split_files:
            src = os.path.join(class_path, file_name)
            dst = os.path.join(split_folder, file_name)
            shutil.copy2(src, dst)  # use copy2 to preserve metadata
