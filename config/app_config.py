from colorama import Fore

"""
This file contain all constants for error, successful messages
also this fail contains constants for configuration like <LOGIN_ATTEMPTS> and <SECONDS_TO_NEXT_ATTEMPT>
use these constants to display a message in command prompt
"""

COLOR_RED = Fore.RED
COLOR_GREEN = Fore.GREEN

# Basic config
LOGIN_ATTEMPTS = 3
SECONDS_TO_NEXT_ATTEMPT = 5
AMAZON_CHARGES_PER_KG = 1
AMAZON_SPENDING_LIMIT = 500
CURRENCY = "EURO"
DATE_FORMAT = "%m/%d/%Y"

# Registration messages
REGISTRATION_PASSWORD_ERROR_MESSAGE = f"{COLOR_RED}Invalid password please try again"
REGISTRATION_USERNAME_ERROR_MESSAGE = f"{COLOR_RED}Invalid username please try again"
REGISTRATION_SUCCESSFUL_MESSAGE = f"{COLOR_GREEN}\nRegistration successful!"
REPEAT_REGISTRATION_ERROR_MESSAGE = f"{COLOR_RED}No such user with entered username and password please try to register"

# Phone number messages
PHONE_ERROR_MESSAGE = f"{COLOR_RED}Phone number is not valid, please enter a valid number"

# Login messages
LOGIN_ERROR_MESSAGE = f"{COLOR_RED}\nUsername or password is wrong please try again"
LOGIN_ATTEMPTS_ERROR_MESSAGE = f"{COLOR_RED}To many attempts please try again in {SECONDS_TO_NEXT_ATTEMPT} seconds"
LOGIN_SUCCESSFUL_MESSAGE = f"{COLOR_GREEN}\nLogin successful!\n"

# Amazon menu messages
MENU_ITEM_ERROR_MESSAGE = f"{COLOR_RED}\nInvalid menu item please select valid menu item\n"

# Report message
REPORT_GENERATION_ERROR = f"{COLOR_RED}\nPlease insert at least one item to generate a report"

# Order messages
ORDER_SUCCESSFUL_PURCHASE_MESSAGE = f"{COLOR_GREEN}\nPurchase saved !\n"
ORDER_DATE_MESSAGE = "\nEnter the date of the purchase in format (MM/DD/YYYY, MM-DD-YYYY): "
ORDER_DATE_ERROR = f"{COLOR_RED}The purchase date is not valid please try again"
ORDER_NAME_MESSAGE = "Enter the item purchased: "
ORDER_NAME_ERROR = f"{COLOR_RED}\nThe item name is not valid name must contain at least 3 characters\n"
ORDER_COST_MESSAGE = "Enter the cost of the item in Euro: "
ORDER_COST_ERROR = f"{COLOR_RED}The purchased item cost is not valid please try again"
ORDER_WEIGHT_MESSAGE = "Enter the weight of the item in kg: "
ORDER_WEIGHT_ERROR = f"{COLOR_RED}The item weight is not valid please try again"
ORDER_QUANTITY_MESSAGE = "Enter the quantity purchased: "
ORDER_QUANTITY_ERROR = f"{COLOR_RED}The item quantity is not valid must be a positive number please try again"

# Formatted messages
GREETING_MESSAGE = "Hello, %s! Welcome to the Amazon Expense Tracker!"
CLOSE_APP_MESSAGE = f"\nThank you for your visit, %s. Goodbye!"
AMAZON_WELCOME_MESSAGE = """
    ----------------------
    | Welcome to Amazon! |
    ----------------------
"""