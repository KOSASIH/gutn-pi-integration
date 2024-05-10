from user import User
from exceptions import GUTNException

class Payment:
    def __init__(self, user):
        self.user = user

    def buy_ticket(self, transportation_type, destination, date, time):
        try:
            # Purchase ticket logic
            pass
        except Exception as e:
            raise GUTNException(f"Failed to buy ticket: {str(e)}")
