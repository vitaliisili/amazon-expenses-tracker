import sys

from auth.auth import Auth


class Login(Auth):

    def __init__(self):
        pass

    def login(self):
        self.print_message("Please login to your account")

        while username := input("Username: "):
            if self.validate_username(username):
                break
            print("User with username not found please try again")

        attempts = 5
        while password := input("Password: "):
            attempts -= 1

            if self.validate_password(password):
                break

            if attempts == 0:
                print("To many attempts please register again")
                sys.exit()

            if attempts == 1:
                print("Incorrect password, to many attempts wait 5 seconds and try again, remain attempts", attempts)
                continue

            print("Password is not correct please try again remain attempts", attempts)

    def validate_username(self, username):
        return True

    def validate_password(self, password):
        return True
