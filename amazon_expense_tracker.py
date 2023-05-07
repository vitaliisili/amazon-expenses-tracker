from auth.login_service import Login
from auth.registration_service import RegistrationService
from service.amazon_service import AmazonService


def run():
    registration_service = RegistrationService()
    registration_service.register_user()

    login_service = Login()
    login_service.login()

    amazon_service = AmazonService()
    amazon_service.show_menu()


if __name__ == "__main__":
    run()
