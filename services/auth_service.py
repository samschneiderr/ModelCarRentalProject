from database import load_data, save_data

class AuthService:
    def __init__(self):
        pass

    def register(self, username, password, role, email):
        data = load_data()
        # check duplicate
        for user in data["users"]:
            if user["username"] == username:
                return False
        data["users"].append({
            "username": username,
            "password": password,
            "role": role,
            "email": email
        })
        save_data(data)
        return True

    def login(self, username, password):
        data = load_data()
        for user in data["users"]:
            if user["username"] == username and user["password"] == password:
                return user
        return None
