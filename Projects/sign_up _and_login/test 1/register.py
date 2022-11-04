class register:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
