class User:
    email = ''
    password = ''
    name = ''

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name