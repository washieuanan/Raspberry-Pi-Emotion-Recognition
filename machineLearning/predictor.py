import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
from tensorflow.keras.models import load_model


model = load_model(
    r"C:\Users\washi\Desktop\Coding\raspberry_pi_emotion_detection\snapshot\machineLearning\model.h5",
    compile=True,
)


class Predictor:
    def __init__(self):
        return

    def resize(self, src):
        """Resizes the image to the size of the images that the model trained on."""
        large_img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        resize_img = cv2.resize(large_img, (48, 48))
        new_img = cv2.imwrite(
            r"C:\Users\washi\Desktop\Coding\raspberry_pi_emotion_detection\snapshot\output\new_ml_image.jpg",
            resize_img,
        )
        img = Image.open(
            r"C:\Users\washi\Desktop\Coding\raspberry_pi_emotion_detection\snapshot\output\new_ml_image.jpg",
            "r",
        )
        pixels = np.array(list(img.getdata()))
        pixels = pixels.flatten()

        image = pixels.reshape((48, 48, 1)).astype("float32")
        image = np.expand_dims(image, axis=0)

        return image

    def predict(self, src):
        mapper = {
            0: "happy",
            1: "sad",
            2: "neutral",
        }
        prediction = np.argmax(model.predict_classes(src), axis=0)

        return prediction
