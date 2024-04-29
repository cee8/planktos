from PIL import Image
import os

def preprocess_image(image_path, output_path, scale_factor=5.5):
    """
    Processes an image by scaling it down, converting it to grayscale, and saving it as a PNG.

    Args:
    image_path (str): The path to the input image.
    output_path (str): The path where the processed image will be saved.
    scale_factor (float): The factor by which the image dimensions will be reduced.
    """
    # Open an image file
    with Image.open(image_path) as img:
        # Convert image to grayscale
        img = img.convert('L')  # 'L' mode is for grayscale

        # Scale down the image
        width, height = img.size
        new_width = int(width / 5.5)
        new_height = int(height / 5.5)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Save the processed image as PNG
        img.save(output_path, 'PNG')

    print(f"Processed image saved to {output_path}")

def process_all_images(raw_folder, preprocessed_folder):
    """
    Processes all images in the specified raw folder and saves the processed images in the preprocessed folder.

    Args:
    raw_folder (str): The folder containing the raw images.
    preprocessed_folder (str): The folder where the processed images will be saved.
    """
    if not os.path.exists(preprocessed_folder):
        os.makedirs(preprocessed_folder)
    
    # Process each image in the raw folder
    for img_name in os.listdir(raw_folder):
        # Check for common image file extensions
        if img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(raw_folder, img_name)
            output_path = os.path.join(preprocessed_folder, os.path.splitext(img_name)[0] + '.png')
            preprocess_image(img_path, output_path)

# Example usage: process all images in 'data/raw' and save to 'data/preprocessed'
if __name__ == '__main__':
    raw_images_folder = 'data/raw'
    preprocessed_images_folder = 'data/preprocessed'
    process_all_images(raw_images_folder, preprocessed_images_folder)
