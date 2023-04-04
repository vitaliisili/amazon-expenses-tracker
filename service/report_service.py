import service.user_service as service
import config.app_config as config
from datetime import datetime
from typing import Union


def generate_report(user_data: dict) -> str:
    """  Generate detailed report

    The generate_report function is used to generate a report based on the user's data.
    It takes a dictionary containing the user's data as a parameter and returns
    a string containing the generated report.

    :param: user_data: (dict) A dictionary containing the user's data to be used to generate the report.
    :return: (str)  A string containing detailed generated report.
    """

    def space_size(total: int, start_text: Union[str, int, float]) -> str:
        """  Add additional spaces between items

        This is helper function that calculate how many spaces are necessarily between two items
        in base on <start_text> argument and <total>

        :param total: (int)  Total space between two elements
        :param start_text:  text before spaces
        :return: (str) Return string of spaces required between two elements
        """

        return " " * (total - len(str(start_text)))

    def get_delivery_cost(item: dict) -> Union[float, int]:
        """  Calculate delivery cost per item

        This function calculates the delivery cost for a package based on its weight and the cost per kilogram

        :param item: (dict) A dictionary that contain key about weight
        :return: (float, int): the calculated delivery cost
        """

        item_delivery: float = item["weight"] * config.AMAZON_CHARGES_PER_KG

        if item_delivery % 1 == 0:
            return int(item_delivery)

        return round(item_delivery, 2)

    def get_item_cost(item: dict) -> Union[float, int]:
        """  Calculate item cost without delivery

        This function calculate how much cost one item without delivery

        :param item: (dict) A dictionary that contain key about total cost
        :return: (float, int) Return cost per item without delivery
        """

        item_cost: float = item["total_cost"] - get_delivery_cost(item)

        if item_cost % 1 == 0:
            return int(item_cost)

        return round(item_cost, 2)

    def total_delivery_charges(orders: list) -> Union[float, int]:
        """  Calculate total delivery for all orders

        This function calculates the total delivery charges for a list of orders,
        where each order is a dictionary containing the weight and cost per kilogram of the package.

        :param orders: (list): A list of orders, where each order is a dictionary.
        :return: (float, int): the total delivery charges for all the orders in the list.
        """

        total: float = sum([get_delivery_cost(order) * order["quantity"] for order in orders])

        if total % 1 == 0:
            return int(total)

        return round(total, 2)

    def total_items_cost(orders: list) -> Union[float, int]:
        """  Calculate total cost for all items

        This function calculates the total cost of all the items in a list of orders,
        where each order is a dictionary containing a list of items with their respective prices and quantities.

        :param orders: (list): a list of orders, where each order is a dictionary.
        :return: (float, int): The total cost of all the items only in the list of orders.
        """

        total_cost: float = sum([order['total_cost'] * order["quantity"] for order in orders])
        items_only = total_cost - total_delivery_charges(orders)

        if items_only % 1 == 0:
            return int(items_only)

        return round(items_only, 2)

    def calculate_average(orders: list) -> Union[float, int]:
        """  Calculate average of all orders.

        This function calculate average of a list of items including delivery

        :param orders: (list): A list of orders, where each order is a dictionary.
        :return: (float, int): the average cost of all orders
        """

        total_cost: float = sum([order['total_cost'] * order["quantity"] for order in orders])
        total_items: int = sum([order['quantity'] for order in orders])
        items_average: float = total_cost / total_items

        if items_average % 1 == 0:
            return int(items_average)

        return round(items_average, 2)

    def sorted_items_by_cost(orders: list) -> list:
        """ Sort list of items by cost

        This function takes a list of orders, where each order is a dictionary
        Sort all items by cost in ascending order.

        :param orders: (list): A list of orders, where each order is a dictionary.
        :return: (list): A list of items sorted by their costs in ascending order
        """

        orders.sort(key=lambda item: get_item_cost(item))

        return orders

    def sorted_items_by_date(orders: list) -> list:
        """  Sort list of items by date

        his function takes a list of orders, where each order is a dictionary
        Sort all items by date in ascending order.

        :param orders: (list) A list of orders, where each order is a dictionary.
        :return: (lit) A list of items sorted by their date in ascending order
        """

        orders.sort(key=lambda item: datetime.strptime(item["purchase_date"], config.DATE_FORMAT))

        return orders

    def hide_password() -> str:
        """  Hide password

        This function replace password with asterix

        :return: (str) Return a string with replaced password with asterix
        """

        return "***"

    def hide_phone(phone_number: str) -> str:
        """  Replace phone number with asterix

        This function takes in a phone number as a string and returns a
        modified version of the string with the three asterix instead of digits in middle of a string.
        Example: +49***32

        :param phone_number: (str) A string representing a phone number.
        :return: (str) A string representing the modified phone number
        """

        modified_phone: str = phone_number[0:3] + '***' + phone_number[-2:]

        return modified_phone

    def get_extended_limit(items_total_cost: Union[float, int], delivery_total_cost: Union[float, int]) -> str:
        """ Show spending limit info

        It returns a string that describes the extended limit
        based on the total cost of the items and the delivery cost.

        :param items_total_cost: (float, int): The total cost of the items
        :param delivery_total_cost: (float, int): The total cost of delivery
        :return: (str) A string that describes the extended limit.
        """

        total_sum = items_total_cost + delivery_total_cost

        if total_sum > config.AMAZON_SPENDING_LIMIT:
            return f"You have exceeded the spending limit of {user_data['spending_limit']}"

        return f"You have not exceeded the spending limit of {user_data['spending_limit']}"

    if len(user_data["orders"]) == 0:
        service.print_message(config.REPORT_GENERATION_ERROR)
        return ""

    username: str = user_data["username"]
    password: str = hide_password()
    phone: str = hide_phone(user_data["phone"])
    date: str = datetime.now().strftime(config.DATE_FORMAT)
    delivery: Union[float, int] = total_delivery_charges(user_data["orders"])
    items_cost: Union[float, int] = total_items_cost(user_data["orders"])
    sorted_list_by_cost: list = sorted_items_by_cost(user_data["orders"])
    sorted_list_by_date: list = sorted_items_by_date(user_data["orders"])
    most_expensive_item_name: str = sorted_list_by_cost[-1]["item_name"]
    least_expensive_item_name: str = sorted_list_by_cost[0]["item_name"]
    highest_item_price: Union[float, int] = get_item_cost(sorted_list_by_cost[-1])
    lower_item_price: Union[float, int] = get_item_cost(sorted_list_by_cost[0])
    currency: str = config.CURRENCY
    average: Union[float, int] = calculate_average(user_data["orders"])
    spending_limit_string: str = get_extended_limit(items_cost, delivery)

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
    cost: {highest_item_price} {currency}  {space_size(8, highest_item_price)} cost: {lower_item_price} {currency}
    
    AVERAGE COST OF ITEM PER ORDER: {average} {currency}
    PURCHASE DATE RANGE: {sorted_list_by_date[0]["purchase_date"]} to {sorted_list_by_date[-1]["purchase_date"]}
    ---------
    Note: {spending_limit_string} {currency}
    
    """

    return report
