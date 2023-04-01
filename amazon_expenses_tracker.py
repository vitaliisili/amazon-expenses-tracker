from argparse import ArgumentParser
import service.user_service as service
import service.amazon_service as amazon
import config.app_config as config

parser = ArgumentParser(description="description")  # TODO: add description

parser.add_argument("username",
                    help="help")  # TODO: add help description

parser.add_argument("password",
                    help="help")  # TODO: add help description

args = parser.parse_args()
username = args.username
password = args.password

service.register_user(username, password)
service.print_message(config.AMAZON_WELCOME_MESSAGE)
service.save_user_phone_number()
service.login_user()