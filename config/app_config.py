from colorama import Fore

"""
This file contain all constants for error, successful messages
also this fail contains constants for configuration like <LOGIN_ATTEMPTS> and <SECONDS_TO_NEXT_ATTEMPT>
use these constants to display a message in command prompt
"""

COLOR_RED = Fore.RED
COLOR_GREEN = Fore.LIGHTGREEN_EX
COlOR_RESET = Fore.RESET
COLOR_YELLOW = Fore.LIGHTYELLOW_EX

# Basic config
LOGIN_ATTEMPTS = 3
SECONDS_TO_NEXT_ATTEMPT = 5
AMAZON_CHARGES_PER_KG = 1
AMAZON_SPENDING_LIMIT = 500
CURRENCY = "EURO"
DATE_FORMAT = "%m/%d/%Y"

# Registration messages
REGISTRATION_PASSWORD_ERROR_MESSAGE = f"{COLOR_RED}Invalid password please try again{COlOR_RESET}"
REGISTRATION_USERNAME_ERROR_MESSAGE = f"{COLOR_RED}Invalid username please try again{COlOR_RESET}"
REGISTRATION_SUCCESSFUL_MESSAGE = f"{COLOR_GREEN}\nRegistration successful!{COlOR_RESET}"
REPEAT_REGISTRATION_ERROR_MESSAGE = f"{COLOR_RED}No such user with entered username and password please try to register{COlOR_RESET}"

# Phone number messages
PHONE_ERROR_MESSAGE = f"{COLOR_RED}Phone number is not valid, please enter a valid number{COlOR_RESET}"

# Login messages
LOGIN_ERROR_MESSAGE = f"{COLOR_RED}\nUsername or password is wrong please try again{COlOR_RESET}"
LOGIN_ATTEMPTS_ERROR_MESSAGE = f"{COLOR_RED}To many attempts please try again in {SECONDS_TO_NEXT_ATTEMPT} seconds{COlOR_RESET}"
LOGIN_SUCCESSFUL_MESSAGE = f"{COLOR_GREEN}\nLogin successful!\n{COlOR_RESET}"

# Amazon menu messages
MENU_ITEM_ERROR_MESSAGE = f"{COLOR_RED}\nInvalid menu item please select valid menu item\n{COlOR_RESET}"

# Report message
REPORT_GENERATION_ERROR = f"{COLOR_RED}\nPlease insert at least one item to generate a report{COlOR_RESET}"

# Order messages
ORDER_SUCCESSFUL_PURCHASE_MESSAGE = f"{COLOR_GREEN}\nPurchase saved !\n{COlOR_RESET}"
ORDER_DATE_MESSAGE = "\nEnter the date of the purchase in format (MM/DD/YYYY, MM-DD-YYYY): "
ORDER_DATE_ERROR = f"{COLOR_RED}\nThe purchase date is not valid please try again{COlOR_RESET}"
ORDER_NAME_MESSAGE = "Enter the item purchased: "
ORDER_NAME_ERROR = f"{COLOR_RED}\nThe item name is not valid name must contain at least 3 characters{COlOR_RESET}"
ORDER_COST_MESSAGE = "Enter the cost of the item in Euro: "
ORDER_COST_ERROR = f"{COLOR_RED}\nThe purchased item cost is not valid please try again{COlOR_RESET}"
ORDER_WEIGHT_MESSAGE = "Enter the weight of the item in kg: "
ORDER_WEIGHT_ERROR = f"{COLOR_RED}\nThe item weight is not valid please try again{COlOR_RESET}"
ORDER_QUANTITY_MESSAGE = "Enter the quantity purchased: "
ORDER_QUANTITY_ERROR = f"{COLOR_RED}\nThe item quantity is not valid must be a positive number please try again{COlOR_RESET}"

# Formatted messages
GREETING_MESSAGE = f"{COLOR_GREEN}Hello, {COLOR_YELLOW}%s !{COLOR_GREEN} Welcome to the Amazon Expense Tracker!{COlOR_RESET}"
CLOSE_APP_MESSAGE = f"{COLOR_GREEN}\nThank you for your visit, {COLOR_YELLOW}%s{COLOR_GREEN}. Goodbye!{COlOR_RESET}"
AMAZON_WELCOME_MESSAGE = f"""{COLOR_YELLOW}
    ----------------------
    | Welcome to Amazon! |
    ----------------------
{COlOR_RESET}"""