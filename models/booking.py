from enums import BookingStatus

class Booking:
    def __init__(self, booking_id, username, car_id, start_date, end_date, add_ons, total_price):
        self.booking_id = booking_id
        self.username = username
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.add_ons = add_ons
        self.total_price = total_price
        self.status = BookingStatus.PENDING.value
        self.mileage = 0

    def to_dict(self):
        return self.__dict__
