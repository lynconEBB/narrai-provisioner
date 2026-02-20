import datetime


class AccessPassword:
    def __init__(self, password):
        self.password_hash = password
        self.lastUpdate = datetime.datetime.now()

    def check_password(self, password):
        self.password_hash = (password)