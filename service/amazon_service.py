import service.validation_service as validation
import service.user_service as service
import service.order_service as order
from anotation.decorator_delay import progress_delay
import config.app_config as config
from dao.user_database import user_db


def show_menu() -> None:
    """

    :return:
    """

    def select_menu(menu_number: int) -> None:
        match menu_number:  # IMPORTANT: Required Python 3.10 or newer
            case 1:
                get_order()
            case 2:
                show_report()
            case 3:
                close_app()
            case _:
                service.print_message(config.MENU_ITEM_ERROR_MESSAGE)

    while True:
        print(f"What would you like to do?")
        print("""
        1. Enter a purchase
        2. Generate a report
        3. Quit
        """)
        menu_choice = input("Enter your choice (1/2/3): ")
        select_menu(int(menu_choice) if menu_choice.isnumeric() else -1)


def get_order() -> None:  # TODO: Refactor: remove all closed method and create universal one
    """ Get order from user input

    This functe collect data from user input

    :return: (None) This function does not return any value
    """

    item = {
        "purchase_date": "",
        "item_name": "",
        "total_cost": 0.0,
        "weight": 0.0,
        "quantity": 0
    }

    def get_item_date() -> str:
        date: str = input("Enter the date of the purchase in format (MM/DD/YYYY, MM-DD-YYYY): ")
        if not validation.is_date_valid(date):
            service.print_message("The purchase date is not valid please try again")
            get_item_date()

        return date

    def get_item_name() -> str:
        name: str = input("Enter the item purchased: ")
        if not validation.is_item_name_valid(name):
            service.print_message("The item name is not valid name must contain at least 3 characters")
            get_item_name()

        return name

    def get_item_cost() -> float:
        cost: str = input("Enter the cost of the item in Euro: ")
        if not validation.is_item_cost_valid(cost):
            service.print_message("The purchased item cost is not valid please try again")
            get_item_cost()

        return float(cost)

    def get_item_weight() -> float:
        weight: str = input("Enter the weight of the item in kg: ")
        if not validation.is_item_weight_valid(weight):
            service.print_message("The item weight is not valid please try again")
            get_item_weight()

        return float(weight)

    def get_item_quantity() -> int:
        quantity: str = input("Enter the quantity purchased: ")
        if not validation.is_item_quantity_valid(quantity):
            service.print_message("The item quantity is not valid must be a positive number please try again")
            get_item_quantity()
        return int(quantity)

    item["purchase_date"] = get_item_date()
    item["item_name"] = get_item_name()
    item["total_cost"] = get_item_cost()
    item["weight"] = get_item_weight()
    item["quantity"] = get_item_quantity()

    order.save_order(item)


@progress_delay(prefix_msg="Generating report ")
def show_report() -> None:
    """  TODO: add base description
    TODO: add full description
    :return:
    """

    # TODO: call generate_report function from report service
    # show_menu()


@progress_delay(prefix_msg="Quitting program ")
def close_app() -> None:
    """

    :return:
    """
    service.print_message(config.GOODBYE_MESSAGE % user_db["username"], exit_app=True)
