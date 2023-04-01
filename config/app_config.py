"""
This file contain all constants for error, successful messages
also this fail contains constants for configuration like <LOGIN_ATTEMPTS> and <SECONDS_TO_NEXT_ATTEMPT>
use these constants to display a message in command prompt
"""

LOGIN_ATTEMPTS = 3
SECONDS_TO_NEXT_ATTEMPT = 5
AMAZON_CHARGES_PER_KG = 1
AMAZON_SPENDING_LIMIT = 500

REGISTRATION_PASSWORD_ERROR_MESSAGE = "Invalid password please try again"
REGISTRATION_USERNAME_ERROR_MESSAGE = "Invalid username please try again"
REGISTRATION_SUCCESSFUL_MESSAGE = "Registration successful!"
REPEAT_REGISTRATION_ERROR_MESSAGE = "No such user with entered username and password please try to register"

PHONE_ERROR_MESSAGE = "Phone number is not valid, please enter a valid number"

LOGIN_ERROR_MESSAGE = f"\nUsername or password is wrong please try again"
LOGIN_ATTEMPTS_ERROR_MESSAGE = f"To many attempts please try again in {SECONDS_TO_NEXT_ATTEMPT} seconds"
LOGIN_SUCCESSFUL_MESSAGE = "Login successful!"

MENU_ITEM_ERROR_MESSAGE = f"\nInvalid menu item please select valid menu item\n"

ORDER_SUCCESSFUL_MESSAGE = f"\nPurchase saved.\n"

GREETING_MESSAGE = "Hello, %s! Welcome to the Amazon Expense Tracker!"
GOODBYE_MESSAGE = f"\nThank you for your visit, %s. Goodbye!"
AMAZON_WELCOME_MESSAGE = """
---------------------
| Welcome to Amazon! |
---------------------
"""