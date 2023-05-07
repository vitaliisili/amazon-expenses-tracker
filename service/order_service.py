from dao.user_db import user_db
from model.item_model import Item


class OrderService:
    def __init__(self):
        pass

    def save_order(self, item: Item):
        user_db["orders"].append(item)
