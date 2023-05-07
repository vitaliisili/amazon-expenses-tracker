from abc import ABC, abstractmethod


class Auth(ABC):

    @abstractmethod
    def validate_username(self, username):
        pass

    @abstractmethod
    def validate_password(self, password):
        pass

    def print_message(self, message):
        print(message)
