from model.user_model import User
from dao.user_db import user_db


class UserService:
    def __init__(self):
        pass

    def save_user(self, user: User):
        user_db["username"] = user.username
        user_db["password"] = user.password
        user_db["phone"] = user.phone
