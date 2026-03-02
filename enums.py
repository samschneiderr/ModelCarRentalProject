from enum import Enum

class UserRole(Enum):
    CUSTOMER = "Customer"
    ADMIN = "Admin"
    RENTAL_AGENT = "RentalAgent"
    MEMBERSHIP_MANAGER = "MembershipManager"
    MAINTENANCE = "MaintenanceTeam"

class BookingStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    ACTIVE = "Active"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class CarStatus(Enum):
    AVAILABLE = "Available"
    RENTED = "Rented"
    MAINTENANCE = "Maintenance"
