from tensorflow.keras.models import load_model
import numpy as np
import cv2

def load_pill_detection_model(model_path='pill_detector_model.h5'):
    return load_model(model_path)

def predict_pills(image, model):
    image = cv2.resize(image, (64, 64))
    image = np.expand_dims(image, axis=0)
    return model.predict(image)
