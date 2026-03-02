from database import load_data, save_data

class CarService:
    def __init__(self):
        pass

    def add_car(self, brand, model, price, location):
        data = load_data()
        car_id = len(data["cars"]) + 1
        data["cars"].append({
            "id": car_id,
            "brand": brand,
            "model": model,
            "price": price,
            "location": location,
            "status": "Available"
        })
        save_data(data)
        return True
