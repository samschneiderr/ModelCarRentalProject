from database import load_data, save_data
from models.booking import Booking
from enums import BookingStatus
from services.payment_service import PaymentService
from services.notification_service import NotificationService


class BookingService:

    def create_booking(self, username, car_id, start_date, end_date, add_ons):

        data = load_data()

        car = next((c for c in data["cars"] if c["car_id"] == car_id), None)

        if not car or car["status"] != "Available":
            print("Car not available.")
            return False

        days = (end_date - start_date).days
        total_price = car["price_per_day"] * days

        for addon in add_ons:
            total_price += addon["price"]

        if not PaymentService.process_payment(total_price):
            print("Payment failed.")
            return False

        booking_id = len(data["bookings"]) + 1

        booking = Booking(
            booking_id,
            username,
            car_id,
            str(start_date),
            str(end_date),
            add_ons,
            total_price
        )

        booking.status = BookingStatus.CONFIRMED.value
        data["bookings"].append(booking.to_dict())

        car["status"] = "Rented"

        save_data(data)

        NotificationService.send_booking_confirmation(username)

        print("Booking confirmed.")
        return True
