from typing import Callable
import service.validation_service as validation
import service.user_service as service
from anotation.decorator_delay import progress_delay
import config.app_config as config
from dao.user_database import user_db
import service.report_service as report


def show_menu() -> None:
    """ Show menu for authenticated users.

    This function shows the menu in the command line and also asks the user for further actions.

    :return: This function does not return any value.
    """

    def select_menu(menu_number: int) -> None:
        """  Call menu function

        This is a help function that helps to choose the right function depending on the menu number.
        If the menu number is not found, the function will show an error message.

        :param menu_number: (int)  An integer that determines which menu execute.
        :return: (None) This function does not return any value.
        """

        match menu_number:  # IMPORTANT: Required Python 3.10 or newer
            case 1:
                save_order()
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


def save_order() -> None:
    """ Get order from user input.

    This functe collect data from user input and create object <item>,
    Pass collected data to <save_order> function.

    :return: (None) This function does not return any value.
    """

    item = {
        "purchase_date": "",
        "item_name": "",
        "total_cost": 0.0,
        "weight": 0.0,
        "quantity": 0
    }

    def get_order_data(info_message: str, error_message: str, validation_func: Callable) -> str:
        data: str = input(info_message)

        while not validation_func(data):
            service.print_message(error_message)
            data: str = input(info_message)

        return data

    item["purchase_date"] = get_order_data(config.ORDER_DATE_MESSAGE,
                                           config.ORDER_DATE_ERROR,
                                           validation.is_date_valid)

    item["item_name"] = get_order_data(config.ORDER_NAME_MESSAGE,
                                       config.ORDER_NAME_ERROR,
                                       validation.is_item_name_valid)

    item["total_cost"] = float(get_order_data(config.ORDER_COST_MESSAGE,
                                              config.ORDER_COST_ERROR,
                                              validation.is_item_cost_valid))

    item["weight"] = float(get_order_data(config.ORDER_WEIGHT_MESSAGE,
                                          config.ORDER_WEIGHT_ERROR,
                                          validation.is_item_weight_valid))

    item["quantity"] = int(get_order_data(config.ORDER_QUANTITY_MESSAGE,
                                          config.ORDER_QUANTITY_ERROR,
                                          validation.is_item_quantity_valid))

    user_db["orders"].append(item)
    service.print_message(config.ORDER_SUCCESSFUL_PURCHASE_MESSAGE)


@progress_delay(prefix_msg="Generating report ")
def show_report() -> None:
    """  Show report in command line

    The show_report function is used to display a report.
    It does not take any parameters and simply displays the report to the user

    :return: (None) This function does not return any value.
    """

    service.print_message(report.generate_report(user_db))


@progress_delay(prefix_msg="Quitting program ")
def close_app() -> None:
    """ Close application

    The close_app function is used to close an application.
    It does not take any parameters and simply closes the application and show goodbye message.

    :return: (None) This function does not return any value.
    """
    service.print_message(config.CLOSE_APP_MESSAGE % user_db["username"], exit_app=True)
