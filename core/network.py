import pi_network
from exceptions import GUTNException

class Network:
    def __init__(self):
        self.pi_network = pi_network.PiNetwork()

    def connect_to_pi_network(self):
        try:
            # Connect to Pi Network logic
            self.pi_network.connect()
        except Exception as e:
            raise GUTNException(f"Failed to connect to Pi Network: {str(e)}")
