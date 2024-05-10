import os
import logging
from user import User
from payment import Payment
from itinerary import Itinerary
from real_time_updates import RealTimeUpdates
from network import Network
from exceptions import GUTNException

def main():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    user = User("John Doe", "john.doe@example.com")
    payment = Payment(user)
    itinerary = Itinerary(user)
    real_time_updates = RealTimeUpdates()
    network = Network()

    try:
        payment.buy_ticket("Bus", "Airport", "2022-05-01", "09:00")
        itinerary.add_leg("Bus", "Airport", "2022-05-01", "09:00")
        real_time_updates.get_updates()
        network.connect_to_pi_network()
    except GUTNException as e:
        logging.error(str(e))

if __name__ == "__main__":
    main()
