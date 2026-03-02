class RewardService:

    @staticmethod
    def add_points(user, amount):
        user["points"] = user.get("points", 0) + int(amount / 10)

    @staticmethod
    def redeem_points(user, points):
        if user.get("points", 0) >= points:
            user["points"] -= points
            return True
        return False
