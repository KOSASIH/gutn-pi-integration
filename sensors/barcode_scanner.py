import zbar
from exceptions import GUTNException

class BarcodeScanner:
    def __init__(self, device='/dev/ttyUSB0'):
        self.device = device
        self.scanner = None

    def connect(self):
        try:
            self.scanner = zbar.Scanner()
            self.scanner.connect(self.device)
        except Exception as e:
            raise GUTNException(f"Failed to connect to barcode scanner: {str(e)}")

    def disconnect(self):
        if self.scanner is not None:
            self.scanner.close()

    def scan(self):
        try:
            raw = self.scanner.scan()
            for symbol in raw:
                return symbol.data

        except Exception as e:
            raise GUTNException(f"Failed to scan barcode: {str(e)}")
