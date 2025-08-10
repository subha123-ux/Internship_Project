from tensorflow.keras.preprocessing import image
import numpy as np

def prepare_image(img_path, target_size=(28, 28)):
    img = image.load_img(img_path, color_mode="grayscale", target_size=target_size)
    img_array = image.img_to_array(img)  # shape: (28, 28, 1)
    img_array = img_array.reshape(1, 28, 28)  # Required shape
    img_array = img_array / 255.0
    return img_array



