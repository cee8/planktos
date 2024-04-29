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

def predict_image(model, img):
    """Predict the class of the image using the loaded model."""
    prediction = model.predict(img)
    return prediction

def main(image_path, model_path):
    """Load model, prepare image, make prediction, and print the result."""
    print("Loading model...")
    model = load_model(model_path)
    print("Model loaded.")

    print("Loading and preparing image...")
    img = load_and_prepare_image(image_path)
    print("Image loaded and prepared.")

    print("Making prediction...")
    prediction = predict_image(model, img)
    print("Prediction:", prediction)

if __name__ == "__main__":
    # Define the path to your image and model here
    image_path = 'data/test/IMG_8786.png'
    model_path = 'src/model.py'  # Adjust this to where your trained model is saved

    main(image_path, model_path)
