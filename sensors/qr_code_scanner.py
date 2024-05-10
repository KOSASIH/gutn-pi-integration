import cv2
import numpy as np
from exceptions import GUTNException

class QRCodeScanner:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.capture = None

    def connect(self):
        try:
            self.capture = cv2.VideoCapture(self.camera_index)
        except Exception as e:
            raise GUTNException(f"Failed to connect to QR code scanner: {str(e)}")

    def disconnect(self):
        if self.capture is not None:
            self.capture.release()

    def scan(self):
        try:
            ret, frame = self.capture.read()
            if not ret:
                raise GUTNException("Failed to capture frame from camera")

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            barcode_detector = cv2.QRCodeDetector()
            _, decoded_info, _ = barcode_detector.detectAndDecode(gray)

            if decoded_info is not None:
                return decoded_info

        except Exception as e:
            raise GUTNException(f"Failed to scan QR code: {str(e)}")
