from config.app_config import AMAZON_SPENDING_LIMIT

"""
Imitation for database dictionary is used to save data from user input,
<user_db> contains user base information and user order list.
Use <user_db> to do CRUD operations
"""

user_db = {
    "username": "",
    "password": "",
    "phone": "",
    "spending_limit": AMAZON_SPENDING_LIMIT,
    "orders": []
}
