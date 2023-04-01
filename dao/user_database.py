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
    "orders": [
        {
            "purchase_date": "",
            "item_name": "",
            "total_cost": 0.0,
            "weight": 0.0,
            "quantity": 0
        }
    ]
}
