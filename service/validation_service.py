import re
import config.app_config as config


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
    """ Check if passed phone number is a valid German phone number
    
    A valid German phone number must start with either "0" or "+49" (the country code for Germany),
    followed by the area code and the local number. The area code must be enclosed in parentheses,
    and can either be 2-5 digits long or a special one-digit code for mobile phones. 
    The local number can be 3-7 digits long.
    
    :param phone_number: (str) A string representing the phone number to be checked.
    :return: (bool) Returns True if the input phone number is a valid German phone number, otherwise returns False.
    """
    pattern = re.compile(r"^((00)|(\+))49(\s?\(?\d{2,4}\)?\s?\d{2,4})\s?\d{4}$")
    phone: str = ''

    if bool(pattern.match(phone_number)):
        if phone_number[0:2] == '00':
            phone = re.sub(r"[\s()]", "", phone_number[4:])
        else:
            phone = re.sub(r"[\s()]", "", phone_number[3:])

    return len(phone) in [10, 11]


def is_date_valid(date: str) -> bool:
    """Check if passed date is valid

    Description: Determines whether a given date is valid or not.
    A valid date must be in the format "MM-DD-YYYY" or "MM/DD/YYYY".

    :param date: (str) A string representing the date.
    :return: (bool) Returns True if the input date is a valid date, otherwise returns False.
    """

    pattern = re.compile(r"^\d{2}[-/]\d{2}[-/]\d{4}$")

    if not pattern.match(date):
        return False

    date_parts = re.split('[-/]', date)
    month, day, year = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])

    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return False
        elif day > 28:
            return False
    return True


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


def is_cost_weight_rapport_valid(weight: float, cost: float, quantity: int) -> bool:
    """ Check if rapport between item cost and weight

    This function check rapport between item weight and cost if weight is bigger than cost that mean
    delivery cost more than total item cost in this case <is_cost_weight_rapport_valid> return false

    :param quantity: (int) item quantity
    :param weight: (float) item weight that should be checked
    :param cost: (float) item cost that should be checked
    :return: (bool)  Return boolean if rapport between two items is valid
    """
    total_cost = cost * quantity
    delivery = weight * config.AMAZON_CHARGES_PER_KG * quantity
    return total_cost >= delivery
