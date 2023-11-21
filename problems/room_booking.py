from datetime import datetime, timedelta

class SingleRoom:
    def __init__(self, room_number):
        self.__room_number = room_number
        self.__reservations = []
        self.__price = 100

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self.__price = value

    def reserve(self, reservation: tuple):
        date_from, date_to = reservation
        if date_from > date_to:
            reservation = ([date_to, date_from], reservation[1])

        is_available = True
        for dates, _ in self.__reservations:
            booked_from, booked_to = dates
            if date_to <= booked_from or date_from >= booked_to: 
                continue

            is_available = False
            break

        if not is_available:
            return False

        self.__reservations.append(reservation)
        return True
