from argparse import ArgumentParser, RawTextHelpFormatter
import service.user_service as service
import service.amazon_service as amazon
import config.app_config as config


def main():
    parser = ArgumentParser(description=config.APP_LOGO, formatter_class=RawTextHelpFormatter)
    parser.add_argument("username", help="User Username")
    parser.add_argument("password", help="User Password")

    args = parser.parse_args()
    username: str = args.username
    password: str = args.password

    service.register_user(username, password)
    service.print_message(config.AMAZON_WELCOME_MESSAGE)
    service.get_user_phone_number()
    service.login_user(config.LOGIN_ATTEMPTS)
    amazon.show_menu()


if __name__ == "__main__":
    main()
