from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String(20), nullable=False, default="USER")

    invoices = relationship("Invoice", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', role='{self.role}')"