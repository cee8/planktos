import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

def load_dataset(dataset_path, image_size=(128, 128)):
    X, y = [], []
    labels = sorted(os.listdir(dataset_path))
    label_dict = {label: index for index, label in enumerate(labels)}

    for label in labels:
        imgs_path = os.path.join(dataset_path, label)
        for img_name in os.listdir(imgs_path):
            img_path = os.path.join(imgs_path, img_name)
            img = load_img(img_path, target_size=image_size)
            img_array = img_to_array(img)
            X.append(img_array)
            y.append(label_dict[label])
    
    X = np.array(X, dtype="float32") / 255.0  # Normalize to [0, 1]
    y = to_categorical(np.array(y))  # One-hot encode the labels

    return X, y

# Path to your processed data
data_path = 'data/processed/phyto_skye/phyto'
X, y = load_dataset(data_path)

# Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
