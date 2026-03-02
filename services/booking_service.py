from ..database import load_data, save_data
from ..datetime import date

class BookingService:
    def __init__(self):
        pass

    def create_booking(self, username, car_id, start_date: date, end_date: date, add_ons=[]):
        data = load_data()
        car = next((c for c in data["cars"] if c["id"] == car_id), None)
        if not car or car["status"] != "Available":
            return False
        booking_id = len(data["bookings"]) + 1
        data["bookings"].append({
            "id": booking_id,
            "username": username,
            "car_id": car_id,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "add_ons": add_ons
        })
        car["status"] = "Rented"
        save_data(data)
        return True
