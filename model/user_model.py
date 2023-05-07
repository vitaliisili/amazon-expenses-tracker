class User:

    def __init__(self, username: str, password: str, phone: str):
        self.username = username
        self.password = password
        self.phone = phone

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def __repr__(self):
        return f"User({self._username}, {self._password}, {self._phone})"

    def __str__(self):
        return f"User(username: {self._username}, password: {self._password}, phone: {self._phone})"
