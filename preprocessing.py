import os
import random
import cv2
import shutil
import numpy as np

# ==============================
# CONFIGURATION
# ==============================

SOURCE_DIR = r"C:/Users/Divya/Desktop/IOMP/Datasetraw/plantvillage dataset/color"        
DEST_DIR = "dataset_processed"     # Output folder

TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
TEST_RATIO = 0.15

IMG_SIZE = 224
SEED = 42
random.seed(SEED)

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png")
MAX_IMAGES_PER_CLASS = 250

# ==============================
# CLEAN OLD DATASET
# ==============================

def clean_output_folder():
    if os.path.exists(DEST_DIR):
        shutil.rmtree(DEST_DIR)
    for split in ["train", "val", "test"]:
        os.makedirs(os.path.join(DEST_DIR, split), exist_ok=True)

# ==============================
# IMAGE PREPROCESSING
# ==============================

def preprocess_image(image_path, save_path):
    try:
        img = cv2.imread(image_path)

        if img is None:
            print("❌ Skipping corrupted:", image_path)
            return False

        # Convert to RGB (important for deep learning)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Resize
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

        # Save image
        cv2.imwrite(save_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

        return True

    except Exception as e:
        print("❌ Error processing:", image_path, "|", e)
        return False


# ==============================
# SPLIT + PROCESS
# ==============================

def split_and_process():

    clean_output_folder()

    total_processed = 0

    for class_name in os.listdir(SOURCE_DIR):

        class_path = os.path.join(SOURCE_DIR, class_name)

        if not os.path.isdir(class_path):
            continue

        images = [
            img for img in os.listdir(class_path)
            if img.lower().endswith(VALID_EXTENSIONS)
        ]

        if len(images) == 0:
            continue

        random.shuffle(images)
        images = images[:MAX_IMAGES_PER_CLASS]

        total = len(images)
        train_end = int(TRAIN_RATIO * total)
        val_end = train_end + int(VAL_RATIO * total)

        splits = {
            "train": images[:train_end],
            "val": images[train_end:val_end],
            "test": images[val_end:]
        }

        print(f"\n📁 Processing class: {class_name} ({total} images)")

        for split, image_list in splits.items():

            split_class_path = os.path.join(DEST_DIR, split, class_name)
            os.makedirs(split_class_path, exist_ok=True)

            for img_name in image_list:

                src = os.path.join(class_path, img_name)
                dest = os.path.join(split_class_path, img_name)

                success = preprocess_image(src, dest)

                if success:
                    total_processed += 1

    print("\n✅ Dataset Preprocessing Completed!")
    print("📊 Total Images Processed:", total_processed)


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    split_and_process()