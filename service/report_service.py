import service.user_service as service
import config.app_config as config


def generate_report(user_data: dict) -> str:
    """  Generate detailed report

    The generate_report function is used to generate a report based on the user's data.
    It takes a dictionary containing the user's data as a parameter and returns
    a string containing the generated report.

    :param: user_data: (dict) A dictionary containing the user's data to be used to generate the report.
    :return: (str)  A string containing the generated report.
    """

    # TEST BLOCK --> REMOVE THIS BLOCK AFTER TESTING
    test_item = {
        "purchase_date": "23/11/2023",
        "item_name": "Notebook",
        "total_cost": 100.0,
        "weight": 3.0,
        "quantity": 90
    }
    user_data["orders"].append(test_item)
    # TEST BLOCK

    if len(user_data["orders"]) == 0:
        service.print_message(config.REPORT_GENERATION_ERROR)
        return ""

    username = user_data["username"]
    password = hide_password(user_data["password"])
    phone = hide_phone(user_data["phone"])
    date = get_date()
    delivery = total_delivery_charges(user_data["orders"])
    items_cost = total_items_cost(user_data["orders"])
    sorted_list_by_cost = sorted_item_by_cost(user_data["orders"])
    sorted_list_by_date = sorted_item_by_date(user_data["orders"])
    most_expensive_item_name = "TV"
    least_expensive_item_name = "Notebook"
    most_expensive_item_price = sorted_list_by_cost[0]
    least_expensive_item_price = sorted_list_by_cost[-1]
    currency = config.CURRENCY
    average = calculate_average(user_data["orders"])
    spending_limit = user_data["spending_limit"]

    report = f"""
    
                      -------------------------
                      | Amazon Expense Report |
                      -------------------------   
    Name: {username}   Password: {password}   Tel: {phone}   Date: {date}
    ----------------------------------------------
    DELIVERY CHARGES      TOTAL ITEM COST
        {delivery} {currency}  {space_size(12, delivery)}  {items_cost} {currency}
    
    MOST EXPENSIVE        LEAST EXPENSIVE
    name: {most_expensive_item_name}  {space_size(13, most_expensive_item_name)} name: {least_expensive_item_name}
    cost: {most_expensive_item_price} {currency}  {space_size(8, most_expensive_item_price)} cost: {least_expensive_item_price} {currency}
    
    AVERAGE COST OF ITEM PER ORDER: {average} {currency}
    PURCHASE DATE RANGE: {sorted_list_by_date[0]} to {sorted_list_by_date[-1]}
    ---------
    Note: You have not exceeded the spending limit of {spending_limit} {currency}
    
    """

    return report


def get_delivery_cost(weight: float, kg_cost: int) -> float:
    """  TODO: add base description
    TODO: add full description
    :param weight:
    :param kg_cost:
    :return:
    """
    return 8  # TODO: add logic to calculate delivery and return float


def get_item_cost(item: dict) -> float:
    """  TODO: add base description
    TODO: add full description
    :param item:
    :return:
    """
    return 35.70  # TODO add logic that calculate cost only for one item and return it


def total_delivery_charges(orders: list) -> float:
    """  TODO: add base description
    TODO: add full description
    :param orders:
    :return:
    """
    return 832  # TODO: add logic to calculate total delivery for all orders and return it


def total_items_cost(orders: list) -> float:
    """  TODO: add base description
    TODO: add full description
    :param orders:
    :return:
    """
    return 2  # TODO: add logic to calculate total cost for all items and return it


def calculate_average(orders: list) -> float:
    """  TODO: add base description
    TODO: add full description
    :param orders:
    :return:
    """
    return 10.3  # TODO: calculate average for all items


def sorted_item_by_cost(orders: list) -> list:
    """

    :param orders:
    :return:
    """
    return [8, 10]


def sorted_item_by_date(orders: list) -> list:
    """

    :param orders:
    :return:
    """
    return ["14/11/2023", "16/12/2023"]


def hide_password(password: str) -> str:
    """  Hide password

    This function replace password wit asterix

    :param password: (str) password that should be replaced
    :return: (str) Return a string with replaced password with asterix
    """

    return "***"  # TODO: Add logi that replace real password with asterix


def hide_phone(phone) -> str:
    """

    :param phone:
    :return:
    """
    return "+49***36"


def get_date() -> str:
    """  Return current date

    This function return current date in format DD/MM/YYYY

    :return:
    """
    return "02/12/2023"


def space_size(total, start_text) -> str:
    """

    :param total:
    :param start_text:
    :return:
    """
    return " " * (total - len(str(start_text)))
