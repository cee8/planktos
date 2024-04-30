import os
import random
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img

def display_random_images(data_path, num_images=5):
    classes = [d for d in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, d))]
    for cls in classes:
        print(f"Class: {cls}")
        cls_path = os.path.join(data_path, cls)
        images = os.listdir(cls_path)
        random_images = random.sample(images, min(num_images, len(images)))
        
        plt.figure(figsize=(12, 10))
        for i, img_name in enumerate(random_images, 1):
            img_path = os.path.join(cls_path, img_name)
            img = load_img(img_path)
            plt.subplot(1, num_images, i)
            plt.imshow(img)
            plt.axis('off')
        plt.show()

# Usage
data_path = 'data/training/phyto_skye/phyto'
display_random_images(data_path)
