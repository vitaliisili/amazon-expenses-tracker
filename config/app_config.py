"""
This file contain all constants for error, successful messages
also this fail contains constants for configuration like <LOGIN_ATTEMPTS> and <SECONDS_TO_NEXT_ATTEMPT>
use these constants to display a message in command prompt
"""

LOGIN_ATTEMPTS = 3
SECONDS_TO_NEXT_ATTEMPT = 5

REGISTRATION_ERROR_MESSAGE = "Invalid password please try again"
PHONE_ERROR_MESSAGE = "Phone number is not valid, please enter a valid number"
LOGIN_ERROR_MESSAGE = "Username or password is wrong please try again"
LOGIN_ATTEMPTS_ERROR_MESSAGE = f"To many attempts please try again in {SECONDS_TO_NEXT_ATTEMPT} seconds"
REPEAT_REGISTRATION_ERROR_MESSAGE = "No such user with entered username and password please try to register"

REGISTRATION_SUCCESSFUL_MESSAGE = "Registration successful!"
LOGIN_SUCCESSFUL_MESSAGE = "Login successful!"
GREETING_MESSAGE = "Hello, %s! Welcome to the Amazon Expense Tracker!"
AMAZON_WELCOME_MESSAGE = """
---------------------
| Welcome to Amazon! |
---------------------
"""