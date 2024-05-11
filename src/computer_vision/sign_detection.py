import cv2
import numpy as np

def detect_traffic_signs(image):
    # Load the traffic sign classifier
    traffic_sign_classifier = cv2.CascadeClassifier('traffic_sign_classifier.xml')

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect traffic signs
    traffic_signs = traffic_sign_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected traffic signs
    for (x, y, w, h) in traffic_signs:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image
