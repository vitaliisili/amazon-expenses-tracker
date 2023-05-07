import sys
from typing import Callable

from dao.user_db import user_db
from model.item_model import Item
from service.order_service import OrderService
from service.report_sservice import ReportService


class AmazonService:
    def __init__(self):
        pass

    def show_menu(self):

        while True:
            print("What would you like to do?")
            print("""
            1. Enter a purchase
            2. Generate a report
            3. Quit
            """)

            menu_choice = input("Select menu number: ")

            match menu_choice:
                case "1":
                    self.__get_purchase()
                case "2":
                    self.__show_report()
                case "3":
                    self.__close_app()
                case _:
                    print("Selected menu is not correct")

    def __get_purchase(self):
        item = Item()

        def get_order_data(info_message: str, error_message: str, validation_func: Callable) -> str:
            while data := input(info_message):
                if validation_func:
                    return data

                print(error_message)

        item.name = get_order_data("Enter item name: ",
                                   "Item name is not valid please try again",
                                   self.__is_item_name_valid)

        item.purchase_date = get_order_data("Enter purchase date: ",
                                            "Purchase date is not valid please try again",
                                            self.__is_item_date_valid)

        item.price = get_order_data("Enter item price: ",
                                    "Item price is not valid please try again",
                                    self.__is_item_price_valid)

        item.weight = get_order_data("Enter item weight: ",
                                     "Item weight is not valid please try again",
                                     self.__is_item_weight_valid)

        item.quantity = get_order_data("Enter item quantity: ",
                                       "Item quantity is not valid",
                                       self.__is_item_quantity_valid)

        order_service = OrderService()
        order_service.save_order(item)

        print("Item has been saved")

    def __show_report(self):
        report_service = ReportService(user_db)
        print(report_service.generate_report())

    def __close_app(self):
        sys.exit()

    def __is_item_name_valid(self, name):
        return len(name) >= 3

    def __is_item_date_valid(self, date):
        return True

    def __is_item_price_valid(self, price):
        return True

    def __is_item_weight_valid(self, weight):
        return True

    def __is_item_quantity_valid(self, quantity):
        return True
