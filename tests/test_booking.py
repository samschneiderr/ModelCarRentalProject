import unittest
from datetime import date
from services.booking_service import BookingService
from services.car_service import CarService
from database import save_data, load_data


class TestBookingService(unittest.TestCase):

    def setUp(self):
        save_data({"users": [], "cars": [], "bookings": []})

        self.car_service = CarService()
        self.car_service.add_car("Honda", "Civic", 60, "LA")

        self.booking_service = BookingService()

    def test_create_booking(self):
        start = date(2026, 3, 1)
        end = date(2026, 3, 5)

        result = self.booking_service.create_booking(
            username="john",
            car_id=1,
            start_date=start,
            end_date=end,
            add_ons=[]
        )

        self.assertTrue(result)

        data = load_data()
        self.assertEqual(len(data["bookings"]), 1)
        self.assertEqual(data["cars"][0]["status"], "Rented")


if __name__ == "__main__":
    unittest.main()
