import unittest
from services.car_service import CarService
from database import save_data


class TestCarService(unittest.TestCase):

    def setUp(self):
        save_data({"users": [], "cars": [], "bookings": []})
        self.car_service = CarService()

    def test_add_car(self):
        self.car_service.add_car("Toyota", "Corolla", 50, "NY")
        from database import load_data
        data = load_data()

        self.assertEqual(len(data["cars"]), 1)
        self.assertEqual(data["cars"][0]["brand"], "Toyota")


if __name__ == "__main__":
    unittest.main()
