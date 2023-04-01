from dao.user_database import user_db
import service.user_service as service
import config.app_config as config


def save_order(item: dict) -> None:
    """  TODO: add base description
    TODO: add full description, parameters, return description
    :param item:
    :return:
    """

    service.print_message(config.ORDER_SUCCESSFUL_MESSAGE)
    pass  # TODO: save order in <user_db.orders> and print successful message


def is_order_list_empty() -> bool:
    """  TODO: add base description
    TODO: add full description
    :return:
    """
    return True  # TODO: check if order list is empty in <user_db.orders>


def get_all_orders() -> list:
    """   TODO: add base description
    TODO: add full description
    :return:
    """
    pass


def sort_orders_by_date(orders: list) -> list:
    """  TODO: add base description
    TODO: add full description
    :param orders:
    :return:
    """
    pass  # TODO: sort orders list by date Ascending

# def sort_orders_by_cost(orders: list) -> list:
#     """  TODO: add base description
#     TODO: add full description
#     :param orders:
#     :return:
#     """
#
#     pass  # TODO: sort orders list by date Ascending
