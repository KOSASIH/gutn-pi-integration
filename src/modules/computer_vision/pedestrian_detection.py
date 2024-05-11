import cv2
import numpy as np

def detect_pedestrians(image):
    # Load the pedestrian classifier
    pedestrian_classifier = cv2.CascadeClassifier('pedestrian_classifier.xml')

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect pedestrians
    pedestrians = pedestrian_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected pedestrians
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return image
