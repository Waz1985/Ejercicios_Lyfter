class User:
    def __init__(self, name):
        self.name = name

class AuthMixin:
    def login(self):
        return f"{self.name} logged in"

class LogMixin:
    def log_action(self, action):
        return f"LOG: {self.name} -> {action}"

class Admin(User, AuthMixin, LogMixin):
    pass

