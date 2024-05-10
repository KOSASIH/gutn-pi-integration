import serial
from exceptions import GUTNException

class Printer:
    def __init__(self, port='/dev/ttyAMA0', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1.0)
            self.ser.flush()
        except Exception as e:
            raise GUTNException(f"Failed to connect to printer: {str(e)}")

    def disconnect(self):
        if self.ser is not None:
            self.ser.close()

    def print_text(self, text):
        try:
            self.ser.write(f"{text}\n".encode())
            self.ser.flush()
        except Exception as e:
            raise GUTNException(f"Failed to print text: {str(e)}")
