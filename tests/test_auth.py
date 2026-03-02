import unittest
from services.auth_service import AuthService
from database import load_data, save_data

class TestAuthService(unittest.TestCase):

    def setUp(self):
        save_data({"users": [], "cars": [], "bookings": []})
        self.auth = AuthService()

    def test_register_user(self):
        result = self.auth.register("john", "1234", "Customer", "john@test.com")
        self.assertTrue(result)
        data = load_data()
        self.assertEqual(len(data["users"]), 1)

    def test_login_success(self):
        self.auth.register("john", "1234", "Customer", "john@test.com")
        user = self.auth.login("john", "1234")
        self.assertIsNotNone(user)

    def test_login_fail(self):
        user = self.auth.login("fake", "wrong")
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
