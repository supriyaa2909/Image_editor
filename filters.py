import cv2

def apply_blur(image, ksize):
    if ksize > 1:
        return cv2.GaussianBlur(image, (ksize, ksize), 0)
    return image

def apply_sharpness(image, alpha):
    blurred = cv2.GaussianBlur(image, (0, 0), 3)
    return cv2.addWeighted(image, 1 + alpha, blurred, -alpha, 0)

def apply_brightness(image, beta):
    return cv2.convertScaleAbs(image, alpha=1.0, beta=beta)

def apply_contrast(image, alpha):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

def apply_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

def apply_edge_detection(image, t1, t2):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, t1, t2)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))