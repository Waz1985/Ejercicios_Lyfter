import jwt
from config import PRIVATE_KEY_PATH, PUBLIC_KEY_PATH, JWT_ALGORITHM


class JWTManager:
    def __init__(self):
        with open(PRIVATE_KEY_PATH, "r", encoding="utf-8") as private_file:
            self.private_key = private_file.read()

        with open(PUBLIC_KEY_PATH, "r", encoding="utf-8") as public_file:
            self.public_key = public_file.read()

        self.algorithm = JWT_ALGORITHM

    def encode(self, data):
        try:
            return jwt.encode(data, self.private_key, algorithm=self.algorithm)
        except Exception:
            return None

    def decode(self, token):
        try:
            return jwt.decode(token, self.public_key, algorithms=[self.algorithm])
        except Exception:
            return None