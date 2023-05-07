from pwinput import pwinput
from auth.auth import Auth
from model.user_model import User
from service.user_service import UserService


class RegistrationService(Auth):
    def __init__(self):
        pass

    def register_user(self):
        self.print_message("Hello to amazon please register new account")

        while username := input("Username: "):
            if self.validate_username(username):
                break
            print("Username is not valid please try again")

        while password := pwinput(prompt="Password: ", mask="*"):
            if self.validate_password(password):
                break
            print("Password is not valid please try again")

        while phone := input("Phone number: "):
            if self.__validate_phone(phone):
                break
            print("Phone number is not valid please try again")

        user = User(username, password, phone)
        user_service = UserService()
        user_service.save_user(user)

    def validate_username(self, username):
        return True

    def validate_password(self, password):
        return True

    def __validate_phone(self, phone):
        return True
