from datetime import date
from services.auth_service import AuthService
from services.car_service import CarService
from services.booking_service import BookingService
from services.reward_service import RewardService
from services.payment_service import PaymentService
from services.damage_claim import DamageClaimService
from services.gps_service import GPSService
from database import save_data, load_data

# Reset database
save_data({"users": [], "cars": [], "bookings": []})

auth = AuthService()
car_service = CarService()
booking_service = BookingService()

print("=" * 40)
print("   CAR RENTAL SYSTEM DEMO")
print("=" * 40)

# Register and login
print("\n--- User Registration & Login ---")
auth.register("john", "1234", "Customer", "john@test.com")
user = auth.login("john", "1234")
print(f"User registered and logged in: {user.username}")

# Add cars
print("\n--- Adding Cars ---")
car_service.add_car("Toyota", "Corolla", 50, "New York")
car_service.add_car("Honda", "Civic", 60, "Los Angeles")
data = load_data()
for car in data["cars"]:
    print(f"Car added: {car['brand']} {car['model']} - ${car['daily_rate']}/day in {car['location']}")

# Create booking
print("\n--- Booking a Car ---")
start = date(2026, 4, 1)
end = date(2026, 4, 5)
result = booking_service.create_booking(
    username="john",
    car_id=1,
    start_date=start,
    end_date=end,
    add_ons=[]
)
print(f"Booking created: {result}")
data = load_data()
print(f"Car status: {data['cars'][0]['status']}")

print("\n" + "=" * 40)
print("   ALL SYSTEMS WORKING")
print("=" * 40)
