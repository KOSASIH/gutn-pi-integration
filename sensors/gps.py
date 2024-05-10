import serial
import time
from exceptions import GUTNException

class GPS:
    def __init__(self, port='/dev/ttyAMA0', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1.0)
            self.ser.flush()
        except Exception as e:
            raise GUTNException(f"Failed to connect to GPS: {str(e)}")

    def disconnect(self):
        if self.ser is not None:
            self.ser.close()

    def get_location(self):
        try:
            self.ser.write(b"$GPGGA")
            time.sleep(1.0)
            data = self.ser.readline().decode().strip()

            if data.startswith("$GPGGA"):
                latitude, longitude, quality, satellites, hdop, altitude = data.split(",")[2:8]
                return (float(latitude), float(longitude))

        except Exception as e:
            raise GUTNException(f"Failed to get location from GPS: {str(e)}")
