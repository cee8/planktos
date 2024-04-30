import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def load_and_prepare_image(image_path, target_size=(128, 128)):
    """Load an image and prepare it for prediction."""
    img = load_img(image_path, target_size=target_size)
    img = img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def predict_image(model, img, class_names):
    """Predict the class of the image using the loaded model."""
    prediction = model.predict(img)
    predicted_class_index = np.argmax(prediction)
    predicted_class_name = class_names[predicted_class_index]
    return predicted_class_name, prediction


def main(image_path, model_path, label_path):
    print("Loading model...")
    model = load_model(model_path)
    print("Model loaded.")

    # Load class names
    with open(label_path, 'r') as f:
        class_names = json.load(f)

    print("Loading and preparing image...")
    img = load_and_prepare_image(image_path)
    print("Image loaded and prepared.")

    print("Making prediction...")
    predicted_class_name, prediction = predict_image(model, img, list(class_names.keys()))
    print("Predicted Class:", predicted_class_name)
    print("Raw Prediction:", prediction)

if __name__ == "__main__":
    # Define the path to your image and model here
    image_path = 'data/test/Nodularia_spumigena_51.png'  # Replace with a valid image path
    model_path = 'models/model.keras'  # Adjust this to where your trained model is saved
    phyto_dir = 'data/training/phyto_skye/phyto'

    # Filter out hidden files and ensure only directories are counted as classes
    class_names = sorted([d for d in os.listdir(phyto_dir)
                          if os.path.isdir(os.path.join(phyto_dir, d)) and not d.startswith('.')])

    # Load model
    model = load_model(model_path)
    print("Model loaded.")

    # Load and prepare image
    img = load_and_prepare_image(image_path)
    print("Image loaded and prepared.")

    # Make a prediction
    predictions = model.predict(img)
    predicted_class_index = np.argmax(predictions)
    predicted_class_name = class_names[predicted_class_index]
    
    print("Predicted Class Index:", predicted_class_index)
    print("Predicted Class Name:", predicted_class_name)
    print("Raw Prediction:", predictions)
    print("Class names:", class_names)