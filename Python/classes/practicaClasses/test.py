class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class AdminUser(User):
    def __init__(self, name, role):
        super().__init__(name, role)
    