import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.utils import to_categorical
import numpy as np
from sklearn.model_selection import train_test_split

def load_dataset(dataset_path, image_size=(128, 128), test_size=0.2):
    X, y = [], []
    labels = sorted([label for label in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, label))])
    label_dict = {label: index for index, label in enumerate(labels)}
    print("Label dictionary:", label_dict)
    
    for label in labels:
        imgs_path = os.path.join(dataset_path, label)
        for img_name in os.listdir(imgs_path):
            if img_name.endswith(('.png', '.jpg', '.jpeg')):  # Ensure it's an image file
                img_path = os.path.join(imgs_path, img_name)
                img = load_img(img_path, target_size=image_size)
                img_array = img_to_array(img)
                X.append(img_array)
                y.append(label_dict[label])

    X = np.array(X, dtype="float32") / 255.0  # Normalize to [0, 1]
    y = to_categorical(np.array(y), num_classes=len(labels))  # One-hot encode the labels

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test, label_dict
