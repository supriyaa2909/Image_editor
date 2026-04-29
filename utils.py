import cv2
import numpy as np
from PIL import Image

def pil_to_cv(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

def cv_to_pil(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb)

def image_to_bytes(image):
    _, buffer = cv2.imencode('.png', image)
    return buffer.tobytes()