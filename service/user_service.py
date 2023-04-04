import sys
from typing import Union

import config.app_config as config
import service.validation_service as validation
from dao.user_database import user_db
import time


def register_user(username: str, password: str) -> None:
    """  Register new user

    This function is used to register a new user to a database by inserting their
    username and password into the database

    :param username: (str) The username of the user to be registered.
    :param password: (str) The password of the user to be registered
    :return: (None) This function does not return any value. It only inserts the new user information into the database
    """

    if not validation.is_password_valid(password):
        print_message(config.REGISTRATION_PASSWORD_ERROR_MESSAGE, exit_app=True)

    if not validation.is_username_valid(username):
        print_message(config.REGISTRATION_USERNAME_ERROR_MESSAGE, exit_app=True)

    user_db["username"] = username
    user_db["password"] = password

    print_message(config.REGISTRATION_SUCCESSFUL_MESSAGE)


def login_user(login_attempt: int) -> None:
    """ Ask user to insert login credentials

    This function read from user input username and password for authentication

    :return: (None) This function does not return any value
    """

    for i in range(login_attempt, -1, -1):
        print_message(f"\nPlease login to system with your username and password")
        username: str = input("Username: ")
        password: str = input("Password: ")

        if authenticate_user(username, password):
            print_message(config.LOGIN_SUCCESSFUL_MESSAGE)
            break

        if i == 0 and not authenticate_user(username, password):
            print_message(config.REPEAT_REGISTRATION_ERROR_MESSAGE, exit_app=True)

        if i == 1 and not authenticate_user(username, password):
            print_message(config.LOGIN_ATTEMPTS_ERROR_MESSAGE)
            time.sleep(config.SECONDS_TO_NEXT_ATTEMPT)

        print_message(config.LOGIN_ERROR_MESSAGE)  # TODO: Decide if show attempt

    print_message(config.GREETING_MESSAGE % user_db["username"])


def authenticate_user(username: str, password: str) -> bool:
    """ Check if user can be authenticated

    This function check for user username and user password if
    there are equal to database username and password return True if there are equal otherwise False

    :param username: (str) A string representing the username
    :param password: (str) A string representing the username
    :return: (bool) Return true if username and password match
     """

    return user_db["username"] == username and user_db["password"] == password


def get_user_phone_number() -> None:
    """  Get phone number from user input

    This function is used to get the phone number from user input

    :return: (None) This function does not return any value.
    """

    phone = input("Please enter phone number to continue: ")

    if not validation.is_phone_valid(phone):
        print_message(config.PHONE_ERROR_MESSAGE)
        get_user_phone_number()

    update_user("phone", phone)
    print_message(config.PHONE_SUCCESS_MESSAGE)


def update_user(key: str, value: Union[str, int, float]) -> None:
    """ Update a user's information in the database

    This function is used to update a user's information in the database
    based on the key-value pair provided.

    :param key: (str) The key for the user information to be updated.
    :param value: [str, int, float]  The new value for the user information to be updated
    :return: (None) This function does not return any value. It only updates the user information in the database based
    """

    user_db[key] = value


def print_message(msg: str, exit_app: bool = False) -> None:
    """  Print message to console

    Get argument <msg>: str and print this message to console
    also after printing message the flow can be stopped if <exit_app> is set to False

    :param msg: (str) Get string message
    :param exit_app: (bool) stop the flow default is False
    :return: (None)
    """

    print(msg)
    if exit_app:
        sys.exit()
