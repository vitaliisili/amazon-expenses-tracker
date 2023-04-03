import re


def is_password_valid(password: str) -> bool:
    """ Check if password is valid

    This function takes a string as input and checks if it meets the criteria for a valid password.
    A valid password must meet the following criteria:
    1. Be at least (6-20) characters long
    2. Contain at least one uppercase letter
    3. Contain at least one lowercase letter
    4. Contain at least one number
    5. Contain at least one special character from the following list: !@#$%^&*()-_=+`~[]{}|;:'",.<>/?

    Note: This function does not check if the password is secure or not.
    It only checks if it meets the minimum requirements for a valid password.

    :param password: (str) A string representing the password that needs to be checked for validity.
    :return: (bool) A boolean value indicating whether the password meets the specified criteria for validity.
    """

    pattern = re.compile(r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){6,20}$")

    return bool(pattern.match(password))


def is_username_valid(username: str) -> bool:
    """ Check if passed username is valid

    This function takes a string as input and checks if it meets the criteria for a valid username.
    A valid username must meet the following criteria:

    1. Be at least 1 characters long

    :param username: (str) A string representing the username to be checked.
    :return: (bool)  boolean value indicating whether the username is valid or not.
    """

    return len(username) >= 1


def is_phone_valid(phone_number: str) -> bool:
    """ TODO: add base description
    TODO: add full description and parameters description
    :param phone_number:
    :return:
    """
    return True  # TODO: add logic for German phone number validation return boolean


def is_date_valid(date: str) -> bool:
    """  Check if passed date is valid

    Description: Determines whether a given date is valid or not.
    A valid date must be in the format "MM-DD-YYYY" or "MM/DD/YYYY".

    :param date: (str) A string representing the date.
    :return: (bool) Returns True if the input date is a valid date, otherwise returns False.
    """

    pattern = re.compile(r"^\d{2}[-/]\d{2}[-/]\d{4}$")

    return True  # TODO Finish the logic to validate date


def is_item_name_valid(name: str) -> bool:
    """  Check if name of item is valid

    Determines whether a given item name is valid or not. A valid item name must be a non-empty string.
    And name must be at least 3 character long

    :param name: (str) A string representing the item name.
    :return: (bool) Returns True if the input name is a valid item name, otherwise returns False.
    """

    return len(name) >= 3


def is_item_cost_valid(cost: str) -> bool:
    """  Check if passed number is valid

    Determines whether a given item cost is valid or not.
    A valid item cost must be a string representing positive float or integer.

    :param cost: (str)  A string representing the item cost.
    :return: (bool) Returns True if the input cost is a valid item cost, otherwise returns False.
    """

    float_pattern = re.compile(r"^\d+\.\d{1,2}$")

    return bool(float_pattern.match(cost)) or cost.isnumeric()


def is_item_weight_valid(weight: str) -> bool:
    """  Check if passed weight is valid

    Determines whether a given item weight is valid or not.
    A valid item weight must be a string representing positive float or integer.

    TODO: add full description and parameters description
    :param weight: (str) A string representing the item weight
    :return: (bool) Returns True if the input weight is valid, otherwise returns False.
    """

    float_pattern = re.compile(r"^\d+\.\d{1,2}$")

    return bool(float_pattern.match(weight)) or weight.isnumeric()


def is_item_quantity_valid(quantity: str) -> bool:
    """ Check if passed quantity is valid number

    Determines whether a given item quantity is valid or not.
    A valid item quantity must be a string representing integer.

    :param quantity: (str) A string representing the item quantity
    :return: (bool) Returns True if the input is a valid item quantity, otherwise returns False.
    """
    return quantity.isnumeric()
