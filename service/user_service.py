import sys
import config.app_config as config


def register_user(username: str, password: str) -> None:
    """  TODO: add base description
    TODO: add full description, parameters, return description
    :param username:
    :param password:
    :return:
    """
    #  TODO: validate user password and username
    # print_message(config.REGISTRATION_SUCCESSFUL_MESSAGE) #TODO: show this if username and password are valid
    # print_message(config.REGISTRATION_ERROR_MESSAGE, exit_app=True) #TODO: show this if username and password fail
    pass  # TODO: add logic to save new user in dictionary <user_db>


def login_user() -> None:
    """ TODO: add base description
    TODO: add full description, return description
    :return:
    """
    # TODO: ask user to login with username and password,
    # TODO: check if user exist in database(<user_db>) use method <is_user_present>
    # TODO: if user exist authenticate user use function <authenticate_user>
    # TODO: Check how many times user try to login see README.md file Instruction section task 4
    # TODO: Use constant <LOGIN_ATTEMPTS> and <SECONDS_TO_NEXT_ATTEMPT> from app_config.py file already imported
    # TODO: use print_message method to print message and stop the flow if is needed
    pass


def authenticate_user(username: str, password: str) -> bool:
    """ TODO: add base description
    TODO: add full description, parameters description
    :param username:
    :param password:
    :return:
    """
    # TODO: Add logic to authenticate user,
    # TODO: get user by username and check the equality of the password if everything is fine return True
    # TODO if password not mach return False
    pass


def is_user_present(username: str) -> bool:
    """  TODO: add base description
    TODO: add full description, parameters, return description
    :param username:
    :return:
    """
    pass  # TODO add logic to check if user exist in <user_db>


def save_user_phone_number() -> None:
    """  TODO: add base description
    TODO: add full description and return description
    :return:
    """
    # TODO: add logic to get phone number from input
    # TODO: validate number if number is correct return in other case ask for the number again
    pass  # TODO: Save phone number in <user_db>


def print_message(msg: str, exit_app: bool = False) -> None:
    """  Print message to console

    Get argument <msg>: str and print this message to console
    also after printing message you need stop the flow change <exit_app> argument to True

    :param msg: (str) Get string message
    :param exit_app: (bool) stop the flow default is False
    :return: (None)
    """

    print(msg)
    if exit_app:
        sys.exit()
