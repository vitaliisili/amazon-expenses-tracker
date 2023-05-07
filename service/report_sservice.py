class ReportService:
    def __init__(self, user_data):
        self.__user_data = user_data

    def generate_report(self):
        return self.__user_data
