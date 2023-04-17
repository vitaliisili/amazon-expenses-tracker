from colorama import Fore

"""
This file contain all constants for error, successful messages, colors and basic configuration
also this fail contains constants for configuration
use these constants to display a message in command prompt
"""

# Text Colors
COLOR_RED = Fore.LIGHTRED_EX
COLOR_GREEN = Fore.LIGHTGREEN_EX
COlOR_RESET = Fore.RESET
COLOR_YELLOW = Fore.LIGHTYELLOW_EX
COLOR_WHITE = Fore.LIGHTWHITE_EX
COLOR_BLACK = Fore.LIGHTBLACK_EX
COLOR_BLUE = Fore.LIGHTBLUE_EX

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
PHONE_NUMBER_MESSAGE = f"{COLOR_WHITE}Please enter phone number to continue: {COlOR_RESET}"
PHONE_SUCCESS_MESSAGE = f"{COLOR_GREEN}\nPhone number saved successful !{COlOR_RESET}"
PHONE_ERROR_MESSAGE = f"{COLOR_RED}Phone number is not valid, please enter a valid number\n{COlOR_RESET}"

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
ORDER_DATE_MESSAGE = f"{COLOR_WHITE}Enter the date of the purchase in format (MM/DD/YYYY, MM-DD-YYYY): {COlOR_RESET}"
ORDER_DATE_ERROR = f"{COLOR_RED}The purchase date is not valid please try again{COlOR_RESET}"
ORDER_NAME_MESSAGE = f"{COLOR_WHITE}Enter the item purchased: {COlOR_RESET}"
ORDER_NAME_ERROR = f"{COLOR_RED}The item name is not valid name must contain at least 3 characters{COlOR_RESET}"
ORDER_COST_MESSAGE = f"{COLOR_WHITE}Enter the cost of the item in Euro: {COlOR_RESET}"
ORDER_COST_ERROR = f"{COLOR_RED}The purchased item cost is not valid please try again{COlOR_RESET}"
ORDER_WEIGHT_MESSAGE = f"{COLOR_WHITE}Enter the weight of the item in kg: {COlOR_RESET}"
ORDER_WEIGHT_ERROR = f"{COLOR_RED}The item weight is not valid please try again{COlOR_RESET}"
ORDER_QUANTITY_MESSAGE = f"{COLOR_WHITE}Enter the quantity purchased: {COlOR_RESET}"
ORDER_QUANTITY_ERROR = f"{COLOR_RED}The item quantity is not valid must be a positive number please try again{COlOR_RESET}"
ORDER_DELIVERY_ERROR = f"{COLOR_RED}Your delivery is bigger than item total cost please choose one option{COlOR_RESET}"
ORDER_COST_UPDATE_MESSAGE = f"{COLOR_GREEN}Item total cost has been updated successful!{COlOR_RESET}"
ORDER_WEIGHT_UPDATE_MESSAGE = f"{COLOR_GREEN}Item weight has been updated successful!{COlOR_RESET}"
ORDER_UPDATE_MENU_ERROR = f"{COLOR_RED}Entered menu number is not valid please enter one of two options{COlOR_RESET}"

# Formatted messages
GREETING_MESSAGE = f"{COLOR_GREEN}Hello, {COLOR_YELLOW}%s!{COLOR_GREEN} Welcome to the Amazon Expense Tracker!\n{COlOR_RESET}"
CLOSE_APP_MESSAGE = f"{COLOR_GREEN}\nThank you for your visit, {COLOR_YELLOW}%s{COLOR_GREEN}. Goodbye!{COlOR_RESET}"

AMAZON_WELCOME_MESSAGE = f"""{COLOR_WHITE}
    ----------------------
    | Welcome to Amazon! |
    ----------------------
{COlOR_RESET}"""

APP_DESCRIPTION = f"""{COLOR_YELLOW}
                            AMAZON EXPENSE TRACKER
 --------------------------------Description------------------------------------
 |                                                                              |
 |  Amazon expense tracker is command line application that help to generate    |
 |  detailed orders report, amazon-expense-tracker calculate delivery charges,  | 
 |  total item cost, most/least expensive item, average cost of item per order. |
 |                                                                              |
 --------------------------------------------------------------------------------
{COlOR_RESET}"""

APP_LOGO = f"""{COLOR_YELLOW}                                                                                      
           ██     ▀████▄     ▄███▀     ██     ███▀▀▀███ ▄▄█▀▀██▄ ▀███▄   ▀███▀
          ▄██▄      ████    ████      ▄██▄    █▀   ███▄██▀    ▀██▄ ███▄    █  
         ▄█▀██▄     █ ██   ▄█ ██     ▄█▀██▄   ▀   ███ ██▀      ▀██ █ ███   █  
        ▄█  ▀██     █  ██  █▀ ██    ▄█  ▀██      ███  ██        ██ █  ▀██▄ █  
        ████████    █  ██▄█▀  ██    ████████    ███   ▄█▄      ▄██ █   ▀██▄█  
       █▀      ██   █  ▀██▀   ██   █▀      ██  ███   ▄███▄    ▄██▀ █     ███  
     ▄███▄   ▄████▄███▄ ▀▀  ▄████▄███▄   ▄████▄████████ ▀▀████▀▀ ▄███▄    ██
            
            {APP_DESCRIPTION}
{COlOR_RESET}"""
