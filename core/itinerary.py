from user import User
from exceptions import GUTNException

class Itinerary:
    def __init__(self, user):
        self.user = user
        self.legs = []

    def add_leg(self, transportation_type, destination, date, time):
        try:
           # Add itinerary leg logic
            pass
        except Exception as e:
            raise GUTNException(f"Failed to add itinerary leg: {str(e)}")
