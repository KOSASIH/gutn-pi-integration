import cv2
from exceptions import GUTNException

class Screen:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.capture = None

    def connect(self):
        try:
            self.capture = cv2.VideoCapture(self.camera_index)
        except Exception as e:
            raise GUTNException(f"Failed to connect to screen: {str(e)}")

    def disconnect(self):
        if self.capture is not None:
            self.capture.release()

    def display_image(self, image):
        try:
            cv2.imshow("Screen", image)
            cv2.waitKey(1)
        except Exception as e:
            raise GUTNException(f"Failed to display image: {str(e)}")
