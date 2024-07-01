import os
import logging
from typing import Tuple, Dict, List
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.utils import to_categorical
import numpy as np
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO)

def load_dataset(dataset_path: str, image_size: Tuple[int, int] = (128, 128), test_size: float = 0.2) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Dict[str, int]]:
    """
    Load a dataset of images from a directory, split it into training and testing sets, and return them along with a dictionary of labels.

    Parameters:
    - dataset_path: The path to the dataset directory.
    - image_size: The target size of the images.
    - test_size: The proportion of the dataset to include in the test split.

    Returns:
    - A tuple containing the training images, test images, training labels, test labels, and a dictionary of labels.

    Raises:
    - ValueError: If `dataset_path` does not exist or is not a directory.
    """
    if not os.path.exists(dataset_path):
        raise ValueError(f"'{dataset_path}' does not exist.")
    if not os.path.isdir(dataset_path):
        raise ValueError(f"'{dataset_path}' is not a directory.")

    X, y, label_dict = load_images_and_labels(dataset_path, image_size)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test, label_dict

def load_images_and_labels(dataset_path: str, image_size: Tuple[int, int]) -> Tuple[np.ndarray, np.ndarray, Dict[str, int]]:
    """
    Load images and their labels from a directory.

    Parameters:
    - dataset_path: The path to the dataset directory.
    - image_size: The target size of the images.

    Returns:
    - A tuple containing a list of images and a list of their corresponding labels.
    """
    X, y = [], []
    labels = sorted([label for label in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, label))])
    label_dict = {label: index for index, label in enumerate(labels)}
    logging.info("Label dictionary: %s", label_dict)

    for label in labels:
        imgs_path = os.path.join(dataset_path, label)
        for img_name in os.listdir(imgs_path):
            if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):  # Ensure it's an image file
                img_path = os.path.join(imgs_path, img_name)
                try:
                    img = load_img(img_path, target_size=image_size)
                    img_array = img_to_array(img)
                    X.append(img_array)
                    y.append(label_dict[label])
                except Exception as e:
                    logging.warning("Failed to process image %s: %s", img_path, e)

    X = np.array(X, dtype="float32") / 255.0  # Normalize to [0, 1]
    y = to_categorical(np.array(y), num_classes=len(labels))  # One-hot encode the labels

    return X, y, label_dict
