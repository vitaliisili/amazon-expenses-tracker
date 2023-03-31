"""
Imitation for database dictionary is used to save data from user input,
<user_db> contains user base information and user order list
use <user_db> to do CRUD operations
"""

user_db = {
    "username": str,
    "password": str,
    "phone": str,
    "orders": [
        {
            "purchase_date": str,
            "item_name": str,
            "total_cost": float,
            "weight": float,
            "quantity": int
        }
    ]
}
